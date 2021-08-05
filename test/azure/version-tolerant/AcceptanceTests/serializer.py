# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
import isodate
import email
import calendar
import re
import datetime
from base64 import b64encode, b64decode
import xml.etree.ElementTree as ET

try:
    from datetime import timezone as _FixedOffset
except ImportError:  # Python 2.7
    class _FixedOffset(datetime.tzinfo):  # type: ignore
        """Fixed offset in minutes east from UTC.
        Copy/pasted from Python doc
        :param datetime.timedelta offset: offset in timedelta format
        """

        def __init__(self, offset):
            self.__offset = offset

        def utcoffset(self, dt):
            return self.__offset

        def tzname(self, dt):
            return str(self.__offset.total_seconds()/3600)

        def __repr__(self):
            return "<FixedOffset {}>".format(self.tzname(None))

        def dst(self, dt):
            return datetime.timedelta(0)

        def __getinitargs__(self):
            return (self.__offset,)

try:
    from datetime import timezone
    TZ_UTC = timezone.utc  # type: ignore
except ImportError:
    TZ_UTC = UTC()  # type: ignore

DAYS = {0: "Mon", 1: "Tue", 2: "Wed", 3: "Thu",
            4: "Fri", 5: "Sat", 6: "Sun"}
MONTHS = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
              7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}

VALID_DATE = re.compile(
        r'\d{4}[-]\d{2}[-]\d{2}T\d{2}:\d{2}:\d{2}'
        r'\.?\d*Z?[-+]?[\d{2}]?:?[\d{2}]?')

class UTC(datetime.tzinfo):
    """Time Zone info for handling UTC"""

    def utcoffset(self, dt):
        """UTF offset for UTC is 0."""
        return datetime.timedelta(0)

    def tzname(self, dt):
        """Timestamp representation."""
        return "Z"

    def dst(self, dt):
        """No daylight saving for UTC."""
        return datetime.timedelta(hours=1)

def serialize_base64(attr):
    encoded = b64encode(attr).decode('ascii')
    return encoded.strip('=').replace('+', '-').replace('/', '_')

def deserialize_base64(attr):
    padding = '=' * (3 - (len(attr) + 3) % 4)
    attr = attr + padding
    encoded = attr.replace('-', '+').replace('_', '/')
    return b64decode(encoded)

def deserialize_date(attr):
    return isodate.parse_date(attr)

def deserialize_datetime(attr):
    return isodate.parse_datetime(attr)

def serialize_rfc(attr):
    try:
        utc = attr.utctimetuple()
    except AttributeError:
        raise TypeError("RFC1123 object must be valid Datetime object.")

    return "{}, {:02} {} {:04} {:02}:{:02}:{:02} GMT".format(
        DAYS[utc.tm_wday], utc.tm_mday,
        MONTHS[utc.tm_mon], utc.tm_year,
        utc.tm_hour, utc.tm_min, utc.tm_sec
    )

def serialize_iso(attr):
    if isinstance(attr, str):
        attr = isodate.parse_datetime(attr)
    utc = attr.utctimetuple()
    if utc.tm_year > 9999 or utc.tm_year < 1:
        raise OverflowError("Hit max or min date")

    microseconds = str(attr.microsecond).rjust(6,'0').rstrip('0').ljust(3, '0')
    if microseconds:
        microseconds = '.'+microseconds
    date = "{:04}-{:02}-{:02}T{:02}:{:02}:{:02}".format(
        utc.tm_year, utc.tm_mon, utc.tm_mday,
        utc.tm_hour, utc.tm_min, utc.tm_sec)
    return date + microseconds + 'Z'

def deserialize_iso(attr):
    if isinstance(attr, ET.Element):
        attr = attr.text
    attr = attr.upper()
    match = VALID_DATE.match(attr)
    if not match:
        raise ValueError("Invalid datetime string: " + attr)

    check_decimal = attr.split('.')
    if len(check_decimal) > 1:
        decimal_str = ""
        for digit in check_decimal[1]:
            if digit.isdigit():
                decimal_str += digit
            else:
                break
        if len(decimal_str) > 6:
            attr = attr.replace(decimal_str, decimal_str[0:6])

    date_obj = isodate.parse_datetime(attr)
    test_utc = date_obj.utctimetuple()
    if test_utc.tm_year > 9999 or test_utc.tm_year < 1:
        raise OverflowError("Hit max or min date")
    return date_obj

def deserialize_bytearray(attr):
    if isinstance(attr, ET.Element):
        attr = attr.text
    return bytearray(b64decode(attr))

def serialize_bytearray(attr):
    return b64encode(attr).decode()

def serialize_date(attr):
    if isinstance(attr, str):
        attr = isodate.parse_date(attr)
    t = "{:04}-{:02}-{:02}".format(attr.year, attr.month, attr.day)
    return t

def deserialize_duration(attr):
    if isinstance(attr, ET.Element):
        attr = attr.text
    return isodate.parse_duration(attr)

def serialize_duration(attr):
    if isinstance(attr, str):
        attr = isodate.parse_duration(attr)
    return isodate.duration_isoformat(attr)

def deserialize_rfc(attr):
    if isinstance(attr, ET.Element):
        attr = attr.text
    parsed_date = email.utils.parsedate_tz(attr)
    date_obj = datetime.datetime(
        *parsed_date[:6],
        tzinfo=_FixedOffset(datetime.timedelta(minutes=(parsed_date[9] or 0)/60))
    )
    if not date_obj.tzinfo:
        date_obj = date_obj.astimezone(tz=TZ_UTC)
    return date_obj

def deserialize_unix(attr):
    if isinstance(attr, ET.Element):
        attr = int(attr.text)
    return datetime.datetime.fromtimestamp(attr, TZ_UTC)

def serialize_unix(attr):
    if isinstance(attr, int):
        return attr
    return int(calendar.timegm(attr.utctimetuple()))

def deserialize_time(attr):
    if isinstance(attr, ET.Element):
        attr = attr.text
    return isodate.parse_time(attr)

def serialize_time(attr):
    if isinstance(attr, str):
        attr = isodate.parse_time(attr)
    t = "{:02}:{:02}:{:02}".format(attr.hour, attr.minute, attr.second)
    if attr.microsecond:
        t += ".{:02}".format(attr.microsecond)
    return t
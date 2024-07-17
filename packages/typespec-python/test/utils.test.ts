import { strictEqual } from "assert";
import { describe, it } from "vitest";
import { camelToSnakeCase } from "../src/utils.js";

describe("typespec-python: utils", () => {
    it("camelToSnakeCase", async () => {
        const cases = {
            "StandardSSD": "standard_ssd",
            "StandardSSD_LRS": "standard_ssdlrs",
            "QRCode": "qr_code",
            "MicroQRCode": "micro_qr_code",
            "detection_01": "detection01",
            "2020-02-15-preview.01": "2020_02_15_preview01",
            "v1.1-preview.1": "v1_1_preview1",
            "pointInTimeUTC": "point_in_time_utc",
            "diskSizeGB": "disk_size_gb",
            "lastModifiedTS": "last_modified_ts",
        };
        for (const [input, expected] of Object.entries(cases)) {
            strictEqual(camelToSnakeCase(input), expected);
        }
    });
});

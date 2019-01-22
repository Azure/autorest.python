# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .key_value_pair_py3 import KeyValuePair
    from .tag_py3 import Tag
    from .frame_py3 import Frame
    from .frames_py3 import Frames
    from .classification_category1_py3 import ClassificationCategory1
    from .classification_category2_py3 import ClassificationCategory2
    from .classification_category3_py3 import ClassificationCategory3
    from .classification_py3 import Classification
    from .status_py3 import Status
    from .email_py3 import Email
    from .ssn_py3 import SSN
    from .ipa_py3 import IPA
    from .phone_py3 import Phone
    from .address_py3 import Address
    from .pii_py3 import PII
    from .detected_terms_py3 import DetectedTerms
    from .screen_py3 import Screen
    from .face_py3 import Face
    from .found_faces_py3 import FoundFaces
    from .candidate_py3 import Candidate
    from .ocr_py3 import OCR
    from .evaluate_py3 import Evaluate
    from .match_py3 import Match
    from .match_response_py3 import MatchResponse
    from .detected_language_py3 import DetectedLanguage
    from .image_list_py3 import ImageList
    from .term_list_py3 import TermList
    from .refresh_index_py3 import RefreshIndex
    from .image_additional_info_item_py3 import ImageAdditionalInfoItem
    from .image_py3 import Image
    from .image_ids_py3 import ImageIds
    from .terms_in_list_py3 import TermsInList
    from .terms_data_py3 import TermsData
    from .terms_paging_py3 import TermsPaging
    from .terms_py3 import Terms
    from .review_py3 import Review
    from .job_execution_report_details_py3 import JobExecutionReportDetails
    from .job_py3 import Job
    from .job_list_result_py3 import JobListResult
    from .job_id_py3 import JobId
    from .error_py3 import Error
    from .api_error_py3 import APIError, APIErrorException
    from .body_py3 import Body
    from .create_review_body_item_metadata_item_py3 import CreateReviewBodyItemMetadataItem
    from .create_review_body_item_py3 import CreateReviewBodyItem
    from .content_py3 import Content
    from .transcript_moderation_body_item_terms_item_py3 import TranscriptModerationBodyItemTermsItem
    from .transcript_moderation_body_item_py3 import TranscriptModerationBodyItem
    from .body_model_py3 import BodyModel
    from .create_video_reviews_body_item_video_frames_item_reviewer_result_tags_item_py3 import CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem
    from .create_video_reviews_body_item_video_frames_item_metadata_item_py3 import CreateVideoReviewsBodyItemVideoFramesItemMetadataItem
    from .create_video_reviews_body_item_video_frames_item_py3 import CreateVideoReviewsBodyItemVideoFramesItem
    from .create_video_reviews_body_item_metadata_item_py3 import CreateVideoReviewsBodyItemMetadataItem
    from .create_video_reviews_body_item_py3 import CreateVideoReviewsBodyItem
    from .video_frame_body_item_reviewer_result_tags_item_py3 import VideoFrameBodyItemReviewerResultTagsItem
    from .video_frame_body_item_metadata_item_py3 import VideoFrameBodyItemMetadataItem
    from .video_frame_body_item_py3 import VideoFrameBodyItem
except (SyntaxError, ImportError):
    from .key_value_pair import KeyValuePair
    from .tag import Tag
    from .frame import Frame
    from .frames import Frames
    from .classification_category1 import ClassificationCategory1
    from .classification_category2 import ClassificationCategory2
    from .classification_category3 import ClassificationCategory3
    from .classification import Classification
    from .status import Status
    from .email import Email
    from .ssn import SSN
    from .ipa import IPA
    from .phone import Phone
    from .address import Address
    from .pii import PII
    from .detected_terms import DetectedTerms
    from .screen import Screen
    from .face import Face
    from .found_faces import FoundFaces
    from .candidate import Candidate
    from .ocr import OCR
    from .evaluate import Evaluate
    from .match import Match
    from .match_response import MatchResponse
    from .detected_language import DetectedLanguage
    from .image_list import ImageList
    from .term_list import TermList
    from .refresh_index import RefreshIndex
    from .image_additional_info_item import ImageAdditionalInfoItem
    from .image import Image
    from .image_ids import ImageIds
    from .terms_in_list import TermsInList
    from .terms_data import TermsData
    from .terms_paging import TermsPaging
    from .terms import Terms
    from .review import Review
    from .job_execution_report_details import JobExecutionReportDetails
    from .job import Job
    from .job_list_result import JobListResult
    from .job_id import JobId
    from .error import Error
    from .api_error import APIError, APIErrorException
    from .body import Body
    from .create_review_body_item_metadata_item import CreateReviewBodyItemMetadataItem
    from .create_review_body_item import CreateReviewBodyItem
    from .content import Content
    from .transcript_moderation_body_item_terms_item import TranscriptModerationBodyItemTermsItem
    from .transcript_moderation_body_item import TranscriptModerationBodyItem
    from .body_model import BodyModel
    from .create_video_reviews_body_item_video_frames_item_reviewer_result_tags_item import CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem
    from .create_video_reviews_body_item_video_frames_item_metadata_item import CreateVideoReviewsBodyItemVideoFramesItemMetadataItem
    from .create_video_reviews_body_item_video_frames_item import CreateVideoReviewsBodyItemVideoFramesItem
    from .create_video_reviews_body_item_metadata_item import CreateVideoReviewsBodyItemMetadataItem
    from .create_video_reviews_body_item import CreateVideoReviewsBodyItem
    from .video_frame_body_item_reviewer_result_tags_item import VideoFrameBodyItemReviewerResultTagsItem
    from .video_frame_body_item_metadata_item import VideoFrameBodyItemMetadataItem
    from .video_frame_body_item import VideoFrameBodyItem

__all__ = [
    'KeyValuePair',
    'Tag',
    'Frame',
    'Frames',
    'ClassificationCategory1',
    'ClassificationCategory2',
    'ClassificationCategory3',
    'Classification',
    'Status',
    'Email',
    'SSN',
    'IPA',
    'Phone',
    'Address',
    'PII',
    'DetectedTerms',
    'Screen',
    'Face',
    'FoundFaces',
    'Candidate',
    'OCR',
    'Evaluate',
    'Match',
    'MatchResponse',
    'DetectedLanguage',
    'ImageList',
    'TermList',
    'RefreshIndex',
    'ImageAdditionalInfoItem',
    'Image',
    'ImageIds',
    'TermsInList',
    'TermsData',
    'TermsPaging',
    'Terms',
    'Review',
    'JobExecutionReportDetails',
    'Job',
    'JobListResult',
    'JobId',
    'Error',
    'APIError', 'APIErrorException',
    'Body',
    'CreateReviewBodyItemMetadataItem',
    'CreateReviewBodyItem',
    'Content',
    'TranscriptModerationBodyItemTermsItem',
    'TranscriptModerationBodyItem',
    'BodyModel',
    'CreateVideoReviewsBodyItemVideoFramesItemReviewerResultTagsItem',
    'CreateVideoReviewsBodyItemVideoFramesItemMetadataItem',
    'CreateVideoReviewsBodyItemVideoFramesItem',
    'CreateVideoReviewsBodyItemMetadataItem',
    'CreateVideoReviewsBodyItem',
    'VideoFrameBodyItemReviewerResultTagsItem',
    'VideoFrameBodyItemMetadataItem',
    'VideoFrameBodyItem',
]

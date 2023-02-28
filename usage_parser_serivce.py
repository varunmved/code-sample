import json
import typing
from parser_models.parsed_object import ParsedObject
from exceptions import UsageParserServiceException


class UsageParserService:
    """
    The parser service that will handle inputs and return JSON
    """

    # @route('/create_parsed', @method=POST)
    def create_parsed_object(self, parse_request: str):
        parse_request_json = json.loads(parse_request)
        is_valid = validate_request(parse_request)
        return parse_request_json

    @staticmethod
    def validate_request(parse_request:str):
        if ',' not in parse_request
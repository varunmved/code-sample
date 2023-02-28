import json
import re
from usage_parser import UsageParser


class UsageParserServiceException(Exception):
    pass


class UsageParserService:
    """
    The parser service that will handle inputs and return JSON in some web api layer
    """

    # @route('/create_parsed', @method=POST)
    def create_parsed_object(self, parse_request: str):
        request_string = json.loads(parse_request)
        self.validate_request(parse_request)
        UsageParser.parse(request_string)

    @staticmethod
    def validate_request(parse_request: str):
        if ',' not in parse_request:
            raise UsageParserServiceException
        if re.search('[a-zA-Z]', parse_request):
            raise UsageParserServiceException

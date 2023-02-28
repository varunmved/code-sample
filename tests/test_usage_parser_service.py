import typing
import unittest

from usage_parser_serivce import UsageParserService

class TestCreateParsedObject(unittest.TestCase):
    input: str
    expected: typing.List[typing.Mapping[str, typing.Any]]

    def setUp(self):
        self.input = '7291,293451'
        self.expected = dict(
                id=7291,
                bytes_used=293451,
                cellid=None,
                dmcc=None,
                ip=None,
                mnc=None,
            )
        
        self.usage_parser_service = UsageParserService()

    def test_response_ok(self):
        self.assertListEqual(
            self.usage_parser_service.create_parsed_object(self.input),
            self.expected
        )

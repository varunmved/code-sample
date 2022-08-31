import typing
from parser_objects.parsed_object import ParsedObject


class UsageParser:

    def parse(self, *input: str) -> typing.List[typing.Mapping[str, typing.Any]]:
        outlist = []
        for data_string in input:
            outlist.append(self.parse_helper(data_string))

        return outlist

    def parse_helper(self, data_string: str):
        split_data_string = data_string.split(',')
        id = split_data_string[0]
        if id[-1] == '4':
            return self.parse_extended(id, split_data_string)
        if id[-1] == '6':
            print(id, split_data_string)
            return self.parse_hex(id, split_data_string)
        else:
            return self.parse_basic(id, split_data_string)

    def parse_basic(self, id, data_string: typing.List):
        parsed_object = ParsedObject(id=id, bytes_used=data_string[1])
        return parsed_object.to_dict()

    def parse_extended(self, id: int, data_string: typing.List):
        parsed_object = ParsedObject(
            id=id,
            dmcc=data_string[1],
            mnc=data_string[2],
            bytes_used=data_string[3],
            cellid=data_string[4]
        )
        return parsed_object.to_dict()

    def parse_hex(self, id: int, data_string: typing.List):
        hex_string = data_string[1]
        mnc = int(hex_string[0:4], 16)
        bytes_used = int(hex_string[4:8], 16)
        cellid = int(hex_string[8:16], 16)
        ip = UsageParser.generate_ip_from_hex(hex_string[16:24])

        parsed_object = ParsedObject(
            id,
            mnc=mnc,
            bytes_used=bytes_used,
            cellid=cellid,
            ip=ip)

        return parsed_object.to_dict()

    @staticmethod
    def generate_ip_from_hex(ip_as_hex):
        ip_as_string = ''
        for i in range(0, len(ip_as_hex), 2):
            ip_as_string += str(int(ip_as_hex[i:i+2], 16)) + '.'
        return ip_as_string[:-1]

import typing
from parser_models.parsed_object import ParsedObject


class UsageParser:
    """
    The parser class that handles business logic for how each string is parsed
    """

    def parse(self, *input: str) -> typing.List[typing.Mapping[str, typing.Any]]:
        output = []
        for unparsed in input:
            output.append(self.generate_parsed_string(unparsed))

        return output

    def generate_parsed_string(self, unparsed: str):
        """
        a helper method to determine which parser to call and to build the solution for each input
        """
        split_data_string = unparsed.split(',')
        # id is always the first item in the , separated list
        id = split_data_string[0]

        # determine which parser to call based on last digit of id
        if id[-1] == '4':
            return self.parse_extended(id, split_data_string)
        if id[-1] == '6':
            print(id, split_data_string)
            return self.parse_hex(id, split_data_string)
        else:
            return self.parse_basic(id, split_data_string)

    def parse_basic(self, id: int, split_data: typing.List):
        """
        parse basic strings, we only need the bytes_used which is always the first element
        """
        parsed_object = ParsedObject(id=id, bytes_used=split_data[1])
        return parsed_object.to_dict()

    def parse_extended(self, id: int, split_data: typing.List):
        """
        parse extended strings, no logic here except passing the comma separated values
        """
        parsed_object = ParsedObject(
            id=id,
            dmcc=split_data[1],
            mnc=split_data[2],
            bytes_used=split_data[3],
            cellid=split_data[4]
        )
        return parsed_object.to_dict()

    def parse_hex(self, id: int, split_data: typing.List):
        """
        parse hex strings, we can slice the string by index given the # of bytes provided in the prolem statement
        """
        hex_data = split_data[1]
        mnc = int(hex_data[0:4], 16)
        bytes_used = int(hex_data[4:8], 16)
        cellid = int(hex_data[8:16], 16)
        # seperate method for readability
        ip = UsageParser.generate_ip_from_hex(hex_data[16:24])

        parsed_object = ParsedObject(
            id,
            mnc=mnc,
            bytes_used=bytes_used,
            cellid=cellid,
            ip=ip)

        return parsed_object.to_dict()

    @staticmethod
    def generate_ip_from_hex(ip_as_hex: str):
        """
        convert the ip from a hex string to the ip format
        every pair of bytes is a hex, so convert and add a '.' at the end
        remove the last period when returning
        """
        ip_as_string = ''
        for i in range(0, len(ip_as_hex), 2):
            ip_as_string += str(int(ip_as_hex[i:i+2], 16)) + '.'
        return ip_as_string[:-1]

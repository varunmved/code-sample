
class ParsedObject:
    """
    a simple ParsedObject class that will handle the type conversion
    if we ever need to extend the functionality of how the parsed data is stored, it can be done in this class
    """

    def __init__(self, id, **kwargs):
        """
        the init handles all the data type changes
        """
        self.id = int(id)
        self.bytes_used = int(kwargs.get('bytes_used')
                              ) if kwargs.get('bytes_used') else None
        self.cellid = int(kwargs.get('cellid')) if kwargs.get(
            'cellid') else None
        self.dmcc = str(kwargs.get('dmcc')) if kwargs.get('dmcc') else None
        self.ip = str(kwargs.get('ip')) if kwargs.get('ip') else None
        self.mnc = int(kwargs.get('mnc')) if kwargs.get('mnc') else None

    def to_dict(self):
        """
        use python's built in to_dict to return class variables as a key/value pair
        """
        return vars(self)

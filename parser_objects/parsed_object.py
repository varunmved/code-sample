class ParsedObject:
    
    def __init__(self, id, **kwargs):
        self.id = int(id)
        self.bytes_used = int(kwargs.get('bytes_used')) if kwargs.get('bytes_used') else None
        self.cellid = int(kwargs.get('cellid')) if kwargs.get('cellid') else None
        self.dmcc = str(kwargs.get('dmcc')) if kwargs.get('dmcc') else None
        self.ip = str(kwargs.get('ip')) if kwargs.get('ip') else None
        self.mnc = int(kwargs.get('mnc')) if kwargs.get('mnc') else None

    def to_dict(self):
        return vars(self)
    
class MapList:
    def __init__(self):
        self._table : dict[str, list] = dict()
    
    def add(self, key : str, value):
        if key in self._table.keys():
            self._table[key].append(value)
            return
        self._table[key] = [value]
    
    def get_table(self):
        return self._table
    
    def __str__(self):
        return str(self._table)
    
    def __repr__(self):
        return repr(self._table)
        

import json

class Database:
    def __init__(self, base_file):
        self.base_file = base_file
        
    def add(self, item):
        with open(self.base_file, "r") as handle:
            db = json.loads(handle.read())
            key = str(list(map(int, list(db.keys())))[-1]+1)
            db[key] = item 
            
        with open(self.base_file, "w") as handle:
            json.dump(db, handle, ensure_ascii=False, indent=4)
            return key
    
    def sub(self, index):
        with open(self.base_file, "r") as handle:
            db = json.loads(handle.read())
            del db[str(index)]
            
        with open(self.base_file, "w") as handle:
            json.dump(db, handle, ensure_ascii=False, indent=4)
            
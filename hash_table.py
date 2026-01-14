class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self,value: str):
        total = 0
        for char in value:
            total += ord(char)
        return total
            
    def add(self,key,value):
        hashed_key =self.hash(key)
        if hashed_key not in self.collection:
            self.collection[hashed_key] = {key:value}
        else:
            self.collection[hashed_key][key] = value
    def remove(self,key):
        hashed_key =self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                del self.collection[hashed_key][key]

        
    def lookup(self,key):
        hashed_key =self.hash(key)
        if hashed_key in self.collection:
            if key in self.collection[hashed_key]:
                return self.collection[hashed_key][key]
        return None

hash_1 = HashTable()

print(hash_1.collection)
hash_1.add("amne","zombie")
print(hash_1.collection)
hash_1.remove("amne")
print(hash_1.collection)
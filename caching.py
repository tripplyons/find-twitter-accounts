import pickle
import gzip

class Cache:
    def __init__(self, path):
        self.path = path
        self.data = {}
        self.load()
    
    def load(self):
        try:
            with gzip.open(self.path, 'rb') as f:
                self.data = pickle.load(f)
        except:
            pass
    
    def save(self):
        with gzip.open(self.path, 'wb') as f:
            pickle.dump(self.data, f)

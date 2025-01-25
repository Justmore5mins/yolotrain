import os

class Folder:
    def init(self, path:str):
        self.path = path
        if not os.path.isdir(path):
            raise ValueError("The path must be folder")
        self.isDataset = "data.yaml" in os.listdir(path)
        
class WTFRUDoin(Exception):
    def __init__(self, *args):
        super().__init__(*args)
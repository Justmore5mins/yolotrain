from ultralytics import YOLO
from packages import *

class Train:
    def __init__(self, model:str, dataset:Folder, device:str|int|list[int] = "cpu",verbose:bool = True):
        '''
        This class can train models from given model like yolo11n.pt
        '''
        self.model = YOLO(model,verbose)
        if not dataset.isDataset:
            raise ValueError("The folder must be a dataset")
        self.dataset = dataset.path
        self.model.to(device) if device != "cpu" else None
        
    def train(self, epochs:int = 100, batch_size:int = None, resume:bool = False, cache:bool = False):
        '''
        start the training process
        '''
        self.model.train(dataset=self.dataset, epochs=epochs, batch_size=batch_size, resume=resume, cache=cache)
        
    def export(self, model:str, format:str, data:Folder = None, half:bool = False):
        if not data.isDataset:
            raise ValueError("The folder must be YOLO dataset")
        self.model.export(model, format, data.path, half)
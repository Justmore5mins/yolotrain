from ultralytics import YOLO
from cv2 import VideoCapture

class Detect:
    def __init__(self,model:str,src:int|str|list[str]|VideoCapture,device:str|int|list[int] = "cpu",verbose:bool = False):
        self.model = YOLO(model,verbose)
        self.mode.to(device) if device != "cpu" else None
        if type(src) in [int, str]:
            self.source = [VideoCapture(src)]
        elif type(src) == list:
            self.source = [VideoCapture(i) for i in src]
        else:
            self.source = [src]
            
    def detect(self):
        for src in self.source:
            success = True
            while success:
                success, frame = src.read()
                result = self.model(frame,stream=True)
                for res in result:
                    for box in res.boxes:
                        x1,y1,x2,y2 = box.xyxy
                        confidence = box.conf.item()
                        cls = int(box.cls)
                        print(f"Detected {self.model.names[cls]} with confidence {confidence*100}% at {x1,y1,x2,y2}",flush=True)
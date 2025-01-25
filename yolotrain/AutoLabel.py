from ultralytics import YOLO
from packages import *
from cv2 import imread

class Autolabel:
    def __init__(self, model:str, dataset:Folder, target:str, device:str|int|list[int] = "cpu"):
        '''
        This class can autolabel images from pretrained model like yolo11n.pt
        '''
        self.model = YOLO(model)
        if dataset.isDataset:
            raise WTFRUDoin("The folder is a complete dataset.")
        self.dataset = dataset.path
        if not os.path.isdir(target):
            raise WTFRUDoin("The target must be a folder.")
        self.model.to(device) if device != "cpu" else None
        
    def start(self, output:str = "labels"):
        '''
        start the autolabeling process
        '''
        ImageLeft:int = len(os.listdir(self.dataset))
        if not os.path.isdir(output):
            os.mkdir(output)
        while ImageLeft >= 0:
            for img in os.listdir(self.dataset):
                img = imread(f"{self.dataset}/{img}")
                result = self.model(img,stream=True)
                with open(f"{output}/{img}.txt","w") as f:
                    for res in result:
                        for box in res.boxes:
                            x,y,w,h = box.xywh
                            confidence = box.conf.item()
                            cls = int(box.cls)
                            print("{} detected {} with confidence {} at {},{},{},{}".format(img,self.model.names[cls],confidence*100,x,y,w,h),flush=True)
                            f.write("{} {} {} {} {}".format(cls,x,y,w,h))
                        
            ImageLeft -= 1
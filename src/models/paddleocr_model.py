from paddleocr import PaddleOCR, draw_ocr
import paddleocr
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import numpy as np


def get_model(lang="en"):
    '''
    Get model with language specified
    '''
    return PaddleOCR(lang=lang)

def get_bounding_box(model, img):
    '''
    Get bounding box with model and img
    Model: from get_model
    img: can be either path or np array
    '''
    return np.array(model.ocr(img, rec=False))

def get_text_from_bounding_box(model, img, boxes = None):
    '''
    Get text from bounding box
    model: from get_model
    boxes: np array indicate boxes position
    img: image, path or np array
    If boxes = None, so PaddleOCR will automatically get text from img
    '''
    if boxes is None:
        result = model.ocr(img)[0]
        texts = [res[1][0] for res in result]
        return "\n".join(texts)
    
    if isinstance(img, str):
        img = cv2.imread(img)
        img =np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    texts =[]
    for pos in boxes[0]:
        pos= np.array(pos)
        x_min = int(np.min(pos[:,0]))
        x_max = int(np.max(pos[:,0]))
        y_min = int(np.min(pos[:,1]))
        y_max = int(np.max(pos[:,1]))
        text, _ = model.ocr(img[y_min:y_max,x_min:x_max, :], det=False)[0][0]
        texts.append(text)
    return "\n".join(texts)

if __name__ == "__main__":
    # Testing purposes
    model = get_model()
    boxes = get_bounding_box(model, "../../data/no-text/tree-736885_1280.jpg")

    

    print(get_text_from_bounding_box(model,"../../data/no-text/tree-736885_1280.jpg",boxes))
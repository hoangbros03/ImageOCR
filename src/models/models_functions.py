from paddleocr import PaddleOCR, draw_ocr
import paddleocr
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import numpy as np
from mmocr.apis import MMOCRInferencer
from models_functions import text_detection_dict, text_recognition_dict


def get_bounding_box_PaddleOCR(model_name, img):
    '''
    Get bounding box with model and img
    Model_name: string - model name
    img: can be either path or np array
    '''
    if model_name in text_detection_dict['PaddleOCR']:
        model=PaddleOCR(lang="en")
        return np.array(model.ocr(img, rec=False))
    else:
        infer = MMOCRInferencer(det=model)
        result = infer(img, return_vis=True)
        return np.array(result['predictions'][0]['det_polygons'])

def get_text_from_bounding_box(model, img, boxes = None):
    '''
    Get text from bounding box
    model: from get_model
    boxes: np array indicate boxes position
    img: image, path or np array
    If boxes = None, so model (PaddleOCR) will automatically get text from img
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

def get_bounding_box_mmocr(model, img):
    '''
    Get bounding box using mmocr
    '''
    


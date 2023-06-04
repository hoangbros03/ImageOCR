from paddleocr import PaddleOCR, draw_ocr
import paddleocr
import matplotlib.pyplot as plt
import cv2
import os
from PIL import Image
import numpy as np

from mmocr.apis import MMOCRInferencer
from .models_list import text_detection_dict, text_recognition_dict


def get_bounding_box(model_name, img):
    """
    Get bounding box with model and img
    Args:
    Model_name: string - model name
    img: can be either path or np array
    Return:
    The np array that contains the bounding box. Can be in any shape.
    """
    if model_name in text_detection_dict["PaddleOCR"]:
        model = PaddleOCR(lang="en")
        return np.array(model.ocr(img, rec=False))
    elif model_name in text_detection_dict["mmocr"]:
        infer = MMOCRInferencer(det=model_name)
        result = infer(img, return_vis=True)
        # print("result 2 get bb: ",result)
        result = np.array(result["predictions"][0]["det_polygons"])
        print("Result shape: ", result.shape)
        return result
    else:
        print("wrong model name!")
        return None


def get_text_from_bounding_box(model_name: str, img, boxes=None):
    """
    Get text from bounding box
    Args:
    model_name: name of the model
    boxes: np array indicate boxes position
    img: image, path or np array
    Return:
    Texts that generated from bounding boxes
    If boxes = None, so model (PaddleOCR) will automatically get text from img
    """
    # Reshape if bounding box is made from mmocr
    boxes = np.array(boxes)
    if boxes.ndim != 4:
        boxes = boxes.reshape((1, -1, 4, 2))
        print("boxes shape: ", boxes.shape)

    # Make instance of model if needed
    if model_name in text_recognition_dict["PaddleOCR"]:
        model = PaddleOCR(lang="en")
    elif model_name in text_recognition_dict["mmocr"]:
        infer = MMOCRInferencer(rec=model_name)
    else:
        return "Wrong model name. Please re-check!"

    if boxes is None:
        model = PaddleOCR(lang="en")
        result = model.ocr(img)[0]
        texts = [res[1][0] for res in result]
        return "\n".join(texts)

    if isinstance(img, str):
        img = cv2.imread(img)
        img = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    texts = []

    for pos in boxes[0]:
        pos = np.array(pos)
        x_min = int(np.min(pos[:, 0]))
        x_max = int(np.max(pos[:, 0]))
        y_min = int(np.min(pos[:, 1]))
        y_max = int(np.max(pos[:, 1]))
        if model_name in text_recognition_dict["PaddleOCR"]:

            text, _ = model.ocr(img[y_min:y_max, x_min:x_max, :], det=False)[0][0]
        elif model_name in text_recognition_dict["mmocr"]:

            text = infer(
                img[y_min:y_max, x_min:x_max, :], save_vis=True, return_vis=True
            )
            # print("Text: ", text)
            text = " ".join(text["predictions"][0]["rec_texts"])
        texts.append(text)
    return "\n".join(texts)

import argparse
from src.models.models_functions import *


parser = argparse.ArgumentParser(
    description="Parser for specifying the model to do the OCR"
)
parser.add_argument("--img_path", dest="img_path",type=str, help="path for img")

parser.add_argument(
    "--detect",
    type=str,
    dest="text_detection",
    help="choose model to detect the texts",
    default="paddleocr",
)
parser.add_argument(
    "--recog",
    type=str,
    dest="text_recognition",
    help="choose model to recognize the texts",
    default="paddleocr",
)
parser.add_argument(
    "--postprocess",
    dest="postprocess",
    type=bool,
    help="Choose to post processing the text or not",
    default=False,
)

args = parser.parse_args()


def get_text(text_detection='PaddleOCR', text_recognition="PaddleOCR", url= None):
    '''
    Get text from an image (both text detection and text recognition)
    Parameters:
    text_dectection: Options for text detection
    text_recognition: Options for text recognition
    url: Image address (locally)
    Output:
    text
    '''
    if text_detection =="YOLO":
        return "text detection YOLO is not supported yet. Please choose others."
    elif url is None:
        return "URL isn't provided"
    else:
        model = get_model_PaddleOCR()
        boxes = get_bounding_box_PaddleOCR(model, url)
        texts = get_text_from_bounding_box_PaddleOCR(model, url, boxes)
        return texts

if __name__=="__main__":
    get_text()

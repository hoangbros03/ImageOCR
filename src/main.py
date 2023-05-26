import argparse
from models.paddleocr_model import *


parser = argparse.ArgumentParser(description="Parser for specifying the model to do the OCR")
parser.add_argument("img_path", type=str, help="path for img")

parser.add_argument("--detect", type=str, dest="text_detection", help="choose model to detect the texts", default="paddleocr" )
parser.add_argument("--recog", type= str, dest="text_recognition", help="choose model to recognize the texts", default="paddleocr")
parser.add_argument("--postprocess", dest="postprocess", type=bool, help="Choose to post processing the text or not", default= False )

args=parser.parse_args()

model = get_model()
boxes = get_bounding_box(model, args.img_path)
texts = get_text_from_bounding_box(model, args.img_path,boxes)
print("Result: ")
print(texts)

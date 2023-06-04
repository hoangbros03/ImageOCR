import sys
sys.path.append("models/mmocr")
from src.mainProgram import get_text
from src.models.models_list import *
options=get_options()

def test_image_to_text(check_det = ['PaddleOCR','dbnetpp'], check_rec= ['PaddleOCR', 'svtr-small'], url = "data/en-text/1.jpg"):
    '''
    Check if image ocr is working
    Args:
    check_det: List of detection models
    check_rec: List of recognition models
    url: Url to the local image
    '''
    img_link = url
    check_det = check_det
    check_rec = check_rec
    num=1
    for i in check_det:
        for j in check_rec:
            texts = get_text(i,j,url=img_link)
            print(f"check #{num}:\n",texts,"\n")
            num+=1

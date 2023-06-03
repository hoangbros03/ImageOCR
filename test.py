import sys
sys.path.append("models/mmocr")
from src.mainProgram import get_text
from src.models.models_list import *
options=get_options()

img_link = "data/en-text/1.jpg"

check_det = ['PaddleOCR','dbnetpp']
check_rec = ['PaddleOCR', 'svtr-small']
num=1
for i in check_det:
    for j in check_rec:
        texts = get_text(i,j,url=img_link)
        print(f"check #{num}:\n",texts,"\n")
        num+=1

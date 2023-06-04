
# Image OCR Project
This is a web application that extracts texts from images.
## Introduction

This product will help you get the texts from an image. What you have to do is only upload your image, select the models, click the submit button, and see the magic! On the other hand, it also supports converting from pdf to images, which would be useful for whom having pdf file(s).
## How it works

In fact, this web application takes advantages from open-source projects (PaddleOCR and mmocr). 


In the recent years, numerous OCR models was invented by researchers. However, each of these models has its own strengh and weeknesses. As a result, different images (scene image and document image for example) need to use different models to achieve the best result. Image OCR Project was created based on that idea.

The workflow of the Image OCR Project feature works as follows: when a user submits an image containing text, the application sends it to the OCR models (both text detection model and text recognition model), which processes it using PaddleOCR and/or mmocr. These engines then analyze the image and extract the text content from it. Finally, the extracted text is sent back to the user in textarea, allowing user for editing and copying.

Language support: English.

`PaddleOCR aims to create multilingual, awesome, leading, and practical OCR tools that help users train better models and apply them into practice.`


`MMOCR is an open-source toolbox based on PyTorch and mmdetection for text detection, text recognition, and the corresponding downstream tasks including key information extraction.`



## Features

- Detect text with following model: PaddleOCR, MaskCRNN, DRBG, FCENet, PANet_CTW, dbnetpp. You can also add some models if interested by modify the `models_list.py` file.

- Recognize text with following model: PaddleOCR, ABINet_Vision, ASTER, CRNN, MASTER, svtr-small. You can also add some models if interested by modify the `models_list.py` file.

- Convert pdf to images. Images will be grouped in a .zip files that user can download it.

There are also some other fun features like make contact or purchase the VIP plan, but it's on the developing. I will update it in the future.
## How to install

These steps below will help you install and run this web application. Beside pip and python, you should have Anaconda installed to separate environments and avoid future errors.

Notice: Steps may vary on different OS-es and computers. There may be minor problems when following, but the general idea is remain the same

Step 1: Create new conda env: `conda create --name YOUR_ENV_NAME`

Step 2: Clone this repo: `git clone https://github.com/hoangbros03/ImageOCR.git`

Step 3: Move to repo folder: `cd ImageOCR`

Step 4: Install all packages in requirements.txt file: `pip install -r requirements.txt `

Step 5: Make 'models' folder. This will be used to store paddleOCR and mmocr repos

Step 6: Move to models folder and clone these 2 repos:

`cd models`

`git clone https://github.com/PaddlePaddle/PaddleOCR.git`

`git clone https://github.com/open-mmlab/mmocr.git`

Step 7: Follow the instruction to install necessary packages for 2 repos. Please review the docummentation associated with these repos for details.

Step 8: Back to the main repo folder and run app.py: `python app.py`

Step 9: Go to `localhost:8000`. Enjoying <3
## Usage

### Extract texts from image
Step 1: Upload image you want to extract the text. Remember that only image is accepted.

Step 2: Choose text detection model (default is PaddleOCR)

Step 3: Choose text recognition model (default is PaddleOCR)

Step 4: Click submit

### Convert pdf to image

Step 1: Upload pdf file you want to extract the images. Remember that only .pdf file is accepted.

Step 3: Click submit

Step 3: Click download to download the .zip file
## Citations
There are resources that helps me a lot to complete this project:
 - [Paddle OCR](https://github.com/PaddlePaddle/PaddleOCR)
 - [mmocr](https://github.com/open-mmlab/mmocr)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)



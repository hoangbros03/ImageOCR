import argparse
from .models.models_functions import get_bounding_box, get_text_from_bounding_box
from .models.models_list import get_options

parser = argparse.ArgumentParser(
    description="Parser for specifying the model to do the OCR"
)
parser.add_argument("--img_path", dest="img_path", type=str, help="path for img")

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
options = get_options()


def get_text(text_detection="PaddleOCR", text_recognition="PaddleOCR", url=None):
    """
    Get text from an image (both text detection and text recognition)
    Parameters:
    text_dectection: Options for text detection
    text_recognition: Options for text recognition
    url: Image address (locally)
    Output:
    text
    """
    if text_detection == "YOLO":
        return "text detection YOLO is not supported yet. Please choose others."
    elif url is None:
        return "URL isn't provided"
    else:
        # Check model name valid
        if (
            text_detection in options["textDetectionOptions"]
            and text_recognition in options["textRecognitionOptions"]
        ):
            boxes = get_bounding_box(model_name=text_detection, img=url)
            texts = get_text_from_bounding_box(
                model_name=text_recognition, img=url, boxes=boxes
            )
        else:
            texts = "Wrong model names (either in Text det or rec)"
        return texts


if __name__ == "__main__":
    """
    For some reasons, please run the Flask app instead of running this file.
    """
    print(options)

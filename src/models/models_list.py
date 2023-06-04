text_detection_dict = {
    "PaddleOCR": ["PaddleOCR"],
    "mmocr": ["MaskRCNN", "DRRG", "FCENet", "PANet_CTW", "dbnetpp"],
}

text_recognition_dict = {
    "PaddleOCR": ["PaddleOCR"],
    "mmocr": ["ABINet_Vision", "ASTER", "CRNN", "MASTER", "svtr-small"],
}


def get_options():
    """
    get an dict that contain both text rec and det with 2 flatten lists separated
    """
    options = {"textDetectionOptions": [], "textRecognitionOptions": []}
    for i in text_detection_dict.keys():
        for j in text_detection_dict[i]:
            options["textDetectionOptions"].append(j)
    for i in text_recognition_dict.keys():
        for j in text_recognition_dict[i]:
            options["textRecognitionOptions"].append(j)
    return options

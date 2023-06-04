# To preload the model in mmocr
from src.models.models_list import *
from mmocr.apis import MMOCRInferencer


def preload_models():
    """
    preload the mmocr models, ensure that checkpoints are downloaded
    """
    options = get_options()
    num = 1
    total = len(options["textDetectionOptions"]) + len(
        options["textRecognitionOptions"]
    )
    for i in options["textDetectionOptions"]:
        infer = MMOCRInferencer(det=i)
        print(f"Loaded {num}/{total} models")
        num += 1

    for i in options["textRecognitionOptions"]:
        infer = MMOCRInferencer(rec=i)
        print(f"Loaded {num}/{total} models")
        num += 1

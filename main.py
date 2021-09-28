import fire
import numpy as np
from PIL import Image
from easyocr import Reader

from settings import settings


def get_image_l(
        path: str,
):
    """
    Get image
    :param path: Path to image in local file storage
    :return: Image pixels matrix
    """

    image = Image.open(path)
    image = image.convert('L')
    image = np.array(image)

    return image


def read(
        path: str,
        additional_info: bool = True,
        reader_settings: dict = settings.get('reader'),
):
    """
    Get text from image
    :param path: Path to image in local file storage
    :param additional_info: Return or not additional info
    :param reader_settings: EasyOCR Reader settings
    :return: Parsed text
    """

    reader = Reader(**reader_settings)

    path = path.strip()
    image = get_image_l(path)
    prediction = reader.readtext(image)

    if additional_info:
        prediction = ' '.join([_[1] for _ in prediction])

    return prediction


if __name__ == '__main__':
    fire.Fire()

import os
import fire
import numpy as np
from PIL import Image
from easyocr import Reader

from settings import settings


class TextReader:
    def __init__(
            self,
            reader_settings: dict,
    ):
        self.__reader = Reader(**reader_settings)

    def read_local(
            self,
            path: str,
            additional_info: bool = True,
    ):
        """
        Get text from image
        :param path: Path to image in local file storage
        :param additional_info: Return or not additional info
        :return: Parsed text
        """

        path = path.strip()
        image = self._get_image(path)
        prediction = self.__reader.readtext(image)

        if additional_info:
            prediction = ' '.join([_[1] for _ in prediction])

        return prediction

    def read_local_map(
            self,
            path: str,
            additional_info: bool = True,
    ):
        """
        Get text from images from directory
        :param path: Path to directory with images
        :param additional_info: Return or not additional info
        :return: Parsed texts
        """

        images = os.listdir(path)
        images = [os.path.join(path, image) for image in images]

        for image in images:
            yield self.read_local(image, additional_info)

    @staticmethod
    def _get_image(
            path: str,
    ):
        """
        Get image
        :param path: Path to image in local file storage
        :return: Image pixels matrix
        """

        image = Image.open(path)
        image = image.convert('RGB')
        image = np.array(image)

        return image


def read_local(
        path: str,
        additional_info: bool = True,
        reader_settings=settings.get('reader'),
):
    reader = TextReader(reader_settings)
    return reader.read_local(path, additional_info)


if __name__ == '__main__':
    fire.Fire()

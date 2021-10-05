# Copyright Pincer 2021-Present
# Full MIT License can be found in `LICENSE` at the project root.

from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
import os
from typing import Optional

from PIL.Image import Image

from ...utils import APIObject


@dataclass
class File(APIObject):
    """
    A file that is prepared by the user to be send to the discord
    API.

    :param content:
        File bytes.

    :param filename:
        The name of the file when its uploaded to discord.
    """

    content: bytes
    filename: str

    @classmethod
    def from_file(cls, filepath: str, filename: str = None) -> File:
        """
        :param filepath:
            The path to the file you want to send. Must be string. The file's
            name in the file path is used as the name when uploaded to discord
            by default.

        :param filename:
            The name of the file. Will override the default name.
        """

        with open(filepath, "rb") as data:
            file = data.read()

        return cls(
            content=file,
            filename=filename or os.path.basename(filepath)
        )

    @classmethod
    def from_pillow_image(
            cls,
            img: Image,
            filename: str,
            image_format: Optional[str] = None,
            **kwargs
    ) -> File:
        """
        Creates a file object from a PIL image
        Supports GIF, PNG, JPEG, and WEBP.

        :param img:
            Pillow image object.

        :param filename:
            The filename to be used when uploaded to discord. The extension is
            used as image_format unless otherwise specified.

        Keyword Arguments:

        :param image_format:
            The image_format to be used if you want to override the file
            extension.

        :return: File
        """

        if image_format is None:
            image_format = os.path.splitext(filename)[1][1:]

            if image_format == "jpg":
                image_format = "jpeg"

<<<<<<< HEAD
        imgByteArr = BytesIO()
        img.save(imgByteArr, format=image_format, **kwargs)
        img_bytes = imgByteArr.getvalue()
=======
        # https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array
        # Credit goes to second answer
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format=image_format)
        img_bytes = img_byte_arr.getvalue()
>>>>>>> 8395b2b8e666b0ab72d3699e0d393455403f6d1d

        return cls(
            content=img_bytes,
            filename=filename
        )

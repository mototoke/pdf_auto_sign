#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
from pdf2image import convert_from_path
from src.utils.img_type_convert import pil2cv


class PdfToImage:
    def __init__(self):
        import platform
        pf = platform.system()
        if pf == 'Windows':
            print('on Windows')
            # poppler/binを環境変数PATHに追加する
            poppler_dir = Path(__file__).parent.absolute() / "poppler-0.68.0/bin"
            os.environ["PATH"] += os.pathsep + str(poppler_dir)

    @staticmethod
    def convert_to_images(pdf_file: str):
        """
        pdfを画像に変換します
        :param pdf_file:
        :return:
        """
        # PDFファイルのパス
        pdf_path = Path(pdf_file)

        # PDF -> Image に変換（200dpi）
        images = convert_from_path(str(pdf_path), 200, grayscale=True)
        result = []
        for i, image in enumerate(images):
            # PIL形式からOpenCv(numpy)形式に変換
            img = pil2cv(image)
            result.append(img)

        return result

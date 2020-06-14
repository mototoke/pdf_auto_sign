#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
import numpy as np


def show_pdf_analysis(pdf_path):
    """
    pdf情報の表示
    :param pdf_path:
    :return:
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page_first = pdf_reader.getPage(0)
        print(pdf_reader)
        print(page_first)
        print(page_first.mediaBox.upperLeft)
        print(page_first.mediaBox.upperRight)
        print(page_first.mediaBox.lowerRight)
        print(page_first.mediaBox.lowerLeft)
        print(page_first.get('/Rotate'))


def get_pdf_4coordinate(pdf_path) -> list:
    """
    pdfの1ページ目から左上、右上、右下、 左下、の各4点の座標リストを取得します。(単位：mm)
    :param pdf_path:
    :return:
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        page_first = pdf_reader.getPage(0)
        pts_arr = [
            [page_first.mediaBox.upperLeft[0], page_first.mediaBox.upperLeft[1]],
            [page_first.mediaBox.upperRight[0], page_first.mediaBox.upperRight[1]],
            [page_first.mediaBox.lowerRight[0], page_first.mediaBox.lowerRight[1]],
            [page_first.mediaBox.lowerLeft[0], page_first.mediaBox.lowerLeft[1]]
        ]
        print(f"PDF:pts_arr:{pts_arr}")
        mm_arr = [
            [pts_to_mm(i[0]), pts_to_mm(i[1])] for i in pts_arr
        ]
        print(f"PDF:mm_arr:{mm_arr}")

        return mm_arr


def get_image_4coordinate(img: np.ndarray) -> list:
    """
    画像から左上、右上、右下、 左下、の各4点の座標リストを取得します。(単位：mm)
    :param img:
    :return:
    """
    h, w = img.shape[0], img.shape[1]
    arr = [
        [0.0, 0.0],
        [w, 0.0],
        [w, h],
        [0.0, h]
    ]
    print(f"Image:arr:{arr}")

    return arr


def pts_to_mm(pts) -> float:
    """
    ptsからmmに変換します
    ページサイズの計算方法
    Page sizeの単位は、ptsです。例えば、横幅が420 ptsだと、420 pts / 72 (pts/inch) * 25.4 (mm/inch) = 148 mmでA5となります
    ※ 72 (pts/inch) * 25.4 (mm/inch) ≒  0.352778
    :param pts:
    :return:
    """
    return float(pts) * 0.352778


def mm_to_pts(mm) -> float:
    """
    mmからptsに変換します
    ページサイズの計算方法
    Page sizeの単位は、ptsです。例えば、横幅が420 ptsだと、420 pts / 72 (pts/inch) * 25.4 (mm/inch) = 148 mmでA5となります
    ※ 72 (pts/inch) * 25.4 (mm/inch) ≒  0.352778
    :param mm:
    :return:
    """
    return float(mm) / 0.352778


if __name__ == '__main__':
    test = 'C:/sample2.pdf'
    get_pdf_4coordinate(test)

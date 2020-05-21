#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PdfEditor:
    def __init__(self):
        pass

    @staticmethod
    def insert_text_output_pdf(pdf_file_path, target_coordinate, insert_text):
        """
        既存のPDFファイルに文字を挿入し、別名で出力します
        :param pdf_file_path:       既存のPDFファイルパス
        :param target_coordinate:   テキストを挿入座標値(mm)
        :param insert_text:         挿入するテキスト
        :return:
        """
        import numpy as np
        from pdfrw import PdfReader
        from pdfrw.buildxobj import pagexobj
        from pdfrw.toreportlab import makerl
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.pdfbase import pdfmetrics
        from reportlab.lib.units import mm
        from src.utils.time_util import get_now

        output_name = f"{get_now()}.pdf"
        cc = canvas.Canvas(output_name)
        fontname_g = "HeiseiKakuGo-W5"
        pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))
        cc.setFont(fontname_g, 16)

        page = PdfReader(pdf_file_path, decompress=False).pages
        pp = pagexobj(page[0])
        cc.doForm(makerl(cc, pp))

        target_coordinate_arr = np.squeeze(np.asarray(target_coordinate))
        target_x, target_y = target_coordinate_arr[0], target_coordinate_arr[1]
        cc.drawString(target_x*mm, target_y*mm, insert_text)
        cc.showPage()
        cc.save()

    @staticmethod
    def test(pdf_file_path):
        """
        既存のPDFファイルに文字を挿入し、別名で出力します
        :param pdf_file_path:       既存のPDFファイルパス
        :param target_coordinate:   テキストを挿入座標値(mm)
        :param insert_text:         挿入するテキスト
        :return:
        """
        from PyPDF2 import PdfFileWriter, PdfFileReader
        from io import BytesIO
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import A4

        buffer = BytesIO()

        p = canvas.Canvas(buffer, pagesize=A4)
        p.drawString(100, 100, "holaaaaaaaaaaaa")
        p.showPage()
        p.save()

        # move to the beginning of the StringIO buffer
        buffer.seek(0)
        new_pdf = PdfFileReader(buffer)
        # read your existing PDF
        existing_pdf = PdfFileReader(open(pdf_file_path, 'rb'), strict=False)
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))

        output.addPage(page)
        # finally, write "output" to a real file
        output_stream = open('output.pdf', 'wb')
        output.write(output_stream)
        output_stream.close()

    @staticmethod
    def insert_text_output_pdf_fitz(pdf_file_path, target_coordinate, insert_text):
        """
        既存のPDFファイルに文字を挿入し、別名で出力します
        :param pdf_file_path:       既存のPDFファイルパス
        :param target_coordinate:   テキストを挿入座標値(mm)
        :param insert_text:         挿入するテキスト
        :return:
        """
        import fitz
        # read your existing PDF
        reader = fitz.open(pdf_file_path)
        writer = fitz.open()
        writer.insertPDF(reader, from_page=0, to_page=0)

        page = writer.loadPage(0)
        target_coordinate_arr = np.squeeze(np.asarray(target_coordinate))
        target_x, target_y = target_coordinate_arr[0], target_coordinate_arr[1]
        p = fitz.Point(50, 10)  # start point of 1st line
        rc = page.insertText(p,  # bottom-left of 1st char
                               insert_text,  # the text (honors '\n')
                               fontname="helv",  # the default font
                               fontsize=8,  # the default font size
                               rotate=0,  # also available: 90, 180, 270
                               )
        writer.save("out.pdf")


if __name__ == '__main__':
    PdfEditor.test("test.pdf")

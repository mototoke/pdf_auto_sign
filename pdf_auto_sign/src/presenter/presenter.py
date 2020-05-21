#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from src.utils.const import *
from src.utils.analysis import *
from src.utils.homography import *
from src.models.pdf_edit import PdfEditor
from src.models.image_proc import ImageProc
from src.models.pdf_to_image import PdfToImage
from src.presenter.validator import Validator


class Presenter:
    def __init__(self, window: sg.Window):
        self.window = window
        self.validator = Validator
        self.pdf2img = PdfToImage()
        self.image_proc = ImageProc()
        self.pdf_editor = PdfEditor()

    # ------------------to Model-------------------


    # -----------------from Model-------------------


    # ------------------to View---------------------

    # -----------------from View--------------------
    def get_select_file_path(self) -> str:
        """
        ファイル選択テキストボックスから値を取得します
        :return: file_path
        """
        event, values = self.window.read()
        # テキストボックスの値を取得
        file_path = values[SELECT_FILE_PATH]

        return file_path

    def get_insert_text(self) -> str:
        """
        PDF挿入テキストボックスから値を取得します
        :return: insert_text
        """
        event, values = self.window.read()
        # テキストボックスの値を取得
        insert_text = values[INSERT_TEXT]

        return insert_text

    def get_check_state(self) -> bool:
        """
        チェックボックスの値を取得します
        :return check:
        """
        event, values = self.window.read()
        # チェックボックスの値を取得
        check_state = values[CONFIRM_CHECK]

        return check_state

    # ---------------- Event process----------------
    def execute_event(self, values):
        """
        実行処理
        :param values:
        :return:
        """
        # テキストの値取得(選択したファイルパス)
        pdf_file_path = values[SELECT_FILE_PATH]
        if not self.validator.is_null_or_empty(pdf_file_path):
            self.show_popup('ファイルが選択されていません')
            return

        if not self.validator.is_pdf_extension_validate(pdf_file_path):
            self.show_popup('PDFを選択してください')
            return

        if not self.validator.file_exist_validate(pdf_file_path):
            self.show_popup('選択したファイルが存在しません')
            return

        # テキストの値取得(挿入する文字)
        insert_text = values[INSERT_TEXT]
        if not self.validator.is_null_or_empty(pdf_file_path):
            self.show_popup('挿入する文字を入力ください')
            return
            # # 空の場合デフォルト値を埋めます
            # insert_text = DEFAULT_INSERT_VALUE

        # チェックボックスの値取得
        check_state = values[CONFIRM_CHECK]

        # PDFをIMAGE(opencv形式)に変換
        images = self.pdf2img.convert_to_images(pdf_file_path)

        # PDFと画像の対応する各4点の入ったリストの作成
        src = get_image_4coordinate(images[0])
        dst = get_pdf_4coordinate(pdf_file_path)

        # 射影変換行列作成(各4点のパラメータ)
        homo = find_homography(src, dst)
        # デバッグ
        # _ = numpy.array([4677, 3307, 1])
        # t = numpy.dot(homo, _)
        # print(t)

        # IMAGEから空き領域探索(画像処理, 途中処理表示であればimshow()で表示する)
        # 空き領域の座標取得(画像座標系での座標)
        self.image_proc.set_image(images[0], check_state)
        img_target_x, img_target_y = self.image_proc.get_large_blank_erea()

        # 画像座標系の位置をPDF座標系に変換(射影変換行列を利用)
        img_target_coordinate = numpy.array([img_target_x, img_target_y, 1])
        pdf_target_coordinate = numpy.dot(homo, img_target_coordinate)
        print(f'img_target_coordinate:{img_target_coordinate}')
        print(f'pdf_target_coordinate:{pdf_target_coordinate}')

        # PDFに空き領域の場所にテキストを挿入して別の名前で保存
        self.pdf_editor.insert_text_output_pdf(pdf_file_path, pdf_target_coordinate, insert_text)

        self.show_popup('出力が完了しました')

    # ---------------- Util ----------------
    def show_popup(self, message: str):
        """
        ポップメッセージを表示します
        :param message: 表示メッセージ
        :return:
        """
        # self.window.hide()
        sg.Popup(message, title='')
        # self.window.unhide()

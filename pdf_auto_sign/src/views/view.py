#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PySimpleGUI as sg
from src.views.style import *


class InterFace:
    """
    Viewのインターフェースを定義します
    """
    def __init__(self):
        """
        コンストラクタ
        Viewの定義をします
        """
        self.input_frame = [sg.Frame('Input', font='Any 15', layout=[
            # コントロールの配置を定義
                    [sg.InputText('Select a file, Please', **input_select_text_style), sg.FileBrowse('Select', **input_file_browse_style)],
                    [sg.Text('Enter the insert text in pdf file', **input_text_style)],
                    [sg.InputText('', **input_insert_text_style)],
                    [sg.Checkbox('processing', **input_check_box_style), sg.Button('Execute', **input_button_style)]
                    ])]

        self.layout = [self.input_frame]

        self.window = sg.Window(title='pdf_auto_sign', layout=self.layout, **window_style)

        # self.input_frame = [sg.Frame('Input', font='Any 15', layout=[
        #     # コントロールの配置を定義
        #             [sg.InputText('ファイルを選択してください', **input_select_text_style), sg.FileBrowse('選択', **input_file_browse_style)],
        #             [sg.Text('PDFに挿入する文字を記入してください', **input_text_style)],
        #             [sg.InputText('', **input_insert_text_style)],
        #             [sg.Checkbox('途中処理表示', **input_check_box_style), sg.Button('実行', **input_button_style)]
        #             ])]

        # self.layout = [self.input_frame]

        # self.window = sg.Window(title='PDFから空き領域を探して書いてみよう', layout=self.layout, **window_style)

    def close(self):
        """
        画面終了処理
        :return:
        """
        self.window.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path


class Validator:
    """
    妥当性チェック
    """
    @classmethod
    def file_exist_validate(cls, file_path) -> bool:
        """
        ファイルの存在有無を判定します
        :param file_path:
        :return:
        """
        return Path(file_path).exists()

    @classmethod
    def is_pdf_extension_validate(cls, file_path) -> bool:
        """
        ファイル拡張子がpdfかどうか判定します
        :param file_path:
        :return:
        """
        return True if Path(file_path).suffix == '.pdf' else False

    @classmethod
    def is_null_or_empty(cls, text: str) -> bool:
        """
        文字列が空白 or NULLかどうかを判定します
        :param text:
        :return:
        """
        return True if text else False

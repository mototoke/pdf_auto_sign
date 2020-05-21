#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.utils.const import *

# -------------Window--------------
window_style = {
    'auto_size_text': False,
    'auto_size_buttons': False,
    'default_element_size': (20, 1),
    'text_justification': 'right',
}

# -----------Input Frame-----------
input_select_text_style = {
    'key': SELECT_FILE_PATH,
    'font': (None, 12),
    'justification': 'left',
    'size': (40, 1),
}

input_file_browse_style = {
    'key': SELECT_FILE,
    'size': (10, 1),
    'file_types': (('PDFファイル', '*.pdf'),)
}

input_text_style = {
    'font': (None, 12),
    'justification': 'left',
    'size': (40, 1),
}

input_insert_text_style = {
    'key': INSERT_TEXT,
    'font': (None, 12),
    'justification': 'left',
    'size': (40, 1),
}

input_check_box_style = {
    'key': CONFIRM_CHECK,
    'size': (40, 1)
}

input_button_style = {
    'key': EXECUTE,
    'size': (15, 1),
}

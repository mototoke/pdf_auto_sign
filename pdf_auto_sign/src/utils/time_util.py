#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


def get_now() -> str:
    """
    現在時刻をyyyyMMddHHmmss形式で出力します
    :return:
    """
    # 日本時刻
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    ret = now.strftime('%Y%m%d%H%M%S')
    print(ret)
    return ret

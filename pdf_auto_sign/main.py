#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.presenter.presenter import Presenter
from src.presenter.handler import Handler
from src.views.view import InterFace


def main():
    """
    Main関数
    Model, View, Presenterを生成します
    :return:
    """
    interface = InterFace()
    presenter = Presenter(window=interface.window)
    handler = Handler(presenter)

    while True:
        event, values = interface.window.read()
        handler.handle(event, values)

        if event is None:
            break

    interface.close()


if __name__ == '__main__':
    main()

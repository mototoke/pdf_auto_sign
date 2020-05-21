#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.presenter.presenter import Presenter
from src.utils.const import *


class Handler:
    def __init__(self, presenter: Presenter):
        self.presenter = presenter
        self.func_dict = {
           EXECUTE: self.presenter.execute_event
        }

    def handle(self, event_key, values):
        if event_key not in self.func_dict:
            return
        event_func = self.func_dict[event_key]
        event_func(values)

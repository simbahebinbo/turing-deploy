# coding: utf-8


class Struct:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

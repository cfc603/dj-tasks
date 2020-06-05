# -*- coding: utf-8 -*-

from importlib import import_module


def get_class(dot_path):
    # get path
    dot_path = dot_path.split(".")
    path = ".".join(dot_path[:-1])

    # get class name
    dot_path.reverse()
    class_name = dot_path[0]

    # return Class
    module = import_module(path)
    return getattr(module, class_name)

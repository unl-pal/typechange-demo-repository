#!/usr/bin/env python
# coding: utf-8

from typing import Union

def foo(a: str):
    return a

def bar(x) -> Union[int, float]:
    return x + 1

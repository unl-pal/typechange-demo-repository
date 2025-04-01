#!/usr/bin/env python
# coding: utf-8

from typing import Union, TypeVar

T = TypeVar('T')

def foo(a) -> int:
    return a

def bar(x: Union[int, float]) -> Union[int, float]:
    return x + 1

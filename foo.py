#!/usr/bin/env python
# coding: utf-8

from typing import Union

def foo(a: str) -> str:
    return a

def bar(x: Union[int, float]) -> Union[int, float]:
    return x + 1

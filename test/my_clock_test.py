# -*- coding: utf-8 -*-
from my_clock import my_clock as pm
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


def get_time_test1():
    assert(pm.get_time(['1s', '2m', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 1)


def get_time_test2():
    assert(pm.get_time(['100s', '2m', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 100)


def get_time_test3():
    assert(pm.get_time(['100s', '2', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 100)


def get_terminal_escape_test():
    assert(pm.get_terminal_escape("Pomodoro") == "'Pomodoro'")


def get_terminal_escape_test2():
    assert(pm.get_terminal_escape("Pomodoro Job") == "'Pomodoro Job'")

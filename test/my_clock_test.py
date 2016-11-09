# -*- coding: utf-8 -*-
from my_clock import my_clock as cl
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

def get_default_opts():
    return {
        'message': cl.DEFAULT_MESSAGE,
        'title': cl.DEFAULT_TITLE,
        'show_tasks': False,
        'verbose': False,
        'ring_bell': False,
        'time': [],
        'hide_popup': False,
        'bell_sound': cl.DEFAULT_BELL_SOUND_FILENAME,
    }


def get_time_test1():
    assert(cl.get_time(['1s', '2m', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 1)


def get_time_test2():
    assert(cl.get_time(['100s', '2m', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 100)


def get_time_test3():
    assert(cl.get_time(['100s', '2', '3h'], []) == 3 * 60 * 60 + 2 * 60 + 100)


def get_terminal_escape_test():
    assert(cl.get_terminal_escape("Pomodoro") == "'Pomodoro'")


def get_terminal_escape_test2():
    assert(cl.get_terminal_escape("Pomodoro Job") == "'Pomodoro Job'")

def get_option_value_test1():
    pass

def get_config_options_test():
    conf_filename = os.path.dirname(os.path.abspath(__file__)) + \
        '/confs/clock1.json5'
    options = cl.get_config_options(conf_filename)  # use default task
    assert(options == {
        "title": "MyTitle",
        "message": "MyMessage",
        "time": ["3s"]
    })


def get_config_options_test2():
    conf_filename = os.path.dirname(os.path.abspath(__file__)) + \
        '/confs/clock1.json5'
    options = cl.get_config_options(conf_filename, task_name='pomodoro-job')
    assert(options == {
        "title": "Pomodoro Job",
        "message": "finished",
        "time": ["25m"]
    })


def get_config_options_test3():
    conf_filename = os.path.dirname(os.path.abspath(__file__)) + \
        '/confs/clock1.json5'
    options = cl.get_config_options(conf_filename, task_name=None)
    assert(options == {
        "default": {
            "title": "MyTitle",
            "message": "MyMessage",
            "time": ["3s"]
        },
        "pomodoro-job": {
            "title": "Pomodoro Job",
            "message": "finished",
            "time": ["25m"]
        },
        "pomodoro-rest": {
            "title": "Pomodoro Rest",
            "message": "Rest is finished",
            "time": ["5m"]
        }
    })


def get_task_names_test():
    conf_filename = os.path.dirname(os.path.abspath(__file__)) + \
        '/confs/clock1.json5'
    task_names = cl.get_task_names(conf_filename)
    assert(set(task_names) == {"default", "pomodoro-job", "pomodoro-rest"})


def get_task_names_test2():
    conf_filename = os.path.dirname(os.path.abspath(__file__)) + \
        '/confs/empty.json5'
    task_names = cl.get_task_names(conf_filename)
    assert(set(task_names) == {"default"})


def merge_options_message_test1():
    """ なにもOptionがない場合のmessageのテスト """
    assert cl.merge_options(get_default_opts(), {})['message'] == \
        cl.DEFAULT_MESSAGE

def merge_options_message_test2():
    """ ConfだけOptionがある場合のmessageのテスト """
    assert cl.merge_options(get_default_opts(), {'message': 'ConfMessage'}
        )['message'] == 'ConfMessage'

def merge_options_message_test3():
    """ inputだけOptionがある場合のmessageのテスト """
    default_opts = get_default_opts()
    default_opts['message'] = 'DefaultMessage'
    assert cl.merge_options(default_opts, {})['message'] == 'DefaultMessage'

def merge_options_message_test4():
    """ inputもconfもOptionがある場合のmessageのテスト """
    default_opts = get_default_opts()
    default_opts['message'] = 'DefaultMessage'
    assert cl.merge_options(default_opts, {'message': 'ConfMessage'})['message'] ==  \
        'DefaultMessage'

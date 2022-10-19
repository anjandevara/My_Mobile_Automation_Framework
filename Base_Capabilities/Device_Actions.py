import subprocess

from Base_Capabilities.Commands import *


class DeviceActions:

    @classmethod
    def swipe_little_from_bottom_to_top(cls):
        popen = subprocess.Popen(swipe_little_from_bottom_to_top, stdout=subprocess.PIPE, shell=True)
        self_popen = popen
        p = self_popen
        (output, err) = p.communicate()
        p.wait()

    @classmethod
    def swipe_from_left_to_right(cls):
        p = subprocess.Popen(swipe_from_left_to_right, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

    @classmethod
    def hide_keyboard(cls):
        p = subprocess.Popen(hide_keyboard, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

    @classmethod
    def text_input(cls, text):
        popen = subprocess.Popen(text_enter + text, stdout=subprocess.PIPE, shell=True)
        self_popen = popen
        p = self_popen
        (output, err) = p.communicate()
        p.wait()
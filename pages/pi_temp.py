#!/usr/bin/env python3

from .lcd_util import label_line
import dothat.lcd as lcd


def display():
    with open('/sys/class/thermal/thermal_zone0/temp') as ff:
        temp = int(ff.read()) / 1000
    disp_temp = '{:.2f}C'.format(temp)

    lcd.clear()
    lcd.set_cursor_position(0, 0)
    lcd.write(label_line('CPU temp', disp_temp))

#!/usr/bin/env python3

import dothat.lcd as lcd
import fcntl
import socket
import struct
from .lcd_util import label_line


def _get_addr(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])
    except IOError:
        return 'inactive'


def display():
    wlan0 = _get_addr('wlan0')
    eth0 = _get_addr('eth0')
    host = socket.gethostname()

    lcd.clear()

    lcd.set_cursor_position(0, 0)
    lcd.write(label_line('h', host))

    lcd.set_cursor_position(0, 1)
    lcd.write(label_line('e', eth0))

    lcd.set_cursor_position(0, 2)
    lcd.write(label_line('w', wlan0))

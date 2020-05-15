#!/usr/bin/env python3

from .lcd_util import label_line
import dothat.lcd as lcd
import fcntl
import socket
import struct


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

    lines = (
        label_line('h', host),
        label_line('e', eth0),
        label_line('w', wlan0),
    )

    lcd.clear()
    for idx, line in enumerate(lines):
        lcd.set_cursor_position(0, idx)
        lcd.write(line)

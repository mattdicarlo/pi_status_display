#!/usr/bin/env python3

from . import ip_address, pi_temp
import dothat.backlight as backlight
import dothat.lcd as lcd
import signal
from dothat import touch


class PageList:
    def __init__(self):
        self.pages = [ip_address, pi_temp]
        self.current = 0

    def update(self):
        self.pages[self.current].display()

    def next(self):
        self.current = (self.current + 1) % len(self.pages)
        self.update()

    def previous(self):
        self.current = (self.current - 1) % len(self.pages)
        self.update()


_pages = PageList()


def run():
    reset()

    # Interval timer emits SIGALRM in n seconds, then every n after.
    signal.signal(signal.SIGALRM, _on_update)
    signal.setitimer(signal.ITIMER_REAL, 1, 1)

    # Cause the process to sleep until a signal is received.
    while True:
        signal.pause()


def reset():
    clear()

    lcd.set_contrast(45)
    backlight.rgb(128, 128, 128)


def clear():
    # Reset the LED states and polarity
    backlight.graph_off()

    # Empty the screen
    lcd.clear()

    # Turn off the backlight
    backlight.rgb(0, 0, 0)


@touch.on(touch.LEFT)
def _on_touch_left(channel, event):
    _pages.previous()


@touch.on(touch.RIGHT)
def _on_touch_right(channel, event):
    _pages.next()


def _on_update(signum, frame):
    _pages.update()

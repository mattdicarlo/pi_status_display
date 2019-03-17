#!/usr/bin/env python3

LINE_LEN = 16


def truncate_line(str, length=LINE_LEN):
    format_str = '{{:.{}}}'.format(length)
    return format_str.format(str)


def label_line(label, data):
    # If there's no room for a label, just return as much data as possible.
    if LINE_LEN - len(data) <= 2:
        return truncate_line(data)

    # If it fits, pad the line to justify things nicely.
    spaces = LINE_LEN - (len(label) + 1 + len(data))
    if spaces >= 0:
        return '{}:{}{}'.format(label, ' ' * spaces, data)

    # Gotta truncate the label to make things fit.
    label_len = LINE_LEN - len(data) - 1
    return '{}:{}'.format(truncate_line(label, label_len), data)

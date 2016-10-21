#!/bin/sh
adb pull /proc/dumchar_info

./scatter.py

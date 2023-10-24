#!/bin/bash

scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir Pictures/Screenshots/)'
notify-send "Screenshot Saved"

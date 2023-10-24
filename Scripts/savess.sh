#!/bin/bash

scrot '%Y-%m-%d-%s_screenshot_$wx$h.jpg' -e 'mv $f $$(xdg-user-dir Wallpapers/Screenshots/)'
notify-send "Screenshot Saved"

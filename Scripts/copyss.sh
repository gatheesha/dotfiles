#!/bin/bash

scrot -e 'xclip -selection clipboard -t image/png -i $f'
notify-send "Screenshot Copied to Clipboard"

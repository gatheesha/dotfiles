#!/bin/bash

CURRENT_STATE=`amixer get Master | egrep 'Playback.*?\[o' | egrep -o '\[o.+\]'`

if [[ $CURRENT_STATE == '[on]' ]]; then
    amixer set Master mute
else
    amixer set Master unmute
    amixer set Front unmute
    amixer set Headphone unmute
    amixer set Front unmute
fi

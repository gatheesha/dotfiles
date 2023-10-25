from libqtile import bar, layout, hook, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, hook, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.dgroups import simple_key_binder
from time import sleep

mod = "mod4"
terminal = "kitty"

bgcolor = '#101014'
fgcolor = '#a9b1d6'
accent = '#73daca'
accent2 = '#9ece6a'
accent3 = '#414868'
border1 = accent

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█ █▄▀ ▄█

keys = [
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "control"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"],"space",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Spawn a command using a prompt widget"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc='powermenu'),

    Key([mod], "Print", lazy.spawn("bash Scripts/savess.sh")),
    Key([mod, "control"], "Print", lazy.spawn("bash Scripts/copyss.sh")),
# C U S T O M

    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%"), desc='Volume Up'),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%"), desc='volume down'),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute"), desc='Volume Mute'),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 10%+"), desc='brightness UP'),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 10%-"), desc='brightness Down'),
    Key([mod],"e", lazy.spawn("thunar"), desc='file manager'),
	Key([mod], "h", lazy.spawn("roficlip"), desc='clipboard'),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc='Screenshot'),
]

# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█

groups = [
    Group("1",label=" "),
    Group("2",label=" ", matches=[Match(wm_class=["firefox"])]),
    Group("3",label="󰓇 ", matches=[Match(wm_class=["spotify"])]),
    Group("4",label="󰙯 ", matches=[Match(wm_class=["discord"])]),
    Group("5",label="5"),
    Group("6",label="6"),
    Group("7",label="7"),
    Group("8",label="8"),
    ]
for i in groups:
    keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                    ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & move focused window to group {}".format(i.name),
                    ),
                ]
            )

# L A Y O U T S

layouts = [
    layout.Columns(
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
    ),

    layout.Max(
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
    ),

    layout.Floating(
        border_focus=bgcolor,    
	    border_width=0,
	),
    # Try more layouts by unleashing below layouts
   #  layout.Stack(num_stacks=2),
   #  layout.Bsp(),
     layout.Matrix(
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
	),
     layout.MonadTall(
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
	),
    layout.MonadWide(
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
	),
   #  layout.RatioTile(),
     layout.Tile(	
        border_focus=border1,
	    border_normal=bgcolor,
        border_width=1,
    ),
   #  layout.TreeTab(),
   #  layout.VerticalTile(),
   #  layout.Zoomy(),
]



widget_defaults = dict(
    font="JetBrains Mono Bold",
    fontsize=12,
    padding=3,
)
extension_defaults = [ widget_defaults.copy()
        ]



def search():
    qtile.cmd_spawn("rofi -show drun")

def spot():
    qtile.cmd_spawn("qtile cmd-obj -o group 3 -f toscreen")

def power():
    qtile.cmd_spawn("sh -c ~/.config/rofi/scripts/power")
def mute():
    qtile.cmd_spawn("sh -c ~/.config/qtile/mute.sh")

myfontsize=12 
myiconsize=14
# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄

screens = [
    Screen(
        wallpaper='~/Wallpapers/wallhaven-m3oq1k.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.TextBox(
                    fmt='',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=fgcolor,
                    mouse_callbacks={"Button1": search},
                    padding=12,
                ),

                widget.GroupBox(
                    fontsize=myfontsize,
                    borderwidth=1,
                    highlight_method='block',
                    active=fgcolor,
                    block_highlight_text_color=accent,
                    highlight_color=bgcolor,
                    inactive=accent3,
                    foreground=fgcolor,
                    background=bgcolor,
                    this_current_screen_border=bgcolor,
                    this_screen_border=bgcolor,
                    other_current_screen_border=bgcolor,
                    other_screen_border=bgcolor,
                    urgent_border=bgcolor,
                    rounded=False,
                    disable_drag=True,
                 ),


                widget.Spacer(
                    length=8,
                    background=bgcolor,
                ),

                widget.CurrentLayout(
                    background=bgcolor,
                    foreground=accent,
                    padding=8,
                    fmt=' {}',
                    font="JetBrains Mono Bold",
                    fontsize=myfontsize,
                ),

                widget.WindowName(
                    background = bgcolor,
                    format = "{name}",
                    font='JetBrains Mono Bold',
                    foreground=fgcolor,
                    empty_group_string = 'Desktop',
                    fontsize=myfontsize,
                    padding=8,

                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.TextBox(
                    fmt=' ',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=accent2,
                    padding=None,
                    mouse_callbacks={"Button1": spot},
                ),
                widget.Mpris2(
                    name='spotify',
                    font='JetBrainsMono Bold',
                    fontsize=myfontsize,
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title'],
                    #format='{xesam:titlei}',
                    stop_pause_text='',
                    padding = 8,
                    margin=[2,2,2,2],
                    width = 250,
                    foreground= accent2,
                    background=bgcolor,
                ),

                widget.Systray(
                    background=bgcolor,
                    fontsize=0.4,
                    padding=8,
                ),
   
                widget.TextBox(
                    fmt=' ',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=fgcolor,
                    padding=None,
                ),

                widget.Net(
                #format=' {up}{down} ',
                format='{down}',
                background=bgcolor,
                foreground=fgcolor,
                font="JetBrains Mono Bold",
                prefix='k',
                fontsize=myfontsize,
                padding=4,
                ),

                widget.TextBox(
                    fmt=' 󰍛',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=fgcolor,
                    padding=None,
                ),

                widget.Memory(
                    background=bgcolor,
                    format='{MemUsed:.0f}{mm}',
                    foreground=fgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myfontsize,
                    update_interval=5,
                    padding=4,
                ),

                widget.Volume(
                    fmt=' ',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=accent,
                    padding=None,
                    mute_command="sh -c ~/.config/qtile/mute.sh",
                ),

                widget.Volume(
                    font='JetBrainsMono Nerd Font',
                    #theme_path='~/.config/qtile/Assets/Volume/',
                    cardid=1,
                    channel='Master',
                    mute_command="sh -c ~/.config/qtile/mute.sh",
                    fmt='{}',
                    fontsize=myfontsize,
                    background=bgcolor,
                    foreground=accent,
                    padding=4,
                ),

                widget.TextBox(
                    fmt=' ',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    foreground=fgcolor,
                    padding=None,
                ),


                widget.Clock(
                    format='%I:%M %p',
                    background=bgcolor,
                    foreground=fgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myfontsize,
                ),
                widget.Spacer(
                    length=8,
                    background=bgcolor,
                ),

             widget.TextBox(
                    fmt='  ',
                    background=bgcolor,
                    font="JetBrains Mono Bold",
                    fontsize=myiconsize,
                    padding=0,
                    foreground=fgcolor,
                    mouse_callbacks={"Button1": power},
                    ),
            ],
            28,
            border_color = accent,
            #border_width = [1,1,1,1],
            margin = [0,0,0,0],
            background=bgcolor,

        ),
    ),
]



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
	border_focus='#1F1D2E',
	border_normal='#1F1D2E',
	border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)




from libqtile import hook
# some other imports
import os
import subprocess
# stuff
@hook.subscribe.startup_once
def autostart():
    #subprocess.run('~/.config/qtile/autostart_once.sh')# path to my script, under my user directory
    #subprocess.call([home])
    home = os.path.expanduser('~/.config/qtile/autostart_once.sh')
    subprocess.call([home])


@hook.subscribe.client_new
def new_client(client):
    if client.name == "firefox":
        client.togroup(8)
    elif client.name == "dzen":
        client.static(0)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
#wmname = "LG3D"
wmname = "qtile"



# E O F

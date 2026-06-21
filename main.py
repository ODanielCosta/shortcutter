import keyboard as kb
import pygetwindow as gw
import pyautogui as autog

print("  +------------------------+")
print("  |       Shortcutter      |")
print("  |       Version 1.0      |")
print("  +------------------------+")


#SHORTCUTS###############
#
def win1 ():
    autog.hotkey('win','1')
    print("win + 1")

kb.add_hotkey("shift+s",win1)


kb.wait()
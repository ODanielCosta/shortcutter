import keyboard as kb
import pygetwindow as gw
import pyautogui as autog
import pywin
import psutil

print("  +------------------------+")
print("  |       Shortcutter      |")
print("  |       Version 1.0      |")
print("  +------------------------+")

#PROCESSOS###############
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)


#SHORTCUTS###############
#
def win1 ():
    autog.hotkey('win','1')
    print("win + 1")

kb.add_hotkey("shift+s",win1)


kb.wait()
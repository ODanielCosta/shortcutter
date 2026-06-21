import keyboard as kb
import pygetwindow as gw
import pyautogui as autog
import psutil #Vai buscar processos e info
import win32gui
import win32process
import win32api

print("  +------------------------+")
print("  |       Shortcutter      |")
print("  |       Version 1.0      |")
print("  +------------------------+")

#PROCESSOS###############
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info["name"]== "brave.exe":
        print(proc.info)

for janela in win32gui.EnumWindows(hwnd,extra):
    print(janela)

#SHORTCUTS###############
#
def win1 ():
    autog.hotkey('win','1')
    print("win + 1")

kb.add_hotkey("shift+s",win1)


kb.wait()
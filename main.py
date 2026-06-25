import keyboard as kb
import pygetwindow as gw
import pyautogui as autog
import psutil #Vai buscar processos
import win32gui #Vai buscar o Handle Window
import win32process #Liga o Handle Window a um processo
import win32api

print("  +------------------------+")
print("  |       Shortcutter      |")
print("  |       Version 1.0      |")
print("  +------------------------+")

#PROCESSOS###############
brave_pid = []

#1 psutil → processos (PID)
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info["name"]== "brave.exe":
        brave_pid.append(proc.info['pid'])
print(brave_pid)

#3 GetWindowThreadProcessId → liga HWND → PID
def callback(hwnd, extra):
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]
    if pid in brave_pid:
        print(hwnd, pid)

#2 EnumWindows → janelas (HWND (Handle Window))
win32gui.EnumWindows(callback,None)



#SHORTCUTS###############
#
"""
def win1 ():
    autog.hotkey('win','1')
    print("win + 1")

kb.add_hotkey("shift+s",win1)


kb.wait()
"""
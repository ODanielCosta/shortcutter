import keyboard as kb
import pygetwindow as gw
import pyautogui as autog
import psutil #Vai buscar processos
import win32gui #Vai buscar o Handle Window
import win32process #Liga o Handle Window a um processo
import win32api

print("         +------------------------+")
print("         |       Shortcutter      |")
print("         |       Version 1.0      |")
print("         +------------------------+")

#PROCESSOS###############
brave_pid = []
brave_hwnd = []

#1 psutil → processos (PID)
for proc in psutil.process_iter(['pid', 'name']):
    if proc.info["name"]== "brave.exe":
        brave_pid.append(proc.info['pid'])
print("PROCESSOS:", brave_pid)

#3 GetWindowThreadProcessId → liga HWND → PID
def callback(hwnd, extra):    
    pid = win32process.GetWindowThreadProcessId(hwnd)[1]
    if pid in brave_pid and "Default IME" not in win32gui.GetWindowText(hwnd) and "MSCTFIME UI" not in win32gui.GetWindowText(hwnd) and len(win32gui.GetWindowText(hwnd)) > 1:
        #win32gui.IsIconic deteta se está minimizado
        print(f"hwnd: {hwnd} | Minimizado: {win32gui.IsIconic(hwnd)} | {win32gui.GetWindowText(hwnd)} | Processo: {pid}")

        brave_hwnd.append(hwnd)
        brave_true_hwnd = brave_hwnd[0]
        print(brave_true_hwnd)
        print(win32gui.GetForegroundWindow())

        #win32gui.GetForegroundWindow() VAI BUSCAR A JANELA SELECIONADA ATUAL
        if win32gui.GetForegroundWindow() == brave_true_hwnd:
            print("Match")
            foreground_hwnd = brave_true_hwnd

    
    #if pid in brave_pid:
    #   print(f"hwnd: {hwnd} | Minimizado: {win32gui.IsIconic(hwnd)} | {win32gui.GetWindowText(hwnd)} | Processo: {pid}")


#2 EnumWindows → janelas (HWND (Handle Window))
win32gui.EnumWindows(callback,None)

#VERIFICAR ESTADO #########




#SHORTCUTS###############
#
"""
def win1 ():
    autog.hotkey('win','1')
    print("win + 1")

kb.add_hotkey("shift+s",win1)


kb.wait()
"""
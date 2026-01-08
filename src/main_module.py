"""
Сrossword Solver


License: MIT
Copyright (c) 2026 [Anga Paduga]

This project uses Python and its standard libraries, which are
distributed under the Python Software Foundation License.

Attention! Be careful!

After you have indicated the screen coordinates of all letters to this program, do not move the crossword puzzle window, do not minimize it or change its scale!
Also, do not cover it with other application windows on the screen!
Do not press any keys on your keyboard or move your mouse while this program is running!
All this can lead to incorrect crossword solutions, as well as accidental damage or deletion of files on your desktop.
If you need to immediately emergency stop this program, press the SPACE key.

WARNING!
THE USER USES THIS PROGRAM AT YOUR OWN RISK. THE DEVELOPER IS NOT RESPONSIBLE FOR ANY LOSSES INCURRED BY THE USER OR ANY OTHER PERSONS AS A RESULT OF THE RUNNING OF THIS PROGRAM.
IF YOU ARE CONCERNED THAT ANY DATA IN YOUR SYSTEM WILL BE DAMAGED AND YOU WILL EXPERIENCE FINANCIAL OR OTHER DAMAGE,DO NOT RUN THIS SOFTWARE ON YOUR COMPUTER.
"""

import multiprocessing as mp  
import itertools
import time
from tkinter import *
import ctypes
from ctypes import wintypes, Structure, POINTER
import signal
import sys

class POINT(Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

VK_SPACE = 0x20
user32 = ctypes.windll.user32
GetAsyncKeyState = user32.GetAsyncKeyState
VK_LBUTTON = 0x01

def hotkey_listener(space_pressed):
    msg = wintypes.MSG()
    user32.RegisterHotKey(None, 1, 0, VK_SPACE)
    
    while True:
        if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
            if msg.message == 0x0312:
                space_pressed.value = True

def cleanup(listener_process):
    if listener_process.is_alive():
        listener_process.terminate()
        listener_process.join(timeout=2)
        if listener_process.is_alive():
            listener_process.kill()
    print("Program terminated...")
    user32.mouse_event(4, 0, 0, 0, 0)

def signal_handler(signum, frame, listener_process):
    cleanup(listener_process)
    sys.exit(0)

def get_cursor_coordinateX():
    point = POINT()
    if user32.GetCursorPos(ctypes.byref(point)):
        return point.x
    else:
        return None

def get_cursor_coordinateY():
    point = POINT()
    if user32.GetCursorPos(ctypes.byref(point)):
        return point.y
    else:
        return None

root = Tk()
root.title("ENTER the LETTERS")
root.geometry('215x80+0+0')    


leters = [ ]
lbls3 = [0, 0, 0]
lbls4 = [0, 0, 0, 0]
lbls5 = [0, 0, 0, 0, 0]
lbls6 = [0, 0, 0, 0, 0, 0]
lbls7 = [0, 0, 0, 0, 0, 0, 0]
x_coordinates3 = [0, 0, 0]
y_coordinates3 = [0, 0, 0]
x_coordinates4 = [0, 0, 0, 0]
y_coordinates4 = [0, 0, 0, 0]
x_coordinates5 = [0, 0, 0, 0, 0]
y_coordinates5 = [0, 0, 0, 0, 0]
x_coordinates6 = [0, 0, 0, 0, 0, 0]
y_coordinates6 = [0, 0, 0, 0, 0, 0]
x_coordinates7 = [0, 0, 0, 0, 0, 0, 0]
y_coordinates7 = [0, 0, 0, 0, 0, 0, 0]

user32 = ctypes.windll.user32

def button_clickedAA():
    leters.append('а')
    root.quit()
def button_clickedBE():
    leters.append('б')
    root.quit()
def button_clickedVE():
    leters.append('в')
    root.quit()
def button_clickedGE():
    leters.append('г')
    root.quit()
def button_clickedDE():
    leters.append('д')
    root.quit()
def button_clickedEE():
    leters.append('е')
    root.quit()
def button_clickedYO():
    leters.append('ё')
    root.quit()
def button_clickedZH():
    leters.append('ж')
    root.quit()
def button_clickedZE():
    leters.append('з')
    root.quit()
def button_clickedII():
    leters.append('и')
    root.quit()
def button_clickedIY():
    leters.append('й')
    root.quit()
def button_clickedKK():
    leters.append('к')
    root.quit()
def button_clickedLL():
    leters.append('л')
    root.quit()
def button_clickedMM():
    leters.append('м')
    root.quit()
def button_clickedNN():
    leters.append('н')
    root.quit()
def button_clickedOO():
    leters.append('о')
    root.quit()
def button_clickedPP():
    leters.append('п')
    root.quit()
def button_clickedRR():
    leters.append('р')
    root.quit()
def button_clickedSS():
    leters.append('с')
    root.quit()
def button_clickedTT():
    leters.append('т')
    root.quit()
def button_clickedUU():
    leters.append('у')
    root.quit()
def button_clickedFF():
    leters.append('ф')
    root.quit()
def button_clickedHH():
    leters.append('х')
    root.quit()
def button_clickedCE():
    leters.append('ц')
    root.quit()
def button_clickedCH():
    leters.append('ч')
    root.quit()
def button_clickedSH():
    leters.append('ш')
    root.quit()
def button_clickedSC():
    leters.append('щ')
    root.quit()
def button_clickedSC():
    leters.append('щ')
    root.quit()
def button_clickedHARD():
    leters.append('ъ')
    root.quit()
def button_clickedSOFT():
    leters.append('ь')
    root.quit()
def button_clickedIII():
    leters.append('ы')
    root.quit()
def button_clickedYE():
    leters.append('э')
    root.quit()
def button_clickedYU():
    leters.append('ю')
    root.quit()
def button_clickedYA():
    leters.append('я')
    root.quit()

f = Frame(root, width = 215, height = 80, bg = "white")
f.pack(side = LEFT, fill = BOTH)
f.place(x=0, y=0)

buttonAA = Button(f, text = "а", command = button_clickedAA)
buttonBE = Button(f, text = "б", command = button_clickedBE)
buttonVE = Button(f, text = "в", command = button_clickedVE)
buttonGE = Button(f, text = "г", command = button_clickedGE)
buttonDE = Button(f, text = "д", command = button_clickedDE)
buttonEE = Button(f, text = "е", command = button_clickedEE)
buttonYO = Button(f, text = "ё", command = button_clickedYO)
buttonZH = Button(f, text = "ж", command = button_clickedZH)
buttonZE = Button(f, text = "з", command = button_clickedZE)
buttonII = Button(f, text = "и", command = button_clickedII)
buttonIY = Button(f, text = "й", command = button_clickedIY)
buttonKK = Button(f, text = "к", command = button_clickedKK)
buttonLL = Button(f, text = "л", command = button_clickedLL)
buttonMM = Button(f, text = "м", command = button_clickedMM)
buttonNN = Button(f, text = "н", command = button_clickedNN)
buttonOO = Button(f, text = "о", command = button_clickedOO)
buttonPP = Button(f, text = "п", command = button_clickedPP)
buttonRR = Button(f, text = "р", command = button_clickedRR)
buttonSS = Button(f, text = "с", command = button_clickedSS)
buttonTT = Button(f, text = "т", command = button_clickedTT)
buttonUU = Button(f, text = "у", command = button_clickedUU)
buttonFF = Button(f, text = "ф", command = button_clickedFF)
buttonHH = Button(f, text = "х", command = button_clickedHH)
buttonCE = Button(f, text = "ц", command = button_clickedCE)
buttonCH = Button(f, text = "ч", command = button_clickedCH)
buttonSH = Button(f, text = "ш", command = button_clickedSH)
buttonSC = Button(f, text = "щ", command = button_clickedSC)
buttonHARD = Button(f, text = "ъ", command = button_clickedHARD)
buttonSOFT = Button(f, text = "ь", command = button_clickedSOFT)
buttonIII = Button(f, text = "ы", command = button_clickedIII)
buttonYE = Button(f, text = "э", command = button_clickedYE)
buttonYU = Button(f, text = "ю", command = button_clickedYU)
buttonYA = Button(f, text = "я", command = button_clickedYA)

buttonAA.grid(row = 0, column = 0, sticky = NW+SE)
buttonBE.grid(row = 0, column = 1, sticky = NW+SE)
buttonVE.grid(row = 0, column = 2, sticky = NW+SE)
buttonGE.grid(row = 0, column = 3, sticky = NW+SE)
buttonDE.grid(row = 0, column = 4, sticky = NW+SE)
buttonEE.grid(row = 0, column = 5, sticky = NW+SE)
buttonYO.grid(row = 0, column = 6, sticky = NW+SE)
buttonZH.grid(row = 0, column = 7, sticky = NW+SE)
buttonZE.grid(row = 0, column = 8, sticky = NW+SE)
buttonII.grid(row = 0, column = 9, sticky = NW+SE)
buttonIY.grid(row = 0, column = 10, sticky = NW+SE)
buttonKK.grid(row = 1, column = 0, sticky = NW+SE)
buttonLL.grid(row = 1, column = 1, sticky = NW+SE)
buttonMM.grid(row = 1, column = 2, sticky = NW+SE)
buttonNN.grid(row = 1, column = 3, sticky = NW+SE)
buttonOO.grid(row = 1, column = 4, sticky = NW+SE)
buttonPP.grid(row = 1, column = 5, sticky = NW+SE)
buttonRR.grid(row = 1, column = 6, sticky = NW+SE)
buttonSS.grid(row = 1, column = 7, sticky = NW+SE)
buttonTT.grid(row = 1, column = 8, sticky = NW+SE)
buttonUU.grid(row = 1, column = 9, sticky = NW+SE)
buttonFF.grid(row = 1, column = 10, sticky = NW+SE)
buttonHH.grid(row = 2, column = 0, sticky = NW+SE)
buttonCE.grid(row = 2, column = 1, sticky = NW+SE)
buttonCH.grid(row = 2, column = 2, sticky = NW+SE)
buttonSH.grid(row = 2, column = 3, sticky = NW+SE)
buttonSC.grid(row = 2, column = 4, sticky = NW+SE)
buttonHARD.grid(row = 2, column = 5, sticky = NW+SE)
buttonSOFT.grid(row = 2, column = 6, sticky = NW+SE)
buttonIII.grid(row = 2, column = 7, sticky = NW+SE)
buttonYE.grid(row = 2, column = 8, sticky = NW+SE)
buttonYU.grid(row = 2, column = 9, sticky = NW+SE)
buttonYA.grid(row = 2, column = 10, sticky = NW+SE)


def main():
    
    space_pressed = mp.Value('b', False)
    lettrs_number = int(input("Введите количество букв на круге -> "))

    for i in range(1,lettrs_number+1):
        root.mainloop()
        if i == lettrs_number:
            root.destroy()

    for currnt_ltter in range(0, len(leters)):
        print("Поставьте курсор на очередную букву и кликните левой кнопкой мыши... ")
        if len(leters) == 3:
            while GetAsyncKeyState(VK_LBUTTON) & 0x8000:
                time.sleep(0.01)
            while not (GetAsyncKeyState(VK_LBUTTON) & 0x8000):
                time.sleep(0.01)
            x_coordinates3[currnt_ltter] = get_cursor_coordinateX()
            y_coordinates3[currnt_ltter] = get_cursor_coordinateY()
        if len(leters) == 4:
            while GetAsyncKeyState(VK_LBUTTON) & 0x8000:
                time.sleep(0.01)
            while not (GetAsyncKeyState(VK_LBUTTON) & 0x8000):
                time.sleep(0.01)
            x_coordinates4[currnt_ltter] = get_cursor_coordinateX()
            y_coordinates4[currnt_ltter] = get_cursor_coordinateY()
        if len(leters) == 5:
            while GetAsyncKeyState(VK_LBUTTON) & 0x8000:
                time.sleep(0.01)
            while not (GetAsyncKeyState(VK_LBUTTON) & 0x8000):
                time.sleep(0.01)
            x_coordinates5[currnt_ltter] = get_cursor_coordinateX()
            y_coordinates5[currnt_ltter] = get_cursor_coordinateY()
        if len(leters) == 6:
            while GetAsyncKeyState(VK_LBUTTON) & 0x8000:
                time.sleep(0.01)
            while not (GetAsyncKeyState(VK_LBUTTON) & 0x8000):
                time.sleep(0.01)
            x_coordinates6[currnt_ltter] = get_cursor_coordinateX()
            y_coordinates6[currnt_ltter] = get_cursor_coordinateY()
        if len(leters) == 7:
            while GetAsyncKeyState(VK_LBUTTON) & 0x8000:
                time.sleep(0.01)
            while not (GetAsyncKeyState(VK_LBUTTON) & 0x8000):
                time.sleep(0.01)
            x_coordinates7[currnt_ltter] = get_cursor_coordinateX()
            y_coordinates7[currnt_ltter] = get_cursor_coordinateY()
    
    listener_process = mp.Process(target=hotkey_listener, args=(space_pressed,))
    listener_process.start()

    def handler_wrapper(signum, frame):
        signal_handler(signum, frame, listener_process)
    
    signal.signal(signal.SIGINT, handler_wrapper)
    signal.signal(signal.SIGTERM, handler_wrapper)

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("Remember! You can stop the program at any time by pressing the SPACE key.")
    print("Помните! Вы можете остановить программу в любой момент нажатием клавиши ПРОБЕЛ.")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(1.0)

    try:
        for k in range(3,len(leters)+1):
            for nabor in itertools.permutations(leters, k):
                slovo = ''.join(nabor)
                slovo = slovo.lower()
                
                if len(leters) == 3:

                    for j in range(0,len(lbls3)):
                        lbls3[j] = 0
                
                    for i in range(0,len(nabor)):
                        for j in range(0,len(leters)):
                            if space_pressed.value:
                                cleanup(listener_process)
                                return
                            if leters[j] == nabor[i] and lbls3[j] == 0:
                                user32.SetCursorPos(x_coordinates3[j], y_coordinates3[j])
                                if i == 0:
                                    time.sleep(0.5)
                                    user32.mouse_event(2, 0, 0, 0, 0)
                                lbls3[j] = 1
                                time.sleep(0.5)
                                break
                    user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(0.5)

                if len(leters) == 4:

                    for j in range(0,len(lbls4)):
                        lbls4[j] = 0
                
                    for i in range(0,len(nabor)):
                        for j in range(0,len(leters)):
                            if space_pressed.value:
                                cleanup(listener_process)
                                return
                            if leters[j] == nabor[i] and lbls4[j] == 0:
                                user32.SetCursorPos(x_coordinates4[j], y_coordinates4[j])
                                if i == 0:
                                    time.sleep(0.5)
                                    user32.mouse_event(2, 0, 0, 0, 0)
                                lbls4[j] = 1
                                time.sleep(0.5)
                                break
                    user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(0.5)
                
                if len(leters) == 5:

                    for j in range(0,len(lbls5)):
                        lbls5[j] = 0
                
                    for i in range(0,len(nabor)):
                        for j in range(0,len(leters)):
                            if space_pressed.value:
                                cleanup(listener_process)
                                return
                            if leters[j] == nabor[i] and lbls5[j] == 0:
                                user32.SetCursorPos(x_coordinates5[j], y_coordinates5[j])
                                if i == 0:
                                    time.sleep(0.5)
                                    user32.mouse_event(2, 0, 0, 0, 0)
                                lbls5[j] = 1
                                time.sleep(0.5)
                                break
                    user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(0.5)

                if len(leters) == 6:

                    for j in range(0,len(lbls6)):
                        lbls6[j] = 0
                
                    for i in range(0,len(nabor)):
                        for j in range(0,len(leters)):
                            if space_pressed.value:
                                cleanup(listener_process)
                                return
                            if leters[j] == nabor[i] and lbls6[j] == 0:
                                user32.SetCursorPos(x_coordinates6[j], y_coordinates6[j])
                                if i == 0:
                                    time.sleep(0.5)
                                    user32.mouse_event(2, 0, 0, 0, 0)
                                lbls6[j] = 1
                                time.sleep(0.5)
                                break
                    user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(0.5)

                if len(leters) == 7:

                    for j in range(0,len(lbls7)):
                        lbls7[j] = 0
                
                    for i in range(0,len(nabor)):
                        for j in range(0,len(leters)):
                            if space_pressed.value:
                                cleanup(listener_process)
                                return
                            if leters[j] == nabor[i] and lbls7[j] == 0:
                                user32.SetCursorPos(x_coordinates7[j], y_coordinates7[j])
                                if i == 0:
                                    time.sleep(0.5)
                                    user32.mouse_event(2, 0, 0, 0, 0)
                                lbls7[j] = 1
                                time.sleep(0.5)
                                break
                    user32.mouse_event(4, 0, 0, 0, 0)
                    time.sleep(0.5)
                    
        cleanup(listener_process)

    except Exception as er:
        print(f"Error is occured: {er}")
        cleanup(listener_process)

if __name__ == "__main__":
    main()






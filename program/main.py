#импорт библиотек для работы программы
from tkinter import *
import serial
import pygame, sys, time
from pygame.locals import *

#инициализация pygame для воспроизведения звукового сигнала
pygame.init()
DISPLAYSURF = pygame.display.set_mode((100, 100))
soundObj = pygame.mixer.Sound('alarm.wav')

#получение данных с COM3-порта, который подключен к разработанному устройству
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    timeout=10,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

#создание главного меню приложения
root = Tk()
root.title("Темп. и влажн. в картофелехранилище")
root.geometry("750x250")

class Clock:
       def __init__(self):
           #отсеивание лишних данных с поступивших на ПК через COM3-порт с устройства
           self.line = self.printline()
           self.humidity = self.line[2:7]
           self.temperature = self.line[9:14]

           #создание интерфейса приложения
           self.tempFrame = Frame(root)
           self.humFrame = Frame(root)
           self.informationErr = Frame(root)
           self.textTemplabel = Label(self.tempFrame, text="Температура:    ", font=('Arial',20))
           self.textHumlabel = Label(self.humFrame, text="Влажность:        ", font=('Arial',20))
           self.showTemplabel = Label(self.tempFrame, text=self.temperature, bg='white', font=('times',24), width=6)
           self.showHumlabel = Label(self.humFrame, text=self.humidity, bg='white', font=('times',24), width=6)
           self.textTempDegree = Label(self.tempFrame, text=" °C ", font=('times',20,'bold'))
           self.textHumProcent = Label(self.humFrame, text="  % ", font=('times',20,'bold'))
           self.textinformationlabel = Label(self.informationErr, bg='white', text="Идет анализ...", font=('Comic Sans MS',18), height=5)

           self.tempFrame.pack(pady=10)
           self.humFrame.pack()
           self.informationErr.pack()

           self.textTemplabel.pack(side=LEFT)
           self.showTemplabel.pack(side=LEFT)
           self.textHumlabel.pack(side=LEFT)
           self.showHumlabel.pack(side=LEFT)
           self.textTempDegree.pack(side=LEFT)
           self.textHumProcent.pack(side=LEFT)
           self.textinformationlabel.pack(side=BOTTOM, pady=30)

           #вызов функции получения данных
           self.changeLabel()

       def changeLabel(self):
           #отсеивание лишних данных с поступивших на ПК через COM3-порт с устройства
           self.line = self.printline()
           self.humidity = self.line[2:7]
           self.temperature = self.line[9:14]

           #подсветка окна с температур красный-превышена/синий-занижена/зеленый-норма
           self.showTemplabel.configure(text=self.temperature)
           if self.temperature == "2":
               self.showTemplabel.configure(bg='green')
           if self.temperature > "2":
               self.showTemplabel.configure(bg='red')
           if self.temperature < "2":
               self.showTemplabel.configure(bg='blue')

           #подсветка окна с влажностью красный-превышена/синий-занижена/зеленый-норма
           self.showHumlabel.configure(text=self.humidity)
           if self.humidity == "93" :
               self.showHumlabel.configure(bg='green')
           if self.humidity > "93":
               self.showHumlabel.configure(bg='red')
           if self.humidity < "93":
               self.showHumlabel.configure(bg='blue')

            ###Информационное сообщение###
           if self.temperature == "2" and self.humidity == "93" :#all is OK
               self.textinformationlabel.configure(text="OK", fg='green')

           if self.temperature > "2" and self.humidity == "93":
               self.textinformationlabel.configure(text="Температура - ПРЕВЫШЕНА, Влажность - НОРМА \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature < "2" and self.humidity == "93":
               self.textinformationlabel.configure(text="Температура - НИЖЕ НОРМЫ, Влажность - НОРМА \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature == "2" and self.humidity > "93":
               self.textinformationlabel.configure(
                   text="Температура - НОРМА, Влажность - ПРЕВЫШЕНА \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature == "2" and self.humidity < "93":
               self.textinformationlabel.configure(
                   text="Температура - НОРМА, Влажность - НИЖЕ НОРМЫ \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature > "2" and self.humidity > "93":
               self.textinformationlabel.configure(
                   text="Температура - ПРЕВЫШЕНА, Влажность - ПРЕВЫШЕНА \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')
               soundObj.play()
               time.sleep(2)  # wait and let the sound play for X second
               soundObj.stop()

           if self.temperature < "2" and self.humidity < "93":
               self.textinformationlabel.configure(
                   text="Температура - НИЖЕ НОРМЫ, Влажность - НИЖЕ НОРМЫ \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature > "2" and self.humidity < "93":
               self.textinformationlabel.configure(
                   text="Температура - ПРЕВЫШЕНА, Влажность - НИЖЕ НОРМЫ \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')

           if self.temperature < "2" and self.humidity > "93":
               self.textinformationlabel.configure(
                   text="Температура - НИЖЕ НОРМЫ, Влажность - ПРЕВЫШЕНА \n ИДЕТ РАБОТА СИСТЕМЫ...", fg='orange')








           self.tempFrame.after(2, self.changeLabel) #it'll call itself continuously
           #self.humFrame.after(10, self.changeLabel)  # it'll call itself continuously

       def printline(self):
           out = ''
           # let's wait one second before reading output (let's give device time to answer)
           time.sleep(0.3)
           out = ser.readline()
           line = (out.decode(encoding="utf-8"))
           return line

obj1 = Clock()
root.mainloop()
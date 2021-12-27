"""
----------------------------------------------------------    
    Interfaz gráfica para controlar al robot Vlasbot V1
    Creado por: Vladimir Guajardo 
    Fecha de creación: Noviembre 2021
----------------------------------------------------------    
Librerias instaladas: - pynput - 
"""
from tkinter import Button, Entry, Frame, Label, PhotoImage, Tk
from typing import Text, TextIO
from pynput import keyboard
from pynput.keyboard import Key, Listener
from time import sleep
import RPi.GPIO as gpio 

#Configuración pines GPIO 
gpio.setmode(gpio.BCM)

# Declaración de variables para los motores  
motor_a_en=4
motor_a_pin1=26
motor_a_pin2=21

motor_b_en=17
motor_b_pin1=27
motor_b_pin2=18

# Configuración como salida motor A
gpio.setup(motor_a_en, gpio.OUT)
gpio.setup(motor_a_pin1, gpio.OUT)
gpio.setup(motor_a_pin2, gpio.OUT)

# Configuración como salida motor B
gpio.setup(motor_b_en, gpio.OUT)
gpio.setup(motor_b_pin1, gpio.OUT)
gpio.setup(motor_b_pin2, gpio.OUT)

# Configuración de la velocidad
pwm_a=gpio.PWM(motor_a_en, 1000)
pwm_b=gpio.PWM(motor_a_en, 1000)

#Funciones
def avanzar():
    print("Avanzando")
    gpio.output(motor_a_pin1, gpio.HIGH)
    gpio.output(motor_a_pin2, gpio.LOW)
    pwm_a.start(100)
    
def retroceder():
    print("Retroceder")

def GirarIzquierda():
    print("Girar izquierda")

def GirarDerecha():
    print("Girar Derecha")

def stop():
    print("Stop")
    gpio.output(motor_a_pin1, gpio.LOW)
    gpio.output(motor_a_pin2, gpio.LOW)
    #pwm_a.start(100)

def show(tecla):
    if tecla==tecla.up:
        print("Arriba")
        

windows=Tk()
windows.geometry("800x400")
windows.title("Interfaz de Control VlasBot | V 1.0")
#windows.configure(background='black')
windows.config(bg="#393939")
windows.iconbitmap("logo.ico")

frame_direction=Frame()
frame_direction.pack() # Se ubica el frame ddentro de la raiz
frame_direction.config(bg="black", width="380",height="300")
frame_direction.place(x="400",y="80")
#Bótones ####################################################################
btn_avanzar=Button(frame_direction, text="AVANZAR", command=avanzar)
btn_avanzar.config(width="10",height="2")
btn_avanzar.place(x="150",y="50")

btn_retroceder=Button(frame_direction, text="RETROCEDER", command=retroceder)
btn_retroceder.config(width="10",height="2")
btn_retroceder.place(x="150",y="220")

btn_izquierda=Button(frame_direction, text="IZQUIERDA", command=GirarIzquierda)
btn_izquierda.config(width="10",height="2")
btn_izquierda.place(x="20",y="135")

btn_derecha=Button(frame_direction, text="DERECHA", command=GirarDerecha)
btn_derecha.config(width="10",height="2")
btn_derecha.place(x="270",y="135")

img_btn_stop=PhotoImage(file='btnstop.png')
btn_stop=Button(frame_direction,image=img_btn_stop,command=stop)
#btn_stop.config(width="10",height="2")
btn_stop.place(x="140",y="105")

############################################################################
frame_ultrasonic= Frame()
frame_ultrasonic.pack()
frame_ultrasonic.config(bg="#507899",width="350",height="40")
frame_ultrasonic.place(x="20",y="80")

lbl_ultrasonic= Label(frame_ultrasonic,font=("calibri",15),bg="#507899",fg="white",text="Distancia en CMS: ")
lbl_ultrasonic.place(x="20",y="10")

# Se muestra el valor en tiempo real del sensor ultrasonido
lbl_valor_ultra=Label(frame_ultrasonic,font=("calibri",15),bg="#507899",fg="white",text=valor)
lbl_valor_ultra.place(x="180",y="10")
#----------------------------------------
# trtar de ejecutar llistener y windows.mainloo()
#with Listener(on_press = show) as listener: 
#    listener.join() 

##### main @@@@@@



windows.mainloop()




"""
frame_dirección=Frame(windows)
frame_dirección.config(width='200',height='200', relief='sunken')
frame_dirección.place(x=30, y=30)
#frame_dirección.pack()
"""







    

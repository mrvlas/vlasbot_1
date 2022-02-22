"""
----------------------------------------------------------    
    Interfaz gráfica para controlar al robot Vlasbot V1
    Creado por: Vladimir Guajardo 
    Fecha de creación: Noviembre 2021
----------------------------------------------------------    
Librerias instaladas: 
"""
from tkinter import *
from pynput.keyboard import Key, Listener
import threading
from time import sleep
import RPi.GPIO as gpio 

#Clase Gui Robot
class GuiRobot():
    def __init__(self):

        self.velocidad=100

        self.windows=Tk()
        self.windows.geometry("800x400")
        self.windows.title("Interfaz de Control VlasBot | V 1.0")
        self.windows.config(bg="#393939") 
        
        self.frame_direction=Frame()
        self.frame_direction.pack() # Se ubica el frame dentro de la raiz windows 
        self.frame_direction.config(bg="black", width="380",height="300")
        self.frame_direction.place(x="400",y="80")
        #Botón activar interfaz
        #btn_activar_gui=Button(windows,text="Activar interfaz", command=Activar_tec)
        #btn_activar_gui.place(x="650",y="30")
        #Botones ####################################################################
        self.btn_avanzar=Button(self.frame_direction, text="AVANZAR",command=self.avanzar)
        self.btn_avanzar.config(width="10",height="2")
        #self.#btn_avanzar.bind("<w>",avanzar)
        self.btn_avanzar.place(x="150",y="50")

        self.btn_retroceder=Button(self.frame_direction, text="RETROCEDER", command=self.retroceder)
        self.btn_retroceder.config(width="10",height="2")
        self.btn_retroceder.place(x="150",y="220")

        self.btn_izquierda=Button(self.frame_direction, text="IZQUIERDA", command=self.GirarIzquierda)
        self.btn_izquierda.config(width="10",height="2")
        self.btn_izquierda.place(x="20",y="135")

        self.btn_derecha=Button(self.frame_direction, text="DERECHA", command=self.GirarDerecha)
        self.btn_derecha.config(width="10",height="2")
        self.btn_derecha.place(x="270",y="135")

        self.img_btn_stop=PhotoImage(file='btnstop.png') # Imagen del boton stop 
        self.btn_stop=Button(self.frame_direction,image=self.img_btn_stop,command=self.stop)
        #btn_stop.config(width="10",height="2")
        self.btn_stop.place(x="150",y="106")

        ############################################################################
        self.frame_ultrasonic= Frame()
        self.frame_ultrasonic.pack()
        self.frame_ultrasonic.config(bg="#507899",width="350",height="40")
        self.frame_ultrasonic.place(x="20",y="80")

        self.lbl_ultrasonic= Label(self.frame_ultrasonic,font=("calibri",15),bg="#507899",fg="white",text="Distancia en CMS: ")
        self.lbl_ultrasonic.place(x="20",y="10")

        # Se muestra el valor en tiempo real del sensor ultrasonido
        self.lbl_valor_ultra=Label(self.frame_ultrasonic,font=("calibri",15),bg="#507899",fg="white",text="12,00")
        self.lbl_valor_ultra.place(x="180",y="10")
        #####################################################################
        # Boton LED
        self.btn_led=Button(self.windows, text="Encender LED", command=self.encender_led)
        self.btn_led.place(x="250", y="185")
        #####################################################################

        # Scale para controlar la velocidad 
        self.scale_velocidad=Scale(self.windows,variable=self.velocidad,orient= HORIZONTAL,length=200)
        self.scale_velocidad.place(x=200, y=135)
        
        # Se inicia un nuevo hilo
        threading.Thread(target=self.teclado).start()
        
        self.windows.mainloop()
        gpio.cleanup()
    
############# Métodos #######################
#     
    def teclado(self):
        # Collect events until released
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()       
    
    def on_press(self, key):
        #print('{0} pressed'.format(key))            
        if key== key.up:
            print("avanza")
            self.btn_avanzar.config(bg="red")            
        
        if key== Key.right:
            print("Derecha")
    
    def on_release(self, key):
        #print('{0} release'.format(key))
        if key==key.up:
            print("detnido")
            #self.btn_avanzar.config(bg='')
            
        if key == Key.esc:
            # Stop listener
            return False  

    def Activar_tec(self):
        print("Teclado Activado")

    def avanzar(self):
        print("Avanzando")
        pwm_b.start(self.velocidad) 
        pwm_a.start(self.velocidad)
        gpio.output(motor_a_pin2,gpio.HIGH)
        #gpio.output(motor_a_pin1,gpio.LOW)  
        gpio.output(motor_b_pin2,gpio.HIGH)
        #gpio.output(motor_b_pin1,gpio.LOW

    def stop(self):
        print("Stop")
        gpio.output(motor_a_pin2,gpio.LOW)
        gpio.output(motor_b_pin2,gpio.LOW)

        gpio.output(motor_a_pin1,gpio.LOW)
        gpio.output(motor_b_pin1,gpio.LOW)
    
    def retroceder(self):
        print("Retroceder")
        pwm_b.start(self.velocidad.get())
        pwm_a.start(self.velocidad.get())
        gpio.output(motor_a_pin1,gpio.HIGH)
        #gpio.output(motor_a_pin1,gpio.LOW)  
        gpio.output(motor_b_pin1,gpio.HIGH)
        #gpio.output(motor_b_pin1,gpio.LOW)

    def GirarIzquierda(self):
        print("Girar izquierda")
        pwm_b.start(self.velocidad.get()) 
        pwm_a.start(self.velocidad.get())
        gpio.output(motor_b_pin1,gpio.HIGH)
        gpio.output(motor_a_pin2,gpio.HIGH)

    def GirarDerecha(self):
        print("Girar Derecha")
        pwm_a.start(self.velocidad.get())
        pwm_b.start(self.velocidad.get())
        gpio.output(motor_a_pin1,gpio.HIGH)
        gpio.output(motor_b_pin2,gpio.HIGH)

    def encender_led(self):
        print("Encender LED")
        gpio.output(5,gpio.HIGH)
        gpio.output(6,gpio.HIGH)
        gpio.output(13,gpio.HIGH)
        sleep(3)
        print("Apagar LED")
        gpio.output(5,gpio.LOW)
        gpio.output(6,gpio.LOW)
        gpio.output(13,gpio.LOW)


############### main #################

gpio.setwarnings(False)
#Configuración pines GPIO 
gpio.setmode(gpio.BCM)
# Motor A
motor_a_en=4
motor_a_pin1=26
motor_a_pin2=21
# Motor B
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
pwm_b=gpio.PWM(motor_b_en, 1000)
# Configuracion pin LED
gpio.setup(5,gpio.OUT)
gpio.setup(6,gpio.OUT)
gpio.setup(13,gpio.OUT)

# Se crea el objeto
app=GuiRobot()


import serial
import tkinter 

class SerialMonitor:
    
    def __init__(self, win): #Constructor
        self.win = win
        
        self.ser = serial.Serial('COM3', 9600, timeout=1) 

        # Crear un widget de texto para mostrar los datos recibidos
        self.texto1 = tkinter.Text(win, width=30, height=2)
        self.texto1.place(x=20, y=60)

        # Crear un widget de texto para mostrar los datos decodificados
        self.texto2 = tkinter.Text(win, width=30, height=2)
        self.texto2.place(x=20, y=120)

        # Crear un botón para cerrar el puerto serial
        self.boton = tkinter.Button(win, text="Cerrar comunicacion", command=self.close_serial_port)
        self.boton.place(x=90, y=200)

        # Iniciar el monitoreo serial
        self.monitor_serial()

    def decodeManchester(self, datos):
        decode = ""
        if datos[:2] == "01":
            decode = "0"
        elif datos[:2] == "10":
            decode = "1"
        
        for i in range(2, len(datos), 2):
            if datos[i:i+2] == datos[i-2:i]:
                decode += "0"
            else:
                decode += "1"
        
        return decode

    def monitor_serial(self):
        try:
            line = self.ser.readline().decode()            
            if line:
                decoded_data = self.decodeManchester(line)
                
                # Mostrar datos recibidos 
                self.texto1.delete(1.0, tkinter.END)
                self.texto1.insert(tkinter.END, f"Recibido: {line}\n")
                self.texto1.see (tkinter.END)
                # Mostrar datos decodificados 
                self.texto2.delete(1.0, tkinter.END)
                self.texto2.insert(tkinter.END, f"Decodificado: {decoded_data}\n")
                self.texto2.see (tkinter.END)
        except serial.SerialException as e:
            print(f"Error: {e}")
        finally:
            self.win.after(100, self.monitor_serial)

    def close_serial_port(self):  
        #self.ser.close()
        print("Puerto serial cerrado.")
        self.win.destroy()

def main():
    # Configurar la ventana principal
    win = tkinter.Tk()
    win.geometry("550x280")
    win.title("Python GUI")
    
    # Agregar un label de título
    msg = tkinter.Label(win, text="Python GUI Proyecto-Comunicacion-Grupo 7")
    msg.place(x=140, y=11)

    #agrega una imagen
    imagen = tkinter.PhotoImage(file="D:\logo.gif")
    msg2 = tkinter.Label(win, image= imagen,bd=0)
    msg2.place(x=300,y=40)

    # Iniciar el loop principal de la GUI
    SerialMonitor(win)
    win.mainloop()

main()

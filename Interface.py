import serial
import tkinter as tk

class SerialMonitor:
    def __init__(self, win):
        self.win = win
        self.ser = serial.Serial('COM3', 9600, timeout=1)

        # Agregar un label de título
        msg = tk.Label(win, text="Python GUI Proyecto-Comunicacion-Grupo3")
        msg.place(x=100, y=11)

        # Create a text widget to display the received data
        self.text_widget = tk.Text(win, width=60, height=10)
        self.text_widget.place(x=20, y=40)

        # Create a button to close the serial port
        self.close_button = tk.Button(win, text="Close Serial Port", command=self.close_serial_port)
        self.close_button.place(x=20, y=240)

        # Start the serial monitoring loop
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
                self.text_widget.insert(tk.END, f"Recibido: {line} -> Decodificado: {decoded_data}\n")
                self.text_widget.see(tk.END)
        except serial.SerialException as e:
            print(f"Error: {e}")
        finally:
            self.win.after(100, self.monitor_serial)

    def close_serial_port(self):
        self.ser.close()
        print("Puerto serial cerrado.")
        self.win.destroy()

# Configurar la ventana principal
win = tk.Tk()
win.geometry("600x280")
win.title("Python GUI")

# Iniciar el loop principal de la GUI
app = SerialMonitor(win)
win.mainloop()
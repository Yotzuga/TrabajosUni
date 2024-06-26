import serial
from bluedot.btcomm import BluetoothServer

# Configurar la comunicación serie con el Arduino
arduino = serial.Serial("/dev/ttyACM0", 9600)

def filtro(data):
    if len(data) == 5:
        for i in data:
            if i != '0' and i != '1':
                return "Error de filtro"
        return data
    else:
        return "Error de datos"

def codificacion(data):
    df = ""
    if data[0] == "0":
        df = "01"
    elif data[0] == "1":
        df = "10"

    for i in range(1, len(data)):
        if data[i] == "0":
            df += df[-2] + df[-1]
        elif data[i] == "1":
            if df[-1] == "0":
                df += "01"
            else:
                df += "10"
    return df

def bluetooth(data):
    # Filtrar los datos recibidos:
    codigo = filtro(data)

    print("Datos recibidos por Bluetooth: ", codigo)

    if codigo == "Error de filtro":
        print("Error de filtro: Los datos recibidos no son válidos.")
    elif codigo == "Error de datos":
        print("Error de datos: La longitud de los datos recibidos no es válida.")
    else:
        # Codificar el string recibido
        resultado = codificacion(codigo)
        
        # Convertir el resultado a string para enviarlo por el puerto serie
        arduino.write(resultado.encode())
        

def main():
    # Iniciar el servidor Bluetooth
    BluetoothServer(bluetooth)

main()

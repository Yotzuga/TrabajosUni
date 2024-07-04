import serial
from bluedot.btcomm import BluetoothServer

# Configurar la comunicación serie con el Arduino
arduino = serial.Serial("/dev/ttyACM0", 9600)

def filtro(data):
    if len(data) == 5:
        for i in data:
            if i != '0' and i != '1':
                return "Error datos"
        return data
    else:
        return "Error longitud"

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
    
    if codigo == "Error datos":
        print(f"Los datos recibidos [{data}] no son binarios [0,1]")
    elif codigo == "Error longitud":
        print(f"La longitud de los datos es mayor a [5] en [{len(data)-5}]")
    else:
        print("Datos recibidos por Bluetooth: ", codigo)
        # Codificar el string recibido
        resultado = codificacion(codigo)
        
        # Convertir el resultado a string para enviarlo por el puerto serie
        arduino.write(resultado.encode())
        print("Manchester: ", resultado )

def main():
    # Iniciar el servidor Bluetooth
    BluetoothServer(bluetooth)

main()

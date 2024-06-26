import random

def aleatorio_codigo():#numeros pares
    codigo = random.randint(100000, 200000)
    if codigo % 2 != 0:  
        codigo = codigo + 1 
    return codigo

def aleatorio_ingles():#numeros impares
    codigo = random.randint(1, 15)
    if codigo % 2 == 0:  
        codigo = codigo + 1  
    return codigo

def leer_registro():
    registros = []
    with open('registro.txt', 'r',encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for idx, linea in enumerate(lineas):
            if idx > 0:  # Comienza desde la segunda línea gracias a enumerate()
                linea_str = linea.strip()
                linea_list = linea_str.split('|')

                
                codigo = int(linea_list[0])
                nombre = linea_list[1]
                tipo = linea_list[2]
                horario = linea_list[3]
                numero_de_creditos = int(linea_list[4])
                docente = linea_list[5]
                jefe_practica = linea_list[6] == 'True'
                ingles = linea_list[7] == 'True'
                p_docente = int(linea_list[8])
                p_jefe_practica = int(linea_list[9])
                p_ingles = int(linea_list[10])

                registro = {
                    'codigo': codigo,
                    'nombre': nombre,
                    'tipo': tipo,
                    'horario': horario,
                    'numero_de_creditos': numero_de_creditos,
                    'docente': docente,
                    'jefe_practica': jefe_practica,
                    'ingles': ingles,
                    'p_docente': p_docente,
                    'p_jefe_practica': p_jefe_practica,
                    'p_ingles': p_ingles
                }
                registros.append(registro)
                
    return registros



def agregar(registro):
    with open('registro.txt', 'a',encoding='utf-8') as archivo:
        #nueva-liena [dicc]
        linea = f"{registro['codigo']}|{registro['nombre']}|{registro['tipo']}|{registro['horario']}|{registro['numero_de_creditos']}|{registro['docente']}|{registro['jefe_practica']}|{registro['ingles']}|{registro['p_docente']}|{registro['p_jefe_practica']}|{registro['p_ingles']}\n"
        archivo.write(linea)
    

def crear_nueva_linea():
    codigo = aleatorio_codigo()
    nombre = input('Ingrese el nombre del curso: ').lower().capitalize()
    selector = int(input('Tipo del curso [1][Teórico-Práctico] [2][Investigación] [3][Taller]: '))
    if selector == 1:
        tipo = "Teórico-Práctico"
    elif selector ==2:
        tipo = "Investigación"
    else:
        tipo = "Taller"  
    horario = input('Ingrese el horario del curso [10am-12pm]: ').lower()
    numero_de_creditos = int(input('Ingrese el número de créditos del curso: '))
    docente = input('Ingrese el nombre del docente: ').lower().capitalize()
    jefe_practica = input('¿Tiene jefe de práctica? (True/False): ').lower().capitalize()  # Convertir a minúsculas
    if jefe_practica == "True":
        p_jefe_practica = random.randint(1, 20)  
    else:
        p_jefe_practica = 0
    ingles = input('¿Se imparte en inglés? (True/False): ').lower().capitalize()  # Convertir a minúsculas
    if ingles == "True":
        p_ingles = aleatorio_ingles() 
    else:
        p_ingles = 0
    p_docente = random.randint(1, 20)
    
    nueva_linea_registro = {
        'codigo': codigo,
        'nombre': nombre,
        'tipo': tipo,
        'horario': horario,
        'numero_de_creditos': numero_de_creditos,
        'docente': docente,
        'jefe_practica': jefe_practica,
        'ingles': ingles,
        'p_docente': p_docente,
        'p_jefe_practica': p_jefe_practica,
        'p_ingles': p_ingles
    }

    return nueva_linea_registro 

def editar_registro(line_edit):#linea a editar{dicc}
    registros = leer_registro()
    contenido = 'codigo_curso|nombre_curso|tipo|horario|numero_de_creditos|docente|jefe_practica|ingles|p_docente|p_jefe_practica|p_ingles'
    for registro in registros:
        if registro['codigo'] == line_edit['codigo']:
            linea = f"\n{line_edit['codigo']}|{line_edit['nombre']}|{line_edit['tipo']}|{line_edit['horario']}|{line_edit['numero_de_creditos']}|{line_edit['docente']}|{line_edit['jefe_practica']}|{line_edit['ingles']}|{line_edit['p_docente']}|{line_edit['p_jefe_practica']}|{line_edit['p_ingles']}"
        else:
            linea = f"\n{registro['codigo']}|{registro['nombre']}|{registro['tipo']}|{registro['horario']}|{registro['numero_de_creditos']}|{registro['docente']}|{registro['jefe_practica']}|{registro['ingles']}|{registro['p_docente']}|{registro['p_jefe_practica']}|{registro['p_ingles']}"
        contenido = contenido + linea

    with open('registro.txt', 'w',encoding='utf-8') as archivo:
        archivo.write(contenido)

def eliminar_registro(codigo_a_eliminar):
    registros = leer_registro()

    with open('registro.txt', 'w',encoding='utf-8') as archivo:
        archivo.write('codigo_curso|nombre_curso|tipo|horario|numero_de_creditos|docente|jefe_practica|ingles|p_docente|p_jefe_practica|p_ingles\n')
        for registro in registros:
            if registro['codigo'] != codigo_a_eliminar:#excluir la linea_a_eliminar
                linea = f"{registro['codigo']}|{registro['nombre']}|{registro['tipo']}|{registro['horario']}|{registro['numero_de_creditos']}|{registro['docente']}|{registro['jefe_practica']}|{registro['ingles']}|{registro['p_docente']}|{registro['p_jefe_practica']}|{registro['p_ingles']}\n"
                archivo.write(linea)#sobreescribe-lista-dicc menos_linea_a_eliminar



    




def bubble_sort_dict_list(lista, key):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j][key] > lista[j + 1][key]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]                
                                                
def quicksort_dict_list(lista, key):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = []
        mayores = []
        for i in range(1, len(lista)):
            if lista[i][key] > pivot[key]:
                mayores.append(lista[i])
            else:
                menores.append(lista[i])
        mayores = quicksort_dict_list(mayores, key)
        menores = quicksort_dict_list(menores, key)
        return menores + [pivot] + mayores

def imprimir_cursos(lista_cursos):#lista-dicc
    # Imprimir encabezado de la tabla
    print(f"{'Código':<10}{'Nombre':<25}{'Tipo':<20}{'Horario':<15}{'Créditos':<10}"
          f"{'Docente':<15}{'Jefe_practica':<20}{'Inglés':<10}{'P_Docente':<10}{'P_Jefe':<10}{'P_Inglés':<10}")

    # Imprimir los datos de cada curso
    for curso in lista_cursos:
        codigo = curso['codigo']
        nombre = curso['nombre']
        tipo = curso['tipo']
        horario = curso['horario']
        creditos = curso['numero_de_creditos']
        docente = curso['docente']
        jefe_practica = 'Sí' if curso['jefe_practica'] else 'No'
        ingles = 'Sí' if curso['ingles'] else 'No'
        p_docente = curso['p_docente']
        p_jefe = curso['p_jefe_practica']
        p_ingles = curso['p_ingles']

        # Imprimir cada fila de la tabla
        print(f"{codigo:<10}{nombre:<25}{tipo:<20}{horario:<15}{creditos:<10}"
              f"{docente:<15}{jefe_practica:<20}{ingles:<10}{p_docente:<10}{p_jefe:<10}{p_ingles:<10}")


def busqueda_binaria(registros, puntaje_buscado, key):
    izquierda, derecha = 0, len(registros) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if registros[medio][key] == puntaje_buscado:
            return medio + 1, registros[medio]['docente']
        elif registros[medio][key] < puntaje_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, None  # Devolver -1 y None si no se encuentra


        
def main():
    
    while True:
        print("==================================")
        print("""
    Opciones:
      1) Crear nuevo registro
      2) Editar registro
      3) Eliminar registro
      4) Reporte
      5) Buscar puntaje
      6) Salir
        """)
        print("==================================\n")
        opcion = int(input('Ingrese una opción: '))
        
        
        if opcion == 1:
            while True:
                print("----------------------------------------------------------------")
                agregar(crear_nueva_linea())
                print("----------------------------------------------------------------")
                continuar = input("¿Desea crear otro registro? (Sí/No): ").lower()
                if continuar != 'si':
                    break
            
        elif opcion == 2:
            while True:
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                imprimir_cursos(leer_registro()) #mostrar la tabla de registro
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                codigo = int(input('Ingrese el codigo a editar: '))
                
                existeCodigo = False
                for lines in leer_registro():
                    if codigo == lines["codigo"]:
                        existeCodigo = True
                
                if not existeCodigo:
                    print("El codigo no existe: " + str(codigo))
                    continue
                
                nombre = input('Ingrese el nombre del curso: ').lower().capitalize()
                selector = int(input('Tipo del curso [1][Teórico-Práctico] [2][Investigación] [3][Taller]: '))
                if selector == 1:
                    tipo = "Teórico-Práctico"
                elif selector ==2:
                    tipo = "Investigación"
                else:
                    tipo = "Taller"    
                horario = input('Ingrese el horario del curso "10am-12pm": ').lower()
                numero_de_creditos = int(input('Ingrese el número de créditos del curso: '))
                docente = input('Ingrese el nombre del docente: ').lower().capitalize()
                p_docente = int(input('Ingrese el p_docente correcto[1,20]: '))
                jefe_practica = input('¿Tiene jefe de práctica? (True/False): ').lower().capitalize()  # Convertir a minúsculas
                if jefe_practica == "True":
                    p_jefe_practica = int(input('Ingrese el p_jefe_practica correcto[1,20]: '))  
                else:
                    p_jefe_practica = 0
                ingles = input('¿Se imparte en inglés? (True/False): ').lower().capitalize()  # Convertir a minúsculas
                if ingles == "True":
                    p_ingles = int(input('Ingrese el p_ingles correcto[1,15][impar]: '))   
                else:
                    p_ingles = 0
                
                registro_actualizado = {
                'codigo': codigo,
                'nombre': nombre,
                'tipo': tipo,
                'horario': horario,
                'numero_de_creditos': numero_de_creditos,
                'docente': docente,
                'jefe_practica': jefe_practica,
                'ingles': ingles,
                'p_docente': p_docente,
                'p_jefe_practica': p_jefe_practica,
                'p_ingles': p_ingles
                }
                
                editar_registro(registro_actualizado)
                
                print()
                # Pregunta si desea seguir editando
                continuar = input("¿Desea seguir editando registros? (Sí/No): ").lower()
                print()
                if continuar != 'si':
                    break
            
        elif opcion == 3:
            while True:
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                imprimir_cursos(leer_registro()) #mostrar la tabla de registro
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
                codigo_a_eliminar = int(input('Ingrese el codigo a eliminar: '))
                eliminar_registro(codigo_a_eliminar)
                print()
                print("Opción de eliminación seleccionada.")
                
                # Pregunta si desea seguir eliminando
                continuar = input("¿Desea seguir eliminando registros? (Sí/No): ").lower()
                if continuar != 'si':
                    break
            
        elif opcion == 4:
            while True:
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                cursos_ordenados = quicksort_dict_list(leer_registro(), 'p_docente')
                imprimir_cursos(cursos_ordenados)
                print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
                
                registros = leer_registro()
                
                with open('registro.txt', 'w',encoding='utf-8') as archivo:
                    archivo.write('codigo_curso|nombre_curso|tipo|horario|numero_de_creditos|docente|jefe_practica|ingles|p_docente|p_jefe_practica|p_ingles\n')
                    for registro in registros:
                        linea = f"{registro['codigo']}|{registro['nombre']}|{registro['tipo']}|{registro['horario']}|{registro['numero_de_creditos']}|{registro['docente']}|{registro['jefe_practica']}|{registro['ingles']}|{registro['p_docente']}|{registro['p_jefe_practica']}|{registro['p_ingles']}\n"
                        archivo.write(linea)
                
                # Pregunta si desea seguir viendo reportes
                continuar = input("¿Desea seguir viendo reportes? (Sí/No): ").lower()
                if continuar != 'si':
                    break
            
        elif opcion == 5:
            
            while True:
                nota=int(input("puntaje: "))
                
                registro_data = leer_registro()

                bubble_sort_dict_list(registro_data, 'p_docente')
                lista_ordenada =[]
                for persona in registro_data:
                    lista_ordenada.append(persona)
                registro = lista_ordenada
    
                posicion, nombre_docente = busqueda_binaria(registro, nota, 'p_docente')
                if posicion != -1:
                    print(f"El docente con puntaje {nota} se encuentra en la posición {posicion} y se llama {nombre_docente}.")
                else:
                    print("No se encontró ningún docente con ese puntaje.")


                continuar = input("¿Desea seguir buscando puntajes? (Sí/No): ").lower()
                if continuar != 'si':
                    break

        elif opcion == 6:
            # Salir del bucle si la opción es 6
            break

        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

    print('¡FIN!')  
main()



















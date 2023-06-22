import easygui as eg
from tkinter import messagebox

informacion_gramaticas = []
informacion_ap = []

def salir():
    exit()

def verificar_producciones(gramatica):
    producciones = gramatica['producciones']

    for produccion in producciones:
        expresion = produccion[1:]

        # Verificar si la expresión tiene más de un símbolo terminal
        terminales = sum(1 for simbolo in expresion if simbolo in gramatica['terminales'])
        if terminales > 1:
            return False

    return True


def cargar_gramaticas():
    global informacion_gramaticas
    lista = []
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    imprimir2 = 'Archivo no seleccionado, vuelva a intentarlo'
    extension = ["*.py", "*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='C:/Users/neri_/OneDrive/Escritorio/*glc',
                             filetypes=extension)
    mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
        75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    f = open(archivo, 'r', encoding="utf8")
    leer = f.read()
    lista_temporal = leer.split('%')
    for element in lista_temporal:
        temporal_sin_vacios = ''
        if element != '' and element != ' ':
            temporal_sin_vacios = element   
        temporal = temporal_sin_vacios.split('\n')
        temporal_sin_vacios = []
        for datos in temporal:
            if datos != '' and datos != ' ':
                temporal_sin_vacios.append(datos)
        if element != '' and element != ' ':
            lista.append(temporal_sin_vacios)
    for element in lista:
        diccionario = {}
        diccionario["nombre"] = element[0]
        diccionario["no terminales"] = element[1].split(',')
        diccionario["terminales"] = element[2].split(',')
        diccionario["no terminal inicial"] = element[3]
        producciones = element[4::]
        producciones_corregidas = []
        for datos in producciones:
            lista_producc = []
            dato = datos.split('::=')
            temporal = dato[1].split(' ')
            lista_producc.append(dato[0])
            for produ in temporal:
                if produ != '' and produ != ' ':
                    lista_producc.append(produ)
            producciones_corregidas.append(lista_producc)
        diccionario["producciones"] = producciones_corregidas
        #Verifica si es Regular o GLC
        es_regular = verificar_producciones(diccionario)
        tipo_gramatica = 'Regular' if es_regular else 'Libre de contexto'
        imprimir2 = f"La gramática '{diccionario['nombre']}' es: {tipo_gramatica}" 
        if tipo_gramatica == 'Libre de contexto':
            informacion_gramaticas.append(diccionario)
            mensaje = imprimir.center(75, ' ') + '\n' + imprimir2.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
            messagebox.showinfo(message=mensaje, title="Mensaje")
        else:
            imprimir3 = 'Por tanto, No se cargó en el sistema'
            mensaje = imprimir.center(75, ' ') + '\n' + imprimir2.center(75, ' ') + '\n' + imprimir3.center(75, ' ') +'\n' + imprimir.center(75, ' ') + '\n'
            messagebox.showerror(message=mensaje, title="Mensaje")
    f.close()
    print(informacion_gramaticas)
import easygui as eg
from tkinter import messagebox ,ttk,Label,Button,Entry,StringVar

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
    # print(informacion_gramaticas)

def buscar_gramatica_por_nombre(nombre):
    for gramatica in informacion_gramaticas:
        if gramatica['nombre'] == nombre:
            return gramatica
    return None

def buscar_automata_por_nombre(nombre):
    for gramatica in informacion_ap:
        if gramatica['nombre'] == nombre:
            return gramatica
    return None

def cargar_automatas_pila():
    global informacion_ap
    lista = []
    imprimir = '*********************************************'
    imprimir1 = 'Archivo Cargado exitosamente'
    imprimir2 = 'Archivo no seleccionado, vuelva a intentarlo'
    extension = ["*.py", "*.pyc"]
    archivo = eg.fileopenbox(msg="Abrir archivo",
                             title="Control: fileopenbox",
                             default='C:/Users/neri_/OneDrive/Escritorio/*ap',
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
        diccionario["alfabeto"] = element[1].split(',')
        diccionario["simbolos pila"] = element[2].split(',')
        diccionario["estados"] = element[3].split(',')
        diccionario["estado inicial"] = element[4]
        diccionario["estado aceptación"] = element[5]
        transiciones = element[6::]
        trans_corregidas = []
        for datos in transiciones:
            lista_trans = []
            dato = datos.split(';')
            temporal = dato[0].split(',')
            dato = dato[1].split(',')
            for trans in temporal:
                if trans != '' and trans != ' ':
                    lista_trans.append(trans)
            for trans in dato:
                if trans != '' and trans != ' ':
                    lista_trans.append(trans)
            trans_corregidas.append(lista_trans)
        diccionario["transiciones"] = trans_corregidas
        informacion_ap.append(diccionario)
    f.close()
    mensaje = 'Ruta del Archivo: ' + str(archivo) + '\n\n\n\n\n' + imprimir.center(
        75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ') + '\n'
    messagebox.showinfo(message=mensaje, title="Mensaje")
    # print(informacion_ap)

def validar_cadena(automata, cadena):
    pila = ['$']  # Pila inicializada con el símbolo inicial
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    
    for simbolo in cadena:
        if simbolo not in automata['alfabeto']:
            return False  # El símbolo no pertenece al alfabeto
        
        transicion_encontrada = False
        
        # Buscar una transición válida para el estado actual y el símbolo de entrada
        for transicion in automata['transiciones']:
            estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
            
            # Comprobar si la transición es válida
            if estado_origen == estado_actual and (simbolo_entrada == simbolo or simbolo_entrada == '$') and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
                # Aplicar la transición actualizando el estado y la pila
                estado_actual = estado_destino
                
                if simbolo_pila != '$':
                    pila.pop()
                
                if simbolo_insertar != '$':
                    pila.extend(list(simbolo_insertar))
                
                transicion_encontrada = True
                break
        
        if not transicion_encontrada:
            return False  # No se encontró una transición válida
    
    # Comprobar si se puede realizar una transición lambda desde el estado actual
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        
        if estado_origen == estado_actual and simbolo_entrada == '$' and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
            estado_actual = estado_destino
            
            if simbolo_pila != '$':
                pila.pop()
            
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            
            break
    
    # Comprobar si el estado actual es un estado de aceptación
    if estado_actual == automata['estado aceptación']:
        return True
    else:
        return False

def ruta_validacion(automata, cadena):
    imprimir = '*********************************************'
    pila = ['$']  # Pila inicializada con el símbolo inicial
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    ruta_transiciones = []  # Lista para almacenar la ruta de transiciones
    
    for simbolo in cadena:
        if simbolo not in automata['alfabeto']:
            return False  # El símbolo no pertenece al alfabeto
        
        transicion_encontrada = False
        
        # Buscar una transición válida para el estado actual y el símbolo de entrada
        for transicion in automata['transiciones']:
            estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
            
            # Comprobar si la transición es válida
            if estado_origen == estado_actual and (simbolo_entrada == simbolo or simbolo_entrada == '$') and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
                # Aplicar la transición actualizando el estado y la pila
                estado_actual = estado_destino
                
                if simbolo_pila != '$':
                    pila.pop()
                
                if simbolo_insertar != '$':
                    pila.extend(list(simbolo_insertar))
                
                # Agregar la transición a la ruta
                ruta_transiciones.append(transicion)
                
                transicion_encontrada = True
                break
        
        if not transicion_encontrada:
            return False  # No se encontró una transición válida
    
    # Comprobar si se puede realizar una transición lambda desde el estado actual
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        
        if estado_origen == estado_actual and simbolo_entrada == '$' and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
            estado_actual = estado_destino
            
            if simbolo_pila != '$':
                pila.pop()
            
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            
            # Agregar la transición a la ruta
            ruta_transiciones.append(transicion)
            
            break
    
    # Comprobar si el estado actual es un estado de aceptación
    if estado_actual == automata['estado aceptación']:
        # Imprimir la ruta de transiciones
        imprimir1 = 'La cadena fue aceptada'
        mensaje = imprimir.center(75, ' ') +  imprimir1.center(75, ' ') + imprimir.center(75, ' ') 
        messagebox.showinfo(message=mensaje, title="Mensaje")
        return ruta_transiciones
    else:
        imprimir1 = 'La cadena no fue aceptada'
        mensaje = imprimir.center(75, ' ') +  imprimir1.center(75, ' ') + imprimir.center(75, ' ')
        messagebox.showinfo(message=mensaje, title="Mensaje")
        return False
    
def generar_tabla_html(automata, cadena):
    pila = ['$']  # Pila inicializada con el símbolo inicial
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    
    # Crear el contenido de la tabla HTML
    contenido_tabla = '<table>'
    contenido_tabla += '<tr><th>Iteraciones</th><th>Pila</th><th>Entrada</th><th>Transición</th></tr>'
    
    for i, simbolo in enumerate(cadena):
        if simbolo not in automata['alfabeto']:
            return False  # El símbolo no pertenece al alfabeto
        
        transicion_encontrada = False
        transicion_obtenida = None
        
        # Buscar una transición válida para el estado actual y el símbolo de entrada
        for transicion in automata['transiciones']:
            estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
            
            # Comprobar si la transición es válida
            if estado_origen == estado_actual and (simbolo_entrada == simbolo or simbolo_entrada == '$') and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
                # Aplicar la transición actualizando el estado y la pila
                estado_actual = estado_destino
                
                if simbolo_pila != '$':
                    pila.pop()
                
                if simbolo_insertar != '$':
                    pila.extend(list(simbolo_insertar))
                
                transicion_encontrada = True
                transicion_obtenida = transicion
                break
        
        # Agregar una fila a la tabla con los datos de la iteración
        contenido_tabla += f'<tr><td>{i + 1}</td><td>{" ".join(pila)}</td><td>{simbolo}</td><td>{transicion_obtenida}</td></tr>'
        
        if not transicion_encontrada:
            return False  # No se encontró una transición válida
    
    # Comprobar si se puede realizar una transición lambda desde el estado actual
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        
        if estado_origen == estado_actual and simbolo_entrada == '$' and (simbolo_pila == pila[-1] or simbolo_pila == '$'):
            estado_actual = estado_destino
            
            if simbolo_pila != '$':
                pila.pop()
            
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            
            break
    
    # Agregar la última fila a la tabla con el estado final
    contenido_tabla += f'<tr><td>{len(cadena) + 1}</td><td>{" ".join(pila)}</td><td>-</td><td>{estado_actual}</td></tr>'
    
    contenido_tabla += '</table>'
    
    # Crear el archivo HTML con estilo
    contenido_html = f'''
    <html>
    <head>
        <title>Tabla de Validación</title>
        <style>
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            
            th, td {{
                padding: 8px;
                text-align: left;
                border-bottom: 1px solid #ddd;
            }}
            
            th {{
                background-color: #f2f2f2;
            }}
        </style>
    </head>
    <body>
        {contenido_tabla}
    </body>
    </html>
    '''
    
    # Guardar el archivo HTML
    with open('tabla_validacion.html', 'w') as archivo_html:
        archivo_html.write(contenido_html)
    
    # Abrir el archivo HTML en un navegador web
    import webbrowser
    webbrowser.open('tabla_validacion.html')
    
    return True


import easygui as eg
from tkinter import messagebox ,ttk,Label,Button,Entry,StringVar
import graphviz
import webbrowser

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
    pila = []  # Pila inicializada vacía
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    
    # Encontrar la primera transición del estado inicial
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        if estado_origen == estado_actual:
            # Actualizar el estado y la pila con la primera transición
            estado_actual = estado_destino
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            break
    
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
    pila = []  # Pila inicializada vacía
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    ruta_transiciones = []  # Lista para almacenar la ruta de transiciones
    
    # Encontrar la primera transición del estado inicial
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        if estado_origen == estado_actual:
            # Actualizar el estado y la pila con la primera transición
            estado_actual = estado_destino
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            # Agregar la transición a la ruta
            ruta_transiciones.append(transicion)
            break
    
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
    pila = []  # Pila inicializada vacía
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    
    # Crear el contenido de la tabla HTML
    contenido_tabla = '<table>'
    contenido_tabla += '<tr><th>Iteraciones</th><th>Pila</th><th>Entrada</th><th>Transición</th></tr>'
    
    # Encontrar la primera transición del estado inicial
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        if estado_origen == estado_actual:
            # Actualizar el estado y la pila con la primera transición
            estado_actual = estado_destino
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            # Agregar una fila a la tabla con los datos de la primera iteración
            contenido_tabla += f'<tr><td>1</td><td>{" ".join(pila)}</td><td>-</td><td>{transicion}</td></tr>'
            break
    
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
        contenido_tabla += f'<tr><td>{i + 2}</td><td>{" ".join(pila)}</td><td>{simbolo}</td><td>{transicion_obtenida}</td></tr>'
        
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
    contenido_tabla += f'<tr><td>{len(cadena) + 2}</td><td>{" ".join(pila)}</td><td>-</td><td>{estado_actual}</td></tr>'
    
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

def generar_grafo_automata_pila(automata):
    nombre = automata['nombre']
    alfabeto = automata['alfabeto']
    simbolos_pila = automata['simbolos pila']
    estados = automata['estados']
    estado_inicial = automata['estado inicial']
    estado_aceptacion = automata['estado aceptación']
    transiciones = automata['transiciones']

    # Crear un objeto Digraph de Graphviz
    grafo = graphviz.Digraph(name=nombre)

    # Configurar el estilo del grafo
    grafo.attr('graph', fontsize='20', labelloc='t')
    grafo.attr(rankdir='LR', size='8,5')

    # Crear un nodo adicional para agregar el texto de información
    info_node_name = 'info_node'
    info_label = f"Nombre: {nombre}\nAlfabeto: {alfabeto}\nEstados: {estados}\nEstado Inicial: {estado_inicial}\nEstado de Aceptación: {estado_aceptacion}"
    grafo.node(info_node_name, label=info_label, shape='plaintext')

    # Agregar nodos al grafo
    for estado in estados:
        if estado != estado_inicial and estado != estado_aceptacion:
            etiqueta = f"Estado: {estado}"
            grafo.node(estado, label=etiqueta, shape='circle')

    # Agregar el nodo de estado de aceptación con un estilo diferente
    estado_aceptacion_label = f"Estado: {estado_aceptacion}"
    grafo.node(estado_aceptacion, label=estado_aceptacion_label, shape='doublecircle', style='bold')

    # Agregar arcos al grafo
    for transicion in transiciones:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_pila_nuevo = transicion
        etiqueta = f"{simbolo_entrada}, {simbolo_pila} -> {simbolo_pila_nuevo}"
        grafo.edge(estado_origen, estado_destino, label=etiqueta)

    # Agregar conexión entre el nodo adicional y el estado inicial
    grafo.edge(info_node_name, estado_inicial, style='invis')

    # Renderizar el grafo y guardarlo como un archivo en formato PDF
    nombre_archivo = f"{nombre}"
    grafo.format = 'png'
    grafo.render(filename=nombre_archivo, cleanup=True)

def generar_tabla_html_paso_a_paso(automata, cadena):
    pila = []  # Pila inicializada vacía
    estado_actual = automata['estado inicial']  # Estado inicial del autómata
    
    # Crear el contenido de la tabla HTML
    contenido_tabla = '<table>'
    contenido_tabla += '<tr><th>Iteraciones</th><th>Pila</th><th>Entrada</th><th>Transición</th></tr>'
    
    # Encontrar la primera transición del estado inicial
    for transicion in automata['transiciones']:
        estado_origen, simbolo_entrada, simbolo_pila, estado_destino, simbolo_insertar = transicion
        if estado_origen == estado_actual:
            # Actualizar el estado y la pila con la primera transición
            estado_actual = estado_destino
            if simbolo_insertar != '$':
                pila.extend(list(simbolo_insertar))
            # Agregar una fila a la tabla con los datos de la primera iteración
            contenido_tabla += f'<tr><td>1</td><td>{" ".join(pila)}</td><td>-</td><td>{transicion}</td></tr>'
            break
    
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
        contenido_tabla += f'<tr><td>{i + 2}</td><td>{" ".join(pila)}</td><td>{simbolo}</td><td>{transicion_obtenida}</td></tr>'
        
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
    contenido_tabla += f'<tr><td>{len(cadena) + 2}</td><td>{" ".join(pila)}</td><td>-</td><td>{estado_actual}</td></tr>'
    
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
    # Obtener la ruta del archivo de imagen
    ruta_imagen = f'{automata["nombre"]}.png'

    # Agregar la etiqueta <img> al contenido HTML
    contenido_html += f'<img src="{ruta_imagen}" alt="Grafo del autómata">'

    # Guardar el archivo HTML
    with open('reporte_paso_a_paso.html', 'w') as archivo_html:
        archivo_html.write(contenido_html)
    
    # Abrir el archivo HTML en un navegador web
    import webbrowser
    webbrowser.open('reporte_paso_a_paso.html')
    
    return True



def generar_grafo_derivacion(gramatica):
    grafo = graphviz.Digraph()

    nombre = gramatica['nombre']
    no_terminales = gramatica['no terminales']
    terminales = gramatica['terminales']
    no_terminal_inicial = gramatica['no terminal inicial']
    producciones = gramatica['producciones']
    # Agregar nodos de no terminales
    for no_terminal in no_terminales:
        grafo.node(no_terminal, shape='ellipse')
    # Agregar nodos de terminales
    for terminal in terminales:
        grafo.node(terminal, shape='box')
    # Agregar aristas de producciones
    for produccion in producciones:
        no_terminal = produccion[0]
        expresion = produccion[1:]
        etiqueta = ' '.join(expresion)
        grafo.edge(no_terminal, etiqueta)
    # Agregar nodo inicial
    grafo.node('Inicio', shape='point')
    grafo.edge('Inicio', no_terminal_inicial)
    return grafo
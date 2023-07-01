import functools
import tkinter
from tkinter import Label, Button, Frame, messagebox, Entry, StringVar, Text, ttk
import easygui as eg
from ttkthemes import ThemedTk
import graphviz
from graphviz import Digraph
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import ImageTk, Image
import os
import sys

import funciones

def cerrar_ventana(segundos_restantes):
    if segundos_restantes > 0:
        label_contador.config(text=f"Esta Pantalla Desaparecerá en {segundos_restantes} Segundos")
        ventana.after(1000, cerrar_ventana, segundos_restantes - 1)
    else:
        miFrameV.pack_forget()
        var_ventana_principal.pack(side="top", fill="both", expand=True)

#LLamado Ventanas
def mostrar_principal():
    miFrameV.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget()
    var_ventana_arbol.pack_forget()
    var_ventana_automata_pila.pack_forget()
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_principal.pack(side="top", fill="both", expand=True)

def mostrar_modulo_gramaticas():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_info_gramaticas.pack_forget()
    var_ventana_arbol.pack_forget()
    var_ventana_automata_pila.pack_forget()
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_gramaticas.pack(side="top", fill="both", expand=True)

def mostrar_informacion_gramaticas():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_arbol.pack_forget()
    var_ventana_automata_pila.pack_forget()
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_info_gramaticas.pack(side="top", fill="both", expand=True)

def mostrar_ventana_arbol():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget()
    var_ventana_automata_pila.pack_forget() 
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_arbol.pack(side="top", fill="both", expand=True)  

def mostrar_ventana_automata_pila():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget() 
    var_ventana_arbol.pack_forget()  
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_automata_pila.pack(side="top", fill="both", expand=True)

def mostrar_ventana_info_ap():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget() 
    var_ventana_arbol.pack_forget()  
    var_ventana_automata_pila.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_info_automatasap.pack(side="top", fill="both", expand=True)

def mostrar_ventana_validar_ap():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget() 
    var_ventana_arbol.pack_forget()  
    var_ventana_automata_pila.pack_forget()
    var_ventana_info_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack(side="top", fill="both", expand=True)
def mostrar_ventana_ruta_validacion_ap():
    miFrameV.pack_forget()
    var_ventana_principal.pack_forget()
    var_ventana_gramaticas.pack_forget()
    var_ventana_info_gramaticas.pack_forget() 
    var_ventana_arbol.pack_forget()  
    var_ventana_automata_pila.pack_forget()
    var_ventana_info_automatasap.pack_forget()
    var_ventana_validar_automatasap.pack_forget()
    var_ventana_ruta_validacion_automatasap.pack(side="top", fill="both", expand=True)

#Ventanas

def ventana_principal(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Menú Principal")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_modulo_gramaticas = Button(frame_centrado, text='Módulo Grámaticas',width=15, height=3, bd="4", command=mostrar_modulo_gramaticas)
    boton_modulo_gramaticas.grid(row=1, column=0, padx=10, pady=10)
    boton_modulo_ap = Button(frame_centrado, text='Módulo AP',width=15, height=3, bd="4", command=mostrar_ventana_automata_pila)
    boton_modulo_ap.grid(row=2, column=0, padx=10, pady=10)
    boton_salir = Button(frame_centrado, text='Salir', width=15,height=3, command=callback, bd="4")
    boton_salir.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def ventana_modulo_gramaticas(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Módulo Grámaticas")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_cargar = Button(frame_centrado,text="Cargar Archivo", command=funciones.cargar_gramaticas , width=15,height=3)
    boton_cargar.grid(row=1,column=0,padx=10,pady=10)
    boton_info = Button(frame_centrado,text="Información General", command=mostrar_informacion_gramaticas , width=15,height=3)
    boton_info.grid(row=2,column=0,padx=10,pady=10)
    boton_arbol = Button(frame_centrado,text="Árbol de Derivación", command=mostrar_ventana_arbol , width=15,height=3)
    boton_arbol.grid(row=3,column=0,padx=10,pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=15,height=3, command=callback, bd="4")
    boton_regresar.grid(row=4, column=0, padx=10, pady=10)
    return main_frame

def ventana_informacion_gramaticas(master, callback=None, args=(), kwargs={}):
    global frame_informacion_gramaticas, boton_regresar
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_informacion_gramaticas = Frame(main_frame, height=310, width=450)
    frame_informacion_gramaticas.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_informacion_gramaticas, text="Modulo información Grámaticas")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_informacion_gramaticas, text="Elija una Grámatica")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_informacion_gramaticas,text='Mostrar Grámaticas',width=15,height=3,command=mostrar_gramaticas,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar = Button(frame_informacion_gramaticas, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def mostrar_gramaticas():
    global combo_gramaticas
    nombres_gramaticas = []
    for element in funciones.informacion_gramaticas:
        nombres_gramaticas.append(element['nombre'])
    combo_gramaticas = ttk.Combobox(frame_informacion_gramaticas,font=('Arial',10),state="readonly",values=nombres_gramaticas)
    combo_gramaticas.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar.grid(row=3, column=1, padx=10, pady=10)
    boton_mostrar = Button(frame_informacion_gramaticas,text='Mostrar Información',width=15,height=3,command=mostrar_info_gramaticas,bd="4")
    boton_mostrar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

def imprimir_producciones_unicas(gramatica):
    producciones = gramatica['producciones']
    no_terminales = gramatica['no terminales']

    no_terminales_mostrados = set()

    for produccion in producciones:
        no_terminal = produccion[0]
        expresion = produccion[1:]

        if no_terminal in no_terminales_mostrados:
            print(f"{' ' * (len(no_terminal) + 3)}| {' '.join(expresion)}")
        else:
            print(f"{no_terminal} > {' '.join(expresion)}")
            no_terminales_mostrados.add(no_terminal)

def mostrar_producciones_unicas_en_texto(gramatica, texto):
    producciones = gramatica['producciones']
    no_terminales = gramatica['no terminales']

    no_terminales_mostrados = set()

    for produccion in producciones:
        no_terminal = produccion[0]
        expresion = produccion[1:]

        if no_terminal in no_terminales_mostrados:
            texto.insert(tkinter.END, ' ' * (len(no_terminal) + 3) + '| ' + ' '.join(expresion) + '\n')
        else:
            texto.insert(tkinter.END, f"{no_terminal} > {' '.join(expresion)}\n")
            no_terminales_mostrados.add(no_terminal)

def mostrar_info_gramaticas():
    gramatica = funciones.buscar_gramatica_por_nombre(combo_gramaticas.get())
    texto_gramaticas = Text(frame_informacion_gramaticas)
    mostrar_producciones_unicas_en_texto(gramatica, texto_gramaticas)
    texto_gramaticas.grid(row=2,column=0,padx=10,pady=10,columnspan=2)

def ventana_arbol_gramaticas(master, callback=None, args=(), kwargs={}):
    global frame_arbol, boton_regresar_arbol
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_arbol = Frame(main_frame, height=310, width=450)
    frame_arbol.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_arbol, text="Modulo Árbol de Derivación")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_arbol, text="Elija una Grámatica")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_arbol,text='Mostrar Grámaticas',width=15,height=3,command=mostrar_gramaticas_arbol,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_arbol = Button(frame_arbol, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_arbol.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def mostrar_gramaticas_arbol():
    global combo_gramaticas_arbol
    nombres_gramaticas = []
    for element in funciones.informacion_gramaticas:
        nombres_gramaticas.append(element['nombre'])
    combo_gramaticas_arbol = ttk.Combobox(frame_arbol,font=('Arial',10),state="readonly",values=nombres_gramaticas)
    combo_gramaticas_arbol.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_arbol.grid(row=3, column=1, padx=10, pady=10)
    boton_mostrar = Button(frame_arbol,text='Mostrar Árbol',width=15,height=3,command=funcion_mostrar_arbol,bd="4")
    boton_mostrar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

def generar_arbol_derivacion_consola(gramatica):
    no_terminal_inicial = gramatica['no terminal inicial']
    producciones = gramatica['producciones']

    def construir_arbol(no_terminal, nivel=0):
        for produccion in producciones:
            if produccion[0] == no_terminal:
                expresion = produccion[1:]
                print('  ' * nivel + no_terminal + ' > ' + ' '.join(expresion))
                for simbolo in expresion:
                    if simbolo in gramatica['no terminales']:
                        construir_arbol(simbolo, nivel + 1)

    print('Árbol de Derivación:')
    construir_arbol(no_terminal_inicial)

def funcion_mostrar_arbol():
    # print(funciones.informacion_gramaticas)
    gramatica = funciones.buscar_gramatica_por_nombre(combo_gramaticas_arbol.get())
    generar_arbol_derivacion_consola(gramatica)

def ventana_modulo_automatas_pila(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)
    main_frame = Frame(master)
    # frame centrado
    frame_centrado = Frame(main_frame, height=310, width=450)
    frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_centrado, text="Módulo Automatas de Pila")
    label.grid(row=0, column=0, padx=10, pady=10)
    boton_cargar = Button(frame_centrado,text="Cargar Archivo", command=funciones.cargar_automatas_pila , width=17,height=3)
    boton_cargar.grid(row=1,column=0,padx=10,pady=10)
    boton_info = Button(frame_centrado,text="Información General", command=mostrar_ventana_info_ap , width=17,height=3)
    boton_info.grid(row=2,column=0,padx=10,pady=10)
    boton_validar = Button(frame_centrado,text="Validar Cadena", command=mostrar_ventana_validar_ap, width=17,height=3)
    boton_validar.grid(row=3,column=0,padx=10,pady=10)
    boton_ruta_validar = Button(frame_centrado,text="Ruta de Validación", command=mostrar_ventana_ruta_validacion_ap , width=17,height=3)
    boton_ruta_validar.grid(row=4,column=0,padx=10,pady=10)
    boton_recorrido = Button(frame_centrado,text="Recorrido paso a paso", command=None , width=17,height=3)
    boton_recorrido.grid(row=5,column=0,padx=10,pady=10)
    boton_validar_pasada = Button(frame_centrado,text="Validar de una pasada", command=None , width=17,height=3)
    boton_validar_pasada.grid(row=6,column=0,padx=10,pady=10)
    boton_regresar = Button(frame_centrado, text='Regresar', width=17,height=3, command=callback, bd="4")
    boton_regresar.grid(row=7, column=0, padx=10, pady=10)
    return main_frame

def ventana_informacion_automapasap(master, callback=None, args=(), kwargs={}):
    global frame_informacion_automatasap, boton_regresar_ap
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_informacion_automatasap = Frame(main_frame, height=310, width=450)
    frame_informacion_automatasap.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_informacion_automatasap, text="Modulo información Automatas de Pila")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_informacion_automatasap, text="Elija una Grámatica")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_informacion_automatasap,text='Mostrar Grámaticas',width=15,height=3,command=mostrar_gramaticas_ap,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_ap = Button(frame_informacion_automatasap, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_ap.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def mostrar_gramaticas_ap():
    global combo_automatasap
    nombres_gramaticas = []
    for element in funciones.informacion_ap:
        nombres_gramaticas.append(element['nombre'])
    combo_automatasap = ttk.Combobox(frame_informacion_automatasap,font=('Arial',10),state="readonly",values=nombres_gramaticas)
    combo_automatasap.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_ap.grid(row=3, column=1, padx=10, pady=10)
    boton_mostrar = Button(frame_informacion_automatasap,text='Mostrar Información',width=15,height=3,command=generar_informacion_automataap,bd="4")
    boton_mostrar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

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
    nombre_archivo = f"{nombre}.pdf"
    grafo.format = 'pdf'
    grafo.render(filename=nombre_archivo, cleanup=True)
    imprimir = '*********************************************'
    imprimir1 = f"Grafo del autómata de pila '{nombre}' generado exitosamente. Se ha guardado como '{nombre_archivo}'."
    mensaje = imprimir.center(75, ' ') + '\n' + imprimir1.center(75, ' ') + '\n' + imprimir.center(75, ' ')
    messagebox.showinfo(message=mensaje, title="Mensaje")
    webbrowser.open_new_tab(f'{nombre_archivo}.pdf')
#
def generar_informacion_automataap():
    automata = funciones.buscar_automata_por_nombre(combo_automatasap.get())
    generar_grafo_automata_pila(automata)

def ventana_validar_automapasap(master, callback=None, args=(), kwargs={}):
    global frame_validar_automatasap, boton_regresar_validar_ap
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_validar_automatasap = Frame(main_frame, height=310, width=450)
    frame_validar_automatasap.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_validar_automatasap, text="Modulo Validar Automatas de Pila")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_validar_automatasap, text="Elija una Grámatica")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_validar_automatasap,text='Mostrar Grámaticas',width=15,height=3,command=mostrar_gramaticas_ap_validar,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_validar_ap = Button(frame_validar_automatasap, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_validar_ap.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def mostrar_gramaticas_ap_validar():
    global combo_automatasap_validar,cadena
    nombres_gramaticas = []
    for element in funciones.informacion_ap:
        nombres_gramaticas.append(element['nombre'])
    combo_automatasap_validar = ttk.Combobox(frame_validar_automatasap,font=('Arial',10),state="readonly",values=nombres_gramaticas)
    combo_automatasap_validar.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_validar_ap.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_validar_automatasap, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='e')
    cadena = StringVar()
    entry_cadena = Entry(frame_validar_automatasap,font=('Arial',12),justify="center",textvariable=cadena)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_mostrar = Button(frame_validar_automatasap,text='Validar Cadena',width=15,height=3,command=validar_cadenas_automataap,bd="4")
    boton_mostrar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

def validar_cadenas_automataap():
    imprimir = '*********************************************'
    autoamata = funciones.buscar_automata_por_nombre(combo_automatasap_validar.get())
    if funciones.validar_cadena(autoamata, cadena.get()):
        imprimir1 = f'La cadena es válida para el autómata {autoamata["nombre"]}'
        mensaje =imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ')
        messagebox.showinfo(message=mensaje, title="Mensaje")
    else:
        imprimir1 = f'La cadena no es válida para el autómata {autoamata["nombre"]}'
        mensaje =imprimir.center(75, ' ') + imprimir1.center(75, ' ') + imprimir.center(75, ' ')
        messagebox.showerror(message=mensaje, title="Mensaje")

def ventana_ruta_validacion_automapasap(master, callback=None, args=(), kwargs={}):
    global frame_ruta_validacion_automatasap, boton_regresar_ruta_validacion_ap
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = Frame(master)
    # frame centrado
    frame_ruta_validacion_automatasap = Frame(main_frame, height=310, width=450)
    frame_ruta_validacion_automatasap.place(relx=0.5, rely=0.5, anchor="center")
    # agregando botones
    label = Label(frame_ruta_validacion_automatasap, text="Modulo Ruta Validacion Automatas de Pila")
    label.grid(row=0, column=0, padx=10, pady=10)
    label1 = Label(frame_ruta_validacion_automatasap, text="Elija una Grámatica")
    label1.grid(row=1, column=0, padx=10, pady=10,sticky='e')
    boton_mostrar = Button(frame_ruta_validacion_automatasap,text='Mostrar Grámaticas',width=15,height=3,command=mostrar_gramaticas_ap_validar_ruta,bd="4")
    boton_mostrar.grid(row=1,column=2,padx=10,pady=10,sticky='w')
    boton_regresar_ruta_validacion_ap = Button(frame_ruta_validacion_automatasap, text='Regresar', width=15,
                            height=3, command=callback, bd="4")
    boton_regresar_ruta_validacion_ap.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

def mostrar_gramaticas_ap_validar_ruta():
    global combo_automatasap_validar_ruta,cadena_ruta
    nombres_gramaticas = []
    for element in funciones.informacion_ap:
        nombres_gramaticas.append(element['nombre'])
    combo_automatasap_validar_ruta = ttk.Combobox(frame_ruta_validacion_automatasap,font=('Arial',10),state="readonly",values=nombres_gramaticas)
    combo_automatasap_validar_ruta.grid(row=1,column=1,padx=10,pady=10)
    boton_regresar_validar_ap.grid(row=3, column=1, padx=10, pady=10)
    label2 = Label(frame_ruta_validacion_automatasap, text="Ingrese una cadena")
    label2.grid(row=2, column=0, padx=10, pady=10,sticky='e')
    cadena_ruta = StringVar()
    entry_cadena = Entry(frame_ruta_validacion_automatasap,font=('Arial',12),justify="center",textvariable=cadena_ruta)
    entry_cadena.grid(row=2, column=1, padx=10, pady=10)
    boton_mostrar = Button(frame_ruta_validacion_automatasap,text='Validar Cadena',width=15,height=3,command=ruta_validacion_automatasap,bd="4")
    boton_mostrar.grid(row=2,column=2,padx=10,pady=10,sticky='w')

def ruta_validacion_automatasap():
    automata = funciones.buscar_automata_por_nombre(combo_automatasap_validar_ruta.get())
    bandera = funciones.ruta_validacion(automata,cadena_ruta.get())
    if bandera != False:
        print('Ruta:')
        for transicion in bandera:
            print(f'{transicion[0]} , {transicion[1]} , {transicion[2]} ; {transicion[4]} , {transicion[3]}')

# Abro venta
ventana = ThemedTk(theme="ubuntu")
ancho_ventana = 1280
alto_ventana = 720
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title('Proyecto 2')
# Frame con nombre proyecto
miFrame = Frame()
miFrame.pack(side="top", fill="x")
miFrame.config(width="500", height="50", relief="solid", bd="3")
label = Label(miFrame, text='Proyecto 2')
label.pack(side="top")
# frame Variable
miFrameV = Frame()
miFrameV.pack(fill="x")
miFrameV.place(x=0, y=25)

miFrameV.config(width=ancho_ventana, height=alto_ventana,relief="solid", bd="3")
# Funciones para ventanas en botones
var_ventana_principal = ventana_principal(ventana, funciones.salir)
var_ventana_gramaticas = ventana_modulo_gramaticas(ventana,mostrar_principal)
var_ventana_info_gramaticas = ventana_informacion_gramaticas(ventana,mostrar_modulo_gramaticas)
var_ventana_arbol = ventana_arbol_gramaticas(ventana,mostrar_modulo_gramaticas)
var_ventana_automata_pila = ventana_modulo_automatas_pila(ventana,mostrar_principal)
var_ventana_info_automatasap = ventana_informacion_automapasap(ventana,mostrar_ventana_automata_pila)
var_ventana_validar_automatasap = ventana_validar_automapasap(ventana,mostrar_ventana_automata_pila)
var_ventana_ruta_validacion_automatasap = ventana_ruta_validacion_automapasap(ventana,mostrar_ventana_automata_pila)

# agregando Items a frame Variable
frame_centrado = Frame(miFrameV, height=310, width=450)
frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
label_nombre_curso = Label(frame_centrado, text="Nombre del Curso: Lab. Lenguajes Formales y de Programación P")
label_nombre_curso.grid(row=0, column=0, padx=10, pady=10)
label_nombre_estudiante = Label(frame_centrado, text='Nombre del Estudiante: Nery José Barrientos Posadas')
label_nombre_estudiante.grid(row=1,column=0,padx=10,pady=10)
label_carne = Label(frame_centrado, text='Carnet del Estudiante: 201807086')
label_carne.grid(row=2,column=0,padx=10,pady=10)
label_contador = Label(frame_centrado, text='Esta Pantalla Desaparecerá en 5 Segundos',relief="raised", bd="3")
label_contador.grid(row=3,column=0,padx=10,pady=10)
# frame Inferior
miFrame1 = Frame()
miFrame1.pack(side="bottom", fill="x")
miFrame1.config(width="500", height="30", relief="solid", bd="3")

ventana.after(0, cerrar_ventana, 5)
ventana.mainloop()
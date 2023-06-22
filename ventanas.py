import functools
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
    miFrameV.pack(side="top", fill="both", expand=True)

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
    boton_modulo_gramaticas = Button(frame_centrado, text='Módulo Grámaticas',width=15, height=3, bd="4", command=None)
    boton_modulo_gramaticas.grid(row=1, column=0, padx=10, pady=10)
    boton_modulo_ap = Button(frame_centrado, text='Módulo AP',width=15, height=3, bd="4", command=None)
    boton_modulo_ap.grid(row=2, column=0, padx=10, pady=10)
    boton_salir = Button(frame_centrado, text='Salir', width=15,height=3, command=callback, bd="4")
    boton_salir.grid(row=3, column=0, padx=10, pady=10)
    return main_frame

# Abro venta
ventana = ThemedTk(theme="ubuntu")
ancho_ventana = 1280
alto_ventana = 720
x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
    "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title('Proyecto 1')
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
# var_ventana_evaluar_afn = ventana_evaluar_afn(ventana,mostrar_ventana_afn)
# var_ventana_validar_afn = ventana_validar_afn(ventana,mostrar_ventana_evaluar_afn)
# var_ventana_ruta_afn = ventana_ruta_afn(ventana,mostrar_ventana_evaluar_afn)
# var_ventana_ruta_afd = ventana_ruta_afd(ventana,mostrar_ventana_evaluar_afd)
# var_ventana_afn_crear = ventana_afn_crear(ventana, mostrar_ventana_afn)
# var_ventana_ayuda_afn = ventana_afn_ayuda(ventana,mostrar_ventana_afn)
# var_ventana_afd = ventana_afd(ventana, mostrar_principal)
# var_ventana_evaluar_afd = ventana_evaluar_afd(ventana,mostrar_ventana_afd)
# var_ventana_validar_afd = ventana_validar_afd(ventana,mostrar_ventana_evaluar_afd)
# var_ventana_afd_crear = ventana_afd_crear(ventana, mostrar_ventana_afd)
# var_ventana_ayuda_afd = ventana_afd_ayuda(ventana,mostrar_ventana_afd)
# var_ventana_oe = ventana_oe(ventana, mostrar_principal)
# var_ventana_cargar_archivos = ventana_cargar(ventana, mostrar_principal)
# agregando Items a frame Variable
frame_centrado = Frame(miFrameV, height=310, width=450)
frame_centrado.place(relx=0.5, rely=0.5, anchor="center")
label_nombre_curso = Label(frame_centrado, text="Nombre del Curso: Lav, Lenguajes Formales y de Programación P")
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
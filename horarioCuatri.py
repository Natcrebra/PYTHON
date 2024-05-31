#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:51:17 2023

@author: nat
"""

# Crear un diccionario que represente un horario semanal
"""horario_semanal = {
    "Lunes": {
        "08:00 AM - 10:00 AM": "Asignatura 1",
        "10:30 AM - 12:30 PM": "Asignatura 2",
        # Agrega más intervalos y asignaturas según tu horario
    },
    "Martes": {
        "08:00 AM - 10:00 AM": "Asignatura 3",
        "10:30 AM - 12:30 PM": "Asignatura 4",
        # Agrega más intervalos y asignaturas según tu horario
    },
    "Miércoles": {
        # Horario del miércoles
    },
    "Jueves": {
        # Horario del jueves
    },
    "Viernes": {
        # Horario del viernes
    },
    "Sábado": {
        # Horario del sábado
    },
    "Domingo": {
        # Horario del domingo
    }
}

# Mostrar el horario semanal
for dia, horario in horario_semanal.items():
    print(f"Día: {dia}")
    for intervalo, asignatura in horario.items():
        print(f"{intervalo}: {asignatura}")
    print()"""
    
import tkinter as tk

# Crear una ventana de tkinter
root = tk.Tk()
root.title("Horario Semanal")

# Definir un horario semanal con colores
horario_semanal = {
    "Lunes": {
        "09:00 AM - 10:00 AM": "Física Xeral I",
        "10:00 AM - 11:00 PM": "Libre",
        "11:00 PM - 12:00 PM": "Métodos Matemáticos I",
        "12:00 PM - 13:00 PM": "Libre",
        "13:00 PM - 14:00 PM": "Informática Teoría",
    },
    "Martes": {
        "10:00 AM - 11:00 PM": "Física Xeral I",
        "11:00 AM - 12:00 PM": "Libre",
        "12:00 PM - 13:00 PM": "Métodos Matemáticos I",
        "16:00 PM - 18:30 PM": "Informática - LAB",
    },
    "Miércoles": {
        "09:00 AM - 10:00 AM": "Física Xeral I",
        "10:00 AM - 11:00 PM": "Libre",
        "11:00 PM - 12:00 PM": "Métodos Matemáticos I",
        "12:00 PM - 13:00 PM": "Libre",
        "13:00 PM - 14:00 PM": "Informática Teoría",
        },
    "Jueves": {
        "10:00 AM - 11:00 PM": "Física Xeral I",
        "11:00 AM - 12:00 PM": "Libre",
        "12:00 PM - 13:00 PM": "Métodos Matemáticos I",
        },
    "Viernes": {
        "9:00 AM - 14:00 PM": "Libre",
        },
    "Sábado": {
        "9:00 AM - 14:00 PM": "Libre",
        },
    "Domingo": {
        "9:00 AM - 14:00 PM": "Libre",
        },
}

# Colores para las asignaturas
colores = {
    "Física Xeral I": "lightblue",
    "Libre": "lightyellow",
    "Métodos Matemáticos I": "lightgreen",
    "Informática Teoría": "lightcoral",
    "Informática - LAB": "lightpink",
}

# Frame para mostrar el horario
frame = tk.Frame(root)
frame.pack()

#Crear una cuadrícula para el horario
for dia, horario in horario_semanal.items():
    dia_frame = tk.Frame(frame)
    dia_frame.pack(side=tk.LEFT)

    tk.Label(dia_frame, text=dia, padx=10).pack()

    for intervalo, asignatura in horario.items():
        color = colores.get(asignatura, "white")
        tk.Label(dia_frame, text=intervalo, bg=color, padx=10).pack()
        tk.Label(dia_frame, text=asignatura, bg=color, padx=10).pack()

# Ejecutar la aplicación tkinter
root.mainloop()
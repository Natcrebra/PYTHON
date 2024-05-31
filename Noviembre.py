#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 09:46:06 2023

@author: nat
"""
import calendar 
# Definir el año y el mes para el calendario personalizado
year = 2023
month = 11

# Crear una instancia de la clase TextCalendar
cal = calendar.TextCalendar(calendar.MONDAY)  # Puedes especificar el primer día de la semana

# Generar y mostrar el calendario personalizado
print(cal.formatmonth(year, month))



# Crear una instancia de la clase TextCalendar
cal2 = calendar.TextCalendar(calendar.SUNDAY)

# Definir el año y el mes
year = 2023
month = 11  # Noviembre

# Definir tus horarios de estudio y asignar materias o temas
horario_de_estudio = {
    "Lunes": {
        "08:00 AM - 10:00 AM": "Matemáticas",
        "10:30 AM - 12:30 PM": "Ciencias",
        "02:00 PM - 04:00 PM": "Historia"
    },
    "Martes": {
        "09:00 AM - 11:00 AM": "Inglés",
        "02:30 PM - 04:30 PM": "Física"
    },
    "Miércoles": {
        "10:00 AM - 12:00 PM": "Literatura",
        "02:00 PM - 04:00 PM": "Química"
    },
    "Jueves": {
        "08:30 AM - 10:30 AM": "Matemáticas",
        "11:00 AM - 01:00 PM": "Biología"
    },
    "Viernes": {
        "09:00 AM - 11:00 AM": "Inglés",
        "02:30 PM - 04:30 PM": "Física"
    },
    "Sábado": {
        "Repaso General"
    },
    "Domingo": {
        "Día Libre"
    }
}

# Mostrar el calendario de estudios
for day, schedule in horario_de_estudio.items():
    print(cal2.formatmonth(year, month))  # Muestra el mes
    print(f"Día de la semana: {day}\n")

    if isinstance(schedule, dict):
        for time, subject in schedule.items():
            print(f"{time}: {subject}")
    else:
        print(schedule)

    print()

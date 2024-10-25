import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox, Toplevel, Label, Text, Scrollbar
from sympy import symbols, integrate, sympify, pretty, lambdify
import matplotlib.pyplot as plt
import numpy as np

# Definir la variable simbólica
x = symbols('x')

# Función para calcular la integral indefinida
def calcular_indefinida():
    try:
        funcion = sympify(entry.get())  # Convertir la entrada en una función de sympy
        integral_indefinida = integrate(funcion, x)  # Calcular la integral indefinida
        
        # Procedimiento detallado
        procedimiento = "Cálculo de la Integral Indefinida Paso a Paso:\n"
        procedimiento += f"1. Identificamos la función a integrar: f(x) = {pretty(funcion)}\n"
        procedimiento += "2. Aplicamos las reglas de integración adecuadas:\n"
        procedimiento += f"   ∫ {pretty(funcion)} dx\n"
        resultado = pretty(integral_indefinida)
        procedimiento += f"3. El resultado de la integral indefinida es:\n   ∫ {pretty(funcion)} dx = {resultado} + C"
        
        # Mostrar resultado en cuadro de texto
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n\nResultado:\n{pretty(integral_indefinida)} + C")
        text_resultado.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

# Función para calcular la integral definida
def calcular_definida():
    try:
        funcion = sympify(entry.get())  # Convertir la entrada en una función de sympy
        limite_inferior = float(entry_limite_inferior.get())  # Obtener límite inferior
        limite_superior = float(entry_limite_superior.get())  # Obtener límite superior
        
        # Calcular la integral definida
        integral_definida = integrate(funcion, (x, limite_inferior, limite_superior))
        
        # Procedimiento detallado
        procedimiento = "Cálculo de la Integral Definida Paso a Paso:\n"
        procedimiento += f"1. Identificamos la función a integrar: f(x) = {pretty(funcion)}\n"
        procedimiento += f"2. Evaluamos la integral definida entre los límites {limite_inferior} y {limite_superior}:\n"
        procedimiento += f"   ∫ {pretty(funcion)} dx de {limite_inferior} a {limite_superior}\n"
        procedimiento += "3. Calculamos la integral indefinida y luego evaluamos los límites:\n"
        resultado = pretty(integral_definida)
        procedimiento += f"4. El resultado de la integral definida es:\n   {resultado}"
        
        # Mostrar resultado en cuadro de texto
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n\nResultado:\n{pretty(integral_definida)}")
        text_resultado.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

# Función para graficar la función
def graficar():
    try:
        funcion = sympify(entry.get())  
        f_lambda = lambdify(x, funcion, "numpy") 
        
        x_vals = np.linspace(0, 10, 400)
        y_vals = f_lambda(x_vals)
        
        plt.plot(x_vals, y_vals, label=f"f(x) = {entry.get()}")
        plt.title("Gráfica de la función")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo graficar: {str(e)}")

# Función para mostrar el procedimiento
def mostrar_procedimiento():
    nueva_ventana = Toplevel(root)
    nueva_ventana.title("Procedimiento de integración")
    
    label = Label(nueva_ventana, text="Procedimiento paso a paso")
    label.pack(pady=10)
    
    # Caja de texto para mostrar el procedimiento
    text_procedimiento = Text(nueva_ventana, height=10, width=50)
    text_procedimiento.pack(padx=10, pady=10)
    
    scrollbar = Scrollbar(nueva_ventana)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_procedimiento.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_procedimiento.yview)
    
    # Mostrar procedimiento desde el campo de texto principal
    procedimiento_texto = text_resultado.get(1.0, tk.END)
    text_procedimiento.insert(tk.END, procedimiento_texto)
    

# Función para agregar texto a la entrada
def agregar_a_entrada(valor):
    entrada_actual = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, entrada_actual + str(valor))

# Función para limpiar la entrada
def limpiar_entrada():
    entry.delete(0, tk.END)

# Crea ventana principal
root = tk.Tk()
root.title("Calculadora de Integrales - Creada por Nery's Group")
root.geometry("450x750")

# Carga y redimension de la imagen de fondo
imagen = Image.open("imagenes\calculadora1.png")
imagen = imagen.resize((450, 750))  # Tamaño según la ventana
imagen_fondo = ImageTk.PhotoImage(imagen)

# Crea un Label para la imagen de fondo y colocarlo en la ventana
fondo_label = tk.Label(root, image=imagen_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crea entrada para la función
entry = tk.Entry(root, width=25, borderwidth=8, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Botones 
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('x', 5, 0), ('(', 5, 1), (')', 5, 2), ('exp', 5, 3),
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
    ('Graficar', 8, 0), ('Mostrar procedimiento', 8, 2)
]

# Añade los botones a la ventana
for (texto, fila, columna) in botones:
    if texto == 'Graficar':
        tk.Button(root, text=texto, padx=10, pady=10, command=graficar).grid(row=fila, column=columna, columnspan=2, sticky="nsew")
    elif texto == 'Mostrar procedimiento':
        tk.Button(root, text=texto, padx=10, pady=10, command=mostrar_procedimiento).grid(row=fila, column=columna, columnspan=2, sticky="nsew")
    else:
        tk.Button(root, text=texto, padx=10, pady=10, command=lambda t=texto: agregar_a_entrada(t)).grid(row=fila, column=columna, sticky="nsew")

# Crea botones para integrales definidas e indefinidas 
tk.Button(root, text="∫ Definida", padx=10, pady=10, command=calcular_definida).grid(row=7, column=0, columnspan=2, sticky="nsew")
tk.Button(root, text="∫ Indefinida", padx=10, pady=10, command=calcular_indefinida).grid(row=7, column=2, columnspan=2, sticky="nsew")

# Ajusta columnas y filas
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for j in range(5):
    root.grid_columnconfigure(j, weight=1)

# Campos para la integral definida 
tk.Label(root, text="Límite inferior").grid(row=9, column=0, columnspan=2, pady=5, sticky="e")
entry_limite_inferior = tk.Entry(root, width=5)
entry_limite_inferior.grid(row=9, column=2, columnspan=2, pady=5)
entry_limite_inferior.config(justify="center")

tk.Label(root, text="Límite superior").grid(row=10, column=0, columnspan=2, pady=5, sticky="e")
entry_limite_superior = tk.Entry(root, width=5)
entry_limite_superior.grid(row=10, column=2, columnspan=2, pady=5)
entry_limite_superior.config(justify="center")

# creditos
creditos = tk.Label(root, text="Creadores: Nery Osorio, Francisco Estrada, Pablo Montiel, Melvin Ramos")
creditos.grid(row=12, column=0, columnspan=5, pady=10, sticky="ew")  
creditos.config(justify="center")  


# Resultado del cálculo
text_resultado = Text(root, height=8, width=40)
text_resultado.grid(row=11, column=0, columnspan=5, padx=10, pady=10)
text_resultado.config(state=tk.DISABLED)


# Ajusta tamaño de los botones
for widget in root.winfo_children():
    if isinstance(widget, tk.Button):
        widget.config(height=2, width=12)

# Ejecuta el loop principal
root.mainloop()


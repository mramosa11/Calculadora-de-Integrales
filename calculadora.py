import tkinter as tk
from tkinter import messagebox
from sympy import symbols, integrate, sympify, pretty, lambdify
import matplotlib.pyplot as plt
import numpy as np

# Definir la variable simbólica
x = symbols('x')

# Función para calcular la integral indefinida
def calcular_indefinida():
    try:
        funcion = sympify(entry_funcion.get())  # Convertir la entrada en una función de sympy
        integral_indefinida = integrate(funcion, x)  # Calcular la integral indefinida
        
        # Mostrar procedimiento
        procedimiento = f"∫ {pretty(funcion)} dx"
        resultado = pretty(integral_indefinida)
        
        # Mostrar en la interfaz
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n\nResultado:\n∫ {pretty(funcion)} dx = {resultado} + C")
        text_resultado.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

# Función para calcular la integral definida
def calcular_definida():
    try:
        funcion = sympify(entry_funcion.get())  # Convertir la entrada en una función de sympy
        limite_inferior = float(entry_limite_inferior.get())  # Obtener límite inferior
        limite_superior = float(entry_limite_superior.get())  # Obtener límite superior
        
        # Calcular la integral definida
        integral_definida = integrate(funcion, (x, limite_inferior, limite_superior))
        
        # Mostrar procedimiento y resultado
        procedimiento = f"∫ {pretty(funcion)} dx de {limite_inferior} a {limite_superior}"
        resultado = pretty(integral_definida)
        
        # Mostrar en la interfaz
        text_resultado.config(state=tk.NORMAL)
        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, f"Procedimiento:\n{procedimiento}\n\nResultado:\n{resultado}")
        text_resultado.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Error en el cálculo: {str(e)}")

# Función para graficar la función
def graficar():
    try:
        funcion = sympify(entry_funcion.get())  # Convertir la entrada en una función de sympy
        f_lambda = lambdify(x, funcion, "numpy")  # Convertir a una función evaluable
        
        # Crear valores de x e y para graficar
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambda(x_vals)
        
        # Graficar la función
        plt.plot(x_vals, y_vals, label=f"f(x) = {entry_funcion.get()}")
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

# Configurar la ventana principal
root = tk.Tk()
root.title("Calculadora de Integrales")
root.geometry("500x600")

# Etiqueta y entrada para la función
label_funcion = tk.Label(root, text="Función a integrar:")
label_funcion.pack(pady=5)
entry_funcion = tk.Entry(root, width=40)
entry_funcion.pack(pady=5)

# Para integral definida
label_limite_inferior = tk.Label(root, text="Límite inferior (solo para definida):")
label_limite_inferior.pack(pady=5)
entry_limite_inferior = tk.Entry(root, width=20)
entry_limite_inferior.pack(pady=5)

label_limite_superior = tk.Label(root, text="Límite superior (solo para definida):")
label_limite_superior.pack(pady=5)
entry_limite_superior = tk.Entry(root, width=20)
entry_limite_superior.pack(pady=5)

# Botones para calcular y graficar
button_indefinida = tk.Button(root, text="Calcular Indefinida", command=calcular_indefinida)
button_indefinida.pack(pady=5)

button_definida = tk.Button(root, text="Calcular Definida", command=calcular_definida)
button_definida.pack(pady=5)

button_graficar = tk.Button(root, text="Graficar", command=graficar)
button_graficar.pack(pady=5)

# Caja de texto para mostrar los resultados
text_resultado = tk.Text(root, height=10, width=60, state=tk.DISABLED)
text_resultado.pack(pady=10)

# Ejecutar el loop de la interfaz
root.mainloop()

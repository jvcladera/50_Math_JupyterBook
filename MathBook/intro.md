# Introducción a 50 Ideas Matemáticas

Bienvenido a la versión interactiva de "50 Ideas Matemáticas que Realmente Necesitas Conocer".

Este libro explora conceptos fundamentales de las matemáticas, desde los números hasta la teoría de juegos, con ejemplos interactivos en Python para una mejor comprensión.

¡Esperamos que disfrutes tu viaje a través del fascinante mundo de las matemáticas!

## Ejemplo Interactivo

A continuación, se muestra un ejemplo de un widget interactivo. Puedes mover el deslizador para cambiar la frecuencia de la onda sinusoidal en el gráfico.

```python
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

def plot_sine_wave(frequency=1.0):
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(frequency * x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y)
    plt.title(f"Onda Sinusoidal con Frecuencia = {frequency:.2f} Hz")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.show()

interactive_plot = interactive(plot_sine_wave, frequency=(1.0, 10.0, 0.1))
display(interactive_plot)
```

import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk  # Asegúrate de importar mplcyberpunk

# Aplica el estilo 'cyberpunk' a Matplotlib
plt.style.use('cyberpunk')

# Datos de ejemplo
x = np.linspace(0, 1, 35)
y = np.cos(2 * np.pi * x)

# Gráfico con estilo 'cyberpunk'
fig, ax = plt.subplots()
ax.plot(x, y, 'aqua', marker='o', linewidth=2)

# Agrega efectos adicionales de mplcyberpunk
mplcyberpunk.make_lines_glow(ax)
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.6)

plt.show()

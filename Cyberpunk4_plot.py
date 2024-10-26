import matplotlib.pyplot as plt
import numpy as np
import mplcyberpunk

plt.style.use('cyberpunk')
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + 1
y2 = np.sin(x + 1) + 1
y3 = np.sin(x + 2) + 1

fig, ax = plt.subplots(figsize=(10, 6))
ax.fill_between(x, y1, color='cyan', alpha=0.6)
ax.fill_between(x, y2, color='magenta', alpha=0.6)
ax.fill_between(x, y3, color='yellow', alpha=0.6)

mplcyberpunk.make_lines_glow(ax)
plt.show()

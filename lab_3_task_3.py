import numpy as np
import lab_3_task_1 as t1

g = t1.g
x0 = 0
y0 = 0
v0 = 30
alpha = 40

v0x = v0 * np.cos(np.radians(alpha))
v0y = v0 * np.sin(np.radians(alpha))

N = 10
data = np.zeros((N, 3))

t = np.round(np.linspace(0, 5, N), 3)
x = np.round(x0 + v0x * t, 3)
y = np.round(y0 + v0y * t - g * t**2, 3)

for i in range(len(t)):
  data[i, 0] = t[i]
  if y[i] < 0:
    y[i] = 0 
    x[i] = x[i-1]
  data[i, 1] = x[i]
  data[i, 2] = y[i]

print(data)
import numpy as np
import lab_3_task_1 as t1

h = 100
α = np.pi / 3
β = 30
g = t1.g
T = 200
ε = 300
k = t1.boltzmann_constant
ℏ = t1.ℏ
e = t1.e

u = ((g * h * np.tan(β)**2)/(2 * np.cos(α)**2 * (1 - np.tan(β) * np.tan(α)))) ** 0.5
print(u)

N = (2 / (np.pi ** 0.5)) * (ℏ / (k * T) ** (3 / 2)) * (e ** (-ε / k * T)) * (ε ** (T / 2))
print(N)
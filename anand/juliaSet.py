import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

def julia(zmin, zmax, hpx, niter, c):
    vpx = round(hpx * abs(np.imag(zmax - zmin) / np.real(zmax - zmin)))
    zRe, zIm = np.meshgrid(np.linspace(zmin.real, zmax.real, hpx),
                           np.linspace(zmin.imag, zmax.imag, vpx))
    z = zRe + 1j * zIm

    M = np.zeros_like(z, dtype=int)

    for s in range(niter):
        mask = np.abs(z) < 2
        M[mask] += 1
        z[mask] = z[mask] ** 2 + c

    M[mask] = 0

    return M

# Example usage:
zmin = -2.0 - 1.5j
zmax = 2.0 + 1.5j
hpx = 800
niter = 100
c = -0.7 + 0.27015j
julia_set = julia(zmin, zmax, hpx, niter, c)

plt.figure(figsize=(10, 8))
plt.imshow(julia_set, cmap='viridis', extent=(zmin.real, zmax.real, zmin.imag, zmax.imag), norm=PowerNorm(0.3))
plt.colorbar(label='Iterations')
plt.title('Julia Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
# plt.grid(True, linestyle='dashed', alpha=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

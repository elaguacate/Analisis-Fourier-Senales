# ============================================
# ANALISIS DE SEÑALES EN DOMINIO DEL TIEMPO
# Y DOMINIO DE LA FRECUENCIA
# Autor: Sergio
# ============================================

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------
# 1. DEFINICIÓN DE PARÁMETROS
# --------------------------------------------

fs = 1000  # Frecuencia de muestreo (Hz)
t = np.arange(0, 1, 1/fs)  # Vector de tiempo

# --------------------------------------------
# 2. DEFINICIÓN DE SEÑALES EN EL TIEMPO
# --------------------------------------------

# Señal senoidal
f1 = 5  # Frecuencia 5 Hz
senal_seno = np.sin(2 * np.pi * f1 * t)

# Pulso rectangular
pulso = np.where((t > 0.4) & (t < 0.6), 1, 0)

# Función escalón
escalon = np.where(t >= 0.5, 1, 0)

# --------------------------------------------
# 3. FUNCION PARA CALCULAR FFT
# --------------------------------------------

def calcular_fft(senal):
    N = len(senal)
    fft_vals = np.fft.fft(senal)
    fft_freq = np.fft.fftfreq(N, 1/fs)
    
    magnitud = np.abs(fft_vals)
    fase = np.angle(fft_vals)
    
    return fft_freq, magnitud, fase

# --------------------------------------------
# 4. ANALISIS DE LA SEÑAL SENOIDAL
# --------------------------------------------

freq, mag, fase = calcular_fft(senal_seno)

# --------------------------------------------
# 5. GRAFICAS
# --------------------------------------------

plt.figure(figsize=(12,8))

# Dominio del tiempo
plt.subplot(3,1,1)
plt.plot(t, senal_seno)
plt.title("Señal Senoidal en el Dominio del Tiempo")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")

# Magnitud
plt.subplot(3,1,2)
plt.plot(freq, mag)
plt.title("Magnitud del Espectro")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(-20,20)

# Fase
plt.subplot(3,1,3)
plt.plot(freq, fase)
plt.title("Fase del Espectro")
plt.xlabel("Frecuencia (Hz)")
plt.xlim(-20,20)

plt.tight_layout()
plt.show()

# --------------------------------------------
# 6. VERIFICACION DE PROPIEDADES
# --------------------------------------------

# LINEALIDAD
senal2 = 0.5 * senal_seno
freq2, mag2, _ = calcular_fft(senal2)

# DESPLAZAMIENTO EN EL TIEMPO
desplazada = np.roll(senal_seno, 100)
freq3, mag3, fase3 = calcular_fft(desplazada)

print("Simulación completada correctamente.")

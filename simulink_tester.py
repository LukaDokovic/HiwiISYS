import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Parameter des simulierten Signals
fs = 44000  # Abtastfrequenz in Hz
f = 500  # Frequenz des Sinussignals in Hz
t = np.arange(0, 1, 1/fs)  # Zeitvektor für 1 Sekunde

# Simuliertes Eingangssignal erzeugen
simulated_amplitude = [1, 1.0, 0.7]
simulated_phase = [0, np.pi/2, -0.6]
simulated_signal = sum([amp * np.sin(2 * np.pi * f * t + phase) for amp, phase in zip(simulated_amplitude, simulated_phase)])

# Rauschen hinzufügen
noise = np.random.normal(0, 0.1, t.shape)
simulated_signal_with_noise = simulated_signal + noise

# Lock-In-Detektor implementieren
# Sinus und Kosinus Referenzsignale
sin_ref = np.sin(2 * np.pi * f * t)
cos_ref = np.cos(2 * np.pi * f * t)

# Multiplikation mit Referenzsignalen
in_phase = simulated_signal_with_noise * sin_ref
quadrature = simulated_signal_with_noise * cos_ref

# Tiefpassfilter (Butterworth)
# Filterdesign
b, a = signal.butter(2, f/(fs/2), btype='low')

# Anwenden des Filters
in_phase_filtered = signal.filtfilt(b, a, in_phase)
quadrature_filtered = signal.filtfilt(b, a, quadrature)

# Berechnung der Amplitude und Phase des Signals
amplitude = 2 * np.sqrt(in_phase_filtered**2 + quadrature_filtered**2)
phase = np.arctan2(quadrature_filtered, in_phase_filtered)

# Visualisierung der Resultate
plt.figure(figsize=(15, 5))

# Eingangssignal mit Rauschen
plt.subplot(1, 3, 1)
plt.title("Eingangssignal mit Rauschen")
plt.plot(t, simulated_signal_with_noise)
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude")

# Gefilterte Komponenten
plt.subplot(1, 3, 2)
plt.title("In-Phase und Quadrature Komponenten (gefiltert)")
plt.plot(t, in_phase_filtered, label='In-Phase')
plt.plot(t, quadrature_filtered, label='Quadrature')
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude")
plt.legend()

# Berechnete Amplitude und Phase
plt.subplot(1, 3, 3)
plt.title("Amplitude und Phase des Signals")
plt.plot(t, amplitude, label='Amplitude')
plt.plot(t, phase, label='Phase')
plt.xlabel("Zeit [s]")
plt.ylabel("Amplitude / Phase")
plt.legend()

plt.tight_layout()
plt.show()
plt.savefig('simulink_result.png')

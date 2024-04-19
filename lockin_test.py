import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Zeitachse definieren
t = np.linspace(0, 1, 1000, False)

# Reines Signal erzeugen
pure_signal = np.sin(2 * np.pi * 50 * t)

# Rauschen hinzufügen
noise = np.random.normal(0, 0.5, pure_signal.shape)
noisy_signal = pure_signal + noise

# Referenzsignal
ref_signal = np.sin(2 * np.pi * 50 * t)

# Lock-in Verstärkung durchführen
mixed_signal = noisy_signal * ref_signal * 2
b, a = butter(3, 0.05)
filtered_signal = lfilter(b, a, mixed_signal)

# Plotten
plt.figure(figsize=(12, 8))
plt.subplot(3, 1, 1)
plt.plot(t, pure_signal, label='Reines Signal')
plt.title('Reines Signal')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, label='Rauschbehaftetes Signal')
plt.title('Rauschbehaftetes Signal')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal, label='Gefiltertes Signal')
plt.title('Nach Lock-in-Verstärkung')
plt.legend()

plt.tight_layout()

plt.savefig('lockin_result.png')

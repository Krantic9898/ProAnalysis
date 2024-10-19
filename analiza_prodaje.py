import numpy as np
import matplotlib.pyplot as plt

artikli_niz = np.random.randint(0, 50, size=(4, 6))
spisak_artikala = ["Kamera", "Monitor", "Kuciste", "Tastatura"]
meseci = ['Januar', 'Februar', 'Mart', 'April', 'Maj', 'Jun']

print(artikli_niz)

suma = np.sum(artikli_niz, axis=1)
min_vrednosti = np.min(artikli_niz, axis=1)
max_vrednosti = np.max(artikli_niz, axis=1)
avg = np.mean(artikli_niz, axis=1)

x = np.arange(len(spisak_artikala))

plt.figure(figsize=(12, 8))
plt.title("ProAnalysis")
plt.subplot(2, 2, 1)
plt.bar(x, suma, color='blue', alpha=0.7)
plt.xticks(x, spisak_artikala)
plt.title('Suma Artikala po Kategorijama')
plt.ylabel('Suma')
plt.grid(axis='y')

plt.subplot(2, 2, 2)
plt.bar(x, min_vrednosti, color='green', alpha=0.7)
plt.xticks(x, spisak_artikala)
plt.title('Minimum Artikala po Kategorijama')
plt.ylabel('Minimum')
plt.grid(axis='y')

plt.subplot(2, 2, 3)
plt.bar(x, max_vrednosti, color='red', alpha=0.7)
plt.xticks(x, spisak_artikala)
plt.title('Maksimum Artikala po Kategorijama')
plt.ylabel('Maksimum')
plt.grid(axis='y')

plt.subplot(2, 2, 4)
plt.bar(x, avg, color='purple', alpha=0.7)
plt.xticks(x, spisak_artikala)
plt.title('Prosek Artikala po Kategorijama')
plt.ylabel('Prosek')
plt.grid(axis='y')

plt.tight_layout()
plt.show()

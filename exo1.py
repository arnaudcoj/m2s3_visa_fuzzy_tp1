import matplotlib.pyplot as plt
import numpy as np

def basse(t):
    return np.clip((-t + 20.) * 0.1, 0., 1.)

def moyenne(t):
    return 1. - np.clip(np.sign(t - 20) * (t - 20) * 0.1, 0., 1.)

def elevee(t):
    return np.clip((t - 20.) * 0.1, 0., 1.)

def get_appartenance(t):
    return [basse(t), moyenne(t), elevee(t)]

def plot():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse(t), label="basse")
    plt.plot(t, moyenne(t), label="moyenne")
    plt.plot(t, elevee(t), label="elevee")

    legend = plt.legend(loc='right', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.show()

def print_appartenance(t):
    l = get_appartenance(t)
    print("Basse = ",l[0])
    print("Moyenne = ",l[1])
    print("Élevée = ",l[2])

print_appartenance(16.)
plot()

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

def draw_plot():
    legend = plt.legend(loc='center left', shadow=True)
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.show()


def plot_3():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse(t), label="Basse")
    plt.plot(t, moyenne(t), label="Moyenne")
    plt.plot(t, elevee(t), label="Élevée")

    draw_plot()

def plot_basse_ou_moyenne():
    t = np.arange(0., 45., 5.)

    plt.plot(t, np.logical_or(basse(t), moyenne(t)), label="Basse OU Moyenne")

    draw_plot()

def print_appartenance(t):
    l = get_appartenance(t)
    print("Basse = ",l[0])
    print("Moyenne = ",l[1])
    print("Élevée = ",l[2])

plot_basse_ou_moyenne()

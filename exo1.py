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

def draw_plot(save_file):
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.show()
    plt.savefig(save_file)

def plot_3():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse(t), label="Basse")
    plt.plot(t, moyenne(t), label="Moyenne")
    plt.plot(t, elevee(t), label="Élevée")

    plt.legend(loc='center left', shadow=True)
    draw_plot("plot_3.png")

def plot_basse_ou_moyenne():
    t = np.arange(0., 45., 5.)

    plt.plot(t, np.maximum(basse(t), moyenne(t)), label="Basse OU Moyenne")

    plt.legend(loc='lower left', shadow=True)
    draw_plot("plot_basse_ou_moyenne.png")

def print_appartenance(t):
    l = get_appartenance(t)
    print("Basse = ",l[0])
    print("Moyenne = ",l[1])
    print("Élevée = ",l[2])


#Q1
print("Question 1 : Plot de l'ensemble flou")
plot_3()
#Q2
print("Question 2 : Appartenance de 16°C")
print_appartenance(16.)
#Q3
print('Question 3 : Plot de l\'ensemble flou "Température Basse OU Moyenne"')
plot_basse_ou_moyenne()

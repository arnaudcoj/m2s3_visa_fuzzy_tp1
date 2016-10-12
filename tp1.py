import matplotlib.pyplot as plt
import numpy as np

#==========
#EXERCICE 1
#==========

#Question 1
def basse(t):
    return np.clip((-t + 20.) * 0.1, 0., 1.)

def moyenne(t):
    return 1. - np.clip(np.sign(t - 20) * (t - 20) * 0.1, 0., 1.)

def elevee(t):
    return np.clip((t - 20.) * 0.1, 0., 1.)

def plot_3():
    t = np.arange(0., 45., 5.)

    plt.plot(t, basse(t), label="Basse")
    plt.plot(t, moyenne(t), label="Moyenne")
    plt.plot(t, elevee(t), label="Élevée")

    plt.legend(loc='center left', shadow=True)
    draw_plot("plot_3.png")

#Question 2
def get_appartenance(t):
    return [basse(t), moyenne(t), elevee(t)]

def print_appartenance(t):
    l = get_appartenance(t)
    print("Basse = ",l[0])
    print("Moyenne = ",l[1])
    print("Élevée = ",l[2])

#Question 3
def plot_basse_ou_moyenne():
    t = np.arange(0., 45., 5.)

    plt.plot(t, op_max(basse, moyenne,t), label="Basse OU Moyenne")

    plt.legend(loc='lower left', shadow=True)
    draw_plot("plot_basse_ou_moyenne.png")

#==========
#EXERCICE 2
#==========

#Question 1
def op_min(f1, f2, t):
    return np.minimum(f1(t), f2(t))

def plot_test_min():
    t = np.arange(0., 45., 5.)

    plt.plot(t, op_min(basse, moyenne, t), label="Min(Basse, Moyenne)")

    plt.legend(loc='lower left', shadow=True)
    draw_plot("plot_test_min.png")


#Question 2
def op_max(f1, f2, t):
    return np.maximum(f1(t), f2(t))

def plot_test_max():
    t = np.arange(0., 45., 5.)

    plt.plot(t, op_max(basse, elevee, t), label="Max(Basse, Elevee)")

    plt.legend(loc='lower left', shadow=True)
    draw_plot("plot_test_max.png")

#==========
#UTILS
#==========
def draw_plot(save_file):
    plt.axis([0, 40, -0.1, 1.1])
    plt.xlabel('Température (°C)')
    plt.ylabel('Discours (%)')
    plt.title("Partition floue de l'univers du discours")
    plt.grid(True)
    plt.show()
    plt.savefig(save_file)


#==========
#TRACE
#==========

#EXERCICE 1
print("EXERCICE 1")
#Q1
print("Question 1 : Plot de l'ensemble flou")
plot_3()
#Q2
print("Question 2 : Appartenance de 16°C")
print_appartenance(16.)
#Q3
print('Question 3 : Plot de l\'ensemble flou "Température Basse OU Moyenne"')
plot_basse_ou_moyenne()

#EXERCICE 2
print("EXERCICE 2")
#Q1
print("Question 1 : Combinaison par opérateur min")
plot_test_min()
#Q2
print("Question 2 : Combinaison par opérateur max")
plot_test_max()

#EXERCICE 3
#TODO

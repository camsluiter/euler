import numpy as np
import matplotlib.pyplot as plt

# interest rate

prin=1
t=2
n=20
term = np.zeros(n,dtype=complex)
rate = complex(0,np.pi)

def term_calculator(rate, n):
    for i in range(n):
        if i ==0:
            term[i]=(1+rate/n)
        else:
            term[i]=term[i-1]*(1+rate/n) 
    return term

def plot_terms(prin, total_time, n, rate, plot_type):

    x=[]
    term = term_calculator(rate,n)

    if(plot_type == "triangle"):
    #trying to demonstrate how the successive multiplications create a circle
        colors = plt.cm.get_cmap('hsv', 100)
        for i in range(n):
            if i == 0:
                x.append(plt.Polygon([[0,0],[1,0], [term[0].real,term[0].imag]],color=colors(i)))
            else:
                x.append(plt.Polygon([[0,0],[term[i-1].real,term[i-1].imag], [term[i].real,term[i].imag]], color=colors(i)))
            plt.gca().add_patch(x[i])

        plt.figure(1)
        plt.gca().add_patch(plt.Circle((0,0), radius=1,edgecolor='b', facecolor='none'))
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.show()

    if(plot_type == "arrow"):
        plt.figure(1)
        plt.quiver(term[:-1].real, term[:-1].imag,term[1:].real-term[:-1].real, term[1:].imag-term[:-1].imag,scale=1, scale_units='xy',angles='xy')
        plt.grid()
        plt.show()

    a = prin*(1+rate/n)**(n*t)
    print(term)
    return a

    
plot_terms(prin, t, n,complex(0,np.pi),"arrow")

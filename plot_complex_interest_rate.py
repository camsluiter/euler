import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# interest rate

prin=1
t=np.pi
n=2
term = np.zeros(n,dtype=complex)
rate = complex(0,1)

def term_calculator(rate, n, total_time):
    for i in range(n):
        if i ==0:
            term[i]=(1+(rate*total_time)/n)
        else:
            term[i]=term[i-1]*(1+(rate*total_time)/n) 
    return term

def plot_terms(prin, total_time, n, rate, plot_type):

    x=[]
    term = term_calculator(rate,n, total_time)

    if(plot_type == "triangles"):
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

    if(plot_type == "arrows"):
        plt.figure(1)
        term = np.insert(term,0,complex(1,0))
        plt.quiver(term[:-1].real, term[:-1].imag,term[1:].real-term[:-1].real, term[1:].imag-term[:-1].imag,scale=1, scale_units='xy',angles='xy')
        plt.grid()
        plt.show()

    if(plot_type=="dots"):
        #plt.figure(1)
        sns.scatterplot(x=term[:].real, y=term[:].imag)
        #plt.grid()
        #plt.show()

    print(term)



plot_terms(prin, t, n,rate,"dots")

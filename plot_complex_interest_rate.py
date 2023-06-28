import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# interest rate

prin=1
t=np.pi
n=19
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
        colors = plt.cm.get_cmap('hsv', n)
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
        sns.set_style("darkgrid")
        colors = sns.color_palette("hls", n)
        print(term)
        if(len(term) <20):
            for x,y in zip(term[:].real, term[:].imag):
                plt.text(x+0.02, y, '%.2f + %.2fi' % (float(x), float(y)))
        point_plot=sns.scatterplot(term,x=term.real, y=term.imag, hue=term.real,legend=False)

        point_plot.set(xlabel="Real",ylabel="Imaginary")
        #point_plot.plot([0],[0],'o',ms=300,mec='r',mfc='none')
        
        circle1 = plt.Circle((0, 0), 1.0, color='black', fill=False,linestyle="--",label="Unit Circle")
        
        point_plot.add_patch(circle1)
        point_plot.legend()
        #plt.grid()
        
        plt.show()




plot_terms(prin, t, n,rate,"dots")

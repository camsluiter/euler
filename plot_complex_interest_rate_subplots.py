import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# interest rate

prin=1
t=np.pi
#n=100

rate = complex(0,1)

def term_calculator(prin,rate, n, total_time,cmplx):
    if(cmplx):
        term = np.zeros(n*total_time,dtype=complex)
    else:
        term=np.zeros(n)
    for i in range(n*total_time):
        if i ==0:
            term[i]=prin*(1+(rate)/n)
        else:
            term[i]=term[i-1]*(1+(rate)/n) 
    return term


def plot_terms(prin, total_time, n, rate, plot_type, unit_circ,coor):
    
    x=[]
    term = term_calculator(prin, rate,n, total_time,1)

    if(plot_type == "arrows"):
        
        colors = sns.color_palette("husl", n*total_time)
        colors = sns.color_palette("mako", n*total_time)
        #sns.set_theme()
        sns.set_style("whitegrid")
        #sns.set_style("darkgrid", {"axes.facecolor": ".9"})
        sns.set_context("paper")
        #fig = plt.figure()
        fig, axs= plt.subplots(2,2)
        arrow_headlength=-0.15*n + 5
        term = np.insert(term,0,complex(1,0))
        axs[0][0].quiver(term[:-1].real, term[:-1].imag,term[1:].real-term[:-1].real, term[1:].imag-term[:-1].imag,scale=1, scale_units='xy',angles='xy', color=colors, headlength=arrow_headlength,headaxislength=arrow_headlength, width=0.005)
        if(coor):
            for x,y in zip(term[:].real, term[:].imag):
                plt.text(x+0.02, y, '%.2f + %.2fi' % (float(x), float(y)))
        if(unit_circ):
            unit_circ = plt.Circle((0, 0), 1.0, color='black', fill=False,linestyle="--",label="Unit Circle")
            axs[0][0].add_patch(unit_circ)

        plt.fill(max(term[:].real+1),max(term[:].imag+1))
        #plt.ylim(min(term[:].real)-0.5,max(term[:].real+0.5))
        #ax.set(xlim=(-1, 1), ylim=(-2, 2))
        #sns.despine()
        # ax.spines[["left", "bottom"]].set_position(("data", 0))
        # Hide the top and right spines.
        # ax.spines[["top", "right"]].set_visible(False)
        # plt.xlim(-3, 3)
        # plt.ylim(-3, 3)
        # if n <15:
        #     for i in range(n*total_time):
        #         xr=2
        #         plt.plot([0, term[i].real], [0, term[i].imag],color="black")
        #         plt.gca().add_patch(plt.Rectangle([term[i].real,term[i].imag],-.05,.05,np.degrees(np.angle(term[i])),facecolor='none',alpha=1,edgecolor='black')  )  
        print(len(term))
        
        # make a rectangle
        # the distance from the imaginary axis to the point is imag_value[i]



plot_terms(prin=1,total_time=5,n=5,rate=complex(0,1),plot_type="arrows",unit_circ=1,coor=0)
#real_compound_interest(1,0.50,12,1)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# interest rate

prin=1
t=np.pi
#n=100

rate = complex(0,1)

def term_calculator(prin,rate, n, total_time,complex):
    if(complex):
        term = np.zeros(n,dtype=complex)
    else:
        term=np.zeros(n)
    for i in range(n):
        if i ==0:
            term[i]=prin*(1+(rate*total_time)/n)
        else:
            term[i]=term[i-1]*(1+(rate*total_time)/n) 
    return term


def plot_terms(prin, total_time, n, rate, plot_type, print_unit_circ,print_coor,complex):
    
    x=[]
    if(complex):
        term = term_calculator(prin, rate,n, total_time,1)
    else:
        term = term_calculator(prin, rate,n, total_time,0)
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

    if(plot_type == "arrows"):
        fig = plt.figure()
        #fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(8, 4))
        #ax = fig.add_axes([0.1,0.1,0.1,0.1])
        colors = sns.color_palette("husl", n)
        colors = sns.color_palette("mako", n)
        sns.set_theme()
        sns.set_style("whitegrid")
        sns.set_style("darkgrid", {"axes.facecolor": ".9"})
        sns.set_context("paper")
        #sns.set(rc={'axes.facecolor':'grey', 'figure.facecolor':'cornflowerblue'})
        #sns.despine()
        arrow_headlength=-0.15*n + 5
        term = np.insert(term,0,complex(1,0))
        arrow_plt=plt.quiver(term[:-1].real, term[:-1].imag,term[1:].real-term[:-1].real, term[1:].imag-term[:-1].imag,scale=1, scale_units='xy',angles='xy', color=colors, headlength=arrow_headlength,headaxislength=arrow_headlength, width=0.005)
        if(print_coor):
            for x,y in zip(term[:].real, term[:].imag):
                plt.text(x+0.02, y, '%.2f + %.2fi' % (float(x), float(y)))
        if(print_unit_circ):
            unit_circ = plt.Circle((0, 0), 1.0, color='black', fill=False,linestyle="--",label="Unit Circle")
            plt.gca().add_patch(unit_circ)

        plt.fill(max(term[:].real+1),max(term[:].imag+1))
        #plt.ylim(min(term[:].real)-0.5,max(term[:].real+0.5))
        #ax.set(xlim=(-1, 1), ylim=(-2, 2))
        #sns.despine()
        if n <15:
            for i in range(n):
                plt.plot([0, term[i].real], [0, term[i].imag],color="black")
                plt.gca().add_patch(plt.Rectangle([term[i].real,term[i].imag],-.05,.05,np.degrees(np.angle(term[i])),facecolor='none',alpha=1,edgecolor='black')  )  
        print(len(term))
        
        # make a rectangle
        # the distance from the imaginary axis to the point is imag_value[i]


    if(plot_type=="dots"):
        colors = sns.color_palette("hls", n)
        
        if(not complex):
            fig, ax = plt.subplots()

        if(len(term) <20):
            for x,y in zip(term[:].real, term[:].imag):
                plt.text(x+0.02, y, '%.2f + %.2fi' % (float(x), float(y)))
        if(complex):
            point_plot=sns.scatterplot(term,x=term.real, y=term.imag, hue=term.real,legend=False)
            
        else:
            sns.set(style='ticks')
            #x = [0] * 10
            x_arr =  [0 for i in range(n)]
            #point_plot=sns.scatterplot(x=x_arr,y=term, hue=term.real,legend=False)
            plt.scatter(x_arr, term, c=colors, alpha=0.5)
            #ax.set_aspect('equal')
            
            ax.grid(True, which='both')
            sns.despine(ax=ax, offset=0) # the important part here
        # point_plot.set(xlabel="Real",ylabel="Imaginary")
        #point_plot.plot([0],[0],'o',ms=300,mec='r',mfc='none')
        
        circle1 = plt.Circle((0, 0), 1.0, color='black', fill=False,linestyle="--",label="Unit Circle")
        if(complex):
            plt.gca().add_patch(circle1)
        plt.gca().legend()
        #plt.grid()





#plot_terms(prin, t, 30,rate,"arrows",1,1)
# fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize=(8, 4))
# plot_terms(prin, t, 5,rate,"arrows")
# plot_terms(prin, t, 10,rate,"arrows")
# plot_terms(prin, t, 20,rate,"arrows")
plot_terms(100,1,1,0.03,"dots",0,0,0)
plt.show()

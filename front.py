import os
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from discretization.discretization import Discretize
from Decision_Tree.create_tree import *
from Decision_Tree.decision_tree import *
from GA.genetic_binning import *
from GA.genetic_features import *
from FIS.fis_prediction import*
from FIS.fis_score import*
import csv


root=Tk()
root.title('Main runner')
root.geometry('800x450')
root['background']='#856ff8'

def bin_input():
    global e
    return int(e.get())
    
    
def ewidth():
   
    m=bin_input()
    dobj=Discretize()
    df=dobj.equiwidth_binning(m)
    messagebox.showinfo('output',df.head().to_string())
   
    
def efreq():
    m=bin_input()
    dobj=Discretize()
    df=dobj.equifrequency_binning(m)
    messagebox.showinfo('output',df.head().to_string())    
  
    
def gen_model():
    
    messagebox.showinfo('Model generated & Score',str(tree_score()))   
    

def rules():
    dic={}
    dic_1={}
    dic_2={}
    dobj = DTree()
    rule_set, consequents= dobj.create_rules()
   
    messagebox.showinfo('Rules',(rule_set[0], consequents[0],'\n','\n',rule_set[1], consequents[1],'\n','\n',rule_set[2], consequents[2],'\n','\n',rule_set[3], consequents[3],'\n','\n',rule_set[4], consequents[4]))	
     
def pop_size():
    global f
    return int(f.get())

def min_fit_score():
    global g
    return float(g.get())

def max_gen():
    global h
    return int(h.get())

def ga_bin():
     o=pop_size()
     p=min_fit_score()
     q=max_gen()
     gbin = GeneticBinning()
    
     genome, fitness, generation = gbin.run_evolution(o,p,q)
     result = "genome " + genome + " fitness " + str(fitness) + " gen " + str(generation)
     messagebox.showinfo('Genome,Fitness,Generation',result)
 
def ga_feat():
     o=pop_size()
     p=min_fit_score()
     q=max_gen()
     gobj = GeneticFeatures()
    
     genome, fitness, generation = gobj.run_evolution(o,p,q)
     result = "genome " + genome + " fitness " + str(fitness) + " gen " + str(generation)
     messagebox.showinfo('Genome,Fitness,Generation',result)    
    
def p_btc():
    global i
    return float(i.get())
    
def mean():
    global j
    return float(j.get())
    
def median():
    global k
    return float(k.get())
    
def trend():
    global l
    return int(l.get())   
    
def predict():
    a1=p_btc()
    b1=mean()
    c1=median()
    d1=trend()  
    fpredict = FISPREDICT() 
    a2=(fpredict.predict(b1,c1,d1,a1)) 
    messagebox.showinfo('Predicted BTC',a2)          
    
def graph():
    fpredict = FISPREDICT() 
    for i in fpredict.antecedent_dict:         
        messagebox.showinfo(fpredict.draw_graph(fpredict.antecedent_dict[i]))   
       #messagebox.showinfo(fpredict.draw_graph(fpredict.antecedent_dict['MEAN']))
    
def m_acc():
    b2=1-(fis_score()) 
    messagebox.showinfo('Model Accuracy',b2)  
    
e = Entry(root)
e.pack()
e.focus_set()
e.place(x=130,y=50)

f = Entry(root)
f.pack()
f.focus_set()
f.place(x=580,y=260)

g = Entry(root)
g.pack()
g.focus_set()
g.place(x=580,y=290)

h = Entry(root)
h.pack()
h.focus_set()
h.place(x=580,y=320)

i = Entry(root)
i.pack()
i.focus_set()
i.place(x=580,y=50)

j = Entry(root)
j.pack()
j.focus_set()
j.place(x=580,y=80)

k = Entry(root)
k.pack()
k.focus_set()
k.place(x=580,y=110)

l = Entry(root)
l.pack()
l.focus_set()
l.place(x=580,y=140)

#Discretizatization
Label(root,text='Discretizatization',font="System").place(x=50,y=20)
Button(root,text='Bins',command=bin_input,activebackground="black",activeforeground="white").place(x=50,y=50)
Button(root,text='Equi-Width',command=ewidth,activebackground="black",activeforeground="white").place(x=50,y=80)
Button(root,text='Equi-Frequency',command=efreq,activebackground="black",activeforeground="white").place(x=150,y=80)

#Decision Tree
Label(root,text='Decision Tree',font="System").place(x=50,y=150)
Button(root,text='Generate Model',command=gen_model,activebackground="black",activeforeground="white").place(x=50,y=180)
Button(root,text='Rule Sets',command=rules,activebackground="black",activeforeground="white").place(x=50,y=210)

#GA
Label(root,text='Genetic Algorithm',font="System").place(x=380,y=230)
Button(root,text='Population Size',command=pop_size,activebackground="black",activeforeground="white").place(x=380,y=260)
Button(root,text='Minimum Fitness Score',command=min_fit_score,activebackground="black",activeforeground="white").place(x=380,y=290)
Button(root,text='Maximum Generation',command=max_gen,activebackground="black",activeforeground="white").place(x=380,y=320)
Button(root,text='GA For Binning',command=ga_bin,activebackground="black",activeforeground="white").place(x=380,y=350)
Button(root,text='GA For Features',command=ga_feat,activebackground="black",activeforeground="white").place(x=380,y=380)

#FIS
Label(root,text='Fuzzy Inference System',font="System").place(x=380,y=20)
Button(root,text='Prev BTC',command=p_btc,activebackground="black",activeforeground="white").place(x=380,y=50)
Button(root,text='Mean',command=mean,activebackground="black",activeforeground="white").place(x=380,y=80)
Button(root,text='Median',command=median,activebackground="black",activeforeground="white").place(x=380,y=110)
Button(root,text='Trend',command=trend,activebackground="black",activeforeground="white").place(x=380,y=140)
Button(root,text='Predict',command=predict,activebackground="black",activeforeground="white").place(x=380,y=170)
Button(root,text='See Graphs',command=graph,activebackground="black",activeforeground="white").place(x=470,y=170)
Button(root,text='Model Accuracy',command=m_acc,activebackground="black",activeforeground="white").place(x=570,y=170)
root.mainloop()


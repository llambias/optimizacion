from gurobipy import GRB, Model
from gurobipy import quicksum
from random import randint,random

model = Model()
model.setParam("TimeLimit", 30)

#conjuntos
nodos = range(100)
tipos = range(7)
dias = range(30)
rutas = range(550)
unidades = range(7*10)
#parametros
A = 100
l = {(i,j): randint(0, 7) for i in nodos for j in dias} #capacidad
b = {(i,j): randint(0,1) for i in nodos for j in nodos} #caminos
#print(l)
#Rf
rf = {i:randint(1,100) for i in rutas}
print(rf)
g = {(i,j,k): randint(0,10) for i in nodos for j in dias for k in tipos}
Emax = 0.0045
s = {(i,j,k): random(0,1) for i in dias for j in nodos for k in rutas} 
e = {(i,j): random(0, 1) for i in nodos for j in dias}
#rd
c = {(i,j):randint(1,30) for i in unidades for j in dias}
Ei = {(i): random(0,100) for i in tipos}
V = 50
o = {(i): randint(10,100) for i in tipos}
t = {(i): randint(150,300) for i in tipos}
m = {(i): randint(150,300) for i in tipos}
k = {(i): randint(0,20) for i in tipos}
N = 15
delta = 3
#a{i: randint(10, 100) for i in Localidades}
#variables
x = model.addVar(vtype = GRB.INTEGER, name="x")
y = model.addVar(vtype = GRB.INTEGER, name="y")
z = model.addVar(vtype = GRB.BINARY, name="z")
w = model.addVar(vtype = GRB.BINARY, name="W")
a = model.addVar(vtype = GRB.CONTINUOUS, name="a")
k = model.addVar(vtype = GRB.INTEGER, name="k")
j = model.addVar(vtype = GRB.BINARY, name="j")
RL = model.addVar(vtype = GRB.CONTINUOUS, name="RL")
# constraints
model.addConstrs((w >= d[i,j]*y[i,j] for i in Localidades for j in Sitios), name="R1")


#model.addConstr(, name="R1")
model.update()


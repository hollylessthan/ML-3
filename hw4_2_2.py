import random as rd
import numpy as np

desk ="/Users/lofangyu/Desktop/"
f = open(desk + "hw4_dataset.txt", "r")
list = f.readlines()


new_list=[]
for i in range(len(list)-1):
    m = list[i]
    n = m.replace(","," ")
    new_list.append(n.split())

learn_rate = [0.1, 0.2, 0.3, 0.4, 0.5]
time = 0


def MSE(X, Z):
   return (X - Z) ** 2


initial = []
initial1 = []
initial2 = []

Conver = []
converge = 0
diverge = 1

for i in range (16):
    I = rd.uniform(-0.1, 0.1)
    J = rd.uniform(-0.1, 0.1)
    initial.append(I)
    initial1.append(J)
for i in range(12):
    K = rd.uniform(-0.1, 0.1)
    initial2.append(K)
initial = [initial[l:l+4] for l in range(0, len(initial),4)]
initial1 = [initial1[l:l+4] for l in range(0, len(initial1),4)]
initial2 = [initial2[l:l+3] for l in range(0, len(initial2),3)]


for b in range (len(new_list)):    
    while diverge > 0:
        Y = []
        T = []
        time = time + 1
        for k in range(len(new_list)):
            hid1 = []
            hid2 = []
            y = []
            q1 = []
            q2 = []
            q3 = []
            target = []
            Delta = []
            Delta1 = []


            h0 = eval(new_list[k][0]) * initial[0][0] + eval(new_list[k][1]) * initial[1][0] + eval(new_list[k][2]) * initial[2][0] + eval(new_list[k][3]) * initial[3][0]
            h1 = eval(new_list[k][0]) * initial[0][1] + eval(new_list[k][1]) * initial[1][1] + eval(new_list[k][2]) * initial[2][1] + eval(new_list[k][3]) * initial[3][1]
            h2 = eval(new_list[k][0]) * initial[0][2] + eval(new_list[k][1]) * initial[1][2] + eval(new_list[k][2]) * initial[2][2] + eval(new_list[k][3]) * initial[3][2]
            h3 = eval(new_list[k][0]) * initial[0][3] + eval(new_list[k][1]) * initial[1][3] + eval(new_list[k][2]) * initial[2][3] + eval(new_list[k][3]) * initial[3][3]
            H0 = (1 + np.e** (- h0)) ** (-1)
            H1 = (1 + np.e** (- h1)) ** (-1)
            H2 = (1 + np.e** (- h2)) ** (-1)
            H3 = (1 + np.e** (- h3)) ** (-1)
            hid1.append(H0)
            hid1.append(H1)
            hid1.append(H2)
            hid1.append(H3)

            h0 = hid1[0] * initial1[0][0] + hid1[1] * initial1[1][0] + hid1[2] * initial1[2][0] + hid1[3] * initial1[3][0]
            h1 = hid1[0] * initial1[0][1] + hid1[1] * initial1[1][1] + hid1[2] * initial1[2][1] + hid1[3] * initial1[3][1]
            h2 = hid1[0] * initial1[0][2] + hid1[1] * initial1[1][2] + hid1[2] * initial1[2][2] + hid1[3] * initial1[3][2]
            h3 = hid1[0] * initial1[0][3] + hid1[1] * initial1[1][3] + hid1[2] * initial1[2][3] + hid1[3] * initial1[3][3]
            H0 = (1 + np.e** (- h0)) ** (-1)
            H1 = (1 + np.e** (- h1)) ** (-1)
            H2 = (1 + np.e** (- h2)) ** (-1)
            H3 = (1 + np.e** (- h3)) ** (-1)
            hid2.append(H0)
            hid2.append(H1)
            hid2.append(H2)
            hid2.append(H3)


            h0 = hid2[0] * initial2[0][0] + hid2[1] * initial2[1][0] + hid2[2] * initial2[2][0] + hid2[3] * initial2[3][0]
            h1 = hid2[0] * initial2[0][1] + hid2[1] * initial2[1][1] + hid2[2] * initial2[2][1] + hid2[3] * initial2[3][1]
            h2 = hid2[0] * initial2[0][2] + hid2[1] * initial2[1][2] + hid2[2] * initial2[2][2] + hid2[3] * initial2[3][2]
            H0 = (1 + np.e** (- h0)) ** (-1)
            H1 = (1 + np.e** (- h1)) ** (-1)
            H2 = (1 + np.e** (- h2)) ** (-1)
            y.append(H0)
            y.append(H1)
            y.append(H2)


            if new_list[k][4] == 'Iris-setosa':
                target = [1, 0, 0]
            elif new_list[k][4] == 'Iris-versicolor':
                target = [0, 1, 0]
            else:
                target = [0, 0, 1]

            for s in range(len(y)):
                q = y[s] * (1 - y[s]) * (target[s] - y[s])
                q1.append(q)

            for i in range (len(initial2)):
                delt = q1[0] * initial2[i][0] + q1[1] * initial2[i][1] + q1[2] * initial2[i][2]
                Delta.append(delt)

            for r in range (len(hid2)):
                q = hid2[r] * (1 - hid2[r]) * Delta[r]
                q2.append(q)

            for i in range (len(initial1)):
                delt = q1[0] * initial1[i][0] + q1[1] * initial1[i][1] + q1[2] * initial1[i][2]
                Delta1.append(delt)
                        
            for r in range (len(hid1)):
                q = hid1[r] * (1 - hid1[r]) * Delta1[r]
                q3.append(q)

            for j in range(len(initial2[0])):
                for i in range(len(initial2)):
                    initial2[i][j] = initial2[i][j] + learn_rate[b] * q1[j] * hid2[i]
            for j in range(len(initial1[0])):
                for i in range(len(initial1)):
                    initial1[i][j] = initial1[i][j] + learn_rate[b] * q2[j] * hid1[i]

            for j in range(len(initial[0])):
                for i in range(len(initial)):
                    initial[i][j] = initial[i][j] + learn_rate[b] * q3[j] * eval(new_list[k][i])
            Y.append(y)
            T.append(target)
        
        Conver = []
        for v in range(len(Y)):
            for u in range(len(Y[0])):
                mse = MSE(T[v][u], Y[v][u])
                converge = converge + mse
            converge = converge / 3
            Conver.append(converge)
            converge = 0
        diverge = 0
        for x in range(len(Conver) - 1):
            if abs((Conver[x + 1] -  Conver[x] ) / Conver[x]) > 0.0001:
                diverge = diverge + 1 
                           
            else:
                diverge = diverge
        
        if diverge == 0:
            print(diverge)
            break 
        else:
            print(diverge)
            continue      
        
        

    
    print(time)
# Homework 3-2

**Introduction**
-
This code is written in Python 3.7.0 64-bit

**Explanation of the Code**
-
The codes were extended from the code of previous question. I changed "learn_rate" to a list that contains 5 learning rate.

I divided the code into two for analysizing the effect of different learning_rate and the result of convergence.


The list,Y = [], is the output neurons of all the examples.
The list,T = [], is the target vectors of all the examples in new_list.

In the first one, hw4_2_1, I used a list, learn_list, to compare the weights based on different laerning rates. In the end, I printed out the updated weights.

In the second one, hw4_2_2, I used the function, MSE, defined in the code, I calculated the mean square errpr in the last part of the code. Moreover, the list,Conver, is a list that decides convergence. To be more specific, if there is any output in the Conver list that doesn't mach the convergence function defined in the code, (diverge > 0) we will start another epoch again for all the examples. Nevertheless, I found that this code wouldn't reach convergence for each learning rate. As a result, I just printed out part of the output (the number of divergences in Conver) and didn't print out the whole output.

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

**Explanation of output**
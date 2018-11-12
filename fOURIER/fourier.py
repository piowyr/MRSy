import numpy as np
import matplotlib.pyplot as plt

def series(x):
    const = 2 * np.pi * x / T
    return lambda x: An(n) * np.cos(const * n) + Bn(n) * np.sin(const * n)

def fab1():
    return lambda n: 0, lambda n: (-2*(-1)**n)/(np.pi * n)

def fab2():
    return lambda n: 1/(np.pi**2 * n**2), lambda n: -1/(np.pi * n)

def fab3():                                                              
    return lambda n: 0, lambda n: 1 if n==1 else 0   

def fun():
    return lambda x: x, lambda x: x**2, lambda x: np.sin(x)

def plotSeries(x, S, fx, ylabel):
    fig = plt.figure()
    plt.xlabel("x")
    plt.ylabel("f(x) = " + ylabel)
    ax = fig.add_subplot(111)
    ax.plot(x, S, x, fx(x), 'r--')
    plt.show()
    
# rng = int(input('Wpisz range: '))
rng = 100
A = [-1, 0, -np.pi]
B = [1, 1, np.pi]
A0 = [0, 2/3, 0] 
F = {"x" : [fab1()], "x^2" : [fab2()], "sin(x)" : [fab3()]}
fx = [fun()]
X = []
Tt = []
for i in range(3):
    X.append(np.linspace(A[i], B[i], num=1000))
    Tt.append(B[i] - A[i])
X = np.array(X)
Tt = np.array(Tt)
for inx, (k, v) in enumerate(F.items()):
    a = A[inx] 
    b = B[inx]
    a0 = A0[inx]
    T = Tt[inx] 
    x = X[inx]
    An, Bn = v[0][0], v[0][1]
    f = series(x)
    S = np.zeros((x.shape))
    for i in range(1, rng+1):
        n = i
        S += f(x)
    S += a0/2
    
    plotSeries(x,S, fx[0][inx], k)

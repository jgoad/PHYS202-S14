import numpy as np
def trpz(func,a,b,N):
    "Estimates the integral using trapazoidal approximation"
    h = (b-a)/N

    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) +func(a+k*h).sum())
    return I
    print "Tapezoidal Rule Integral= ", I

def simps(func,a,b,N):
    "Estimates the integral using Simpsons method"
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a)+func(b)+ 4.*func(a+(2*k1-1)*h).sum() +2.*func(a+2*k2*h).sum())
    return I
    print "Simpson's rule integral=",I
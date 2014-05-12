def twoPtForwardDiff(x,y):
    "Takes an array x and calculates the rate of change of a array y wrt x." 
    "Y should be the output of some function of x. Must be over the same interval as x. 
    dydx1 = np.zeros(y.shape,float)
    dydx1[0:-1] = np.diff(y)/np.diff(x)
    dydx1[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])#backward diff
    return dydx1
def twoPtCenteredDiff(x,y):
    "Better numerical approximation for dy/dx that twoPtForwardDiff
    dydx2 = np.zeros(y.shape,float)
    dydx2[1:-1] = (y[2:] - y[:-2])/(x[2:]-x[:-2])
    dydx2[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])#backward diff
    return dydx2
def fourPtCenteredDiff(x,y):
    '''approximate dx/dy from x and y and lower order approximations for the middle terms.'''
    
    dydx3 = np.zeros(y.shape, float)
    dydx3[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1]- y[4:]) / (12 * (x[1]-x[0]))
    dydx3[-2] = (y[-2] - y[-3])/(x[-2] - x[-3])#backward diff
    dydx3[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])#backward diff
    dydx3[0] = (y[1]-y[0])/(x[1]-x[0])#forward diff
    dydx3[1] = (y[2]-y[1])/(x[2]-x[1])#forward diff
    return dydx3
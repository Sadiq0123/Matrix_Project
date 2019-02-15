import numpy as np
import matplotlib.pyplot as plt
Arr=np.array([-1,1])
omat=np.array([[0,1],[-1,0]])
P=np.array([1,7]).T
n1=np.array([1,-0.5])
P1=np.array([-2.5])
centre=np.array([-8,-6]).T
def dirVec(A,B):
    AB=np.vstack((A,B)).T
    return np.matmul(AB,Arr)
def stLinePlot(A,B):
    M=np.vstack((A,B))
    plt.plot(M[:,0],M[:,1])
    return
def FootOfPerpendicular(P1,n1,point):   #  THIS FUNCTION CALCULATES THE FOOT OF PERPENDUCULAR ON LINE 'n1*x=P1' FROM POINT 'point'
    #   HERE, THE LINES ARE n1*x=p1 and n2*x=p2
    #   WE HAVE THE NORMAL VECTOR OF A LINE n1 FROM n1*x = P1
    #   THEN THE OTHER LINE HAS NORMAL AS normVec(n1) AND P2 = np.matmul(n2, centre)
    #   THE INTERSECTION GIVES THE FOOT OF PERPENDICULAR
    n2 = np.matmul(omat, n1)
    P2 = np.matmul(n2, point)
    N=np.vstack((n1,n2))
    P=np.zeros((2,1))
    P[0]=P1
    P[1]=P2
    return np.matmul(np.linalg.inv(N),P)
def LinePlt(A,n):
    n1=np.matmul(omat,n)
    len = 11
    lam1 = np.linspace(-1, 1, len)
    Mat = np.zeros((2, len))
    for i in range(len):
        temp1 = A + 30 * lam1[i] * n1
        Mat[:, i] = temp1
    plt.plot(Mat[0, :], Mat[1, :])
    return
Q=FootOfPerpendicular(P1,n1,centre)
stLinePlot(Q.T,centre.T)
LinePlt(P,n1)
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]+0.3,Q[1]-0.4,'Q')
plt.plot(centre[0],centre[1],'o')
plt.text(centre[0]-0.2,centre[1]+0.3,'C')
plt.xlim((-15,0))
plt.ylim((-15,0))
plt.show()

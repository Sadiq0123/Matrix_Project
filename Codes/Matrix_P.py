import numpy as np
import matplotlib.pyplot as plt

V=np.array([[1,0],[0,0]])
F=np.array([6])
u=(1/2)*np.array([0,-1]).T
P=np.array([1,7]).T
Arr=np.array([-1,1])
omat=np.array([[0,1],[-1,0]])

centre=np.array([-8,-6]).T
n1=np.matmul(P.T,V)+u.T
P1=-(np.matmul(P.T,u)+F)

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


x = np.linspace(-10, 10, 1000)

# calculate the y value for each element of the x vector
y = x**2 + 6

fig, ax = plt.subplots()
ax.plot(x, y)




circle=plt.Circle((centre[0],centre[1]),np.linalg.norm(centre.T-Q.T),color='blue',fill=False)
ax.add_artist(circle)




LinePlt(P,n1)
stLinePlot(Q.T,centre.T)
plt.plot(P[0],P[1],'o')
plt.text(P[0]+0.3,P[1]-0.4,'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]+0.3,Q[1]-0.4,'Q')
plt.plot(centre[0],centre[1],'o')
plt.text(centre[0]+0.3,centre[1]+0.4,'C')
plt.xlim((-15,10))
plt.ylim((-10,15))
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='lower right')
plt.grid()
plt.show()

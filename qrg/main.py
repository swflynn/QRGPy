#=================20==================40==================60==================80
#                                   QRGPy
#==============================================================================#
#Generate a Quasi-Regular Grid for any d-dimensional system of interest.
#Testing with specific functions, will generalize after
#==============================================================================#
import numpy as np
#==============================================================================#
def P_i(d,x_i,V_i):
#Target distribution function
#In general and d-dimensional system should be allowed, begin by defining sys.
    pass

def Morse(omegas,D_morse,x_i):
#Potential Energy: Sum of 1D Morse potentials
#==============================================================================#
#d                ==>Coordinate dimensionality (x^i=x_1,x_2,...x_d)
#x_i(d)           ==>i-th grid points coordinates (x^i=x_1,x_2,...x_d)
#D_morse          ==>Parameter for Morse Potential
#omegas(d)        ==>Parameter for Morse Potential
#V_i              ==>Potential Energy evaluation V(x_i)
#==============================================================================#
    return D_morse*np.sum((np.exp(-omegas*x_i)-1.)**2 )


def box_size_P():
#compute the box for normalizing P
    pass

def Integral_P():
#Compute the first moment of the distribution to normalize the distribution
    pass

def Initial_Grid():
#Use rejection to generate an initial set of points according to P
    pass

def Pseudo_Pairwise_Energy():
#Define the Pseudo-Potential to minimize when generating the QRG
#In general this could be user defined
    pass


def QR_Minimize():
#Use the QR formalism to generate a QRG from the initial grid
    pass



#==============================================================================#
D_morse=12.
omega_list=list()
omega_list.append(3.)
omega_list.append(4.)
omegas=np.array(omega_list)

x_list=list()
x_list.append(1.)
x_list.append(2.)
x_i=np.array(x_list)

print(Morse(omegas,D_morse,x_i))

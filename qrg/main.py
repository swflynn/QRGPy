#=================20==================40==================60==================80
#                                   QRGPy
#==============================================================================#
#Generate a Quasi-Regular Grid for any d-dimensional system of interest.
#Testing with specific functions, will generalize after
#==============================================================================#
import numpy as np
#==============================================================================#
def P_i(d,E_cut,x_i,integral_P):
#Target distribution function
#In general and d-dimensional system should be allowed, begin by defining sys.
#==============================================================================#
#E_cut              ==>Distribution cutoff contour
#x_i(d)             ==>i-th grid points coordinates (x^i=x_1,x_2,...x_d)
#V_i                ==>Potential Energy evaluation V(x_i)
#E_cut              ==>Distribution cutoff contour
#integral_P         ==>Normalization constant for the distribtion P(x)
#P_i                ==>evaluate P(x_i)
#==============================================================================#
    V_i=Morse(omegas,D_morse,x_i)
    if(V_i<E_cut): P=(E_cut-V_i)**(d/2.)/integral_P
    else: P=1e-20                           #Define distribution=0 beyond Ecut
    return P
#==============================================================================#
def Morse(omegas,D_morse,x_i):
#==============================================================================#
#Potential Energy: Sum of 1D Morse potentials
#==============================================================================#
#omegas(d)        ==>Parameter for Morse Potential
#x_i(d)           ==>i-th grid points coordinates (x^i=x_1,x_2,...x_d)
#D_morse          ==>Parameter for Morse Potential
#==============================================================================#
    return D_morse*np.sum((np.exp(-omegas*x_i)-1.)**2 )
#==============================================================================#
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
d=2
D_morse=12.
E_cut=100.
integral_P=1.
#==============================================================================#
omega_list=list()
omega_list.append(3.)
omega_list.append(4.)
omegas=np.array(omega_list)
#==============================================================================#
x_list=list()
x_list.append(1.)
x_list.append(2.)
x_i=np.array(x_list)
#==============================================================================#
print(Morse(omegas,D_morse,x_i))
print(P_i(d,E_cut,x_i,integral_P))

import numpy as np
import matplotlib.pyplot as plt

#se crea una funcion para retornar la distribucion normal con promedio mean y desviacion estandar sigma

def normal_dist(x, mean, sigma):
    pnormal = np.sqrt(1.0/(2*np.pi*(sigma**2)))*np.exp(-((x-mean)**2)
    return pnormal

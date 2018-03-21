import numpy as np

#se crea una funcion para retornar n numeros aleatorios siguiendo una distribucion discreta
#usando np.random.choice
N = np.array([10, 100 , 1000])
def sample_1(N):
    pr = [-10, -5, 3, 9]
    naleatorio = np.random.choice(pr, N, p=[0.1, 0.4, 0.2, 0.3])
    return naleatorio
# se crea una funcion para retornar n numeros aleatorios que siguen distribucion de probabilidad exponencial
#n.random.exponential con beta igual a 0.5 y size igual a N
def sample_2(N):
    proexp = np.random.exponential(0.5, N)
    return proexp
#se crea duncion para generar m promedios dada una funcion de sampleo, un numero N y el numero de promedios que se requieren M

def get_mean(sampling_fun, N, M):
    numpromedios = np.zeros(M)
    for j in range(M):
        numpromedios[j] = np.mean(sampling_fun(N))
    return numpromedios

#se crean archivos para que se generen M promedios asociados a 10, 100, y 1000
#se crea m y una lista con las funciones de sample 1 y sample 2

M = 10000
lnombre = [sample_1, sample_2]
nombres = ["sample_1", "sample_2"]
for i in range(len(lnombre)):
    for j in range(len(N)):
        genprom =  get_mean(lnombre[i],N[j], M)
        generararchivo = np.savetxt(nombres[i]+"_"+ str(j)+".txt", genprom)
        


    
    

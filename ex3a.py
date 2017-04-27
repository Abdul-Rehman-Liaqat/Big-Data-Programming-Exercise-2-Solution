
#mpi4py: high level interface of MPI for python. Numpy as a default datastructure
#of MPI for easier communication.

from mpi4py import MPI
import numpy as np

#Initializing the communicator and necessary variables
comm = MPI.COMM_WORLD
worker = comm.Get_rank()
num_worker= comm.Get_size()
n=np.array([0])


#Data is in the source process only.
if(worker==0):
    length=40
    arr=np.random.randint(5,size=length,dtype=int)
    print(" \n--------------------------------This is Root Process and Original array :\n ",arr)
    n[0]=int(length/num_worker)
else:
    arr=None
    
#Broadcasting the size of chunk each worker will be receiving. Since it is in 
#Numpy format each worker automatically knows the type of data it will be receiving.
#Each worker will create a local array of numpy of the same size for the reception of data.
comm.Bcast(n,root=0)    
localArr=np.zeros(n[0],dtype=int)

#Scattering the data from source process to workers. Source will sendout the chunks to
#each process. Each process will receive a chunk and store it in the previously created
#numpy arrays
comm.Scatter(arr,localArr,root=0)
print("\nWorker number is = ", worker)
print(localArr)
print("length of local is = ",len(localArr))






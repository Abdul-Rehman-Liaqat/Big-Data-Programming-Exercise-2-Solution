# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 21:45:48 2017

@author: Abdul Rehman
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
worker = comm.Get_rank()
num_worker= comm.Get_size()

print(worker)
N=10000

sendTo=(worker+1)%num_worker
recvFrom=(worker-1)%num_worker
myData=np.zeros(1)

myData[0]=N*worker+num_worker*N
recvData=np.zeros(1)
comm.Send(myData,dest=sendTo)
comm.Recv(recvData,source=recvFrom)
print('recvData= ',recvData,' sendData= ',myData,' rank= ',worker)
#    print(recvData[0])
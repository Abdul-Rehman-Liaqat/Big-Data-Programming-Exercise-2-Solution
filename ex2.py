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

N=10000

if(worker==3):
    sendTo=0
else:
    sendTo=(worker+1)
if(worker==0):
    recvFrom=3
else:   
    recvFrom=(worker-1)  

myData=np.zeros(1)
myData[0]=N*worker+num_worker*N
recvData=np.zeros(1)
temp=np.zeros(0)
comm.Send(myData,dest=sendTo)
comm.Recv(recvData,source=recvFrom)

print('worker = ',worker)
print('recvFrom = ',recvFrom,'  receive = ',recvData)
print('sendTo = ',sendTo,'  send = ',myData,'\n\n')


#    print(recvData[0])
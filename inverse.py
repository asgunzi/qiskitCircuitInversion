# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:59:12 2020

@author: asgun
"""


from qiskit import *

qc = QuantumCircuit(3)

qc.s(0)
qc.h(1)
qc.cx(0,2)

print(qc)

qc2 = qc.inverse()

print(qc2)
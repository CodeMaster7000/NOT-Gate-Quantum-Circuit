import numpy as np
from qiskit import * 
from qiskit.visualization import plot_histogram 

def NOT(inp): 
    qc = QuantumCircuit(1, 1) 
    qc.reset(0) 

    if inp == '1': 
        qc.x(0)  
    qc.barrier() 
    qc.x(0)  
    qc.barrier() 
    qc.measure(0, 0) 
    qc.draw('mpl')  
    backend = Aer.get_backend('qasm_simulator') 
    job = execute(qc, backend, shots=1, memory=True) 
    output = job.result().get_memory()[0] 
    return qc, output 

for inp in ['0', '1']: 
    qc, out = NOT(inp) 
    print('NOT input:', inp, 'Output:', out) 
    display(qc.draw()) 
    print('\n')

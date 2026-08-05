import numpy as np
from gate import *
from quantumstate import QuantumState
from quantumcircuit import QuantumCircuit
from qubit import Qubit

# This file contains examples of how to use the QuantumState, QuantumCircuit, and Qubit classes.

# 1) Create a QuantumState representing a single qubit in the |0> state.

state = QuantumState(np.array([1, 0])) # |0> state
print("Initial state:", state)

# 2) Create and apply the X gate to the state.
x = X() # Create an X gate
state_after_x = x.apply(state) # Apply the X gate to the state
print("State after applying X gate:", state_after_x)

# 3) Create and apply the H gate to the original state.
h = H() # Create a Hadamard gate
state_after_h = h.apply(state) # Apply the H gate to the state
print("State after applying H gate:", state_after_h)

#4) Create a multi-qubit QuantumState and apply a CNOT gate.
# Create a 2-qubit state |00>
two_qubit_state = QuantumState(np.array([1, 0, 0, 0])) # |00> state
print("Initial two-qubit state:", two_qubit_state)
cnot = CNOT() # Create a CNOT gate
after_cnot = cnot.apply(two_qubit_state) # Apply the CNOT gate to the two-qubit state
print("Two-qubit state after applying CNOT gate:", after_cnot)

#5) Create a multi-qubit QuantumState and create a Bell State

#apply a Hadamard gate to the first qubit, and then a CNOT gate.
two_qubit = QuantumState(np.array([1, 0, 0, 0])) # |00> state
print("Initial two-qubit state:", two_qubit_state)

h = H() # Create a Hadamard gate
i = I() # Create an Identity gate
hi = h.tensor(i) # Create a tensor product of H and I that applies H to the first qubit
cnot = CNOT() # Create a CNOT gate

after_hi = hi.apply(two_qubit) # Apply the H gate to the first qubit
print("Two-qubit state after applying H gate to the first qubit:", after_hi)

after_cnot = cnot.apply(after_hi) # Apply the CNOT gate to the two-qubit state
print("Result after applying CNOT gate:", after_cnot)

expected = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)]) # the Bell state
assert np.allclose(after_cnot.state, expected), "Not the Bell state"
print("Bell state verified")



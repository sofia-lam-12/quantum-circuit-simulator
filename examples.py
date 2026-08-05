import numpy as np
from simulator.gate import *
from simulator.quantum_state import QuantumState
from simulator.circuit import QuantumCircuit
from simulator.qubit import Qubit

# This file contains examples of how to use the QuantumState, QuantumCircuit, and Qubit classes.

# 1) Create a QuantumState representing a single qubit in the |0> state.

print()
print("--- 1) Single Qubit Creation ---")

state = QuantumState(np.array([1, 0])) # |0> state
print("Initial state:", state)

# 2) Create and apply the X gate to the state.

print()
print("--- 2) Applying X Gate ---")

x = X() # Create an X gate
state_after_x = x.apply(state) # Apply the X gate to the state
print("State after applying X gate:", state_after_x)

# 3) Create and apply the H gate to the original state.

print()
print("--- 3) Applying H Gate --- ")

h = H() # Create a Hadamard gate
state_after_h = h.apply(state) # Apply the H gate to the state
print("0 State after applying H gate:", state_after_h)

state0 = QuantumState(np.array([1, 0]))
state1 = QuantumState(np.array([0, 1]))

print("H|0> =", H().apply(state0))
print("H|1> =", H().apply(state1))

#4) Create a multi-qubit QuantumState and apply a CNOT gate.

print()
print("---- 4) Multi Qubit CNOT Gate ----")

# Create a 2-qubit state |10>
two_qubit_state = QuantumState(np.array([0, 0, 1, 0])) # |10> state
print("Initial two-qubit state:", two_qubit_state)
cnot = CNOT() # Create a CNOT gate
after_cnot = cnot.apply(two_qubit_state) # Apply the CNOT gate to the two-qubit state
print("Two-qubit state after applying CNOT gate:", after_cnot)

#5) Create a multi-qubit QuantumState and create a Bell State

print()
print("---- 5) Creating a Bell State ----")

#apply a Hadamard gate to the first qubit, and then a CNOT gate.
two_qubit = QuantumState(np.array([1, 0, 0, 0])) # |00> state
print("Initial two-qubit state:", two_qubit)

h = H() # Create a Hadamard gate
i = I() # Create an Identity gate
hi = h.tensor(i) # Create a tensor product of H and I that applies H to the first qubit
# print(hi.matrix)
cnot = CNOT() # Create a CNOT gate

after_hi = hi.apply(two_qubit) # Apply the H gate to the first qubit
print("Two-qubit state after applying H gate to the first qubit:", after_hi)

after_cnot = cnot.apply(after_hi) # Apply the CNOT gate to the two-qubit state
print("Result after applying CNOT gate:", after_cnot)

expected = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)]) # the Bell state
assert np.allclose(after_cnot.state, expected), "Not the Bell state"
print("Bell state verified")

#6) Create a QuantumCircuit and apply it to a QuantumState.

print()
print("---- 6) Creating a Quantum Circuit ----")

qc = QuantumCircuit(2) # Create a QuantumCircuit for 2 qubits
qc.add_gate(hi) # Add the H gate to the first qubit
qc.add_gate(cnot) # Add the CNOT gate

initial = QuantumState(np.array([1, 0, 0, 0])) # |00> state
result = qc.run(initial)
print("Result after running the QuantumCircuit:", result)
assert np.allclose(result.state, expected), "Not the Bell state"
print("Bell state verified")

# 7) Test partial circuit execution with operate()

print()
print("---- 7) Testing Partial Circuit Execution ----")

partial = qc.operate(initial, 1)  # apply only the H gate, not CNOT
expected_partial = np.array([1/np.sqrt(2), 0, 1/np.sqrt(2), 0])  # H applied to qubit 0 of |00>
assert np.allclose(partial.state, expected_partial), "Partial operate() failed"
print("Partial operate() verified")

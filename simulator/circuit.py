import numpy as np
from gate import Gate
from quantum_state import QuantumState

class QuantumCircuit:
    """
    A class representing a QuantumCircuit that can be applied to a QuantumState object.
    When applying this QuantumCircuit to the QuantumState object, the sizes must be
    compatible, meanining that if the QuantumState has n qubits, then the QuantumCircuit
    must be designed to operate of a QuantumState of n qubits.

    Attribute number: the number of qubits required of a QuantumState that this circuit operates on. 
    Invariant: must be positive integer

    Attribute gates: a list of Gates that are in this circuit
    Invariant: must be a list of Gate objects.

    """
    def __init__(self, num):
        assert type(num) == int

        self.number = num
        self.gates = [] #initialize an empty list to the store the gates


    def add_gate(self, gate):
        """
        Adds gate (a Gate object) to this QuantumCircuit.

        Parameter gate: the gate to be added to this circuit.
        Precondition: gate must be a Gate object, with the same number of qubits
        this circuit is designed to operate on.
        """
        assert isinstance(gate, Gate), "gate must be a Gate object"
        assert gate.num == self.number, "Gate and circuit must have the same number of qubits"
        self.gates.append(gate)
    

        
    def run(self, state):
        """
        Performs this QuantumCircuit on a quantum state. 

        Parameter state: the state that this QuantumCircuit operates on.
        Precondition: state must be a QuantumState object, with the same number of qubits
        this circuit is designed to operate on.
        """
        return self.operate(state, len(self.gates))
    

    def operate(self, state, number):
        """
        Performs this QuantumCircuit on a quantum state. 

        Parameter state: the state that this QuantumCircuit operates on.
        Precondition: state must be a QuantumState object, with the same number of qubits
        this circuit is designed to operate on.

        Parameter number: the number of gates to apply from this circuit to the state. If number is 
        greater than the number of gates in this circuit, then all gates will be applied.
        Precondition: number must be a non-negative integer.
        """
        assert isinstance(state, QuantumState), "state must be a QuantumState object"
        assert isinstance(number, int), "number must be an integer"
        assert state.num == self.number, "State and circuit must have the same number of qubits."
        assert number >= 0, "number must be a non-negative integer"

        current = state

        if number >= len(self.gates):
            number = len(self.gates)
        
        for i in range(number):
            gate = self.gates[i]
            current = gate.apply(current)

        return current
        
        


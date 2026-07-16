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
    def __init__(num):
        assert type(num) == int

        self.number = num
        self.gates = [] #initialize an empty list to the store the gates

    def operate(state):
        """
        Performs this QuantumCircuit on a quantum state. 

        Parameter state: the state that this QuantumCircuit operates on.
        Precondition: state must be a QuantumState object, with the same number of qubits
        this circuit is designed to operate on.
        """

#work in progress, create a place where you know what "qubits" the gates operate on, and when.
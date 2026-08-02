import numpy as np

class Gate:
    """
    A class representing a quantum Gate that can be applied to a quantum state. 

    Attribute matrix: A 2d square numpy array (matrix) representing the gate.
    Invariant: The "length" of matrix must be 2^number, where number is the number of qubits the gate operates on.

    Attribute size: An integer representing the size of the gate matrix.
    Invariant: size must be the length of the gate matrix, and 2^number = size.

    Attribute num: An integer representing the number of qubits in the system (n).
    Invariant: num >=0, and 2^num = size.
    """

    def __init__(self, matrix):
        assert matrix.ndim == 2, "Gate matrix must be a 2D array."
        assert matrix.shape[0] > 0, "Gate matrix size must be greater than 0."
        assert matrix.shape[0] == matrix.shape[1], "Gate matrix must be square."
        assert np.allclose(
            matrix.conj().T @ matrix,
            np.eye(matrix.shape[0])), "Gate matrix must be unitary."
        #conj().T --> conjugate transpose
        #for a matrix, M, to be unitary, M*Mdagger = I, where I is identity matrix
        #np.eye(matrix.shape[0])) --> creates identity matrix of the same size (assuming matrix is square)
        assert np.log2(matrix.shape[0]).is_integer(), "Gate matrix size must be a power of 2."
        self.matrix = matrix
        self.size = matrix.shape[0]
        self.num = int(np.log2(self.size))

    def apply(self, state):
        """
        Applies this Gate to a quantum state and returns the resulting quantum state.

        Parameter state: the state that this Gate operates on.
        Precondition: state must be a QuantumState object, with the same number of qubits.
        """
        assert state.num = self.num, "Gate and state must have the same number of qubits"

        new_state = self.matrix @ state.state
        return QuantumState(new_state)


#all the functions for creation of common quantum gates (X, H, CNOT, etc.) are defined here:
#(Each function name is the name of the gate)

def I():
    """
    Returns the identity gate.
    [1 0
     0 1]

    (This gate does not change the state of the qubit it is applied to.)
    """
    array = np.array([[1, 0], [0, 1]])
    return Gate(array)

def X():
    """
    Returns the Pauli-X gate (also known as the NOT gate).
    [0 1
     1 0]

    (This gate flips the state of the qubit it is applied to.)
    """
    array = np.array([[0 , 1] [1, 0]])
    return Gate(array)

def Y():
    """
    Returns the Pauli-Y gate.
    [0   -i
     i    0]
    """
    #note: i is imaginary unit, represented in numpy as 1j
    return Gate(np.array([[0, -1j], [1j, 0]]))
    

    
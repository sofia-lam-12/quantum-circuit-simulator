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
    Returns the Pauli-X gate (also known as the NOT gate), which flips the state of the qubit
    it is applied to.

    [0 1
     1 0]
    """
    array = np.array([[0 , 1] [1, 0]])
    return Gate(array)

def Y():
    """
    Returns the Pauli-Y gate, which flips and applies a phase shift to the qubit.

    [0   -i
     i    0]
    """
    #note: i is imaginary unit, represented in numpy as 1j
    return Gate(np.array([[0, -1j], [1j, 0]]))

def Z():
    """
    Returns the Paul-Z gate, which flips the phase of the qubit it is applied to.

    [1  0
     0 -1]
    """
    return Gate(np.array([[1, 0], [0, -1]]))

def H():
    """
    Returns the Hadamard gate, which creates a superposition of the qubit it is applied to.

    [1/sqrt(2)  1/sqrt(2)
     1/sqrt(2) -1/sqrt(2)]
    """
    array = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    return Gate(array)

def CNOT():
    """
    Returns the controlled-NOT (CNOT) gate. This 2 qubit gate flips the state of the target qubit if
    the control qubit is 1, and does nothing (like the identity gate) if the control qubit
    is 0.

    [1 0 0 0
     0 1 0 0
     0 0 0 1
     0 0 1 0]
    """

    array = np.array([[1, 0, 0, 0],
                      [0, 1, 0, 0], 
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])
    return Gate(array)

def S():
    """
    Returns the S gate, which applies a phase shift of pi/2 to the qubit it is applied to.

    [1 0
     0 i]
    """
    return Gate(np.array([[1, 0], [0, 1j]]))

def T():
    """
    Returns the T gate, which applies a phase shift of pi/4 to the qubit it is applied to.

    [1 0
     0 exp(i*pi/4)]
    """
    fourth = np.exp(1j * np.pi / 4)
    return Gate(np.array([[1, 0], [0, fourth]]))

def SWAP():
    """
    Returns the SWAP gate. This 2-qubit gate swaps the states of the two qubits it is applied to (essentially
    relabeling the two qubits). If the two qubits are entangled, they will remain entangled. 
    [1 0 0 0
     0 0 1 0
     0 1 0 0
     0 0 0 1]
    """
    array = np.array([[1, 0, 0, 0],
                      [0, 0, 1, 0], 
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]])
    return Gate(array)

def CCNOT():
    """
    Returns the Toffoli gate, also known as the controlled-controlled-NOT (CCNOT) gate. This 3-qubit 
    gate flips the state of the target qubit if both control qubits are 1, and does nothing 
    (like the identity gate) if either control qubit is 0.
    """
    m = np.eye(8, dtype=complex) #first create the identity matrix
    # keep everything the same, unless both control qubits are 1, and flip the target bit.
    # so we swap |110> <-> |111> (they map to each other). Swap rows 6 and 7-- whatever used to map
    # to basis vector 6 (|110>) now maps to basis vector 7 (|111>), and vice versa.
    m[[6, 7]] = m[[7, 6]]
    return Gate(m)

def Fredkin():
    """
    Returns the Fredkin gate, also known as the controlled-SWAP gate. This 3-qubit gate swaps the states 
    of the two target qubits if the control qubit is 1, and does nothing to the target qubit if the 
    control qubit is 0.

    The Fredkin gate:
    - Upper left quadrant is the identity matrix -- control qubit is 0, so do nothing to target qubits.
    - Upper right/Lower left quadrants are all zeros -- control qubit does not change
    - Lower right quadrant is the SWAP gate -- control qubit is 1, so swap the target qubits.
    """
    m = np.eye(8, dtype=complex) #first create the identity matrix
    #in swap, just switch the middle two rows. Since we have 0s in the other entries, we can just swap
    # the whole rows.
    m[[5, 6]] = m[[6, 5]]
    return Gate(m)


                    
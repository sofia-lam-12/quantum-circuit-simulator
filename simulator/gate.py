import numpy as py

class Gate:
    """
    A class representing a quantum Gate that can be applied to a quantum state. 

    Attribute matrix: A 2d square numpy array (matrix) representing the gate.
    Invariant: The "length" of matrix must be 2^number, where number is the number of qubits the gate operates on.

    Attribute size: An integer representing the size of the gate matrix.
    Invariant: size must be the length of the gate matrix, and 2^number = size.

    Attribute number: An integer representing the number of qubits in the system (n).
    Invariant: number >=0, and 2^number = size.
    """

    def __init__(self, matrix):
        assert matrix.ndim == 2, "Gate matrix must be a 2D array."
        assert matrix.shape[0] > 0, "Gate matrix size must be greater than 0."
        assert matrix.shape[0] == matrix.shape[1], "Gate matrix must be square."
        assert py.isclose(py.linalg.det(matrix), 1), "Gate matrix must be unitary."
        assert py.isclose(py.linalg.norm(matrix), 1), "Gate matrix must be normalized."
        assert py.log2(matrix.shape[0]).is_integer(), "Gate matrix size must be a power of 2."
        
        self.matrix = matrix
        self.size = matrix.shape[0]
        self.num = int(py.log2(self.size))

    
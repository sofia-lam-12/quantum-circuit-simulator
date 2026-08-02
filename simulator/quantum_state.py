import numpy as np

class QuantumState:
    """
    A class representing a quantum state of an n-qubit system, represented with a state vecotr of size 
    2^n. Allows for representation of both separable and entangled states.

    Attribute state: A numpy array (can be complex)representing the state vector of the quantum system.
    Invariant: The state vector must be normalized.

    Attribute length: An integer representing the length of the state vector in the system.
    Invariant: length must be the length of the state vectory array, and 2^number = length.

    Attribute number: An integer representing the number of qubits in the system (n).
    Invariant: number >=0, and 2^number = length.
    """

    def __init__(self, state):

        assert state.ndim == 1, "State vector must be a 1D array."
        assert state.shape[0] > 0, "State vector size must be greater than 0."
        assert isinstance(state, np.ndarray), "State vector must be a numpy array."
        assert np.isclose(np.linalg.norm(state), 1), "State vector must be normalized."
        assert np.log2(state.shape[0]).is_integer(), "State vector size must be a power of 2."
        
        self.state = state
        self.length = len(state)
        self.num = int(np.log2(self.length)) #2^(number of qubits) = statevector length

    def __repr__(self):
        return str(self.state) + " (Quantum State)"


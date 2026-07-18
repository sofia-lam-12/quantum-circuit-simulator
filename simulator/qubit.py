class Qubit:
    """
    A class representing a single qubit.
    """
    def __init__(self, state):
        self.state = state

    def apply_gate(self, gate):
        # Apply a quantum gate to the qubit's state
        #.shape gets a tuple, so shape[0] gets the first element of tuple (row length)
        assert self.state.shape[0] == gate.size, "Gate size must match qubit size."
        self.state = gate @ self.state #@ is matrix multiplication in numpy

    def measure(self):
        # Measure the qubit and collapse its state
        prob = np.abs(self.state) ** 2
        result = np.random.choice([0, 1], p=prob)
        if result === 0:
            self.state = np.array([1, 0])
        else:
            result = np.array([0, 1])
        return result
    
    # """
    # Combines this qubit with another qubit to form a two-qubit system, using a 
    # tensor product.
    # """
    # def combine(self, other):
        
    #     # Combine this qubit with another qubit to form a two-qubit system
    #     combined_state = np.kron(self.state, other.state)
    #     return QuantumState(combined_state)

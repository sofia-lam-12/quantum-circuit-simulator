# quantum-circuit-simulator
A Quantum circuit simulator from scratch in Python using linear algebra and NumPy.

# features
- Objected oriented design with classes for quantum states (qubit as a subclass), gates, and circuits
- Simulates n-qubit state vectors
- Executes quantum circuits by applying a series of gates
- Implements the following common gates:
    - Identity
    - Pauli X, Y, and Z
    - Hadamard
    - S
    - T
    - CNOT
    - SWAP
    - Toffoli (CCNOT)
    - Fredkin (Control-SWAP)
- Tensor products for quantum states and gates (for multi qubit gates/states)

# Examples/Running
- running python examples.py demonstrates the following:
    - Single and multi-qubit operations
    - Bell state creation from multi-qubit using gates and a circuit
    - Creation of a multi-qubit gate from single qubit ones
    - Quantum circuit execution
    - Partial circuit execution

# Future Improvements
- Measuring quantum states
- Gates operating on select qubits within a larger quantum state
- Qiskit verification

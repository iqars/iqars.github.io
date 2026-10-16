---
title: Quantum Algorithm Research Seminar
permalink: /materials/papers.html
---

<span id="quantum-algorithm-research-seminar-qars"></span>
<span id="papers-and-resources"></span>
# Research Paper Collection

A curated collection of research papers relevant to quantum algorithms and quantum computing, organized by research topic.

<div class="paper-collection" markdown="1">

<nav class="paper-toc" aria-label="Browse by Topic" markdown="1">

## Browse by Topic

1. [Quantum Algorithms & Optimization](#quantum-algorithms-optimization)
1. [Quantum Simulation & Many-Body Physics](#quantum-simulation-many-body-physics)
1. [Dissipative Quantum Algorithms & Open Systems](#dissipative-quantum-algorithms-open-systems)
1. [Quantum Learning, Tomography & Machine Learning](#quantum-learning-tomography-machine-learning)
1. [Quantum Complexity & Computational Advantage](#quantum-complexity-computational-advantage)
1. [Classical Simulability, Entanglement & Randomness](#classical-simulability-entanglement-randomness)
1. [Quantum Computing Architectures & Fault Tolerance](#quantum-computing-architectures-fault-tolerance)

</nav>

<span id="quantum-algorithms"></span>
## Quantum Algorithms & Optimization
{: #quantum-algorithms-optimization}

<span id="grovers-search"></span>
<span id="grand-unification-of-algorithms"></span>
### Fundamental Algorithmic Primitives
{: #fundamental-algorithmic-primitives}

- <span id="paper-2507-23787"></span>**[Amplitude amplification and estimation require inverses](https://arxiv.org/abs/2507.23787)** <span class="paper-meta">— Ewin Tang, John Wright (arXiv, 2025)</span>

- <span id="paper-2507-15065"></span>**[Grover's algorithm is an approximation of imaginary-time evolution](https://arxiv.org/abs/2507.15065)** <span class="paper-meta">— Yudai Suzuki et al. (arXiv, 2025)</span>

- <span id="paper-2504-02385"></span>**[Quantum singular value transformation without block encodings: Near-optimal complexity with minimal ancilla](https://arxiv.org/abs/2504.02385)** <span class="paper-meta">— Shantanav Chakraborty et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Implements QSVT through Trotter simulation with one ancilla and near-optimal complexity, avoiding block encodings.</span>

- <span id="paper-2303-11317"></span>**[Opening the Black Box Inside Grover's Algorithm](https://arxiv.org/abs/2303.11317)** <span class="paper-meta">— E. M. Stoudenmire, Xavier Waintal (Physical Review X, 2024)</span>

- <span id="paper-2105-02859"></span>**[Grand Unification of Quantum Algorithms](https://arxiv.org/abs/2105.02859)** <span class="paper-meta">— John M. Martyn et al. (PRX Quantum, 2021)</span>

<span id="optimization"></span>
### Quantum Optimization
{: #quantum-optimization}

- <span id="paper-10-4230-lipics-tqc-2026-4"></span>**[Provable Speedups in Convex Optimization via Quantum Dynamics](https://doi.org/10.4230/LIPIcs.TQC.2026.4)** <span class="paper-meta">— Shouvanik Chakrabarti et al. (TQC, 2026)</span><br>
  <span class="paper-description">Establishes quantum Hamiltonian descent query bounds, with speedups over known noise-tolerant convex optimization algorithms but no noiseless zeroth-order improvement.</span>

- <span id="paper-2504-14841"></span>**[(Sub)Exponential Quantum Speedup for Optimization](https://arxiv.org/abs/2504.14841)** <span class="paper-meta">— Jiaqi Leng et al. (arXiv, 2025)</span>

- <span id="paper-2503-12789"></span>**[Lower bounding the MaxCut of high girth 3-regular graphs using the QAOA](https://arxiv.org/abs/2503.12789)** <span class="paper-meta">— Edward Farhi et al. (arXiv, 2025)</span>

- <span id="paper-2408-08292"></span>**[Optimization by Decoded Quantum Interferometry](https://arxiv.org/abs/2408.08292)** <span class="paper-meta">— Stephen P. Jordan et al. (Nature, 2025)</span>

- <span id="paper-2401-09421"></span>**[Towards large-scale quantum optimization solvers with few qubits](https://arxiv.org/abs/2401.09421)** <span class="paper-meta">— Marco Sciorilli et al. (Nature Communications, 2025)</span>

- <span id="paper-2510-10967"></span>**[Verifiable Quantum Advantage via Optimized DQI Circuits](https://arxiv.org/abs/2510.10967)** <span class="paper-meta">— Tanuj Khattar et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Optimizes reversible Reed–Solomon decoding circuits for DQI and estimates resources for candidate verifiable quantum advantage, subject to classical-hardness assumptions.</span>

<span id="quantum-algorithms-for-nonlinear-differential-equations"></span>
### Quantum Algorithms for Linear and Nonlinear Problems
{: #quantum-algorithms-for-linear-and-nonlinear-problems}

- <span id="paper-10-1103-xysy-q3fp"></span>**[End-to-End Quantum Algorithm for Nonlinear Fluid Dynamics with Bounded Quantum Advantage](https://doi.org/10.1103/xysy-q3fp)** <span class="paper-meta">— David Jennings et al. (PRX Quantum, 2026)</span><br>
  <span class="paper-description">Develops a Carleman-based lattice-Boltzmann algorithm and bounds possible speedups, with resource estimates suggesting modest advantages for selected observables and error regimes.</span>

- <span id="paper-2507-06198"></span>**[Quantum simulation of a noisy classical nonlinear dynamics](https://arxiv.org/abs/2507.06198)** <span class="paper-meta">— Sergey Bravyi et al. (arXiv, 2025)</span>

- <span id="paper-2011-03185"></span>**[Efficient quantum algorithm for dissipative nonlinear differential equations](https://arxiv.org/abs/2011.03185)** <span class="paper-meta">— Jin-Peng Liu et al. (PNAS, 2021)</span>

<span id="quantum-simulation--many-body-methods"></span>
## Quantum Simulation & Many-Body Physics
{: #quantum-simulation-many-body-physics}

### Hamiltonian Simulation
{: #hamiltonian-simulation}

- <span id="paper-2607-19852"></span>**[Optimal Lower Bounds for Hamiltonian Simulation](https://arxiv.org/abs/2607.19852)** <span class="paper-meta">— Alexander Zlokapa, Richard R. Allen, Aram W. Harrow (arXiv, 2026)</span><br>
  <span class="paper-description">Proves matching gate and query lower bounds for sum-of-terms Hamiltonian simulation, distinguishing physical gate costs from coherent-oracle counts.</span>

- <span id="paper-2505-01528"></span>**[Quantum Simulation with Sum-of-Squares Spectral Amplification](https://arxiv.org/abs/2505.01528)** <span class="paper-meta">— Robbie King et al. (Physical Review Letters, 2026)</span><br>
  <span class="paper-description">Uses sum-of-squares decompositions to amplify low-energy spectra and reduce phase-estimation costs, including model-specific speedups.</span>

- <span id="paper-2502-13784"></span>**[Correcting and Extending Trotterized Quantum Many-Body Dynamics](https://arxiv.org/abs/2502.13784)** <span class="paper-meta">— Gian Gentinetta, Friederike Metz, Giuseppe Carleo (PRX Quantum, 2025)</span>

- <span id="paper-2209-12653"></span>**[Making Trotterization adaptive and energy-self-correcting for NISQ devices and beyond](https://arxiv.org/abs/2209.12653)** <span class="paper-meta">— Hongzheng Zhao et al. (PRX Quantum, 2023)</span>

- <span id="paper-1912-08854"></span>**[Theory of Trotter Error with Commutator Scaling](https://arxiv.org/abs/1912.08854)** <span class="paper-meta">— Andrew M. Childs et al. (Physical Review X, 2021)</span>

### Quantum Chemistry and Molecular Simulation
{: #quantum-chemistry-and-molecular-simulation}

- <span id="paper-2504-06348"></span>**[A comprehensive framework to simulate real-time chemical dynamics on a fault-tolerant quantum computer](https://arxiv.org/abs/2504.06348)** <span class="paper-meta">— Felipe H. da Jornada et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Combines pseudoion Hamiltonians, state preparation, observable estimation, and logical resource estimates for fault-tolerant chemical dynamics.</span>

- <span id="paper-2409-11748"></span>**[Rapid initial state preparation for the quantum simulation of strongly correlated molecules](https://arxiv.org/abs/2409.11748)** <span class="paper-meta">— Dominic W. Berry et al. (PRX Quantum, 2025)</span>

<span id="analog--digital-analog-quantum-computation"></span>
### Analog and Digital-Analog Quantum Simulation
{: #analog-and-digital-analog-quantum-simulation}

- <span id="paper-2308-12040"></span>**[Digital-analog quantum computing of fermion-boson models in superconducting circuits](https://arxiv.org/abs/2308.12040)** <span class="paper-meta">— Shubham Kumar et al. (npj Quantum Information, 2025)</span>

- <span id="paper-2405-17385"></span>**[Thermalization and criticality on an analogue–digital quantum simulator](https://arxiv.org/abs/2405.17385)** <span class="paper-meta">— T. I. Andersen et al. (Nature, 2025)</span>

- <span id="paper-2212-04924"></span>**[Quantum advantage and stability to errors in analogue quantum simulators](https://arxiv.org/abs/2212.04924)** <span class="paper-meta">— Rahul Trivedi, Adrian Franco Rubio, J. Ignacio Cirac (Nature Communications, 2024)</span>

- <span id="paper-10-1038-s41586-022-04940-6"></span>**[Practical quantum advantage in quantum simulation](https://www.nature.com/articles/s41586-022-04940-6)** <span class="paper-meta">— Andrew J. Daley et al. (Nature, 2022)</span>

### Many-Body Dynamics and Simulation Algorithms
{: #many-body-dynamics-and-simulation-algorithms}

- <span id="paper-2506-10191"></span>**[Constructive interference at the edge of quantum ergodic dynamics](https://arxiv.org/abs/2506.10191)** <span class="paper-meta">— Dmitry A. Abanin et al. (arXiv, 2025)</span>

- <span id="paper-2501-09702"></span>**[Quantum-Centric Algorithm for Sample-Based Krylov Diagonalization](https://arxiv.org/abs/2501.09702)** <span class="paper-meta">— Jeffery Yu et al. (arXiv, 2025)</span>

## Dissipative Quantum Algorithms & Open Systems
{: #dissipative-quantum-algorithms-open-systems}

### Quantum Gibbs Sampling
{: #quantum-gibbs-sampling}

- <span id="paper-2510-04954"></span>**[Rapid Mixing of Quantum Gibbs Samplers for Weakly-Interacting Quantum Systems](https://arxiv.org/abs/2510.04954)** <span class="paper-meta">— Štěpán Šmíd et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Proves polylogarithmic mixing bounds for specified Gibbs-sampler Lindbladians in free and controlled interacting regimes.</span>

- <span id="paper-2405-20322"></span>**[Quantum generalizations of Glauber and Metropolis dynamics](https://arxiv.org/abs/2405.20322)** <span class="paper-meta">— András Gilyén et al. (arXiv, 2024)</span>

### Ground-State and Thermal-State Preparation
{: #ground-state-and-thermal-state-preparation}

- <span id="paper-2503-15827"></span>**[Rapid quantum ground state preparation via dissipative dynamics](https://arxiv.org/abs/2503.15827)** <span class="paper-meta">— Yongtao Zhan et al. (Physical Review X, 2026)</span>

- <span id="paper-2508-05703"></span>**[Simple and efficient end-to-end quantum thermal and ground state preparation](https://arxiv.org/abs/2508.05703)** <span class="paper-meta">— Zhiyan Ding et al. (Nature Physics, 2026)</span>

- <span id="paper-2505-21308"></span>**[Dissipative Preparation of Many-Body Quantum States: Towards Practical Quantum Advantage](https://arxiv.org/abs/2505.21308)** <span class="paper-meta">— Lin Lin (APL Computational Physics, 2025)</span>

- <span id="paper-2309-16596"></span>**[Local minima in quantum systems](https://arxiv.org/abs/2309.16596)** <span class="paper-meta">— Chi-Fang Chen et al. (Nature Physics, 2025)</span>

- <span id="paper-2507-02043"></span>**[Scaling Quantum Algorithms via Dissipation: Avoiding Barren Plateaus](https://arxiv.org/abs/2507.02043)** <span class="paper-meta">— Elias Zapusek, Ivan Rojkov, Florentin Reiter (arXiv, 2025)</span>

- <span id="paper-2308-15676"></span>**[Single-ancilla ground state preparation via Lindbladians](https://arxiv.org/abs/2308.15676)** <span class="paper-meta">— Zhiyan Ding, Chi-Fang Chen, Lin Lin (Physical Review Research, 2024)</span>

- <span id="paper-1901-07653"></span>**[Determining eigenstates and thermal states on a quantum computer using quantum imaginary time evolution](https://arxiv.org/abs/1901.07653)** <span class="paper-meta">— Mario Motta et al. (Nature Physics, 2020)</span>

<span id="learning-open-quantum-systems"></span>
### Learning and Characterizing Open Quantum Systems
{: #learning-and-characterizing-open-quantum-systems}

- <span id="paper-2606-18188"></span>**[Learning Arbitrary Lindbladians with Quantum Error Correction](https://arxiv.org/abs/2606.18188)** <span class="paper-meta">— Nikita Romanov et al. (arXiv, 2026)</span><br>
  <span class="paper-description">Uses error-correcting codes to learn sparse Lindbladians without known supports, attaining Heisenberg scaling for noise-unobscured Hamiltonian components and standard-quantum-limit scaling for full reconstruction.</span>

- <span id="paper-2606-30358"></span>**[Learning the structure of open quantum systems](https://arxiv.org/abs/2606.30358)** <span class="paper-meta">— Laura Lewis, Ewin Tang, John Wright (arXiv, 2026)</span><br>
  <span class="paper-description">Learns constant-local Lindbladian coefficients with randomized Pauli measurements without known interaction structure, with parameter-optimal bounds up to logarithmic factors.</span>

<span id="state-learning-testing-and-tomography"></span>
<span id="quantum-machine-learning"></span>
## Quantum Learning, Tomography & Machine Learning
{: #quantum-learning-tomography-machine-learning}

<span id="state-learning-i-classical-shadows"></span>
### Classical Shadows and Shadow Tomography
{: #classical-shadows-and-shadow-tomography}

- <span id="paper-2402-17911"></span>**[Demonstration of Robust and Efficient Quantum Property Learning with Shallow Shadows](https://arxiv.org/abs/2402.17911)** <span class="paper-meta">— Hong-Ye Hu et al. (Nature Communications, 2025)</span>

- <span id="paper-2404-19211"></span>**[Triply efficient shadow tomography](https://arxiv.org/abs/2404.19211)** <span class="paper-meta">— Robbie King et al. (PRX Quantum, 2025)</span>

- <span id="paper-2404-19105"></span>**[Optimal tradeoffs for estimating Pauli observables](https://arxiv.org/abs/2404.19105)** <span class="paper-meta">— Sitan Chen, Weiyuan Gong, Qi Ye (FOCS, 2024)</span>

- <span id="paper-2002-08953"></span>**[Predicting many properties of a quantum system from very few measurements](https://arxiv.org/abs/2002.08953)** <span class="paper-meta">— Hsin-Yuan Huang, Richard Kueng, John Preskill (Nature Physics, 2020)</span>

<span id="state-testing"></span>
### Quantum State Learning and Certification
{: #quantum-state-learning-and-certification}

- <span id="paper-2506-19809"></span>**[Universal and Efficient Quantum State Verification via Schmidt Decomposition and Mutually Unbiased Bases](https://arxiv.org/abs/2506.19809)** <span class="paper-meta">— Yunting Li, Huangjun Zhu (Quantum, 2026)</span>

- <span id="paper-2404-07281"></span>**[Certifying almost all quantum states with few single-qubit measurements](https://arxiv.org/abs/2404.07281)** <span class="paper-meta">— Hsin-Yuan Huang, John Preskill, Mehdi Soleimanifar (Nature Physics, 2025)</span>

- <span id="paper-2506-11355"></span>**[Few Single-Qubit Measurements Suffice to Certify Any Quantum State](https://arxiv.org/abs/2506.11355)** <span class="paper-meta">— Meghal Gupta, William He, Ryan O'Donnell (arXiv, 2025)</span><br>
  <span class="paper-description">Certifies arbitrary pure target states using adaptive single-qubit measurements and proves an exponential copy-complexity lower bound for nonadaptive protocols.</span>

- <span id="paper-2204-13691"></span>**[Foundations for learning from noisy quantum experiments](https://arxiv.org/abs/2204.13691)** <span class="paper-meta">— Hsin-Yuan Huang, Steven T. Flammia, John Preskill (arXiv, 2022)</span>

<span id="state-learning-ii-qram"></span>
### Quantum Learning Theory and Complexity
{: #quantum-learning-theory-and-complexity}

- <span id="paper-2505-22743"></span>**[Information-Computation Gaps in Quantum Learning via Low-Degree Likelihood](https://arxiv.org/abs/2505.22743)** <span class="paper-meta">— Sitan Chen et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Extends low-degree likelihood methods to quantum learning, giving restricted-model hardness results and evidence for information–computation gaps.</span>

- <span id="paper-2305-20069"></span>**[A survey on the complexity of learning quantum states](https://arxiv.org/abs/2305.20069)** <span class="paper-meta">— Anurag Anshu, Srinivasan Arunachalam (Nature Reviews Physics, 2024)</span>

- <span id="paper-2111-05881"></span>**[Exponential Separations Between Learning With and Without Quantum Memory](https://arxiv.org/abs/2111.05881)** <span class="paper-meta">— Sitan Chen et al. (FOCS, 2022)</span>

### Quantum Machine Learning and Generative Models
{: #quantum-machine-learning-and-generative-models}

- <span id="paper-2512-19819"></span>**[Fundamentals of quantum Boltzmann machine learning with visible and hidden units](https://arxiv.org/abs/2512.19819)** <span class="paper-meta">— Mark M. Wilde (arXiv, 2025)</span><br>
  <span class="paper-description">Derives relative-entropy gradients and quantum gradient-estimation algorithms for quantum Boltzmann machines with visible and hidden units.</span>

- <span id="paper-2305-13362"></span>**[On quantum backpropagation, information reuse, and cheating measurement collapse](https://arxiv.org/abs/2305.13362)** <span class="paper-meta">— Amira Abbas et al. (NeurIPS, 2023)</span>

<span id="backpropagation-ml-qml"></span>
### Classical Machine-Learning Foundations
{: #classical-machine-learning-foundations}

- <span id="paper-chap2-html"></span>**[How the backpropagation algorithm works](http://neuralnetworksanddeeplearning.com/chap2.html)** <span class="paper-meta">— Michael A. Nielsen (Neural Networks and Deep Learning, Ch. 2, 2015)</span>

- <span id="paper-10-1109-ijcnn-1989-118638"></span>**[Theory of the backpropagation neural network](https://ieeexplore.ieee.org/document/118638/)** <span class="paper-meta">— Hecht-Nielsen (IJCNN, 1989)</span>

- <span id="paper-10-1038-323533a0"></span>**[Learning representations by back-propagating errors](https://www.nature.com/articles/323533a0)** <span class="paper-meta">— David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams (Nature, 1986)</span>

<span id="complexity--quantum-advantage"></span>
## Quantum Complexity & Computational Advantage
{: #quantum-complexity-computational-advantage}

<span id="complexity"></span>
### Quantum Complexity Classes and Circuit Complexity
{: #quantum-complexity-classes-and-circuit-complexity}

- <span id="paper-2609-13032"></span>**[QMA has perfect completeness](https://arxiv.org/abs/2609.13032)** <span class="paper-meta">— Sabee Grewal, Dorian Rudolph (arXiv, 2026)</span><br>
  <span class="paper-description">Proves QMA = QMA₁ using Hadamard, Toffoli, and X gates, implying QMA-completeness of quantum 3-SAT.</span>

- <span id="paper-2508-08852"></span>**[A Brief Introduction to Quantum Query Complexity](https://arxiv.org/abs/2508.08852)** <span class="paper-meta">— Yassine Hamoudi (arXiv, 2025)</span>

- <span id="paper-2510-04411"></span>**[Quantum precomputation: parallelizing cascade circuits and the Moore-Nilsson conjecture is false](https://arxiv.org/abs/2510.04411)** <span class="paper-meta">— Adam Bene Watts et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Constructs exact, ancilla-free logarithmic-depth implementations of controlled-unitary staircase circuits, refuting the Moore–Nilsson depth conjecture in this model.</span>

<span id="quantum-advantage"></span>
### Quantum Advantage and Computational Separations
{: #quantum-advantage-and-computational-separations}

- <span id="paper-2604-07639"></span>**[Exponential quantum advantage in processing massive classical data](https://arxiv.org/abs/2604.07639)** <span class="paper-meta">— Haimeng Zhao et al. (arXiv, 2026)</span><br>
  <span class="paper-description">Proves quantum–classical memory and sample/time separations for classical-data learning via quantum oracle sketching, with separate empirical evidence on real-world datasets.</span> <span class="paper-note">Discussed 2026-05-19.</span>

- <span id="paper-2506-20658"></span>**[A Framework for Quantum Advantage](https://arxiv.org/abs/2506.20658)** <span class="paper-meta">— Olivia Lanes et al. (arXiv, 2025)</span>

- <span id="paper-2509-07255"></span>**[Demonstrating an unconditional separation between quantum and classical information resources](https://arxiv.org/abs/2509.07255)** <span class="paper-meta">— William Kretschmer et al. (arXiv, 2025)</span>

- <span id="paper-2508-05720"></span>**[The vast world of quantum advantage](https://arxiv.org/abs/2508.05720)** <span class="paper-meta">— Hsin-Yuan Huang et al. (arXiv, 2025)</span>

- <span id="paper-2208-02199"></span>**[Evaluating the evidence for exponential quantum advantage in ground-state quantum chemistry](https://arxiv.org/abs/2208.02199)** <span class="paper-meta">— Seunghoon Lee et al. (Nature Communications, 2023)</span>

- <span id="paper-quant-ph-9701001"></span>**[Strengths and Weaknesses of Quantum Computing](https://arxiv.org/abs/quant-ph/9701001)** <span class="paper-meta">— Charles H. Bennett et al. (SIAM Journal on Computing, 1997)</span>

<span id="nonlocal-games--interactive-proofs"></span>
### Interactive Proofs and Nonlocal Games
{: #interactive-proofs-and-nonlocal-games}

- <span id="paper-2410-23969"></span>**[Interactive proofs for verifying (quantum) learning and testing](https://arxiv.org/abs/2410.23969)** <span class="paper-meta">— Matthias C. Caro et al. (arXiv, 2024)</span>

- <span id="paper-2311-01363"></span>**[Application-level Benchmarking of Quantum Computers using Nonlocal Game Strategies](https://arxiv.org/abs/2311.01363)** <span class="paper-meta">— Jim Furches et al. (arXiv, 2023)</span>

## Classical Simulability, Entanglement & Randomness
{: #classical-simulability-entanglement-randomness}

<span id="tensor-networks-for-quantum-computing"></span>
### Classical Simulation and Tensor Networks
{: #classical-simulation-and-tensor-networks}

- <span id="paper-2607-08396"></span>**[Efficiently simulable quantum circuits with large entanglement, magic, and non-Gaussianity via code-compiled tensor networks](https://arxiv.org/abs/2607.08396)** <span class="paper-meta">— Aydin Deger et al. (arXiv, 2026)</span><br>
  <span class="paper-description">Constructs code-compiled circuit families with large entanglement, magic, and non-Gaussianity that remain efficiently simulable when encoded inputs have efficient matrix-product-state representations.</span>

- <span id="paper-2506-02105"></span>**[Learning Circuits with Infinite Tensor Networks](https://arxiv.org/abs/2506.02105)** <span class="paper-meta">— Joe Gibbs, Lukasz Cincio (arXiv, 2025)</span>

- <span id="paper-2503-04423"></span>**[Tensor Network Techniques for Quantum Computation](https://arxiv.org/abs/2503.04423)** <span class="paper-meta">— Mario Collura et al. (arXiv, 2025)</span>

- <span id="paper-2503-08626"></span>**[Tensor networks for quantum computing](https://arxiv.org/abs/2503.08626)** <span class="paper-meta">— Aleksandr Berezutskii et al. (Nature Reviews Physics, 2025)</span>

- <span id="paper-1008-3477"></span>**[The density-matrix renormalization group in the age of matrix product states](https://arxiv.org/abs/1008.3477)** <span class="paper-meta">— Ulrich Schollwöck (Annals of Physics, 2011)</span> <span class="paper-note">(introductory DMRG reference)</span>

### Entanglement and Simulation Complexity
{: #entanglement-and-simulation-complexity}

- <span id="paper-2509-12014"></span>**[Spectral Small-Incremental-Entangling: Breaking Quasi-Polynomial Complexity Barriers in Long-Range Interacting Systems](https://arxiv.org/abs/2509.12014)** <span class="paper-meta">— Donghoon Kim et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Proves spectral bounds on Rényi entanglement growth and tensor-network approximation guarantees for specified one-dimensional long-range systems, with an adiabatic-path condition for its generalized area law.</span>

- <span id="paper-2408-15699"></span>**[Strongly interacting fermions are non-trivial yet non-glassy](https://arxiv.org/abs/2408.15699)** <span class="paper-meta">— Eric R. Anschuetz et al. (arXiv, 2024)</span>

<span id="random-unitaries-unitary-designs--pseudorandom-unitaries"></span>
### Pseudorandomness and Unitary Designs
{: #pseudorandomness-and-unitary-designs}

- <span id="paper-2508-11487"></span>**[Random Unitaries in Constant (Quantum) Time](https://arxiv.org/abs/2508.11487)** <span class="paper-meta">— Ben Foxman et al. (ITCS, 2026)</span>

- <span id="paper-2407-07754"></span>**[Random unitaries in extremely low depth](https://arxiv.org/abs/2407.07754)** <span class="paper-meta">— Thomas Schuster, Jonas Haferkamp, Hsin-Yuan Huang (Science, 2025)</span>

- <span id="paper-2504-14005"></span>**[Short remarks on shallow unitary circuits](https://arxiv.org/abs/2504.14005)** <span class="paper-meta">— Jeongwan Haah (Quantum, 2025)</span>

- <span id="paper-2509-26310"></span>**[Strong random unitaries and fast scrambling](https://arxiv.org/abs/2509.26310)** <span class="paper-meta">— Thomas Schuster et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Defines stronger random-unitary notions allowing inverse, conjugate, and transpose queries and gives fast-scrambling circuit constructions.</span>

- <span id="paper-2507-06216"></span>**[Unitary designs in nearly optimal depth](https://arxiv.org/abs/2507.06216)** <span class="paper-meta">— Laura Cui et al. (arXiv, 2025)</span>

### Pseudoentanglement
{: #pseudoentanglement}

- <span id="paper-2403-09619"></span>**[Dynamics of Pseudoentanglement](https://arxiv.org/abs/2403.09619)** <span class="paper-meta">— Xiaozhou Feng, Matteo Ippoliti (Journal of High Energy Physics, 2025)</span>

- <span id="paper-10-1103-7p1r-r2p6"></span>**[Pseudoentanglement from Tensor Networks](https://journals.aps.org/prl/abstract/10.1103/7p1r-r2p6)** <span class="paper-meta">— Zihan Cheng, Xiaozhou Feng, Matteo Ippoliti (Physical Review Letters, 2025)</span>

- <span id="paper-2211-00747"></span>**[Quantum Pseudoentanglement](https://arxiv.org/abs/2211.00747)** <span class="paper-meta">— Scott Aaronson et al. (ITCS, 2024)</span>

<span id="quantum-computing-models--architecture"></span>
## Quantum Computing Architectures & Fault Tolerance
{: #quantum-computing-architectures-fault-tolerance}

<span id="from-noisy-to-fault-tolerant"></span>
### Fault Tolerance, Error Correction, and Compilation
{: #fault-tolerance-error-correction-and-compilation}

- <span id="paper-2502-16132"></span>**[A Constant Rate Quantum Computer on a Line](https://arxiv.org/abs/2502.16132)** <span class="paper-meta">— Craig Gidney, Thiago Bergamaschi (arXiv, 2025)</span><br>
  <span class="paper-description">Constructs a nearest-neighbor one-dimensional fault-tolerant architecture with constant coding rate, quasi-polylogarithmic time overhead, and a proved threshold.</span>

- <span id="paper-2510-07223"></span>**[Multi-qubit Toffoli with exponentially fewer T gates](https://arxiv.org/abs/2510.07223)** <span class="paper-meta">— David Gosset, Robin Kothari, Chenyi Zhang (arXiv, 2025)</span><br>
  <span class="paper-description">Approximates multi-qubit Toffoli channels with randomized Clifford+T circuits using O(log(1/ε)) T gates, while proving a linear lower bound for purely unitary constant-error implementations.</span>

- <span id="paper-2004-11893"></span>**[Using Quantum Metrological Bounds in Quantum Error Correction: A Simple Proof of the Approximate Eastin-Knill Theorem](https://arxiv.org/abs/2004.11893)** <span class="paper-meta">— Aleksander Kubica, Rafał Demkowicz-Dobrzański (Physical Review Letters, 2021)</span>

<span id="quantum-memory"></span>
### Hardware Platforms and Quantum Memory
{: #hardware-platforms-and-quantum-memory}

- <span id="paper-2408-16794"></span>**[A quantum random access memory (QRAM) using a polynomial encoding of binary strings](https://arxiv.org/abs/2408.16794)** <span class="paper-meta">— Priyanka Mukhopadhyay (Scientific Reports, 2025)</span>

- <span id="paper-2508-19075"></span>**[Universal Dynamics with Globally Controlled Analog Quantum Simulators](https://arxiv.org/abs/2508.19075)** <span class="paper-meta">— Hong-Ye Hu et al. (arXiv, 2025)</span><br>
  <span class="paper-description">Establishes universality conditions for globally controlled analog simulators and tests synthesized effective interactions on a Rydberg-atom platform.</span>

- <span id="paper-2112-03923"></span>**[A quantum processor based on coherent transport of entangled atom arrays](https://arxiv.org/abs/2112.03923)** <span class="paper-meta">— Dolev Bluvstein et al. (Nature, 2022)</span>

### Distributed Quantum Computing
{: #distributed-quantum-computing}

- <span id="paper-2411-02881"></span>**[Distributed Quantum Simulation](https://arxiv.org/abs/2411.02881)** <span class="paper-meta">— Tianfeng Feng et al. (Physical Review Letters, 2026)</span>

- <span id="paper-2502-03542"></span>**[Distributed Quantum Dynamics on Near-Term Quantum Processors](https://arxiv.org/abs/2502.03542)** <span class="paper-meta">— Vladyslav Bohun, Maxence Grandadam, Maciej Koch-Janusz (arXiv, 2025)</span>

- <span id="paper-2404-01265"></span>**[Review of Distributed Quantum Computing: From single QPU to High Performance Quantum Computing](https://arxiv.org/abs/2404.01265)** <span class="paper-meta">— David Barral et al. (Computer Science Review, 2025)</span>

- <span id="paper-2402-17833"></span>**[Combining quantum processors with real-time classical communication](https://arxiv.org/abs/2402.17833)** <span class="paper-meta">— Almudena Carrera Vazquez et al. (Nature, 2024)</span>

<span id="blind-quantum-computation"></span>
<span id="quantum-programming"></span>
<span id="hybrid-continuous-variable--discrete-variable-computation"></span>
### Hybrid and Alternative Computing Models
{: #hybrid-and-alternative-computing-models}

- <span id="paper-2509-04527"></span>**[The Structure and Interpretation of Quantum Programs I: Foundations](https://arxiv.org/abs/2509.04527)** <span class="paper-meta">— David Wakeham (arXiv, 2025)</span>

- <span id="paper-2509-18854"></span>**[Trading modes against energy](https://arxiv.org/abs/2509.18854)** <span class="paper-meta">— Lukas Brenner, Beatriz Dias, Robert Koenig (arXiv, 2025)</span><br>
  <span class="paper-description">Quantifies mode–energy trade-offs for approximate weak simulation of qubit circuits in a hybrid qubit–oscillator model using high-dimensional approximate GKP encodings.</span>

- <span id="paper-1611-10107"></span>**[Private quantum computation: an introduction to blind quantum computing and related protocols](https://arxiv.org/abs/1611.10107)** <span class="paper-meta">— Joseph F. Fitzsimons (npj Quantum Information, 2017)</span>

- <span id="paper-0807-4154"></span>**[Universal Blind Quantum Computation](https://arxiv.org/abs/0807.4154)** <span class="paper-meta">— Anne Broadbent, Joseph Fitzsimons, Elham Kashefi (FOCS, 2009)</span>

</div>

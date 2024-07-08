# Hybrid Parallel Computing for the Mandelbrot Set: MPI and OpenMP Integration

## Overview

This repository contains the implementation of a hybrid MPI and OpenMP approach to compute and visualize the Mandelbrot set. The project is part of the High Performance Computing course at the Department of Mathematics and Geosciences, University of Trieste.

## Report

The full project report, titled "Hybrid Parallel Computing for the Mandelbrot Set: MPI and OpenMP Integration," can be found in the `SHAHZAD_ex2_Report.pdf` file. The report includes detailed information about the computational architecture, methodology, experiment plan, and results.

## Table of Contents

1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Methodology](#methodology)
    - [Computational Architecture](#computational-architecture)
    - [Mandelbrot Set Implementation](#mandelbrot-set-implementation)
    - [Experiment Plan](#experiment-plan)
4. [Results and Discussion](#results-and-discussion)
    - [MPI Strong Scaling](#mpi-strong-scaling)
    - [MPI Weak Scaling](#mpi-weak-scaling)
    - [OpenMP Strong Scaling](#openmp-strong-scaling)
    - [OpenMP Weak Scaling](#openmp-weak-scaling)
    - [Conclusion](#conclusion)

## Abstract

This project implements a hybrid MPI and OpenMP approach to compute and visualize the Mandelbrot set on the ORFEO high-performance computing cluster. By distributing tasks across multiple processors with MPI and using multi-threading within each processor through OpenMP, the study evaluates both strong and weak scaling. Results show that while OpenMP strong scaling plateaus due to parallel overhead, OpenMP weak scaling increases execution time proportionally with some inefficiencies. MPI strong scaling remains stable up to a point but faces communication overhead issues beyond a certain number of tasks, and MPI weak scaling reveals a non-linear increase in execution time, indicating decreasing parallel efficiency. These findings offer insights into optimizing hybrid parallel implementations for computationally intensive tasks.

## Introduction

The Mandelbrot set is a well-known fractal that serves as a benchmark for testing parallel computing strategies. Defined by the iteration of the function \( f_c(z) = z^2 + c \), where both \( z \) and \( c \) are complex numbers, the set includes points in the complex plane for which the magnitude of \( z \) remains bounded over successive iterations. This computational problem is highly suitable for parallel processing, as each point can be computed independently.

This project employs a hybrid approach using Message Passing Interface (MPI) and Open Multi-Processing (OpenMP) to efficiently compute and visualize the Mandelbrot set. By utilizing MPI for task distribution across multiple processors and OpenMP for threading within each processor, we aim to optimize the computation and reduce execution time. Our performance evaluation includes both strong and weak scaling experiments conducted on the ORFEO high-performance computing cluster.

## Methodology

### Computational Architecture

The project utilizes the ORFEO cluster, particularly the THIN partition, which consists of nodes equipped with Intel Xeon Gold CPUs, each with 12 cores. The nodes are interconnected via a high-speed network, allowing efficient data transfer. This setup supports both MPI for distributed memory parallelism and OpenMP for shared memory parallelism, providing a robust environment for hybrid parallel computing.

### Mandelbrot Set Implementation

The Mandelbrot set is computed and visualized using a hybrid MPI and OpenMP approach. Each point in the complex plane is computed independently, making it suitable for parallel processing. The implementation involves:
1. **MPI Parallelization**: Distributing the workload across multiple processes, each handling a section of the complex plane.
2. **OpenMP Parallelization**: Further dividing the workload within each process among multiple threads.

The core components include:
- `mandelbrot` function: Determines if a point belongs to the Mandelbrot set by iterating the function \( f_c(z) = z^2 + c \).
- `write_pgm_image` function: Generates a PGM image from the computed matrix representing the Mandelbrot set.
- `Main` function: Coordinates the computation by parsing command-line arguments, initializing MPI, distributing tasks, and gathering results.

### Experiment Plan

The experiments are designed to evaluate both strong and weak scaling:
1. **Strong Scaling**: Keeping the problem size constant while varying the number of processing units to measure how the solution time decreases.
2. **Weak Scaling**: Increasing both the problem size and the number of processing units proportionally to measure how the solution time changes.

Scripts used:
- `strong_scaling_openmp.sh`: Evaluates performance by increasing the number of OpenMP threads with a single MPI task.
- `strong_scaling_mpi.sh`: Assesses performance by increasing the number of MPI tasks with one OpenMP thread per task.
- `weak_scaling_openmp.sh`: Examines performance by scaling the problem size with the number of OpenMP threads.
- `weak_scaling_mpi.sh`: Evaluates performance by scaling the problem size with the number of MPI tasks.

## Results and Discussion

### MPI Strong Scaling

The strong scaling plot for MPI shows a non-monotonic relationship between execution time and the number of MPI tasks. Initially, the execution time decreases as the number of tasks increases, indicating effective load distribution and parallel efficiency. However, after a certain point, the execution time increases sharply, suggesting communication overhead and synchronization issues start to dominate, reducing the efficiency gains. At the highest number of tasks, the execution time decreases again, likely due to an optimized use of available resources or a reduction in task contention. These fluctuations highlight the need for careful balancing between computational load and communication overhead in MPI applications.

### MPI Weak Scaling

The weak scaling results for MPI reveal a steady increase in execution time as the number of MPI tasks and the problem size both grow. This linear increase suggests that the MPI implementation scales proportionally with the problem size, but the increase in execution time indicates that communication overhead and synchronization costs rise with the number of tasks. The non-linear segments in the graph further emphasize inefficiencies that might be due to uneven load distribution or increased latency in communication as more nodes are involved. This trend underscores the challenges in maintaining parallel efficiency when scaling up both tasks and problem size in MPI.

### OpenMP Strong Scaling

For OpenMP strong scaling, the execution time significantly drops as the number of threads increases, showing the benefits of parallel computation. The execution time plateaus after reaching a certain number of threads, which indicates that additional threads beyond this point do not contribute to further performance gains. This plateau is likely due to factors such as memory bandwidth limitations or increased overhead from managing a larger number of threads. The initial rapid decrease in execution time suggests that OpenMP effectively utilizes the multi-core architecture up to an optimal thread count.

### OpenMP Weak Scaling

The OpenMP weak scaling plot demonstrates a linear increase in execution time as the number of threads and the problem size both increase. This behavior indicates that while the computation scales with the number of threads, the execution time rises proportionally due to the increased workload. The linearity of the increase implies that OpenMP maintains a consistent level of parallel efficiency across different thread counts, but it also highlights that the overall computational demand grows with the problem size, thus leading to longer execution times.

### Conclusion

The analysis of MPI and OpenMP scaling experiments reveals critical insights into the performance characteristics of hybrid parallel computing. MPI strong scaling shows varying efficiency with different task counts, emphasizing the importance of balancing load distribution and communication overhead. MPI weak scaling indicates that communication costs become significant as both tasks and problem size increase. OpenMP strong scaling demonstrates effective use of multi-core processors up to an optimal thread count, while OpenMP weak scaling shows consistent parallel efficiency but increased computational demand with larger problem sizes. These findings highlight the complexities and trade-offs in optimizing parallel computations for high-performance computing environments. Future work should focus on refining load balancing strategies and minimizing communication overhead to enhance scalability and performance further.

## Authors

- Muhammad Mubashar Shahzad ([SM3600012])

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

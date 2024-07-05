# Analyzing the Performance of OpenMPI’s Collective Operations

## Table of Contents
- [Abstract](#abstract)
- [Introduction](#introduction)
- [Methodology](#methodology)
  - [OSU Micro-Benchmark](#osu-micro-benchmark)
  - [Algorithms](#algorithms)
  - [Mapping](#mapping)
  - [Test Parameters](#test-parameters)
- [Performance Model](#performance-model)
- [Results and Discussion](#results-and-discussion)
  - [Broadcast Operation](#broadcast-operation)
  - [Reduce Operation](#reduce-operation)
- [Conclusion](#conclusion)
- [Author Information](#author-information)

## Abstract
This report investigates the performance of OpenMPI collective operations, specifically focusing on broadcast and reduce functions. Using the OSU Micro-Benchmark tool, various algorithms such as binary tree, chain, pipeline, binomial, rabenseifner, and ignore were evaluated under different parameters like message size, number of processes, and number of cores. Experiments conducted on the EPYC partition of the ORFEO high-performance computing cluster revealed that the binary tree and binomial algorithms consistently outperformed others for large message sizes due to their efficient distribution methods. Conversely, the chain algorithm showed poor scalability with increasing message sizes. These findings are supported by linear model analysis, providing insights into optimizing parallel applications using MPI.

## Introduction
In high-performance computing (HPC), optimizing the efficiency and performance of parallel processing libraries is crucial. This study evaluates the performance of OpenMPI collective operations, particularly the broadcast and reduce functions. The experiments aim to provide insights into the most efficient strategies for different scenarios, enhancing the performance of parallel applications.

### Background and Objectives
OpenMPI is a widely used library for parallel computing, offering various algorithms for collective operations. This study focuses on:
- Evaluating the default OpenMPI implementations of broadcast and reduce operations.
- Comparing the performance of different algorithms, including binary tree, pipeline, chain, binomial, and rabenseifner.
- Analyzing the impact of different message sizes and the number of processes.
- Investigating the effect of process mapping strategies on latency.

## Methodology
The experiments were conducted on the EPYC partition of the ORFEO cluster, utilizing AMD EPYC 7H12 processors with 256 cores. The OSU Micro-Benchmarks were employed to evaluate the performance of broadcast and reduce operations under different configurations.

### OSU Micro-Benchmark
OMB provides benchmarks for a range of MPI blocking collective operations. This study focuses on the average latency for broadcast and reduce operations across various message sizes.

### Algorithms
The research evaluates multiple OpenMPI algorithms:
- **Binary Tree**: Hierarchical structure for efficient scalability.
- **Ignore**: Baseline algorithm for comparison.
- **Pipeline**: Segments data for improved performance with larger messages.
- **Chain**: Sequential data transmission suitable for specific configurations.
- **Binomial**: Balances communication and computation, effective for medium-sized clusters.
- **Linear**: Direct communication between neighboring processes.
- **Rabenseifner**: Combines recursive doubling with reduce-scatter techniques for large systems.

### Mapping
The study analyzed the impact of process mapping strategies, such as core mapping, to identify optimal configurations for minimizing latency.

### Test Parameters
Experiments varied the number of cores from 1 to 128 per node, with message sizes ranging from 1 byte to 218 bytes.

## Performance Model
Linear regression was used to model the relationship between input variables and latency. The general form of the linear regression equation is:
\[ y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots + \beta_px_p + \epsilon \]

### Model Implementation
The general equation for latency (L) as a function of the number of processes (P) is:
\[ L = 1.2175 + 0.0094 \times P \]

## Results and Discussion
### Broadcast Operation
- The pipeline algorithm showed the best performance with consistent, low-latency profiles.
- Ignore and binary tree algorithms had stable and predictable performance.
- The chain algorithm had a significant spike in latency around 190-200 cores.

### Reduce Operation
- The linear algorithm performed well with higher core counts after a notable peak.
- The ignore algorithm provided consistent low latency.
- The binomial algorithm maintained stable and low latency.
- The rabenseifner algorithm showed higher latency peaks, particularly with intermediate core counts.

## Conclusion
The study provides a comprehensive analysis of OpenMPI's collective operations, offering insights into the performance characteristics of different algorithms. The findings help identify optimal configurations and strategies for various HPC scenarios, ultimately improving application performance using OpenMPI.

## Author Information
**Author**: Muhammad Mubashar Shahzad

**Course**: High Performance Computing

**Institution**: Department of Mathematics and Geosciences, University of Trieste

**Year**: 2024

---

Please refer to the full report for detailed data, figures, and further discussion.

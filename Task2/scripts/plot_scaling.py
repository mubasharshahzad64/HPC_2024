import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files
omp_strong = pd.read_csv('../results/strong_scaling_openmp.csv')
omp_weak = pd.read_csv('../results/weak_scaling_openmp.csv')
mpi_strong = pd.read_csv('../results/strong_scaling_mpi.csv')
mpi_weak = pd.read_csv('../results/weak_scaling_mpi.csv')

# Plot OpenMP strong scaling
plt.figure()
plt.plot(omp_strong['OMP_Threads'], omp_strong['Elapsed_Time'], marker='o')
plt.title('OpenMP Strong Scaling')
plt.xlabel('Number of OpenMP Threads')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('../images/openmp_strong_scaling.png')

# Plot OpenMP weak scaling
plt.figure()
plt.plot(omp_weak['OMP_Threads'], omp_weak['Elapsed_Time'], marker='o')
plt.title('OpenMP Weak Scaling')
plt.xlabel('Number of OpenMP Threads')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('../images/openmp_weak_scaling.png')

# Plot MPI strong scaling
plt.figure()
plt.plot(mpi_strong['MPI_Tasks'], mpi_strong['Elapsed_Time'], marker='o')
plt.title('MPI Strong Scaling')
plt.xlabel('Number of MPI Tasks')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('../images/mpi_strong_scaling.png')

# Plot MPI weak scaling
plt.figure()
plt.plot(mpi_weak['MPI_Tasks'], mpi_weak['Elapsed_Time'], marker='o')
plt.title('MPI Weak Scaling')
plt.xlabel('Number of MPI Tasks')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.savefig('../images/mpi_weak_scaling.png')

plt.show()


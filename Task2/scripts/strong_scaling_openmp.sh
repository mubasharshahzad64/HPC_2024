#!/bin/bash
#SBATCH --job-name=mandelbrot_strong_omp
#SBATCH --output=strong_scaling_openmp_output.txt
#SBATCH --error=strong_scaling_openmp_error.txt
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=02:00:00
#SBATCH --partition=THIN

module load openMPI/4.1.5/gnu/

# Navigate to the source directory and compile the program
cd ../src
mpicc -fopenmp -o mandelbrot main.c mandelbrot.c -lm

# Navigate back to the scripts directory
cd ../scripts

sizes=(1 2 4 8 16 32 64 128)
csv_file="../results/strong_scaling_openmp.csv"

# Create CSV file and add headers
echo "OMP_Threads,Elapsed_Time" > $csv_file

for omp_threads in "${sizes[@]}"; do
    export OMP_NUM_THREADS=$omp_threads
    elapsed_time=$(srun --mpi=pmix ../src/mandelbrot 1024 1024 -2.0 -2.0 2.0 2.0 255 ../images/mandelbrot_omp_strongscaling_${omp_threads}.pgm | grep "Elapsed time" | awk '{print $3}')
    echo "${omp_threads},${elapsed_time}" >> $csv_file
done


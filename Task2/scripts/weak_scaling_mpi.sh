#!/bin/bash
#SBATCH --job-name=mandelbrot_weak_mpi
#SBATCH --output=weak_scaling_mpi_output.txt
#SBATCH --error=weak_scaling_mpi_error.txt
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
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
csv_file="../results/weak_scaling_mpi.csv"

# Create CSV file and add headers
echo "MPI_Tasks,Elapsed_Time" > $csv_file

for mpi_tasks in "${sizes[@]}"; do
    side=$((1024 * mpi_tasks))
    elapsed_time=$(srun --mpi=pmix -n $mpi_tasks ../src/mandelbrot $side $side -2.0 -2.0 2.0 2.0 255 ../images/mandelbrot_mpi_weakscaling_${mpi_tasks}.pgm | grep "Elapsed time" | awk '{print $3}')
    echo "${mpi_tasks},${elapsed_time}" >> $csv_file
done


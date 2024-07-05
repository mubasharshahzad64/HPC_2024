#include <mpi.h>
#include <omp.h>
#include <stdlib.h>
#include <stdio.h>
#include <complex.h>
#include <time.h>
#include "mandelbrot.h"

int main(int argc, char *argv[]) {
    MPI_Init(&argc, &argv);
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    if (argc != 9) {
        if (rank == 0) {
            fprintf(stderr, "Usage: %s n_x n_y x_L y_L x_R y_R I_max output_file\n", argv[0]);
        }
        MPI_Finalize();
        return EXIT_FAILURE;
    }

    int n_x = atoi(argv[1]);
    int n_y = atoi(argv[2]);
    double x_L = atof(argv[3]);
    double y_L = atof(argv[4]);
    double x_R = atof(argv[5]);
    double y_R = atof(argv[6]);
    int I_max = atoi(argv[7]);
    const char *output_file = argv[8];

    double dx = (x_R - x_L) / n_x;
    double dy = (y_R - y_L) / n_y;

    int local_n_y = n_y / size;
    int start_y = rank * local_n_y;
    int end_y = (rank + 1) * local_n_y;

    unsigned short *local_data = (unsigned short *)malloc(n_x * local_n_y * sizeof(unsigned short));
    if (!local_data) {
        fprintf(stderr, "Failed to allocate memory for local_data\n");
        MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
    }

    // Start timing
    double start_time = MPI_Wtime();

    #pragma omp parallel for
    for (int j = start_y; j < end_y; ++j) {
        for (int i = 0; i < n_x; ++i) {
            double x = x_L + i * dx;
            double y = y_L + j * dy;
            double complex c = x + y * I;
            local_data[(j - start_y) * n_x + i] = (unsigned short)mandelbrot(c, I_max);
        }
    }

    // End timing
    double end_time = MPI_Wtime();
    double elapsed_time = end_time - start_time;

    if (rank == 0) {
        unsigned short *global_data = (unsigned short *)malloc(n_x * n_y * sizeof(unsigned short));
        if (!global_data) {
            fprintf(stderr, "Failed to allocate memory for global_data\n");
            free(local_data);
            MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
        }
        MPI_Gather(local_data, local_n_y * n_x, MPI_UNSIGNED_SHORT, global_data, local_n_y * n_x, MPI_UNSIGNED_SHORT, 0, MPI_COMM_WORLD);
        write_pgm(output_file, global_data, n_x, n_y, I_max);
        free(global_data);
        // Output elapsed time
        printf("Elapsed time: %f seconds\n", elapsed_time);
    } else {
        MPI_Gather(local_data, local_n_y * n_x, MPI_UNSIGNED_SHORT, NULL, 0, MPI_UNSIGNED_SHORT, 0, MPI_COMM_WORLD);
    }

    free(local_data);
    MPI_Finalize();
    return EXIT_SUCCESS;
}


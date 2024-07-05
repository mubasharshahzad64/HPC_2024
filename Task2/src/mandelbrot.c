#include "mandelbrot.h"
#include <math.h>
#include <stdlib.h>

int mandelbrot(double complex c, int max_iter) {
    double complex z = 0;
    for (int n = 0; n < max_iter; ++n) {
        if (cabs(z) > 2.0) return n;
        z = z * z + c;
    }
    return max_iter;
}

void write_pgm(const char *filename, const unsigned short *data, int width, int height, int max_val) {
    FILE *fp = fopen(filename, "wb");
    if (!fp) {
        fprintf(stderr, "Failed to open file %s for writing\n", filename);
        return;
    }
    fprintf(fp, "P5\n%d %d\n255\n", width, height);
    unsigned char *pgm_data = (unsigned char *)malloc(width * height);
    if (!pgm_data) {
        fprintf(stderr, "Failed to allocate memory for pgm_data\n");
        fclose(fp);
        return;
    }
    for (int i = 0; i < width * height; ++i) {
        unsigned short value = data[i];
        unsigned char scaled_value;
        if (value == max_val) {
            scaled_value = 0;  // Points inside the Mandelbrot set are black
        } else {
            // Apply exponential scaling for better contrast
            scaled_value = (unsigned char)(255 * (1 - exp(-0.1 * value)));
        }
        pgm_data[i] = scaled_value;
    }
    fwrite(pgm_data, sizeof(unsigned char), width * height, fp);
    free(pgm_data);
    fclose(fp);
}


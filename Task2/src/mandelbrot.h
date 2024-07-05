#ifndef MANDELBROT_H
#define MANDELBROT_H

#include <complex.h>
#include <stdio.h>

int mandelbrot(double complex c, int max_iter);
void write_pgm(const char *filename, const unsigned short *data, int width, int height, int max_val);

#endif // MANDELBROT_H


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_heatmap(fig, data, operation, algo, ax):
    subset = data[(data['Operation'] == operation) & (data['ALGO_NAME'] == algo)]
    x = subset['Size']
    y = subset['NP_total']
    z = subset['Avg Latency(us)']

    if len(x.unique()) < 2 or len(y.unique()) < 2:
        print(f"Insufficient unique x or y values to plot 3D heatmap for {operation} with {algo}. Using scatter plot instead.")
        scatter = ax.scatter(np.log2(x), np.log2(y), np.log2(z), c=z, cmap='viridis', edgecolor='k')
    else:
        print(f"Plotting 3D heatmap for {operation} with {algo}.")
        mesh = ax.plot_trisurf(np.log2(x), np.log2(y), np.log2(z), cmap='viridis', edgecolor='k')

    ax.set_xlabel('Message size (bytes)', fontsize=10)
    ax.set_ylabel('Number of Processes', fontsize=10)
    ax.set_zlabel('log2(Avg Latency(us))', fontsize=10)
    ax.set_title(f'{operation.capitalize()} Latency\nmap-by core, {algo} algorithm', fontsize=12)

    yticks_values = [2, 4, 8, 16, 32, 64, 128, 256]
    yticks_labels = ['$2^{%d}$' % int(np.log2(val)) for val in yticks_values]
    ax.set_yticks(np.log2(yticks_values))
    ax.set_yticklabels(yticks_labels, fontsize=8)

    xticks_values = sorted(x.unique())
    xticks_labels = ['$2^{%d}$' % int(np.log2(val)) for val in xticks_values]
    ax.set_xticks(np.log2(xticks_values)[::3])
    ax.set_xticklabels(xticks_labels[::3], fontsize=8)

    if 'mesh' in locals():
        fig.colorbar(mesh, ax=ax, shrink=0.5, aspect=5, pad=0.1)
    else:
        fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5, pad=0.1)

def plot_line_plot(data, operation, benchmark_type, ax):
    subset = data[(data['Operation'] == operation) & (data['BenchmarkType'] == benchmark_type)]
    for algo in subset['ALGO_NAME'].unique():
        algo_data = subset[subset['ALGO_NAME'] == algo]
        ax.plot(algo_data['NP_total'], algo_data['Avg Latency(us)'], label=algo)
    ax.set_xlabel('Number of Cores', fontsize=10)
    ax.set_ylabel('Avg Latency (us)', fontsize=10)
    ax.set_title(f'{operation.capitalize()} {benchmark_type.capitalize()} Latency', fontsize=12)
    ax.legend()

def main():
    # Load the data
    broadcast_fixed = pd.read_csv('broadcast_fixed.txt')
    broadcast_full = pd.read_csv('broadcast_full.txt')
    reduce_fixed = pd.read_csv('reduce_fixed.txt')
    reduce_full = pd.read_csv('reduce_full.txt')

    # Add operation and benchmark type columns
    broadcast_fixed['Operation'] = 'broadcast'
    broadcast_fixed['BenchmarkType'] = 'fixed'
    broadcast_full['Operation'] = 'broadcast'
    broadcast_full['BenchmarkType'] = 'full'
    reduce_fixed['Operation'] = 'reduce'
    reduce_fixed['BenchmarkType'] = 'fixed'
    reduce_full['Operation'] = 'reduce'
    reduce_full['BenchmarkType'] = 'full'

    # Combine data
    combined_data = pd.concat([broadcast_fixed, broadcast_full, reduce_fixed, reduce_full], ignore_index=True)
    print("Loaded data:\n", combined_data.head())

    # Debug unique values
    for operation in combined_data['Operation'].unique():
        for algo in combined_data['ALGO_NAME'].unique():
            print(f"Unique x values for {operation} with {algo}: {combined_data[(combined_data['Operation'] == operation) & (combined_data['ALGO_NAME'] == algo)]['Size'].unique()}")
            print(f"Unique y values for {operation} with {algo}: {combined_data[(combined_data['Operation'] == operation) & (combined_data['ALGO_NAME'] == algo)]['NP_total'].unique()}")

    # Create the plot for broadcast
    fig, axs = plt.subplots(2, 2, figsize=(16, 14), subplot_kw={'projection': '3d'})
    algorithms = combined_data[combined_data['Operation'] == 'broadcast']['ALGO_NAME'].unique()
    for ax, algo in zip(axs.ravel(), algorithms):
        plot_3d_heatmap(fig, combined_data, 'broadcast', algo, ax)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)
    plt.savefig('broadcast_3d_heatmaps.png')
    plt.show()

    # Create the plot for reduce
    fig, axs = plt.subplots(2, 2, figsize=(16, 14), subplot_kw={'projection': '3d'})
    algorithms = combined_data[combined_data['Operation'] == 'reduce']['ALGO_NAME'].unique()
    for ax, algo in zip(axs.ravel(), algorithms):
        plot_3d_heatmap(fig, combined_data, 'reduce', algo, ax)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)
    plt.savefig('reduce_3d_heatmaps.png')
    plt.show()

    # Create line plots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    plot_line_plot(combined_data, 'broadcast', 'fixed', ax1)
    plot_line_plot(combined_data, 'broadcast', 'full', ax2)
    plot_line_plot(combined_data, 'reduce', 'fixed', ax3)
    plot_line_plot(combined_data, 'reduce', 'full', ax4)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.4)
    plt.savefig('benchmark_line_plots.png')
    plt.show()

if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np


def write_results(df, filename='data\\genomes_output.csv'):

    df.to_csv(filename, index=False)


def visualize_genomes(df, plot_filename):
    histogram_vals = df.explode('mutations')['mutations'].value_counts()
    _ = plt.figure()
    x_vals = histogram_vals.index.values.tolist()
    y_vals = np.round(histogram_vals.values.tolist()/histogram_vals.values.sum(), 2)
    _ = plt.bar(x_vals, y_vals)
    plt.savefig(plot_filename)

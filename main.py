import click
from tools.parser import read_genomes, parse_genomes
from tools.generator import visualize_genomes, write_results


@click.command()
@click.option("--input_csv", default='genomes.csv', show_default=True, help="Path to input CSV")
@click.option("--out_vis", default='plot.pdf', show_default=True, help="Path to output pdf")
@click.option("--out_csv", default='out.csv', show_default=True, help="Path to output CSV")
@click.option("--searched_domain", default=None, show_default=True, help="String to be searched")
@click.option("--reference_id", default=None, show_default=True, help="ID of the reference genome")
def cli(input_csv, out_vis, out_csv, searched_domain, reference_id):
    """ This script takes the following options:
        input_csv - Path to input CSV
        out_vis - Path to output pdf
        out_csv - Path to output CSV
        searched_domain - String to be searched
        reference_id - ID of the reference genome
    """

    df = read_genomes(filename=input_csv)
    df_parsed = parse_genomes(df=df, reference=reference_id, domain=searched_domain)
    write_results(df_parsed, filename=out_csv)
    visualize_genomes(df=df_parsed, plot_filename=out_vis)


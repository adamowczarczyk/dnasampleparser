import pandas as pd
import re


def read_genomes(filename='data\\genomes.csv'):
    # this function reads and prepares data for further processing
    # returns only valid, preprocessed rows

    df = pd.read_csv(filename)
    df_out = df[['id', 'genome']].groupby('genome').agg([list, pd.Series.count])
    df_out.columns = df_out.columns.get_level_values(1)
    df_out = df_out.reset_index().rename(columns={'list': 'id'})
    df_out['valid'] = df_out['genome'].apply(lambda x: is_valid_sequence(x))
    df_out_valid = df_out[df_out['valid']].copy()
    df_out_valid['id'] = df_out_valid['id'].apply(lambda x: sorted(x))

    return df_out_valid


def parse_genomes(df, reference, domain='TTATTA'):
    # this function takes prepared dataframe as input
    # and processes it according to defined requirements

    df['mutations'] = df['genome'].apply(lambda x: g_mutations(reference, x))
    df['isDomainPresent'] = df['genome'].apply(lambda x: is_domain(domain, x))

    return df


def is_valid_sequence(seq, alphabet='ATGCN-'):
    # this is a helper function checking whether given sequence
    # is valid, assuming alphabet passed
    for letter in seq:
        if letter not in alphabet:
            return False
    return True


def g_mutations(reference, checked):
    return [''.join([ref_letter, str(index), check_letter])
            for index, (ref_letter, check_letter) in enumerate(list(zip(reference, checked)))
            if (ref_letter != check_letter and 'N' not in (ref_letter, check_letter))
            ]


def is_domain(domain, genome):

    domain = domain.strip('-')
    genome = genome.strip('-')
    pattern = domain.replace('A', '[AN]')\
        .replace('C', '[C|N]')\
        .replace('G', '[G|N]')\
        .replace('T', '[T|N]')\
        .replace('N', '[A|C|G|T|N]')

    if re.search(pattern, genome):
        return 1
    return 0

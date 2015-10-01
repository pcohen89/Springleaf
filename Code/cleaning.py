__author__ = 'p_cohen'

############################### Import libraries #############################
import pandas as pd
import random

############################## Define macros #################################
CLN_PATH = "C:/Repos/Springleaf/Data/Clean"
RAW_PATH = "C:/Repos/Springleaf/Data/Raw"

############################## Define functions ##############################
def random_csv_chunk(path, size):
    """
    :param path: path to file
    :param size: decimal representing % of csv to take
    :return: pandas df
    """
    # Count the lines
    num_lines = sum(1 for l in open(f))
    # Sample size
    size = int(num_lines * size)
    # The row indices to skip - make sure 0 is not included to keep the header!
    skip_idx = random.sample(range(1, num_lines), num_lines - size)
    # Read the data
    df = pd.read_csv(path, skiprows=skip_idx)
    return df

################################ Execute Code ################################
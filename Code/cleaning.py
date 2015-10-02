__author__ = 'p_cohen'

############################### Import libraries #############################
import pandas as pd
import random

############################## Define macros #################################
CLN_PATH = "C:/Repos/Springleaf/Data/Clean/"
RAW_PATH = "C:/Repos/Springleaf/Data/Raw/"

############################## Define functions ##############################
def random_csv_chunk(path, size):
    """
    :param path: path to file
    :param size: decimal representing % of csv to take
    :return: pandas df
    """
    # Count the total lines in the file
    num_lines = sum(1 for l in open(path))
    # Determine number of rows to keep
    size = int(num_lines * size)
    # The row indices to skip - make sure 0 is not included to keep the header!
    skip_idx = random.sample(range(1, num_lines), num_lines - size)
    # Read in csv, skipping chosen rows
    df = pd.read_csv(path, skiprows=skip_idx)
    return df

################################ Execute Code ################################

non_test = random_csv_chunk(RAW_PATH + "train.csv", .01)

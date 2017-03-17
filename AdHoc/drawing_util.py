import numpy as np

def get_data_from_file(filename):
    data = np.loadtxt(filename, skiprows=1, delimiter=",", usecols=(0,1,2,3))
    return data

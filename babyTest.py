
# # Character level language model - Baby Names

import numpy as np
from utils import *
import random


# ### 1.1 - Dataset and Preprocessing
data = open('babiesLarge.txt', 'r').read()
data= data.lower()
chars = list(set(data))
data_size, vocab_size = len(data), len(chars)
print('There are %d total characters and %d unique characters in your data.' % (data_size, vocab_size))




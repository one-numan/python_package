"""Main File for this Project"""

import python_sample_package as pg
from python_sample_package import module1, module2
from python_sample_package.module1 import cal_square
print(pg.__file__)
# Module 1 | Call calculate_Square function
output_sq = module1.cal_square(3)
print(output_sq)

# Module 1 | Call doubler function
output_double = module1.doubler(3)
print(output_double)

# Module 2 Using Mean Function From Modules
list_of_integer = [1, 2, 12, 32, 12, 0, 22, 1]
output_mean = module2.mean(list_of_integer)
print(output_mean)

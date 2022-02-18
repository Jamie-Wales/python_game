""" TM112 21J TMA02 Q5
06/10/2010 - PP
"""

from tma02_stats import median
from tma02_stats import mean
from tma02_stats import corr_coef

""" You can use one of two approaches:
1)  add suitable code below and then run this file
2)  run this file first then do the calculation in the 
    Python interactive shell.
"""


# Quarterly change from a year earlier in visits to the UK from overseas residents (ONS)

visits = [6.9,1.6,2,7.4,8.8,1.5,3.6,13.1,7.9,8.6,9.2,-5.8,-3.4,-4.5,-3,3.8,-2.5,-1.5,2.8,6.4,-16.1]

# Quarterly change from a year earlier in spending during visits to the UK (ONS)

spending = [3.6,5.7,-4.8,5.7,4.1,4.1,8.7,8.3,14.1,9.5,22.5,-1.9,2.3,-3,-16.7,-1.8,-7.5,-0.6,9.4,26.5,-9.6]

output = corr_coef(spending, visits)
output = round(output, 2)
print(output)







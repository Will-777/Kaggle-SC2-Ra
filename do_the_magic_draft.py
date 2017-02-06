"""
2017-02-06,

For more info
https://github.com/Will-777/Kaggle-SC2-Ra/


Just a python version of
https://www.kaggle.com/jonathanbouchet/d/sfu-summit/starcraft-ii-replay-analysis/starcraft2-replay-analysis


"""

#start python3.5

import pandas as pd
from numpy import *
from matplotlib import *

# write the path
my_reviews = pd.read_csv("starcraft(original).csv")


#Display as table data (5 rows by default)
my_reviews.head()
# or my_reviews.my-
my_reviews.tail()

#Get the how many rows & columns are in my_reviews
my_reviews.shape


#Display as table data (display 15 rows)
my_reviews.iloc[0:15,:]

#Entire dataf Frame
#my_reviews.iloc[:,:]

# >>> my_reviews.min()
"""
GameID                   52.000000
LeagueIndex               1.000000
Age                      16.000000
HoursPerWeek              0.000000
TotalHours                3.000000
APM                      22.059600
SelectByHotkeys           0.000000
AssignToHotkeys           0.000000
UniqueHotkeys             0.000000
MinimapAttacks            0.000000
MinimapRightClicks        0.000000
NumberOfPACs              0.000679
GapBetweenPACs            6.666700
ActionLatency            24.093600
ActionsInPAC              2.038900
TotalMapExplored          0.000091
WorkersMade               0.000077
UniqueUnitsMade           0.000020
ComplexUnitsMade          0.000000
ComplexAbilityUsed        0.000000
MaxTimeStamp          25224.000000
dtype: float64

"""

# >>> my_reviews.max()
"""
GameID                  10095.000000
LeagueIndex                 8.000000
Age                        44.000000
HoursPerWeek              168.000000
TotalHours            1000000.000000
APM                       389.831400
SelectByHotkeys             0.043088
AssignToHotkeys             0.001752
UniqueHotkeys               0.000338
MinimapAttacks              0.003019
MinimapRightClicks          0.004041
NumberOfPACs                0.007971
GapBetweenPACs            237.142900
ActionLatency             176.372100
ActionsInPAC               18.558100
TotalMapExplored            0.000832
WorkersMade                 0.005149
UniqueUnitsMade             0.000202
ComplexUnitsMade            0.000902
ComplexAbilityUsed          0.003084
MaxTimeStamp           388032.000000
dtype: float64
"""



#>>> my_reviews.columns
"""
Index(['GameID', 'LeagueIndex', 'Age', 'HoursPerWeek', 'TotalHours', 'APM',
       'SelectByHotkeys', 'AssignToHotkeys', 'UniqueHotkeys', 'MinimapAttacks',
       'MinimapRightClicks', 'NumberOfPACs', 'GapBetweenPACs', 'ActionLatency',
       'ActionsInPAC', 'TotalMapExplored', 'WorkersMade', 'UniqueUnitsMade',
       'ComplexUnitsMade', 'ComplexAbilityUsed', 'MaxTimeStamp'],
      dtype='object')

"""





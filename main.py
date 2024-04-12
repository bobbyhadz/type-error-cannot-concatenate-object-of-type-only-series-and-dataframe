# Cannot concatenate object of type 'X'; only Series and DataFrame objs are valid

import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2],
    'B': [3, 4]
})

df2 = pd.DataFrame({
    'A': [5, 6],
    'B': [7, 8]
})

dataframes = [df1, df2]


df3 = pd.concat(dataframes, ignore_index=True)

#    A  B
# 0  1  3
# 1  2  4
# 2  5  7
# 3  6  8
print(df3)
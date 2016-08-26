# Try to learn the methods in pandas
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Generate date times

# First way to generate it
dt = datetime(2016, 8, 15)
end = datetime(2016, 8, 25)
step = timedelta(days=1)

result = []

while dt < end:
    result.append(dt.strftime('%Y-%m-%d'))
    dt += step

# Second way with Pandas
result_pd = pd.date_range('2016-8-15', periods = 100)

# Generate timeseries
ts = pd.Series(np.random.randn(100), index = result_pd)


# Method Collection

# Slicing: truncate
ts.truncate(after = '2016-11-9')

dir(pd)
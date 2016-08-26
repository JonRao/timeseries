import pandas as pd
import numpy as np

# 72 * 10 hours starting with Aug, 24, 2016
rng = pd.date_range('8/24/2016', periods=72 * 10, freq='3H')

pd.Series(np.random.randn(len(rng)), index=rng)
pd.infer_freq(rng)
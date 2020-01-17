#### Set second to 00 ####

import pandas as pd

s = pd.date_range(last30, periods = 30 * 60 * 60, freq='S')
s1=pd.DataFrame(s)
s1[0].apply(lambda x: x.replace(second=0))

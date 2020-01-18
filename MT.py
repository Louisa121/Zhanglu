#### Set second to 00 ####

import pandas as pd
last30 = pd.datetime.now().replace(microsecond=0) - pd.Timedelta('30H')
s = pd.date_range(last30, periods = 30 * 60 * 60, freq='S')
s1=pd.DataFrame(s)
s1[0].apply(lambda x: x.replace(second=0))

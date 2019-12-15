data = {'uut': ['4C_DEMO', '4C_DEMO', '4C_DEMO'], 'test_area': ['PCB2C', 'PCB2C', 'PCB2C'],
'sernum': ['s2', 's2', 's3']}

import pandas as pd
df = pd.DataFrame(data)

print data
print df.head()

print df['sernum'].nunique()

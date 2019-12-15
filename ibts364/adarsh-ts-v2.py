import pandas as pd
import numpy as np

PERIODS = 10
START_DATE = ""
data_df = pd.read_csv("temp.csv")
data_df["sasdate"] = data_df["sasdate"].astype("datetime64[ns]")
data_df.set_index("sasdate", inplace=True)
data_df.sort_values(by=["sasdate"])
# print data_df.columns
# print data_df.head()
# print data_df.tail()
# print len(data_df)

START_DATE = data_df.ix[0].name
# print START_DATE
actual_sasdate_period = data_df.index.to_list()

total_time_series = pd.date_range(start=START_DATE, freq="MS", periods=PERIODS)
# print total_time_series
total_time_series_data = pd.to_datetime(total_time_series.data)
total_time_period = total_time_series.to_list()
# print actual_sasdate_period
print total_time_period

missing_date_period = [time_period for time_period in total_time_period
                        if time_period not in actual_sasdate_period]
# print 'missing_date_period: ', missing_date_period

# When some data is missing.
if missing_date_period:
    for missing_date in missing_date_period:
        # print missing_date
        needed_time = ''
        for index, row in data_df.iterrows():
            # print index
            if index<missing_date:
                needed_time = index
                continue
            elif index>missing_date:
                # print 'missing_date :', missing_date, 'needed_time :', needed_time
                break

        print 'missing_date :', missing_date, 'needed_time :', needed_time
        previous_row_data = data_df.ix[needed_time]
        previous_row_data.actuals = 0.0
        print previous_row_data
        data_df.loc[missing_date] = previous_row_data
else:
    pass

data_df["sasdate"] = data_df.index
data_df = data_df.reset_index(drop=True)
print data_df.sort_values(by=["sasdate"])

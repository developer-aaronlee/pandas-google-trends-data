import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_tesla = pd.read_csv("TESLA Search Trend vs Price.csv")
# print(df_tesla.shape)
# print(df_tesla.head())
# print(f'Largest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].max()}')
# print(f'Smallest value for Tesla in Web Search: {df_tesla["TSLA_WEB_SEARCH"].min()}')
# print(df_tesla.describe())

df_btc_search = pd.read_csv("Bitcoin Search Trend.csv")
# print(df_btc_search.shape)
# print(df_btc_search.head())
# print(f'largest BTC News Search: {df_btc_search["BTC_NEWS_SEARCH"].max()}')

df_btc_price = pd.read_csv("Daily Bitcoin Price.csv")
# print(df_btc_price.shape)
# print(df_btc_price.head())

df_unemployment = pd.read_csv("UE Benefits Search vs UE Rate 2004-19.csv")
# print(df_unemployment.shape)
# print(df_unemployment.head())
# print(f'Largest value for "Unemployemnt Benefits" in Web Search: {df_unemployment["UE_BENEFITS_WEB_SEARCH"].max()}')

"""Are there any missing values in any of the dataframes? If so, which row/rows have missing values? How many missing values are there?"""
# print(f'Missing values for Tesla?: {df_tesla.isna().values.any()}')
# print(f'Missing values for U/E?: {df_unemployment.isna().values.any()}')
# print(f'Missing values for BTC Search?: {df_btc_search.isna().values.any()}')
# print(f'Missing values for BTC price?: {df_btc_price.isna().values.any()}')

missing_value_count = df_btc_price.isna().values.sum()
# print(f"Number of missing values: {missing_value_count}")
missing_values = df_btc_price[df_btc_price.isna().values.any(axis=1)]
# missing_values = df_btc_price[df_btc_price["CLOSE"].isna()]
# print(missing_values)

# Find NaN values step by step
# all_values_in_bool = df_btc_price.isna()
# print(all_values_bool)
# missing_values_by_row = df_btc_price.isna().any(axis=0)
# print(missing_values_by_row)
# missing_values_by_col = df_btc_price.isna().any(axis=1)
# print(missing_values_by_col)
display_missing_values_df = df_btc_price[df_btc_price.isna().any(axis=1)]
# print(display_missing_values_df)
# print(type(display_missing_values_df))

"""Remove any missing values that you found."""
df_btc_price.dropna(inplace=True)
check_missing_value = df_btc_price.isna().values.any()
# print(check_missing_value)

"""Check the data type of the entries in the DataFrame MONTH or DATE columns. Convert any strings in to Datetime objects."""
df_tesla.MONTH = pd.to_datetime(df_tesla.MONTH)
# print(type(df_tesla.MONTH[0]))
# print(df_tesla.MONTH.head())

df_unemployment.MONTH = pd.to_datetime(df_unemployment.MONTH)
# print(type(df_unemployment.MONTH[0]))
# print(df_unemployment.MONTH.head())

df_btc_search.MONTH = pd.to_datetime(df_btc_search.MONTH)
# print(type(df_btc_search.MONTH[0]))
# print(df_btc_search.MONTH.head())

df_btc_price.DATE = pd.to_datetime(df_btc_price.DATE)
# print(type(df_btc_price.DATE[0]))
# print(df_btc_price.DATE.head())

"""Converting from Daily to Monthly Data"""
df_btc_monthly = df_btc_price.resample(rule="M", on="DATE").last()
# print(df_btc_monthly.shape)
# print(df_btc_monthly.head())

"""Register date converters to avoid warning messages"""
# from pandas.plotting import register_matplotlib_converters
# register_matplotlib_converters()

"""Plot the Tesla stock price against the Tesla search volume using a line chart and two different axes."""
# plt.figure(figsize=(12,8), dpi=120)
# plt.title("Tesla Web Search vs Price", fontsize=18)
#
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
#
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)
#
# plt.show()

"""How to add tick formatting for dates on the x-axis."""
# plt.figure(figsize=(12,8), dpi=120)
# plt.title("Tesla Web Search vs Price", fontsize=18)
#
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt= mdates.DateFormatter("%Y")
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylabel("TSLA Stock Price", color="#E6232E", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.set_ylim([0, 600])
# ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])
#
# ax1.plot(df_tesla.MONTH, df_tesla.TSLA_USD_CLOSE, color="#E6232E", linewidth=3)
# ax2.plot(df_tesla.MONTH, df_tesla.TSLA_WEB_SEARCH, color="skyblue", linewidth=3)
#
# plt.show()

"""Create the same chart for the Bitcoin Prices vs. Search volumes."""
# plt.figure(figsize=(12,8), dpi=120)
# plt.title("Bitcoin News Search vs Resampled Price", fontsize=18)
#
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt= mdates.DateFormatter("%Y")
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(top=15000, bottom=0)
# ax1.set_xlim([df_btc_monthly.index.min(), df_btc_monthly.index.max()])
#
# ax1.set_ylabel("BTC Price", color="#F08F2E", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.plot(df_btc_monthly.index, df_btc_monthly.CLOSE, color="#E6232E", linewidth=3, linestyle="--")
# ax2.plot(df_btc_monthly.index, df_btc_search.BTC_NEWS_SEARCH, color="skyblue", linewidth=3, marker="o")
#
# plt.show()

"""Plot the search for "unemployment benefits" against the unemployment rate."""
# plt.figure(figsize=(12,8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.grid(color="gray", linestyle="--")
#
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt= mdates.DateFormatter("%Y")
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(top=10.5, bottom=3)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
#
# ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.plot(df_unemployment.MONTH, df_unemployment.UNRATE, color="purple", linewidth=3, linestyle="--")
# ax2.plot(df_unemployment.MONTH, df_unemployment.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)
#
# plt.show()

"""Plot the 6-month rolling average search data against the actual unemployment."""
roll_df = df_unemployment[["UE_BENEFITS_WEB_SEARCH", "UNRATE"]].rolling(window=6).mean()
# print(roll_df)

# plt.figure(figsize=(12,8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.grid(color="gray", linestyle="--")
#
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt= mdates.DateFormatter("%Y")
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(top=10.5, bottom=3)
# ax1.set_xlim([df_unemployment.MONTH.min(), df_unemployment.MONTH.max()])
#
# ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.plot(df_unemployment.MONTH, roll_df.UNRATE, color="purple", linewidth=3, linestyle="--")
# ax2.plot(df_unemployment.MONTH, roll_df.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)
#
# plt.show()

"""Convert the MONTH column to Pandas Datetime objects and then plot the chart."""
df_ue_2020 = pd.read_csv("UE Benefits Search vs UE Rate 2004-20.csv")
# print(df_ue_2020.shape)
# print(df_ue_2020.head())

df_ue_2020.MONTH = pd.to_datetime(df_ue_2020.MONTH)
# print(type(df_ue_2020.MONTH[0]))
# print(df_ue_2020.head())

# plt.figure(figsize=(12,8), dpi=120)
# plt.title('Monthly Search of "Unemployment Benefits" in the U.S. vs the U/E Rate', fontsize=18)
# plt.grid(color="gray", linestyle="--")
#
# plt.yticks(fontsize=14)
# plt.xticks(fontsize=12, rotation=45)
#
# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# years = mdates.YearLocator()
# months = mdates.MonthLocator()
# years_fmt= mdates.DateFormatter("%Y")
#
# ax1.xaxis.set_major_locator(years)
# ax1.xaxis.set_major_formatter(years_fmt)
# ax1.xaxis.set_minor_locator(months)
#
# ax1.set_ylim(top=15.5, bottom=3)
# ax1.set_xlim([df_ue_2020.MONTH.min(), df_ue_2020.MONTH.max()])
#
# ax1.set_ylabel("FRED U/E Rate", color="purple", fontsize=15)
# ax2.set_ylabel("Search Trend", color="skyblue", fontsize=15)
#
# ax1.plot(df_ue_2020.MONTH, df_ue_2020.UNRATE, color="purple", linewidth=3, linestyle="--")
# ax2.plot(df_ue_2020.MONTH, df_ue_2020.UE_BENEFITS_WEB_SEARCH, color="skyblue", linewidth=3)
#
# plt.show()






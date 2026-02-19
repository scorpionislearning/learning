import gspread as gs
import pandas as pd
import os as os
os.getcwd

df_csv = pd.read_csv('C:/Users/harya/Documents/HSA/Growth/NIRF Ranking 2020.csv',header=0)
print(df_csv.head())

# ===================================================================Google Sheets API to read data from a Google Sheet

# sheet_id = '15TgCGWaLbGkxhcuzYGZ0Ee3_HypebFboEvBXwA9M1n0'
# sheet_name = 'raw_data'
# gc = gs.service_account(filename='C:/Users/harya/Documents/HSA/Growth/stately-bulwark-486601-d9-6af06ead8bb3.json')
# sheet = gc.open_by_key(sheet_id).worksheet(sheet_name)
# data_gs = sheet.get_all_records()
# df_csv_gs = pd.DataFrame(data_gs)
# print(df_csv_gs.head()) 


# ===================================================================Accessing specific rows and columns in a DataFrame

df_csv_test = df_csv.iloc[30,2]
df_csv_test2 = df_csv.iloc[[14,29],[2,4]]
df_csv_test3 = df_csv.iloc[14:30,2:8]
df_csv_test4 = df_csv.iloc[:10,1:]
df_csv_test5 = df_csv.iloc[-1,-1]
df_csv_test6 = df_csv.iloc[-20:,-3:]

# print(df_csv_test)
# print(df_csv_test2)
# print(df_csv_test3)
# print(df_csv_test4)
# print(df_csv_test5)
# print(df_csv_test6)


df_csv_copy = df_csv.copy()
df_csv_copy.set_index('City', inplace=True)
print(df_csv_copy.head())

df_csv_city = df_csv_copy.loc[['Mumbai','Pune']]
print(df_csv_city)

df_csv_city = df_csv_copy.loc[['Mumbai','Pune'],['RPC','PERCEPTION']]
print(df_csv_city)


df_csv_mumbai = df_csv[df_csv['City'] == "Mumbai"]
print(df_csv_mumbai)

df_csv_high_perception = df_csv[df_csv['PERCEPTION'] > 90]
print(df_csv_high_perception)

df_csv_like_ore = df_csv[df_csv['City'].str.contains("ore")]
print(df_csv_like_ore)

df_csv_like_many = df_csv[(df_csv['City'].str.contains("ore") | df_csv['City'].str.contains("pur")) & (df_csv['PERCEPTION'] > 40)]
print(df_csv_like_many)
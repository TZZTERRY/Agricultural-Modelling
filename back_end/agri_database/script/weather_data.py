import hashlib
import sqlite3
import functools as ft
import pandas as pd
df = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/AUS_v5.csv")
# copy Year, State, temperature, rainfall, and evaporation
aus_table_V1 = df[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
aus_table_V1['average_eva'] = aus_table_V1.iloc[:, 2:13].mean(axis=1)
aus_table_V1['average_temp'] = aus_table_V1.iloc[:, 14:25].mean(axis=1)
aus_table_V1['average_rain'] = aus_table_V1.iloc[:, 26:37].mean(axis=1)
aus_table_V2 = aus_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

aus_eva_list = aus_table_V2['average_eva'].tolist()
aus_tem_list = aus_table_V2['average_temp'].tolist()
aus_rain_list = aus_table_V2['average_rain'].tolist()

#print(aus_table_V2.to_string())
# do the same thing for the other states
df_nsw = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/NSW_v5.csv")
nsw_table_V1 = df_nsw[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
nsw_table_V1['average_eva'] = nsw_table_V1.iloc[:, 2:13].mean(axis=1)
nsw_table_V1['average_temp'] = nsw_table_V1.iloc[:, 14:25].mean(axis=1)
nsw_table_V1['average_rain'] = nsw_table_V1.iloc[:, 26:37].mean(axis=1)
nsw_table_V2 = nsw_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

nsw_eva_list = nsw_table_V2['average_eva'].tolist()
nsw_tem_list = nsw_table_V2['average_temp'].tolist()
nsw_rain_list = nsw_table_V2['average_rain'].tolist()

df_nt = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/NT_v5.csv")
nt_table_V1 = df_nt[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
nt_table_V1['average_eva'] = nt_table_V1.iloc[:, 2:13].mean(axis=1)
nt_table_V1['average_temp'] = nt_table_V1.iloc[:, 14:25].mean(axis=1)
nt_table_V1['average_rain'] = nt_table_V1.iloc[:, 26:37].mean(axis=1)
nt_table_V2 = nt_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

nt_eva_list = nt_table_V2['average_eva'].tolist()
nt_tem_list = nt_table_V2['average_temp'].tolist()
nt_rain_list = nt_table_V2['average_rain'].tolist()

df_qld = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/Qld_v5.csv")
qld_table_V1 = df_qld[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
qld_table_V1['average_eva'] = qld_table_V1.iloc[:, 2:13].mean(axis=1)
qld_table_V1['average_temp'] = qld_table_V1.iloc[:, 14:25].mean(axis=1)
qld_table_V1['average_rain'] = qld_table_V1.iloc[:, 26:37].mean(axis=1)
qld_table_V2 = qld_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

qld_eva_list = qld_table_V2['average_eva'].tolist()
qld_tem_list = qld_table_V2['average_temp'].tolist()
qld_rain_list = qld_table_V2['average_rain'].tolist()

df_sa = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/Sa_v5.csv")
sa_table_V1 = df_sa[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
sa_table_V1['average_eva'] = sa_table_V1.iloc[:, 2:13].mean(axis=1)
sa_table_V1['average_temp'] = sa_table_V1.iloc[:, 14:25].mean(axis=1)
sa_table_V1['average_rain'] = sa_table_V1.iloc[:, 26:37].mean(axis=1)
sa_table_V2 = sa_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

sa_eva_list = sa_table_V2['average_eva'].tolist()
sa_tem_list = sa_table_V2['average_temp'].tolist()
sa_rain_list = sa_table_V2['average_rain'].tolist()

df_ta = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/Ta_v5.csv")
ta_table_V1 = df_ta[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
ta_table_V1['average_eva'] = ta_table_V1.iloc[:, 2:13].mean(axis=1)
ta_table_V1['average_temp'] = ta_table_V1.iloc[:, 14:25].mean(axis=1)
ta_table_V1['average_rain'] = ta_table_V1.iloc[:, 26:37].mean(axis=1)
ta_table_V2 = ta_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

ta_eva_list = ta_table_V2['average_eva'].tolist()
ta_tem_list = ta_table_V2['average_temp'].tolist()
ta_rain_list = ta_table_V2['average_rain'].tolist()

df_vic = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/Vic_v5.csv")
vic_table_V1 = df_vic[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
vic_table_V1['average_eva'] = vic_table_V1.iloc[:, 2:13].mean(axis=1)
vic_table_V1['average_temp'] = vic_table_V1.iloc[:, 14:25].mean(axis=1)
vic_table_V1['average_rain'] = vic_table_V1.iloc[:, 26:37].mean(axis=1)
vic_table_V2 = vic_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()

vic_eva_list = vic_table_V2['average_eva'].tolist()
vic_tem_list = vic_table_V2['average_temp'].tolist()
vic_rain_list = vic_table_V2['average_rain'].tolist()

df_wa = pd.read_csv("/Users/Dawei/PycharmProjects/Agricultural-Modelling/Data/csv/v5/Wa_v5.csv")
wa_table_V1 = df_wa[['Year','State','Jan_eva','Feb_eva','Mar_eva','Apr_eva','May_eva','Jun_eva','Jul_eva','Aug_eva','Sep_eva','Oct_eva','Nov_eva','Dec_eva','Jan_temp','Feb_temp','Mar_temp','Apr_temp','May_temp','Jun_temp','Jul_temp','Aug_temp','Sep_temp','Oct_temp','Nov_temp','Dec_temp','Jan_rain','Feb_rain','Mar_rain','Apr_rain','May_rain','Jun_rain','Jul_rain','Aug_rain','Sep_rain','Oct_rain','Nov_rain','Dec_rain']].copy()
wa_table_V1['average_eva'] = wa_table_V1.iloc[:, 2:13].mean(axis=1)
wa_table_V1['average_temp'] = wa_table_V1.iloc[:, 14:25].mean(axis=1)
wa_table_V1['average_rain'] = wa_table_V1.iloc[:, 26:37].mean(axis=1)
wa_table_V2 = wa_table_V1[['Year','State','average_eva','average_temp','average_rain']].copy()
wa_tem_list = wa_table_V2['average_temp'].tolist()

wa_eva_list = wa_table_V2['average_eva'].tolist()
wa_tem_list = wa_table_V2['average_temp'].tolist()
wa_rain_list = wa_table_V2['average_rain'].tolist()

# join the tables
#data = [aus_table_V2,nsw_table_V2,nt_table_V2,qld_table_V2,sa_table_V2,ta_table_V2,vic_table_V2,wa_table_V2]
#data_final = ft.reduce(lambda left, right: pd.merge(left, right, on='Year'), data)
#print(data_final.to_string())

db_path = '../agri_db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
years = [1990 + i for i in range(32)]
def insert_weather(region_name,tem_list,rain_list,eva_list):
    for i in range(len(years)):
        md5hash = hashlib.md5((region_name + str(years[i])).encode("utf-8"))
        id = md5hash.hexdigest()
        sql = f"""replace into weather(id, region_name,year,temperature,rainfall, evaporation) values 
             ('{id}','{region_name}','{years[i]}','{tem_list[i]}','{rain_list[i]}','{eva_list[i]}') """
        cursor.execute(sql)
        conn.commit()

# import data for every state
insert_weather("aus",aus_tem_list,aus_rain_list,aus_eva_list)

insert_weather("nsw",nsw_tem_list,nsw_rain_list,nsw_eva_list)
insert_weather("nt",nt_tem_list,nt_rain_list,nt_eva_list)
insert_weather("qld",qld_tem_list,qld_rain_list,qld_eva_list)
insert_weather("sa",sa_tem_list,sa_rain_list,sa_eva_list)
insert_weather("ta",ta_tem_list,ta_rain_list,ta_eva_list)
insert_weather("vic",vic_tem_list,vic_rain_list,vic_eva_list)
insert_weather("wa",wa_tem_list,wa_rain_list,wa_eva_list)





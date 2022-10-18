# -*- coding: utf-8 -*-
import sqlite3
from agri_csv_reader import read_csv
import hashlib
db_path = '../agri_db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

years = [2022 + i for i in range(30)]


def insert_predict(region_name, crop_name, crop_id, yield_list):


    for i in range(len(years)):
        md5hash = hashlib.md5((region_name+crop_name+str(years[i])).encode("utf-8"))
        id = md5hash.hexdigest()
        sql = f"""replace into yield_price(id, region_name,crop_name,year,price,crop_id, yield, is_predict) values 
             ('{id}','{region_name}','{crop_name}','{years[i]}','{0}','{crop_id}','{yield_list[i]}','{1}') """
        cursor.execute(sql)
        conn.commit()




NSW_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Nsw\prediction_result\\"

NSW_wheat_path = NSW_path+"NSW_Wheat_Production_prediction.csv"
NSW_wheat = read_csv(NSW_wheat_path, ["Wheat_Production"])[0]

NSW_oats_path = NSW_path+"NSW_Oats_Production_prediction.csv"
NSW_oats = read_csv(NSW_oats_path, ["Oats_Production"])[0]

NSW_corn_path = NSW_path+"NSW_Corn_Production_prediction.csv"
NSW_corn = read_csv(NSW_corn_path, ["Corn_Production"])[0]

NSW_barley_path = NSW_path+"NSW_Barley_Production_prediction.csv"
NSW_barley = read_csv(NSW_barley_path, ["Barley_Production"])[0]

insert_predict("nsw", "wheat", 0, NSW_wheat)
insert_predict("nsw", "oats", 1, NSW_oats)
insert_predict("nsw", "corn", 2, NSW_corn)
insert_predict("nsw", "barley", 3, NSW_barley)




Qld_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Qld\prediction_result\\"

Qld_wheat_path = Qld_path+"Qld_Wheat_Production_prediction.csv"
Qld_wheat = read_csv(Qld_wheat_path, ["Wheat_Production"])[0]

Qld_oats_path = Qld_path+"Qld_Oats_Production_prediction.csv"
Qld_oats = read_csv(Qld_oats_path, ["Oats_Production"])[0]

Qld_corn_path = Qld_path+"Qld_Corn_Production_prediction.csv"
Qld_corn = read_csv(Qld_corn_path, ["Corn_Production"])[0]

Qld_barley_path = Qld_path+"Qld_Barley_Production_prediction.csv"
Qld_barley = read_csv(Qld_barley_path, ["Barley_Production"])[0]

insert_predict("qld", "wheat", 0, Qld_wheat)
insert_predict("qld", "oats", 1, Qld_oats)
insert_predict("qld", "corn", 2, Qld_corn)
insert_predict("qld", "barley", 3, Qld_barley)




Sa_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Sa\prediction_result\\"

Sa_wheat_path = Sa_path+"Sa_Wheat_Production_prediction.csv"
Sa_wheat = read_csv(Sa_wheat_path, ["Wheat_Production"])[0]

Sa_oats_path = Sa_path+"Sa_Oats_Production_prediction.csv"
Sa_oats = read_csv(Sa_oats_path, ["Oats_Production"])[0]

Sa_barley_path = Sa_path+"Sa_Barley_Production_prediction.csv"
Sa_barley = read_csv(Sa_barley_path, ["Barley_Production"])[0]

insert_predict("sa", "wheat", 0, Sa_wheat)
insert_predict("sa", "oats", 1, Sa_oats)
insert_predict("sa", "barley", 3, Sa_barley)




Ta_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Ta\prediction_result\\"

Ta_wheat_path = Ta_path+"Ta_Wheat_Production_prediction.csv"
Ta_wheat = read_csv(Ta_wheat_path, ["Wheat_Production"])[0]

Ta_oats_path = Ta_path+"Ta_Oats_Production_prediction.csv"
Ta_oats = read_csv(Ta_oats_path, ["Oats_Production"])[0]


Ta_barley_path = Ta_path+"Ta_Barley_Production_prediction.csv"
Ta_barley = read_csv(Ta_barley_path, ["Barley_Production"])[0]

insert_predict("ta", "wheat", 0, Ta_wheat)
insert_predict("ta", "oats", 1, Ta_oats)
insert_predict("ta", "barley", 3, Ta_barley)



Vic_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Vic\prediction_result\\"

Vic_wheat_path = Vic_path+"Vic_Wheat_Production_prediction.csv"
Vic_wheat = read_csv(Vic_wheat_path, ["Wheat_Production"])[0]

Vic_oats_path = Vic_path+"Vic_Oats_Production_prediction.csv"
Vic_oats = read_csv(Vic_oats_path, ["Oats_Production"])[0]

Vic_corn_path = Vic_path+"Vic_Corn_Production_prediction.csv"
Vic_corn = read_csv(Vic_corn_path, ["Corn_Production"])[0]

Vic_barley_path = Vic_path+"Vic_Barley_Production_prediction.csv"
Vic_barley = read_csv(Vic_barley_path, ["Barley_Production"])[0]

insert_predict("vic", "wheat", 0, Vic_wheat)
insert_predict("vic", "oats", 1, Vic_oats)
insert_predict("vic", "corn", 2, Vic_corn)
insert_predict("vic", "barley", 3, Vic_barley)



Wa_path = "D:\AgriModeling\Agricultural-Modelling\Algorithm\FinalModels\\Wa\prediction_result\\"

Wa_wheat_path = Wa_path+"Wa_Wheat_Production_prediction.csv"
Wa_wheat = read_csv(Wa_wheat_path, ["Wheat_Production"])[0]

Wa_oats_path = Wa_path+"Wa_Oats_Production_prediction.csv"
Wa_oats = read_csv(Wa_oats_path, ["Oats_Production"])[0]

Wa_corn_path = Wa_path+"Wa_Corn_Production_prediction.csv"
Wa_corn = read_csv(Wa_corn_path, ["Corn_Production"])[0]

Wa_barley_path = Wa_path+"Wa_Barley_Production_prediction.csv"
Wa_barley = read_csv(Wa_barley_path, ["Barley_Production"])[0]

insert_predict("wa", "wheat", 0, Wa_wheat)
insert_predict("wa", "oats", 1, Wa_oats)
insert_predict("wa", "corn", 2, Wa_corn)
insert_predict("wa", "barley", 3, Wa_barley)


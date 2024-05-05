# import packages
import os
import json
import pandas as pd
import pymysql
import plotly.express as px
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#mysql connection
connection = pymysql.connect(
host="localhost",
user="root",
password="adhi",
database="phonepe"
)

connect_data=connection.cursor()

#Retrive the datas in phonepe files

#aggregated insurance
aggre_connect1="C:/Users/study/Downloads/vs code/phonepe/pulse/data/aggregated/insurance/country/india/state/"
aggre_insu_list=os.listdir(aggre_connect1)


aggre_columns1={"states":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}
for state in aggre_insu_list:
    cur_states=aggre_connect1+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            ai=json.load(data)

            for i in ai["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                aggre_columns1["Transaction_type"].append(name)
                aggre_columns1["Transaction_count"].append(count)
                aggre_columns1["Transaction_amount"].append(amount)
                aggre_columns1["states"].append(state)
                aggre_columns1["Years"].append(year)
                aggre_columns1["Quarter"].append(int(file.strip(".json")))
                
aggre_insurance=pd.DataFrame(aggre_columns1)

aggre_insurance["states"]=aggre_insurance["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
aggre_insurance["states"]=aggre_insurance["states"].str.replace('-',' ')
aggre_insurance["states"]=aggre_insurance["states"].str.title()
aggre_insurance["states"]=aggre_insurance["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#aggregate_transaction
aggre_connect2="C:/Users\study/Downloads/vs code/phonepe/pulse/data/aggregated/transaction/country/india/state/"
aggre_tran_list=os.listdir(aggre_connect2)

aggre_columns2={"states":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in aggre_tran_list:
    cur_states=aggre_connect2+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            at=json.load(data)

            for i in at["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                aggre_columns2["Transaction_type"].append(name)
                aggre_columns2["Transaction_count"].append(count)
                aggre_columns2["Transaction_amount"].append(amount)
                aggre_columns2["states"].append(state)
                aggre_columns2["Years"].append(year)
                aggre_columns2["Quarter"].append(int(file.strip(".json")))

aggre_transaction=pd.DataFrame(aggre_columns2)

aggre_transaction["states"]=aggre_transaction["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
aggre_transaction["states"]=aggre_transaction["states"].str.replace('-',' ')
aggre_transaction["states"]=aggre_transaction["states"].str.title()
aggre_transaction["states"]=aggre_transaction["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#aggregate_user
aggre_connect3="C:/Users/study/Downloads/vs code/phonepe/pulse/data/aggregated/user/country/india/state/"
agg_user_list=os.listdir(aggre_connect3)

aggre_columns3={"states":[],"Years":[],"Quarter":[],"Brands":[],"Transaction_count":[],"Precentage":[]}

for state in agg_user_list:
    cur_states=aggre_connect3+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            au=json.load(data)

            try:
                for i in au["data"]["usersByDevice"]:
                    brand=i["brand"]
                    count=i["count"]
                    percentage=i["percentage"]
                    aggre_columns3["Brands"].append(brand)
                    aggre_columns3["Transaction_count"].append(count)
                    aggre_columns3["Precentage"].append(percentage)
                    aggre_columns3["states"].append(state)
                    aggre_columns3["Years"].append(year)
                    aggre_columns3["Quarter"].append(int(file.strip(".json")))
            except:
                pass


aggre_user=pd.DataFrame(aggre_columns3)

aggre_user["states"]=aggre_user["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
aggre_user["states"]=aggre_user["states"].str.replace('-',' ')
aggre_user["states"]=aggre_user["states"].str.title()
aggre_user["states"]=aggre_user["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#map insurance
map_connect1="C:/Users\study/Downloads/vs code/phonepe/pulse/data/map/insurance/hover/country/india/state/"
map_insu_list=os.listdir(map_connect1)

map_columns1={"states":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_insu_list:
    cur_states=map_connect1+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)



        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            mi=json.load(data)

            for i in mi["data"]["hoverDataList"]:
                name=i["name"]
                count=i["metric"][0]["count"]
                amount=i["metric"][0]["amount"]
                map_columns1["Districts"].append(name)
                map_columns1["Transaction_count"].append(count)
                map_columns1["Transaction_amount"].append(amount)
                map_columns1["states"].append(state)
                map_columns1["Years"].append(year)
                map_columns1["Quarter"].append(int(file.strip(".json")))

map_insurance=pd.DataFrame(map_columns1)

map_insurance["states"]=map_insurance["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
map_insurance["states"]=map_insurance["states"].str.replace('-',' ')
map_insurance["states"]=map_insurance["states"].str.title()
map_insurance["states"]=map_insurance["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#map transanctions
map_connect2="C:/Users/study/Downloads/vs code/phonepe/pulse/data/map/transaction/hover/country/india/state/"
map_trans_list=os.listdir(map_connect2)

map_columns2={"states":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_trans_list:
    cur_states=map_connect2+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            mt=json.load(data)

            for i in mt["data"]["hoverDataList"]:
                name=i["name"]
                count=i["metric"][0]["count"]
                amount=i["metric"][0]["amount"]
                map_columns2["Districts"].append(name)
                map_columns2["Transaction_count"].append(count)
                map_columns2["Transaction_amount"].append(amount)
                map_columns2["states"].append(state)
                map_columns2["Years"].append(year)
                map_columns2["Quarter"].append(int(file.strip(".json")))

map_transanction=pd.DataFrame(map_columns2)

map_transanction["states"]=map_transanction["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
map_transanction["states"]=map_transanction["states"].str.replace('-',' ')
map_transanction["states"]=map_transanction["states"].str.title()
map_transanction["states"]=map_transanction["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#map user
map_connect3="C:/Users/study/Downloads/vs code/phonepe/pulse/data/map/user/hover/country/india/state/"
map_user_list=os.listdir(map_connect3)

map_columns3={"states":[],"Years":[],"Quarter":[],"Districts":[],"RegisteredUsers":[],"AppOpens":[]}
for state in map_user_list:
    cur_states=map_connect3+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            mu=json.load(data)

            for i in mu["data"]["hoverData"].items():
                district=i[0]
                registeredUsers=i[1]["registeredUsers"]
                appOpens=i[1]["appOpens"]
                map_columns3["Districts"].append(district)
                map_columns3["RegisteredUsers"].append(registeredUsers)
                map_columns3["AppOpens"].append(appOpens)
                map_columns3["states"].append(state)
                map_columns3["Years"].append(year)
                map_columns3["Quarter"].append(int(file.strip(".json")))
         
map_user=pd.DataFrame(map_columns3)

map_user["states"]=map_user["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
map_user["states"]=map_user["states"].str.replace('-',' ')
map_user["states"]=map_user["states"].str.title()
map_user["states"]=map_user["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#top insurance

top_connect1="C:/Users/study/Downloads/vs code/phonepe/pulse/data/top/insurance/country/india/state/"
top_insu_list=os.listdir(top_connect1)

top_columns1={"states":[],"Years":[],"Quarter":[],"pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for state in top_insu_list:
    cur_states=top_connect1+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            ti=json.load(data)

            for i in ti["data"]["pincodes"]:
                entityname=i["entityName"]
                count=i["metric"]["count"]
                amount=i["metric"]["amount"]
                top_columns1["pincodes"].append(entityname)
                top_columns1["Transaction_count"].append(count)
                top_columns1["Transaction_amount"].append(amount)
                top_columns1["states"].append(state)
                top_columns1["Years"].append(year)
                top_columns1["Quarter"].append(int(file.strip(".json")))

top_insurance=pd.DataFrame(top_columns1)

top_insurance["states"]=top_insurance["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
top_insurance["states"]=top_insurance["states"].str.replace('-',' ')
top_insurance["states"]=top_insurance["states"].str.title()
top_insurance["states"]=top_insurance["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#top transaction
top_connect2="C:/Users/study/Downloads/vs code/phonepe/pulse/data/top/transaction/country/india/state/"
top_trans_list=os.listdir(top_connect2)

top_columns2={"states":[],"Years":[],"Quarter":[],"pincodes":[],"Transaction_count":[],"Transaction_amount":[]}

for state in top_trans_list:
    cur_states=top_connect2+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            tt=json.load(data)

            for i in tt["data"]["pincodes"]:
                entityname=i["entityName"]
                count=i["metric"]["count"]
                amount=i["metric"]["amount"]
                top_columns2["pincodes"].append(entityname)
                top_columns2["Transaction_count"].append(count)
                top_columns2["Transaction_amount"].append(amount)
                top_columns2["states"].append(state)
                top_columns2["Years"].append(year)
                top_columns2["Quarter"].append(int(file.strip(".json")))

top_transaction=pd.DataFrame(top_columns2)

top_transaction["states"]=top_transaction["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
top_transaction["states"]=top_transaction["states"].str.replace('-',' ')
top_transaction["states"]=top_transaction["states"].str.title()
top_transaction["states"]=top_transaction["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#top user
top_connect3="C:/Users/study/Downloads/vs code/phonepe/pulse/data/top/user/country/india/state/"
top_user_list=os.listdir(top_connect3)

top_columns3={"states":[],"Years":[],"Quarter":[],"pincodes":[],"RegisteredUsers":[]}

for state in top_user_list:
    cur_states=top_connect3+state+"/"
    year_list=os.listdir(cur_states)
    
    for year in year_list:
        cur_year=cur_states+year+"/"
        file_list=os.listdir(cur_year)

        for file in file_list:
            all_files=cur_year+file
            data=open(all_files,"r")
            tu=json.load(data)

            for i in tu["data"]["pincodes"]:
                entityname=i["name"]
                registeredUsers=i["registeredUsers"]
                top_columns3["pincodes"].append(entityname)
                top_columns3["RegisteredUsers"].append(registeredUsers)
                top_columns3["states"].append(state)
                top_columns3["Years"].append(year)
                top_columns3["Quarter"].append(int(file.strip(".json")))

top_user=pd.DataFrame(top_columns3)

top_user["states"]=top_user["states"].str.replace("andaman-&-nicobar-islands",'Andaman & Nicobar')
top_user["states"]=top_user["states"].str.replace('-',' ')
top_user["states"]=top_user["states"].str.title()
top_user["states"]=top_user["states"].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#create tables for aggregate
create_table1="""CREATE TABLE if not exists aggre_insurance(states varchar(255),
                                               years int,
                                               quarter int,
                                               Transaction_type varchar(255),
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table1)
connection.commit()

insert_query1='''INSERT INTO aggre_insurance(states, Years, Quarter,Transaction_type,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas1=aggre_insurance.values.tolist()
connect_data.executemany(insert_query1,datas1)
connection.commit() 

#transaction
create_table2="""CREATE TABLE if not exists aggre_transaction(states varchar(255),
                                               years int,
                                               quarter int,
                                               Transaction_type varchar(255),
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table2)
connection.commit()

insert_query2='''INSERT INTO aggre_transaction(states, Years, Quarter,Transaction_type,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas2=aggre_transaction.values.tolist()
connect_data.executemany(insert_query2,datas2)
connection.commit() 

#user
create_table3="""CREATE TABLE if not exists aggre_user(states varchar(255),
                                               years int,
                                               quarter int,
                                               Brands varchar(255),
                                               Transaction_count bigint,
                                               Precentage float)"""

connect_data.execute(create_table3)
connection.commit()

insert_query3='''INSERT INTO aggre_user(states, Years, Quarter,Brands,Transaction_count,Precentage)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas3=aggre_user.values.tolist()

connect_data.executemany(insert_query3,datas3)
connection.commit() 

#create tables for map
create_table4="""CREATE TABLE if not exists map_insurance(states varchar(255),
                                               years int,
                                               quarter int,
                                               Districts varchar(255),
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table4)
connection.commit()

insert_query4='''INSERT INTO map_insurance(states, Years, Quarter,Districts,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas4=map_insurance.values.tolist()
connect_data.executemany(insert_query4,datas4)
connection.commit() 

#transaction
create_table5="""CREATE TABLE if not exists map_transaction(states varchar(255),
                                               years int,
                                               quarter int,
                                               Districts varchar(255),
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table5)
connection.commit()

insert_query5='''INSERT INTO map_transaction(states, Years, Quarter,Districts,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas5=map_transanction.values.tolist()
connect_data.executemany(insert_query5,datas5)
connection.commit() 

#user
create_table6="""CREATE TABLE if not exists map_user(states varchar(255),
                                               years int,
                                               quarter int,
                                               Districts varchar(255),
                                               RegisteredUsers bigint,
                                               AppOpens bigint)"""

connect_data.execute(create_table6)
connection.commit()

insert_query6='''INSERT INTO map_user(states, Years, Quarter,Districts,RegisteredUsers,AppOpens)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas6=map_user.values.tolist()
connect_data.executemany(insert_query6,datas6)
connection.commit() 

#create tables for top
create_table7="""CREATE TABLE if not exists top_insurance(states varchar(255),
                                               years int,
                                               quarter int,
                                               pincodes bigint,
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table7)
connection.commit()

insert_query7='''INSERT INTO top_insurance(states, Years, Quarter,pincodes,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas7=top_insurance.values.tolist()
connect_data.executemany(insert_query7,datas7)
connection.commit() 


#transaction
create_table8="""CREATE TABLE if not exists top_transaction(states varchar(255),
                                               years int,
                                               quarter int,
                                               pincodes bigint,
                                               Transaction_count bigint,
                                               Transaction_amount bigint)"""

connect_data.execute(create_table8)
connection.commit()

insert_query8='''INSERT INTO top_transaction(states, Years, Quarter,pincodes,Transaction_count,Transaction_amount)
                                                                                           VALUES (%s,%s,%s,%s,%s,%s)'''

datas8=top_transaction.values.tolist()
connect_data.executemany(insert_query8,datas8)
connection.commit() 

#user
create_table9="""CREATE TABLE if not exists top_user(states varchar(255),
                                               years int,
                                               quarter int,
                                               pincodes bigint,
                                               RegisteredUsers bigint)"""

connect_data.execute(create_table9)
connection.commit()

insert_query9='''INSERT INTO top_user(states, Years, Quarter,pincodes,RegisteredUsers) VALUES (%s,%s,%s,%s,%s)'''

datas9=top_user.values.tolist()
connect_data.executemany(insert_query9,datas9)
connection.commit() 

#DataFrame creation get data in mysql
#aggregated insurance df
connect_data.execute("SELECT * FROM aggre_insurance")
connection.commit()
table1=connect_data.fetchall()

aggregated_insurance_df=pd.DataFrame(table1,columns=("states", "Years", "Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#aggregated transaction df
connect_data.execute("SELECT * FROM aggre_transaction")
connection.commit()
table2=connect_data.fetchall()

aggregated_transaction_df=pd.DataFrame(table2,columns=("states", "Years", "Quarter","Transaction_type","Transaction_count","Transaction_amount"))

#aggregated user df
connect_data.execute("SELECT * FROM aggre_user")
connection.commit()
table3=connect_data.fetchall()

aggregated_user_df=pd.DataFrame(table3,columns=("states","Years","Quarter","Brands","Transaction_count","Precentage"))

#map insurance df
connect_data.execute("SELECT * FROM map_insurance")
connection.commit()
table4=connect_data.fetchall()

map_insurance_df=pd.DataFrame(table4,columns=("states","Years","Quarter","Districts","Transaction_count","Transaction_amount"))

#map transaction df
connect_data.execute("SELECT * FROM map_transaction")
connection.commit()
table5=connect_data.fetchall()

map_transanction_df=pd.DataFrame(table5,columns=("states","Years","Quarter","Districts","Transaction_count","Transaction_amount"))

#map user df
connect_data.execute("SELECT * FROM map_user")
connection.commit()
table6=connect_data.fetchall()

map_user_df=pd.DataFrame(table6,columns=("states", "Years","Quarter","Districts","RegisteredUsers","AppOpens"))

#top insurance df
connect_data.execute("SELECT * FROM top_insurance")
connection.commit()
table7=connect_data.fetchall()

top_insurance_df=pd.DataFrame(table7,columns=("states", "Years","Quarter","pincodes","Transaction_count","Transaction_amount"))

#top transaction df
connect_data.execute("SELECT * FROM top_transaction")
connection.commit()
table8=connect_data.fetchall()

top_transaction_df=pd.DataFrame(table8,columns=("states", "Years","Quarter","pincodes","Transaction_count","Transaction_amount"))

#top user df
connect_data.execute("SELECT * FROM top_user")
connection.commit()
table9=connect_data.fetchall()

top_user_df=pd.DataFrame(table9,columns=("states", "Years","Quarter","pincodes","RegisteredUsers"))

# Functions creation  
#Aggregate  data visualization 

#aggre_insu_year_count_amount
def ty_count_amount(df,years):
    t_acy=df[df["Years"] == years]
    t_acy.reset_index(drop=True, inplace=True)

    t_acg=t_acy.groupby("states")[["Transaction_count","Transaction_amount"]].sum()
    t_acg.reset_index(inplace=True)

    col1,col2= st.columns(2)
    with col1:
        fig_Count = px.bar(t_acg, x="states", y="Transaction_count", title=f"{years} TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Bluered,height=550,width=500 )
        st.plotly_chart(fig_Count)
    with col2:
        fig_amount = px.bar(t_acg, x="states", y="Transaction_amount", title=f"{years} TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl,height=550,width=500 )
        st.plotly_chart(fig_amount)

    col1,col2 = st.columns(2)

    with col1:

        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)
        data=json.loads(response.content)
        state_names=[]
        for i in data["features"]:
            state_names.append(i["properties"]["ST_NM"])

        state_names.sort()

        fig_india1=px.choropleth(t_acg, geojson=data,locations="states",featureidkey="properties.ST_NM",
                                color="Transaction_count",color_continuous_scale="Rainbow",
                                range_color=(t_acg["Transaction_count"].min(),t_acg["Transaction_count"].max()),
                                hover_name="states",title=f"{years} TRANSACTION COUNT",fitbounds="locations",height=600,width=500)
        fig_india1.update_geos(visible=False)
        st.plotly_chart(fig_india1)
    
    with col2:
        
        fig_india2=px.choropleth(t_acg, geojson=data,locations="states",featureidkey="properties.ST_NM",
                                color="Transaction_amount",color_continuous_scale="Rainbow",
                                range_color=(t_acg["Transaction_amount"].min(),t_acg["Transaction_amount"].max()),
                                hover_name="states",title=f"{years} TRANSACTION AMOUNT",fitbounds="locations",height=600,width=500)
        fig_india2.update_geos(visible=False)
        st.plotly_chart(fig_india2)
        
    return t_acy

#aggre_insu_year_count_amount_quarter 
def ty_Q_count_amount(df , Quarter):
    tac_y_q=df[df["Quarter"] == Quarter]
    tac_y_q.reset_index(drop=True, inplace=True)

    t_acyg=tac_y_q.groupby("states")[["Transaction_count","Transaction_amount"]].sum()
    t_acyg.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:
        fig_count = px.bar(t_acyg, x="states", y="Transaction_count", title=f"{tac_y_q['Years'].unique()} YEAR {Quarter} QUARTER TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.Bluered,height=650,width=600)
        st.plotly_chart(fig_count)

    with col2:
        fig_amount = px.bar(t_acyg, x="states", y="Transaction_amount", title=f"{tac_y_q['Years'].unique()} YEAR {Quarter} QUARTER  TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl,height=650,width=600)
        st.plotly_chart(fig_amount)

    with col1:
        url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response=requests.get(url)
        data=json.loads(response.content)
        state_names=[]
        for i in data["features"]:
            state_names.append(i["properties"]["ST_NM"])
        state_names.sort()

        fig_india1=px.choropleth(t_acyg, geojson=data,locations="states",featureidkey="properties.ST_NM",
                                color="Transaction_count",color_continuous_scale="Rainbow",
                                range_color=(t_acyg["Transaction_count"].min(),t_acyg["Transaction_count"].max()),
                                hover_name="states",title=f"{tac_y_q['Years'].unique()} YEAR {Quarter} QUARTER  TRANSACTION COUNT",fitbounds="locations",height=600,width=500)
        fig_india1.update_geos(visible=False)
        st.plotly_chart(fig_india1)
    
    with col2:
        fig_india2=px.choropleth(t_acyg, geojson=data,locations="states",featureidkey="properties.ST_NM",
                                color="Transaction_amount",color_continuous_scale="Rainbow",
                                range_color=(t_acyg["Transaction_amount"].min(),t_acyg["Transaction_amount"].max()),
                                hover_name="states",title=f"{tac_y_q['Years'].unique()} YEAR {Quarter} QUARTER  TRANSACTION AMOUNT",fitbounds="locations",height=600,width=500)
        fig_india2.update_geos(visible=False)
        st.plotly_chart(fig_india2)

    return tac_y_q

#Aggre_trans_transaction type analysis
def aggregated_transaction_type(df,state):
    t_acy=df[df["states"] == state]
    t_acy.reset_index(drop=True, inplace=True)

    t_acyg=t_acy.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    t_acyg.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:
        fig_pie_1 = px.pie(data_frame =t_acyg,names="Transaction_type",values="Transaction_amount",
                        width=500,title=f"{state.upper()} TRANSACTION AMOUNT",hole=0.5,color_discrete_sequence=px.colors.sequential.RdPu_r)
        st.plotly_chart(fig_pie_1)
    with col2:  
        fig_pie_2 = px.pie(data_frame =t_acyg,names="Transaction_type",values="Transaction_count",
                        width=500,title=f"{state.upper()} TRANSACTION COUNT",hole=0.5,color_discrete_sequence=px.colors.sequential.Rainbow_r)
        st.plotly_chart(fig_pie_2)

#aggregated user year analysis
def aggre_user_year(df,year):
    aggre_uy= df[df["Years"]== year]
    aggre_uy.reset_index(drop = True,inplace = True)

    aggre_uyg = pd.DataFrame(aggre_uy.groupby("Brands")["Transaction_count"].sum())
    aggre_uyg.reset_index(inplace = True)

    fig_bar_1 = px.bar(aggre_uyg, x="Brands", y="Transaction_count", title=f"{year} BRANDS AND TRANSACTION COUNT", 
                        width=800, color_discrete_sequence= px.colors.sequential.Hot,hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aggre_uy

#aggregated user year quarter analysis     
def aggre_user_year_q(df,Quarter):
    aggre_uyq= df[df["Quarter"]== Quarter]
    aggre_uyq.reset_index(drop = True,inplace = True)

    aggre_uyqg=pd.DataFrame(aggre_uyq.groupby("Brands")["Transaction_count"].sum())
    aggre_uyqg.reset_index(inplace=True)

    fig_bar_1 = px.bar(aggre_uyqg, x="Brands", y="Transaction_count", title=f"{Quarter} QUARTER BRANDS AND TRANSACTION COUNT", 
                            width=800, color_discrete_sequence= px.colors.sequential.Viridis,hover_name="Brands")
    st.plotly_chart(fig_bar_1)
     
    return aggre_uyq

#aggregated user year quarter analysis
def aggre_user_year_qs(df, state):
    aggre_uyqs= df[df["states"]== state]
    aggre_uyqs.reset_index(drop= True, inplace= True)

    fig_bar_1 = px.bar(aggre_uyqs, x= "Brands", y= "Transaction_count",title = f"{state} BRANDS AND TRANSACTION COUNT",
                        width=800, color_discrete_sequence= px.colors.sequential.Jet_r)
    st.plotly_chart(fig_bar_1)

#map district analysis
def map_insu_district(df,state):
    m_acd=df[df["states"] == state]
    m_acd.reset_index(drop=True, inplace=True)

    m_acdg=m_acd.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    m_acdg.reset_index(inplace=True)

    col1,col2=st.columns(2)

    with col1:
        fig_bar_1 = px.bar(m_acdg, x="Transaction_count", y= "Districts", orientation="h",height=600,
                            title=f"{state.upper()} DISTRICT AND TRANSACTION COUNT", color_discrete_sequence=px.colors.sequential.Mint_r)
        st.plotly_chart(fig_bar_1)
    with col2:
        fig_bar_2 = px.bar(m_acdg, x="Transaction_amount", y= "Districts", orientation="h",height=600,
                            title=f"{state.upper()} DISTRICT AND TRANSACTION AMOUNT", color_discrete_sequence=px.colors.sequential.Reds_r)
        st.plotly_chart(fig_bar_2)

#map user year analysis
def map_user_year(df,year):
    map_uy= df[df["Years"]== year]
    map_uy.reset_index(drop = True,inplace = True)

    map_uyg = pd.DataFrame(map_uy.groupby("states")[["RegisteredUsers","AppOpens"]].sum())
    map_uyg.reset_index(inplace = True)

    fig_line_1 = px.line(map_uyg, x ="states",y=["RegisteredUsers","AppOpens"],
                        title=f"{year} REGISTERED USERS AND APPOPENS",width = 1000, height=800, markers= True,color_discrete_sequence=["red", "blue"])
    st.plotly_chart(fig_line_1)

    return map_uy

#map user quarter analysis
def map_user_year_quarter(df,quarter):
    map_uyq= df[df["Quarter"]== quarter]
    map_uyq.reset_index(drop = True,inplace = True)

    map_uyqg = pd.DataFrame(map_uyq.groupby("states")[["RegisteredUsers","AppOpens"]].sum())
    map_uyqg.reset_index(inplace = True)

    fig_line_1 = px.line(map_uyqg, x ="states",y=["RegisteredUsers","AppOpens"],
                         title=f"{df['Years'].min()} YEAR {quarter} QUARTER REGISTERED USERS AND APPOPENS",width = 1000, height=800, markers= True,color_discrete_sequence=["orange", "darkblue"])
    st.plotly_chart(fig_line_1)

    return map_uyq

#map user states analysis
def map_user_year_quarter_states(df,states):
    map_uyqs= df[df["states"]== states]
    map_uyqs.reset_index(drop = True,inplace = True)

    fig_bar_1=px.bar(map_uyqs, x= "RegisteredUsers", y= "Districts", orientation="h",height=800,
                    title=f"{states.upper()} REGISTERED USERS", color_discrete_sequence=px.colors.sequential.Rainbow) 
    st.plotly_chart(fig_bar_1)

    fig_bar_2=px.bar(map_uyqs, x= "AppOpens", y= "Districts", orientation="h",height=800,
                    title=f"{states.upper()} APPOPENS USERS", color_discrete_sequence=px.colors.sequential.Oranges_r) 
    st.plotly_chart(fig_bar_2)

# top insu states pincode analysis
def top_in_year_states(df,states):
    top_in_ys= df[df["states"]== states]
    top_in_ys.reset_index(drop = True,inplace = True)

    top_in_ysg = pd.DataFrame(top_in_ys.groupby("pincodes")[["Transaction_count","Transaction_amount"]].sum())
    top_in_ysg.reset_index(inplace = True)

    col1,col2=st.columns(2)
    with col1:
        fig_bar_1=px.bar(top_in_ys, x= "Quarter", y= "Transaction_amount",height=600,width=600,hover_data="pincodes",
                        title=f"{states.upper()} TRANSACTION AMOUNT", color_discrete_sequence=px.colors.sequential.GnBu_r) 
        st.plotly_chart(fig_bar_1)
    with col2:    
        fig_bar_2=px.bar(top_in_ys, x= "Quarter", y= "Transaction_count",height=600,width=600,hover_data="pincodes",
                        title=f"{states.upper()} TRANSACTION COUNT", color_discrete_sequence=px.colors.sequential.Agsunset_r) 
        st.plotly_chart(fig_bar_2)

#top user analysis
def top_user_year(df,years):
    top_uy= df[df["Years"]== years]
    top_uy.reset_index(drop = True,inplace = True)

    top_uyg = pd.DataFrame(top_uy.groupby(["states", "Quarter"])["RegisteredUsers"].sum())
    top_uyg.reset_index(inplace = True)

    fig_bar_1=px.bar(top_uyg, x="states", y="RegisteredUsers", hover_data= "Quarter", width=1000, height=800,
                       title= f"{years} REGISTERED USER",hover_name="states",color_discrete_sequence=px.colors.sequential.Blugrn_r)
    st.plotly_chart(fig_bar_1)
    return top_uy

    #top user states pincode analysis
def top_user_ys(df,state):
    top_uys= df[df["states"]==state]
    top_uys.reset_index(drop = True,inplace = True)

    fig_bar_1= px.bar(top_uys, x="Quarter", y= "RegisteredUsers",title="REGISTERED USER, PINCODE, QUARTER",
                       width= 1000, height=1000,color="RegisteredUsers", hover_data="pincodes",
                       color_continuous_scale=px.colors.sequential.Magenta)
    st.plotly_chart(fig_bar_1)

def top_chart_ta(table_name):
    #mysql connection
    connection = pymysql.connect(
                host="localhost",
                user="root",
                password="adhi",
                database="phonepe")

    connect_data=connection.cursor()

    #plot 1
    query1 = f'''SELECT states, SUM(transaction_amount) AS transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_amount DESC
                LIMIT 10;
             '''

    connect_data.execute(query1)
    table = connect_data.fetchall()
    connection.commit()

    df_1 = pd.DataFrame(table,columns=("states","transaction_amount"))

    col1,col2=st.columns(2)
    with col1:
        fig_bar_df1= px.bar(df_1, x="states", y= "transaction_amount",title="TOP 10 TRANSACTION AMOUNT",hover_name="states",
                            width= 500, height=550,color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_bar_df1)

    #plot 2
    query2 = f'''SELECT states, SUM(transaction_amount) AS transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_amount 
                LIMIT 10;
              '''

    connect_data.execute(query2)
    table2 = connect_data.fetchall()
    connection.commit()

    df_2 = pd.DataFrame(table2,columns=("states","transaction_amount"))
    
    with col2:
        fig_bar_df2= px.bar(df_2, x="states", y= "transaction_amount",title="LAST 10 TRANSACTION AMOUNT",hover_name="states",
                            width= 500, height=550,color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(fig_bar_df2)

    #plot 3
    query3 = f'''SELECT states, AVG(transaction_amount) AS transaction_amount
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_amount;
             '''

    connect_data.execute(query3)
    table3 = connect_data.fetchall()
    connection.commit()

    df_3 = pd.DataFrame(table3,columns=("states","transaction_amount"))

    fig_bar_df3= px.bar(df_3, y="states", x= "transaction_amount",title="AVERAGE TRANSACTION AMOUNT",hover_name="states",orientation="h",
                        width=1000, height=650,color_discrete_sequence=px.colors.sequential.Bluered_r)
    st.plotly_chart(fig_bar_df3)

def top_chart_t_count(table_name):
    #mysql connection
    connection = pymysql.connect(
                host="localhost",
                user="root",
                password="adhi",
                database="phonepe")

    connect_data=connection.cursor()

    #plot 1
    query1 = f'''SELECT states, SUM(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count DESC
                LIMIT 10;
             '''

    connect_data.execute(query1)
    table = connect_data.fetchall()
    connection.commit()

    df_1 = pd.DataFrame(table,columns=("states","transaction_count"))

    col1,col2=st.columns(2)
    with col1:
        fig_bar_df1= px.bar(df_1, x="states", y= "transaction_count",title="TOP 10 TRANSACTION COUNT",hover_name="states",
                            width= 500, height=550,color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_bar_df1)

    #plot 2
    query2 = f'''SELECT states, SUM(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count 
                LIMIT 10;
              '''

    connect_data.execute(query2)
    table2 = connect_data.fetchall()
    connection.commit()

    df_2 = pd.DataFrame(table2,columns=("states","transaction_count"))

    with col2:
        fig_bar_df2= px.bar(df_2, x="states", y= "transaction_count",title="LAST 10 TRANSACTION COUNT",hover_name="states",
                            width= 500, height=550,color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(fig_bar_df2)

    #plot 3
    query3 = f'''SELECT states, AVG(transaction_count) AS transaction_count
                FROM {table_name}
                GROUP BY states
                ORDER BY transaction_count;
             '''

    connect_data.execute(query3)
    table3 = connect_data.fetchall()
    connection.commit()

    df_3 = pd.DataFrame(table3,columns=("states","transaction_count"))

    fig_bar_df3= px.bar(df_3, y="states", x= "transaction_count",title="AVERAGE TRANSACTION COUNT",hover_name="states",orientation="h",
                        width= 1000, height=650,color_discrete_sequence=px.colors.sequential.Bluered_r)
    st.plotly_chart(fig_bar_df3)

def top_chart_register_user(table_name,state):
    #mysql connection
    connection = pymysql.connect(
                host="localhost",
                user="root",
                password="adhi",
                database="phonepe")

    connect_data=connection.cursor()

    #plot1
    query1 = f'''SELECT districts, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers DESC
                LIMIT 10;
             '''

    connect_data.execute(query1)
    table = connect_data.fetchall()
    connection.commit()

    df_1 = pd.DataFrame(table,columns=("districts","RegisteredUsers"))

    col1,col2=st.columns(2)
    with col1:
        fig_bar_df1= px.bar(df_1, x="districts", y= "RegisteredUsers",title="TOP 10 REGISTERED USER",hover_name="districts",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_bar_df1)

    #plot 2
    query2 = f'''SELECT districts, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers
                LIMIT 10;
             '''

    connect_data.execute(query2)
    table = connect_data.fetchall()
    connection.commit()

    df_2 = pd.DataFrame(table,columns=("districts","RegisteredUsers"))

    with col2:
        fig_bar_df2= px.bar(df_2, x="districts", y= "RegisteredUsers",title="TOP 10 REGISTERED USER",hover_name="districts",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(fig_bar_df2)

    #plot 3
    query3 = f'''SELECT districts, AVG(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY RegisteredUsers;
             '''

    connect_data.execute(query3)
    table = connect_data.fetchall()
    connection.commit()

    df_3 = pd.DataFrame(table,columns=("districts","RegisteredUsers"))

    fig_bar_df3= px.bar(df_3, x="districts", y= "RegisteredUsers",title="AVERAGE REGISTERED USER",hover_name="districts",
                        width= 1000, height=650,color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig_bar_df3)

def top_chart_appopens(table_name,state):
    #mysql connection
    connection = pymysql.connect(
                host="localhost",
                user="root",
                password="adhi",
                database="phonepe")


    connect_data=connection.cursor()

    #plot1
    query1 = f'''SELECT districts, SUM(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states='{state}'
                GROUP BY districts
                ORDER BY AppOpens DESC
                LIMIT 10;
             '''

    connect_data.execute(query1)
    table = connect_data.fetchall()
    connection.commit()

    df_1 = pd.DataFrame(table,columns=("districts","AppOpens"))

    col1,col2=st.columns(2)
    with col1:
        fig_bar_df1= px.bar(df_1, x="districts", y= "AppOpens",title="TOP 10 APPOPENS USER",hover_name="districts",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_bar_df1)

    #plot 2
    query2 = f'''SELECT districts, SUM(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY AppOpens
                LIMIT 10;
             '''

    connect_data.execute(query2)
    table = connect_data.fetchall()
    connection.commit()

    df_2 = pd.DataFrame(table,columns=("districts","AppOpens"))

    with col2:
        fig_bar_df2= px.bar(df_2, x="districts", y= "AppOpens",title="TOP 10 APPOPENS USER",hover_name="districts",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(fig_bar_df2)

    #plot 3
    query3 = f'''SELECT districts, AVG(AppOpens) AS AppOpens
                FROM {table_name}
                WHERE states= '{state}'
                GROUP BY districts
                ORDER BY AppOpens;
             '''

    connect_data.execute(query3)
    table = connect_data.fetchall()
    connection.commit()

    df_3 = pd.DataFrame(table,columns=("districts","AppOpens"))

    fig_bar_df3= px.bar(df_3, x="districts", y= "AppOpens",title="AVERAGE APPOPENS USER",hover_name="districts",
                        width=1000 , height=650,color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig_bar_df3)

def top_chart_top_register_users(table_name):
    #mysql connection
    connection = pymysql.connect(
                host="localhost",
                user="root",
                password="adhi",
                database="phonepe")

    connect_data=connection.cursor()

    #plot1
    query1 = f'''SELECT states, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                GROUP BY states
                ORDER BY RegisteredUsers DESC
                LIMIT 10;
             '''

    connect_data.execute(query1)
    table = connect_data.fetchall()
    connection.commit()

    df_1 = pd.DataFrame(table,columns=("states","RegisteredUsers"))

    col1,col2=st.columns(2)
    with col1:
        fig_bar_df1= px.bar(df_1, x="states", y= "RegisteredUsers",title="TOP 10 REGISTERED USER",hover_name="states",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_bar_df1)

    #plot 2
    query2 = f'''SELECT states, SUM(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                GROUP BY states
                ORDER BY RegisteredUsers 
                LIMIT 10;
             '''

    connect_data.execute(query2)
    table = connect_data.fetchall()
    connection.commit()

    df_2 = pd.DataFrame(table,columns=("states","RegisteredUsers"))

    with col2:
        fig_bar_df2= px.bar(df_2, x="states", y= "RegisteredUsers",title="LAST 10 REGISTERED USER",hover_name="states",
                            width= 600, height=650,color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(fig_bar_df2)

    #plot 3
    query3 = f'''SELECT states, AVG(RegisteredUsers) AS RegisteredUsers
                FROM {table_name}
                GROUP BY states
                ORDER BY RegisteredUsers;
             '''

    connect_data.execute(query3)
    table = connect_data.fetchall()
    connection.commit()

    df_3 = pd.DataFrame(table,columns=("states","RegisteredUsers"))

    fig_bar_df3= px.bar(df_3, x="states", y= "RegisteredUsers",title="AVERAGE REGISTERED USER",hover_name="states",
                        width= 1000, height=650,color_discrete_sequence=px.colors.sequential.Blues_r)
    st.plotly_chart(fig_bar_df3)


#streamlit code
st.set_page_config(layout="wide")
st.title(":violet[PHONEPE DATA VISUALIZATION AND EXPLORATION]")


with st.sidebar:

    select=option_menu("Main Menu",["HOME","DATA EXPLORATION","TOP CHARTS"])

if select == "HOME":
    col1,col2= st.columns(2)

    with col1:
        st.header("PHONEPE")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("****Credit & Debit card linking****")
        st.write("****Bank Balance check****")
        st.write("****Money Storage****")
        st.write("****PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.image(Image.open(r"C:\Users\study\Downloads\vs code\phonepe image.jpg"),width= 600)

    col3,col4= st.columns(2)
    
    with col3:
        st.image(Image.open(r"C:\Users\study\Downloads\vs code\phonepe image1.webp"),width= 400)

    with col4:
        st.write("****Easy Transactions****")
        st.write("****One App For All Your Payments****")
        st.write("****Your Bank Account Is All You Need****")
        st.write("****Multiple Payment Modes****")
        st.write("****PhonePe Merchants****")
        st.write("****Multiple Ways To Pay****")
        st.write("****1.Direct Transfer & More****")
        st.write("****2.QR Code****")
        st.write("****Earn Great Rewards****")

    col5,col6= st.columns(2)

    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instantly & Free****")

    with col6:
        st.image(Image.open(r"C:\Users\study\Downloads\vs code\phonepe image2.webp"),width= 600)

elif select == "DATA EXPLORATION":

    tab1,tab2,tab3=st.tabs(["Aggregated Analysis","Map Analysis","Top Analysis"])
    with tab1:
        method=st.radio("Select The Method",["Aggregated Insurance Analysis","Aggregated Transaction Analysis","Aggregated User Analysis"])
        if method == "Aggregated Insurance Analysis":

            col1,col2=st.columns(2)
            with col1:   
                years =st.slider("SELECT THE YEAR",aggregated_insurance_df["Years"].min(),aggregated_insurance_df["Years"].max(),aggregated_insurance_df["Years"].min())
            tac_y = ty_count_amount(aggregated_insurance_df,years)

            col1,col2=st.columns(2)
            with col1:
                Quarters =st.slider("SELECT THE QUARTER",tac_y["Quarter"].min(),tac_y["Quarter"].max(),tac_y["Quarter"].min())
            ty_Q_count_amount(tac_y, Quarters)

        elif method == "Aggregated Transaction Analysis":
            
            col1,col2=st.columns(2)
            with col1:   
                years =st.slider("SELECT THE YEAR",aggregated_transaction_df["Years"].min(),aggregated_transaction_df["Years"].max(),aggregated_transaction_df["Years"].min())
            at_tac_y=ty_count_amount(aggregated_transaction_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The State",at_tac_y["states"].unique())

            aggregated_transaction_type(at_tac_y,states)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE QUARTER",at_tac_y["Quarter"].min(),at_tac_y["Quarter"].max(),at_tac_y["Quarter"].min())
            aggre_at_tac_y_q = ty_Q_count_amount(at_tac_y, Quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The State_Type",aggre_at_tac_y_q["states"].unique())
            aggregated_transaction_type(aggre_at_tac_y_q,states)
        
        elif method == "Aggregated User Analysis":
            col1,col2=st.columns(2)
            with col1:
                years =st.slider("SELECT THE YEAR",aggregated_user_df["Years"].min(),aggregated_user_df["Years"].max(),aggregated_user_df["Years"].min())
            aggre_user_y=aggre_user_year(aggregated_user_df,years)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE QUARTER",aggre_user_y["Quarter"].min(),aggre_user_y["Quarter"].max(),aggre_user_y["Quarter"].min())
            aggre_user_yq = aggre_user_year_q(aggre_user_y, Quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The State_Type",aggre_user_yq["states"].unique())
            aggre_user_year_qs(aggre_user_yq, states)

    with tab2:
        method2=st.radio("Select The Method",["Map Insurance Analysis","Map Transaction Analysis","Map User Analysis"])

        if method2 == "Map Insurance Analysis":

            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Year",map_insurance_df["Years"].min(),map_insurance_df["Years"].max(),map_insurance_df["Years"].min())
            map_in_tac_y=ty_count_amount(map_insurance_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The State",map_in_tac_y["states"].unique())
            map_insu_district(map_in_tac_y,states)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE MAP_QUARTER",map_in_tac_y["Quarter"].min(),map_in_tac_y["Quarter"].max(),map_in_tac_y["Quarter"].min())
            map_insu_tac_yq = ty_Q_count_amount(map_in_tac_y, Quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The MAP_yQ_State",map_insu_tac_yq ["states"].unique())
            map_insu_district(map_insu_tac_yq ,states)
            
        elif method2 == "Map Transaction Analysis":

            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Year",map_transanction_df["Years"].min(),map_transanction_df["Years"].max(),map_transanction_df["Years"].min())
            map_trans_tac_y=ty_count_amount(map_transanction_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The State",map_trans_tac_y["states"].unique())
            map_insu_district(map_trans_tac_y,states)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE MAP_QUARTER",map_trans_tac_y["Quarter"].min(),map_trans_tac_y["Quarter"].max(),map_trans_tac_y["Quarter"].min())
            map_trans_tac_yq  = ty_Q_count_amount(map_trans_tac_y, Quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The MAP_yQ_State",map_trans_tac_yq ["states"].unique())
            map_insu_district(map_trans_tac_yq ,states)

        elif method2 == "Map User Analysis":
            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Year",map_user_df["Years"].min(),map_user_df["Years"].max(),map_user_df["Years"].min())
            map_user_y = map_user_year(map_user_df,years)

            col1,col2=st.columns(2)
            with col1:
                Quarters =st.slider("SELECT THE MAP_USER_QUARTER",map_user_y["Quarter"].min(),map_user_y["Quarter"].max(),map_user_y["Quarter"].min())
            map_user_yq = map_user_year_quarter(map_user_y,Quarters)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The MAP_USER_STATES",map_user_yq ["states"].unique())
            map_user_year_quarter_states(map_user_yq ,states)


    with tab3:
        method3=st.radio("Select The Method",["Top Insurance Analysis","Top Transaction Analysis","Top User Analysis"])
        if method3 == "Top Insurance Analysis":

            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Insurance Year",top_insurance_df["Years"].min(),top_insurance_df["Years"].max(),top_insurance_df["Years"].min())
            Top_insu_y=ty_count_amount(top_insurance_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The TOP_INSURANCE_STATES",Top_insu_y  ["states"].unique())
            top_in_year_states(Top_insu_y ,states)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE TOP INSURANCE QUARTER",Top_insu_y["Quarter"].min(),Top_insu_y["Quarter"].max(),Top_insu_y["Quarter"].min())
            top_insu_y_q=ty_Q_count_amount(Top_insu_y, Quarters)
            
        elif method3 == "Top Transaction Analysis":
            
            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Transaction Year",top_transaction_df["Years"].min(),top_transaction_df["Years"].max(),top_transaction_df["Years"].min())
            Top_trans_y_ta =ty_count_amount(top_transaction_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The TOP_TRANSACTION_STATES",Top_trans_y_ta ["states"].unique())
            top_in_year_states(Top_trans_y_ta  ,states)

            col1,col2=st.columns(2)

            with col1:
                Quarters =st.slider("SELECT THE TOP TRANSACTION QUARTER",Top_trans_y_ta["Quarter"].min(),Top_trans_y_ta["Quarter"].max(),Top_trans_y_ta["Quarter"].min())
            top_trans_y_q=ty_Q_count_amount(Top_trans_y_ta , Quarters)

        elif method3 == "Top User Analysis":
            col1,col2=st.columns(2)
            with col1:   
                years = st.slider("Select The Top User Year",top_user_df["Years"].min(),top_user_df["Years"].max(),top_user_df["Years"].min())
            top_user_y=top_user_year(top_user_df,years)

            col1,col2=st.columns(2)
            with col1:
                states=st.selectbox("Select The Top_User_States",top_user_y["states"].unique())
            top_user_ys(top_user_y,states)
            

elif select == "TOP CHARTS":
     question= st.selectbox("Select the Question",["1. Transaction Amount and Count of Aggregated Insurance",
                                                    "2. Transaction Amount and Count of Map Insurance",
                                                    "3. Transaction Amount and Count of Top Insurance",
                                                    "4. Transaction Amount and Count of Aggregated Transaction",
                                                    "5. Transaction Amount and Count of Map Transaction",
                                                    "6. Transaction Amount and Count of Top Transaction",
                                                    "7. Transaction Count of Aggregated User",
                                                    "8. Registered users of Map User",
                                                    "9. App opens of Map User",
                                                    "10.Registered users of Top User",
                                                    ])
     if question=="1. Transaction Amount and Count of Aggregated Insurance":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("aggre_insurance")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("aggre_insurance")

     elif question=="2. Transaction Amount and Count of Map Insurance":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("map_insurance")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("map_insurance")

     elif question=="3. Transaction Amount and Count of Top Insurance":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("Top_insurance")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("Top_insurance")

     elif question=="4. Transaction Amount and Count of Aggregated Transaction":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("aggre_transaction")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("aggre_transaction")

     elif question=="5. Transaction Amount and Count of Map Transaction":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("map_transaction")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("map_transaction")

     elif question=="6. Transaction Amount and Count of Top Transaction":
         
         st.subheader("TRANSACTION AMOUNT")
         top_chart_ta("top_transaction")

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("top_transaction")

     elif question=="7. Transaction Count of Aggregated User":

         st.subheader("TRANSACTION COUNT")
         top_chart_t_count("aggre_user")

     elif question=="8. Registered users of Map User":
         
         states=st.selectbox("select the state",map_user["states"].unique())
         st.subheader("REGISTERED USER")
         top_chart_register_user("map_user",states)

     elif question=="9. App opens of Map User":
         
         states=st.selectbox("select the state",map_user["states"].unique())
         st.subheader("APPOPENS")
         top_chart_register_user("map_user",states)

     elif question=="10.Registered users of Top User":
         
         st.subheader("REGISTERED USER")
         top_chart_top_register_users("top_user")
     


import numpy as npy
import pandas as pda
import matplotlib.pylab as ply
import pymysql

#连接数据库
conn = pymysql.connect("localhost", "root", "root", "dangdang")
sql = "select * from book1"
sqlList = pda.read_sql(sql,conn)
# print(sqlList)

data=sqlList['评论数']/sqlList['价格']
sqlList['比例']=data
file="./newDangdang.csv"
sqlList.to_csv(file,index=False)


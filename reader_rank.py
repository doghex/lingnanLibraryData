import re
import pymysql
#用于往数据库录入借阅者排行数据
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="usbw",db="librarydata",port=3307)
file_source=open('./Text/put.html','r',encoding='UTF-8')
file_data=file_source.read()
pattern=re.compile(r'年份:(.*)\n排名：(.*)\n姓名：(.*)\n学院：(.*)\n身份：(.*)\n借阅次数：(.*)\n')
file_steam=pattern.findall(file_data)
for line_steam in file_steam:    
    sql_write = "insert into reader_ranking(date,rank,name,college,identity,borrownum) values('%s','%s','%s','%s','%s','%s')" % (line_steam[0],line_steam[1],line_steam[2],line_steam[3],line_steam[4],line_steam[5])
    sql_check = "SELECT *  FROM `reader_ranking` WHERE `date` LIKE '%s' AND `rank` LIKE '%s' AND `name` LIKE '%s' AND `college` LIKE '%s' AND `identity` LIKE '%s' AND `borrownum` LIKE '%s'"% (line_steam[0],line_steam[1],line_steam[2],line_steam[3],line_steam[4],line_steam[5])
    if conn.query(sql_check)==0:
        conn.query(sql_write)
        conn.autocommit(1)
        print(line_steam)
print("over")
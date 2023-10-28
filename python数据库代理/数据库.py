# coding=utf-8
import  requests
import pymysql

# 连接到MySQL数据库
db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="proxy"
)

# 创建游标对象
cursor = db.cursor()

coursor2 = db.cursor()

coursor2.execute("SELECT ip FROM ip ;")

coursor3 = coursor2.fetchall()

print("数据为:", coursor3)

# # 打开ip.txt文件并逐行读取IP数据
# with open(r"C:\Users\21016.LAPTOP-KGP1GRG0\Desktop\ip.txt", "r") as file:
#     for line in file:
#         ip = line.strip()
#
#         # 将IP数据插入到ip表中
#         sql = "INSERT INTO ip (count, ip) VALUES (%s, %s)"
#         values = (len(ip), ip)
#         cursor.execute(sql, values)

# 提交更改并关闭连接
db.commit()
cursor.close()
db.close()
#

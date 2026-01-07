import pymysql
import time

# Retry logic
connection = None
while not connection:
    try:
        print("Connecting to MySQL...")
        connection = pymysql.connect(
            host='db',
            user='root', 
            password='0000',
            port=3306,
            database="titanic",
            cursorclass=pymysql.cursors.DictCursor
        )
        # connection = pymysql.connect(
        #     host='localhost',
        #     user='root', 
        #     password='P@ssw0rd',
        #     port=3306,
        #     database="my_titanic",
        #     cursorclass=pymysql.cursors.DictCursor
        # )
    except pymysql.err.OperationalError:
        print("MySQL is not ready yet. Waiting 5 seconds...")
        time.sleep(5)

print("Connected successfully!")
# connection = pymysql.connect(
#     host='mysql_container01',
#     user='root', 
#     password='user01234',
#     port=3306,
#     database="my_titanic",
#     cursorclass=pymysql.cursors.DictCursor
# )
with connection.cursor() as cursor:
    sql = "SELECT * FROM full_passengers;"
    cursor.execute(sql)
    databases = cursor.fetchall()

print(type(databases))
print(f"第一筆是\n {databases[0]}")
print(f"共 {len(databases)} 筆")

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
# from urllib.parse import quote_plus
# import requests

# 建立 Flask 伺服器
app = Flask(__name__, static_folder="static")

# 自動處理 CORS
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


CORS(app)
@app.route("/titanic")
def titanic():

    resp = jsonify(databases)
    return resp
if __name__ == "__main__":
    # 開發測試用
    app.run(
        host="0.0.0.0", # 允許外部存取
        port=5000, # 服務 port 號
        debug=True # 除錯模式 (開發時使用，正式上線請移除或設為 False)
    )

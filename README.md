# 🛳️ **Titanic Docker 專案（前後端＋資料庫整合）**  共 1309 筆資料

本專案使用 Docker + Docker Compose，整合：

- MySQL（Titanic 資料庫）  
- Flask API（後端）  
- HTML 前端頁面（顯示 Titanic 資料）

---

## 專案結構
```text
titanic_combine-main
.
├── db
│   └── init
│       └── 01_titanic_dump.sql
├── docker-compose.yml
├── mysql_folder
│   ├── Dockerfile
│   └── pymysql_flask.py
├── python_folder
│   ├── Dockerfile
│   └── pymysql_flask.py
├── README.md
└── static
    └── index.html

6 directories, 8 files

---
````


## 步驟說明
```````
Step 1：下載專案
clone <URL>  # 下載檔案
cd <Repo 資料夾名稱>


Step 2：建置並啟動 Docker bash
docker compose up -d --build
如果看到沒有 error，就代表成功，例如：
 ✔ Image python3_image01 Built
 ✔ Container mysql8 Healthy
 ✔ Container titanic_combine-main-python_app-1 Running
 ✔ Container titanic_frontend Running

Step 3：查看容器狀態
docker compose ps
應該看到：
MySQL (mysql:8.0.44)：Healthy [::]:3307->3306/tcp
Flask (python3_image01)：Up [::]:5000->5000/tcp
titanic_frontend（nginx:alpine）: Up [::]:8080->80/tcp


Step 4：
檢查 API 回應
curl http://localhost:5000/titanic

或直接開啟瀏覽器，即可看到前端頁面：
http://localhost:8080/




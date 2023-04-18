<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://vuejs.org/images/logo.png" alt="Vue logo"></a></p>

## django_vue_vote_web
採用前後端分離開發一個簡單的投票網頁，
前端使用Vue3，後端使用Django

## Demo
https://user-images.githubusercontent.com/62460653/232187199-a2ec1568-e8fe-45f7-a3f6-dd08ba51ee1c.mp4


## 架構、安全性配置說明

**架構**
- 採用前後端分離開發
- Web Server = Django 
- Application Server = Django 中的 App
- 關聯式資料庫 = MySQL


**技術**
- 前端開發使用Vue3
- 後端開發使用Python3.7 ,框架為Django
- 使用Restful風格建立後端服務
- 資料庫配置放在backend/vote_web/mainapi/models.py中
- 並將架構分為展示層、業務層、資料層、共用層


**安全性配置**
- 使用Django內建ORM方式操作資料庫避免SQL injection
- 將Django中的settings.py配置檔案中設定SESSION_COOKIE_HTTPONLY設為True來防止前端出現錯誤訊息，減少XSS攻擊風險
- 在settings.py配置檔案中設定CORS_ORIGIN_WHITELIST，讓前端vue可以呼叫到django的api，同時又可防止跨站攻擊(CSRF)及跨網站腳本攻擊(XSS)
- 使用 django套件 transaction.atomic() ,使關連式資料庫遵守ACID原則


## 快速測試

### 後端 :

步驟一 : Clone此專案

步驟二 : 到官方網站下載Python並安裝，本專案使用Python3.7

[下載連結](https://www.python.org/downloads/)

步驟三 : 開啟本專案backend/vote_web/vote_web/settings檔案，找到以下內容修改NAME(MySQL的資料庫名)、USER(使用者名稱)、PASSWORD(使用者密碼)的value值進行資料庫的初始設定
```bash
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'XXXX',
        'USER': 'XXXX',
        'PASSWORD': 'XXXX',
        'HOST': '',
        'PORT': '3306',
    }
}
```
步驟四 : 
開啟CMD命令提式字元，將CMD命令提式字元切換到本專案backend/路徑， 輸入以下指令安裝Django及相關套件
```bash
$ pip install -r requirements.txt
```

步驟五 : 依序輸入以下兩行命令進行資料庫的更新
```bash
$ python manage.py makemigrations
$ python manage.py migrate       

```

步驟六 :
輸入以下指令啟動後端服務在8000port
```bash
$ python manage.py runserver
```

### 前端 :

步驟一 :
先到官網下載node.js

[下載連結](https://nodejs.org/zh-tw/download)


步驟二 :
開啟CMD命令提式字元，將CMD命令提式字元切換到本專案frontend\django_vue路徑下， 輸入以下指令安裝npm及相關套件
```bash
$ npm install
```

步驟三 : 
運行前端vue服務
```bash
$ npm run dev
```
會運行在vite默認端口5173

訪問 http://localhost:5173/ 就可管理投票項目

訪問 http://localhost:5173/vote 就可以進行投票

## 查看投票細節

如要查看投票細節，可創建Django超級使用者登入後，即可在管理頁面看到細節，創建方式如下。在backend/vote_web路徑下，cmd命令列輸入以下指令

```bash
$ python manage.py createsuperuser
```

輸入帳號密碼email後即可在 http://localhost:8000/admin 進行登入



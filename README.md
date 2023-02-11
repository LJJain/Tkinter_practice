# Tkinter 練習

## 教學網址
- link: https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV

## CODE
- link: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

## 日誌:
- 2023.01.07
    1. (已解決)import mysql.connector 連接MSQL會出現:Authentication plugin ‘caching_sha2_password’ is not supported問題
        - 改用 import pymysql
        - 參考資料:https://medium.com/@fadeawaygod/%E7%94%A8python-call-mysql-8-0%E5%87%BA%E7%8F%BEauthentication-plugin-caching-sha2-password-is-not-supported-39c5b907aed7

- 2023.01.10
    1. 將Tkinter 轉 EXE  
        (1) 安裝 pyinstaller (pip install pyinstaller)  
        (2) pyinstaller.exe --onefile --icon=(icon file) (filename.py)

- 2023.02.10
    1.  後續檔案利用檔案23作為編寫方式
    2.  建立圓角(圖形)按鈕:
        Button(frame, image=image, borderwidth=0, command=command)
        - 利用 borderwidth=0 去除邊框即可呈現圖像式按鈕(button)
    
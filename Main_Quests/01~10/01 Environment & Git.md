# 虛擬環境設置 (Python venv)
為了不讓不同專案互相干擾，我們開啟了隔離空間：
建立傳送門： python -m venv venv
進入空間：
Windows: .\venv\Scripts\activate
Mac/Linux: source venv/bin/activate
## 建立一個簡單的腳本來確認環境運行：
```
# main.py 
print("Hello, Information Security World!")
```
## Git Local Commit
初始化倉庫： git init
標記變更： git add .
存檔： git commit -m " "

pip freeze > requirements.txt
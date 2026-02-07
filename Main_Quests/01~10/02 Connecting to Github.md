# 建立遠端節點
在 GitHub 上建立一個名為 My-Security-Journey 的新倉庫。
連結在地與雲端：
```git remote add origin [你的 GitHub 倉庫 URL]```

# 進度上傳 (The Push)
將本地的分支重新命名並推送到遠端：
1. 切換主分支： git branch -M main
2. 全力傳送： git push -u origin main

記得建立 .gitignore 檔案，不要把 venv（虛擬環境資料夾）傳上去，那是你的私人工作台，不應該放在倉庫裡。
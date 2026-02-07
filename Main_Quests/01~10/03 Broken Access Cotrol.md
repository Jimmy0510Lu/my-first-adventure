# A01:2021-Broken Access Control
    核心問題： 伺服器端過度信任用戶輸入（Trusting client-side input）。權限判斷邏輯不應暴露在用戶可修改的參數中。

管理員身分未受保護 可能遭竄改或刪除
在 portswigger 實驗室中，管理員面板就沒有受到保護 
在造訪robots.txt時找到 Disallow: /administrator-panel
導致carlos可以被刪除

安全性誤設定(Security Misconfiguration)
開發者以為只要不把連結放在網頁上，別人就找不到
但疏忽了 robots.txt本身就是公開的
/*很多網站會在根目錄放一個 robots.txt，告訴搜尋引擎爬蟲哪些地方「不該去」。*/

## 漏洞發現
在http請求的cookie發現Admin=false
可以推論系統可能直接信任前端回傳的參數決定使用者全限，而非在後端（Session/Database）進行驗證

## 攻擊步驟
1. 攔截 (Intercept)： 使用 Burp Suite 攔截發往伺服器的請求。
2. 篡改 (Manipulation)： 將 Admin=false 修改為 Admin=true。
3. 重放 (Replay)： 利用 Repeater 工具多次發送修改後的請求，確認伺服器響應中出現了 /admin 導覽標籤。
4. 執行 (Execution)： 成功以管理員身份訪問 /admin 頁面，並執行刪除 carlos 用戶的操作。

## 防禦建議
* 最小權限原則： 權限驗證必須在伺服器端（Server-side）進行，並與不可篡改的 Session 綁定。
* 移除敏感參數： 不要將 Admin、Role 等敏感標籤放在 Cookie 或隱藏欄位（Hidden fields）中傳輸。
* 強身份驗證： 使用成熟的權限管理框架（如 Spring Security 或 Django Auth），確保每個受保護的路由都有嚴格的權限過濾器。

補充: 常見路徑
/admin
/administrator
/login
/dashboard

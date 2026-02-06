# main.py
def welcome():
    print("--- 歡迎來到冒險者計算機 ---")
    #name = input("請輸入你的冒險者稱號: ")
    #print(f"你好, {name}! 準備好進行第一次運算了嗎?")
    num_str = "100"
    result = int(num_str) / 5
    print(f"計算結果: 100 除以 5 等於 {result}")
    
    
if __name__ == "__main__":
    welcome()
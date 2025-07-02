
import random  #ランダムモジュール　（ランダム機能）を使う宣言
import time   #時間モジュール　（時間機能）を使う宣言

start_time = time.time()
print(f"開始時刻: {start_time}")

byousuu = random.randint(3, 5)
print((f"待つ秒数：{byousuu}"))
time.sleep(byousuu)

print("!!!!!!")
input("エンターキーを押して下さい：")

end_time = time.time()
print(f"終了時刻: {end_time}")

kakatta_byousuu = end_time - start_time
print(f"かかった時間: {kakatta_byousuu}")
if kakatta_byousuu < 0.01:
    print("不正をしていますね！")

#print(f"かかった秒数が０.０１")
print("エンターキーが押されました。")








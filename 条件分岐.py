input_member = input("会員の場合はYを入れてください: ")
input_age = input("何歳ですか？: ")

#年齢を入力値を整数に変換
age = int(input_age)

#会員と非会員でぶんき処理
if input_member == "Y":
    if age < 18:
        price = 100
    
    else:
        price = 1000

else:
    if age < 18:
        price = 1000

    else:
        price = 2000

print("料金は: ", price)
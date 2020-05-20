#密碼重試程式

#先在程式碼中 設定好密碼 password = 'a123456'
#讓使用者【最多輸入3次密碼】
#不對的話，就印出"密碼錯誤!還有_次機會"
#對的話，就印出"登入成功"

password = 'a123456'
x = 1
y = 3
while x < 4:
    a = input('請輸入密碼: ')
    if a == password:
        print('登入成功')
        break
    elif a != password and x < 3 :
        x = x + 1
        y = y - 1
        print('密碼錯誤!還有',y,'次機會')	
    else:
        x = x + 1
        y = y - 1
        print('密碼錯誤!還有',y,'次機會')	
        print('你再也沒有機會了!!')
import re
with open('zhuce.txt','r') as f:
    xx = f.read()
x1 = re.findall(r'^\w+',xx,re.M)
x2 = re.findall(r'(\w+) (\w+)$',xx,re.M)
print(x1)
print(x2)
dict1 = dict(zip(x1,x2))
print(dict1)
while 1:
    a = int(input('输入1注册2登入3注销4退出：'))
    if a == 1 :
        print('注册界面')
        while 1 :
            user = input('请输入账号:')
            if user in dict1:
                print('账号已存在')
            else:
                while 1 :
                    password = input('请输入密码:')
                    dict1[user] = password
                    if password == ''  or len(password)<6 :
                        print('密码不能为空或者小于6位')
                    else:
                        while 1 :
                            password2 = input('请确认密码:')
                            if password!=password2 :
                                print('输入的两次密码不相同')
                            else:
                                print('你注册的账号为',user,'密码为：',password)
                                tel = input('请绑定手机号:')

                                if tel == '' or len(tel)<11 :
                                    print('手机号不能为空或者小于11位')
                                else:
                                    dict1[user]=(password,tel)
                                    print('账号注册成功')
                                    with open('zhuce.txt','a') as f:

                                        f.write('\n'+user+' '+password+' '+tel)
                                break
                        break
            break



    elif a == 2 :
        print('欢迎来到登入界面')
        while 1:
            user = input('请输入您的账号')
            if user not in dict1:
                print('该账户不存在')
            else:
                while 1:
                    password = input('请输入您的密码')
                    if dict1[user][0] == password :
                        print('登入成功')
                    else:
                        print('密码错误，请重新输入密码或者选择修改密码')
                        while 1:
                            b = int(input('输入1重新输入密码，2修改密码'))
                            if b==1:
                                while 1:
                                    if dict1[user][0] == password:
                                        print('登入成功')
                                    else:
                                        while 1:
                                            password = input('请重新输入您的密码')
                                            if dict1[user][0] == password:
                                                print('登入成功')
                                                break
                                        break
                            elif b==2:
                                while 1:
                                    user = input('输入你的账号')
                                    if user not in dict1:
                                        print('该账户不存在')
                                    else:
                                        while 1:
                                            tel= input('输入你的手机号')
                                            if tel != dict1[user][1]:
                                                print('请输入正确的手机号')
                                            else:
                                                while 1:
                                                    password = input('请输入您的新密码(密码为六位）')
                                                    dict1[user][0] = password
                                                    if password == '' or len(password) < 6:
                                                         print('密码不能为空且不能小于6位')
                                                    else:
                                                        print('修改成功')
                                                        break#密码
                                                break#手机号
                                        break#账号
                            else:
                                print('请输入正确的数字。输入1重新输入密码，2修改密码')
                            break#1、2
                    break#密码
                break#账号




    elif a==3:
        print('欢迎来到注销界面')
        while 1:
            user = input('请输入您的账号')
            if user not in dict:
                print('该账户不存在')
            else:
                while 1:
                    password = input('请输入您的密码')
                    if dict[user][0] != password:
                        print('密码错误，请重新输入密码')
                    else:
                        while 1:
                            tel= input('输入你的手机号')
                            if dict[user][1] !=tel:
                                print('请输入正确的手机号')
                            else:
                                break
                        break
                dict1.pop(user)
                print('您的账号已注销')
                break


    else:
        print('退出')
        break
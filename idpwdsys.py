#x = int(input('輸入選項：'))
#
#t = 123 == '123'
#if (x ==1):
#    print('1')
#elif (x==2):
#    print('2')
#elif (x==3):
#    print('3')
#else:
#    print('other')
        
#
#x = 10
#t = ['國文', '英文', '數學']
#t2 = range(3,10,1)
#y = x in t2

#x = int(input('input:'))
#prime = False
#for i in range(2,x):
#    if (x%i==0):
#        prime = True
#        break
#if prime:
#    print('Not Prime')
#else:
#    print('Prime')
#s = 0
#count = 0
#x = int(input('input:'))
#while x!=-1:
#    s += x
#    count += 1
#    x = int(input('input:'))
#print('總成績：' + str(s) +'，平均成績：' + str(s/count))
#

#x = [1,2,3,4,5,6]
#x.insert(3, 'apple')
#x.append('apple')
#x.extend(x)
#y_tuple = ('1', '2',123)
#dic1 = {'國文':True,'英文':90, '數學':100}
#rr = dic1['國文']
#t1 = '國文' in dic1
#
#x_key = list(dic1.keys())
#x_value = list(dic1.values())
#
#rr = range(10)
#print(type(rr))
#
#def haha(x, y):
#    return x+y
#
#rr = haha(10, 100)

def inputidpwd(ID, PWD):
    with open('idpwd.txt', 'a') as f:
        f.write(str(ID)+'\n')
        f.write(str(PWD)+'\n')

def showidpwd():
    i = -1;
    title = ['帳號：', '密碼：']
    with open('idpwd.txt', 'r') as f:
        for line in f:
            i += 1
            print(title[i%2] + line, end='')
print('****************')
print('帳號、密碼管理系統')
print('1. 輸入帳號、密碼')
print('2. 顯示帳號、密碼')
print('3. 修改密碼')
print('0. 結束程式')
print('****************')
op = int(input('請輸入功能選項：'))
while op!=0:
    if op==1:
        ID = input('帳號：')
        PWD = input('密碼：')
        inputidpwd(ID, PWD)
    elif op==2:
        showidpwd()
    elif op==3:        
        print()
    else:
        print()
    print('****************')
    print('帳號、密碼管理系統')
    print('1. 輸入帳號、密碼')
    print('2. 顯示帳號、密碼')
    print('3. 修改密碼')
    print('0. 結束程式')
    print('****************')
    op = int(input('請輸入功能選項：'))



# Dict

dict_d = {'jo':1234, 'Bena':'haha', 'monkey':0000}
#print(dict_d['jo'])

dict_d2 = {'jo':123, 'Bena2':'haha', 'monkey2':0000}
dict_d.update(dict_d2)

#print('jo' in dict_d)

def haha():
    #print('haha')
    return 'haha'
'''
e = haha()
'''
def comman(va1=0, va2=4):
    'comman'
    print(va1*3 + va2*5)

comman('haha', '123')
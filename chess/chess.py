#Расставить N ферзей на квадратной доске N×N так, чтобы никакие два не били друг друга — очень непростая задача.
import random


def random_int_x(n):
    rand_x=random.randint(1,n) 
    return rand_x

def random_int_y( n):
    rand_y=random.randint(1,n) 
    return rand_y

def queen(n,arr_x,arr_y):

    x=arr_x
    y=arr_y


    for i in range(len(x)):
        for j in range(i+1,len(y)):

            if x[i]==x[j] or y[i]==y[j] or abs(x[i]-x[j])== abs(y[i]-y[j]):
                print('',x,'\n',y)
                return True 
    return False



def arr_size():
    n= 9
    choos=True
    mass_x=[]
    mass_y=[]
    
    for i in range(1,n):
        drop_while=0
        mass_x.append(random_int_x(n))
        mass_y.append(random_int_y(n))
        choos=queen(n,mass_x,mass_y)

        while choos==True:
            mass_x.pop(i-1)
            mass_y.pop(i-1)
            
            mass_x.append(random_int_x(n))
            mass_y.append(random_int_y(n))
            choos=queen(n,mass_x,mass_y)
            drop_while+=1
            if drop_while>2000:
                arr_size()
            

    print('Answer\n',mass_x,'\n',mass_y)


arr_size()
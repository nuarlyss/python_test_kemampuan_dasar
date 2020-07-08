def fun1():
    l = []
    
    s = input("Enter a member: ")

    l = list(s.split(" "))
        
    l.sort()
    
    for i in range(0, len(l)):
        for j in range(0,int(l[i])):
            print('*', end = '')
        print('\n')
            
fun1()

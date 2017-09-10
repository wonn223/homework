
# coding: utf-8

# In[66]:


def towerOfHanoi(Start,Auxiliary,Destination,N):
    #Start : 출발점, auxiliary: 경유점, Destination:도착점, N: 원판 수
    
    if N == 1:
        print("원판을 {}에서 {}로 옮겼습니다.".format(Start, Destination))
        return
    
    towerOfHanoi(Start,Destination,Auxiliary, N-1)
    towerOfHanoi(Start,Auxiliary,Destination,1)
    towerOfHanoi(Auxiliary,Start,Destination,N-1)
    return 

n = int(input("원판의 수를 입력해주세요:"))
towerOfHanoi('towerA','towerB','towerC',n)    


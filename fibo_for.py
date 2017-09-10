
# coding: utf-8

# In[111]:


#피보나치 수열 반복문으로 증명
# 1 1 2 3 5 8 13 21 34 55


# In[43]:


#for문
def fibo_for():
    li = [1, 1]
    for i in range(0,8) :
        li.append(li[i]+li[i+1])
        
    return li   
fibo_for()



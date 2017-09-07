
# coding: utf-8

# In[37]:


#- python list, 반복문 이용하여 binary search 구현하기
#- 오늘부터 과제 제출은 각자의 github에 homework 레포지토리를 만들어 하겠습니다.


# In[38]:


#바이널 탐색 전제조건 : 데이터를 설정해야하는데 이 때 반드시 정렬이 된 상태야 한다. 

li = [1,2,3,4,5]
#tu = (1,2,3,4,5) 튜플값 실행 가능

def binarysearch(data, target):
    '''
    data에서 target의 인덱스
    target이 없다면 None
    '''
    #start와 end에 '인덱스' 넣어주기    
    start = 0
    end = len(data) -1
    
    #(k*f(n), 최대 연산) 타켓이 1일때, 여러 번에 걸친 비교 과정으 리스트 첫 번째 요소까지 다다르는 경우를 상정
    while(start <= end):
        mid = (start + end) // 2
        if target > data[mid]: 
            start = mid +1
        #찾으려는 값이 중앙값보다 작으면 중앙값 이상의 값은 찾을 필요가 없으니까 폭을 좁히기 위해 end를 중앙값 앞으로 넘긴다
        
        elif target < data[mid]:
            end = mid - 1      
        #찾으려는 값이 중앙값보다 크다면 중앙값을 보다 오른쪽으로 이동시켜야 하므로 start를 mid 우측으로 옮긴다
        
        else:#결과값이 인덱스로 나와서 타켓과 다른 숫자가 나옴. 그래서 li[i]로 접근해서 타켓 값 출력
             return data[mid] 
                
    return None    


binarysearch(li,2)
#binarysearch(tu,3)


# In[39]:


## big-O
# 일종의 표기법. 연산 시간을 계산할 때 보통 결과가 가장 오래 걸리는 연산 조건을 기준으로 잡는다.
# 하지만 모든 연산이 오래 걸리는 것은 안디ㅏ.(ex 이진 검색에서 첫 검산에서 바로 원하는 값을 찾았을 때)
# 그래서 "어떤 계산이 완료되는데 걸리는 최대 예상치(k*f(n) // k: 연산 시도 횟수 n: 연산에 필요한 데이터 크기)가 있지만 
# 대개 그 최대치에 가지않고 f(n)의  big-o만큼 시간이 걸린다"는 것을 나타내기 위해 쓰인다. 표기는 O (log N) 이다.


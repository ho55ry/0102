# 모듈 로딩 --------------------------------------------------------------------------
import pandas as pd                 # 데이터분석용 패키지
import ex_pandas as mp     # 나의 모듈
# -----------------------------------------------------------------------------------

# mp.printSeries  # ex_pandas.py 에서 만들었던 함수 불러와서 사용
srr=pd.Series([11,22,33])
mp.printSeries(srr,'srr')

# ------------------------------------------------------------------------------------
# Series 객체의 요소 다루기 => index 사용
# [사용법] : 객체변수명[인덱스]
# ------------------------------------------------------------------------------------
data = list(range(5,31,5))
sr1=pd.Series(data)

# 요소 1개 읽기 => 변수명[index]
print('sr1[0] :',sr1[0])
print('sr1[5] :',sr1[5],type(sr1[5]))           # int64 타입으로 나옴

for idx in range(len(sr1)):
    print(f'sr1[{idx}] => {sr1[idx]}')
# for idx in sr1.index:                         # range(len(sr1)) = sr1.index 
#     print(f'sr1[{idx}] => {sr1[idx]}') 

# 요소 여러개 읽기 => 변수명[[idx1,idx2,]]
print(sr1[[0,2]],type(sr1[[0,2]]),sep='\n')     # series 타입으로 나옴
print(sr1[2:5],type(sr1[2:5]),sep='\n')         # 슬라이싱 변수명[이상:미만:step]
print(sr1[0:5:2],type(sr1[0:5:2]),sep='\n')     
print(sr1[[0]],type(sr1[[0]]),sep='\n')         # series 타입
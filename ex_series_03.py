# --------------------------------------------------------------------------
# 인덱스와 인덱스라벨(네임) 살펴보기
# - 인덱스 : 판다스 시스템에서 지정하는 정수형 RangeIndex 정수형 (0-base)
# - 인덱스 라벨(네임) : 시리즈 객체 생성시 지정하는 인덱스
# --------------------------------------------------------------------------
import pandas as pd

# Series 객체 생성 ----------------------------------------------------------
# 데이터 : 1~50사이의 3의 배수
# 인덱스 : 문자 'a'~'u'
# ---------------------------------------------------------------------------
data=list(range(3,21,3))
idx=['a','b','c','d','e','f'] # 인덱스 수랑 data수 같아야 실행됨 else 오류
mySr=pd.Series(data,index=idx,name='Score',dtype='float32')
print(mySr)

# 요소 읽기 => 변수명[인덱스]
print(mySr['a'],mySr[0]) # 인덱스 다른걸로 설정해도 정수형으로 있긴함
for idx in mySr.index: print(idx,mySr[idx],sep=' : ')

# 요소 여러개 읽기 => 변수명[[인덱스1, 인덱스2]]
print(mySr[['a','f']],mySr[[0,5]])
print(mySr[::2]) # 2단위로
# 범위지정 요소 읽기 => 슬라이싱
print(mySr[0:5])    # 정수형으로 슬라이싱하면 [이상:미만]인데
print(mySr['a':'f']) # 문자열 인덱스로 슬라이싱하면 [이상:이하]로 출력됨


# ==================================================================================
data=list(range(3,21,3))
idx=['a','b','c','d','e','f'] 
idx2=[11,22,33,44,55,66]
mySr2=pd.Series(data,index=idx2,name='Score')
print(mySr2)
print(mySr2[11])
import pandas as pd

# 시리즈 (series) 데이터 ------------------------------------------------------
# pandas.Series (데이터)
# 속성 (Attribute) : index, values, ndim, shape, ...
# ----------------------------------------------------------------------------
# Series 객체 속성 출력 함수
# printSeries
def printSeries(srObj,srObjname):
    print(srObjname,srObj,sep='\n')
    print(srObj[1])
    print(srObj.index)
    print(srObj.values)
    print(srObj.ndim)  
    print(srObj.shape) 
    print(type(srObj))


print(f'__name__ => {__name__}')

# __name__ : 매직 변수, 시스템에 값을 설정
# 해당 파이썬 파일이 실행 중 여부 확인
# 실행 중 ==> __main__
# import될 경우 => 파일명

if __name__ == '__main__':

    # 1) 리스트 형태 데이터 생성
    sr=pd.Series([10,20,30])
    printSeries(sr,'sr')


    # 2) 딕셔너리 형태 데이터 생성
    sr2=pd.Series({'name':'Shin','job':'student','loc':'Daegu'})
    printSeries(sr2,'sr2')

    # 3) 튜플 형태 데이터 생성
    sr3=pd.Series((11,22))
    printSeries(sr3,'sr3')
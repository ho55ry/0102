# ----------------------------------------------------------------------------------------------------------------------
# 예외 처리 (Exception Handling)
# 실행 중 발생되는 오류로 프로그램이 중단되는 것을 막아주기 위한 방법
# ----------------------------------------------------------------------------------------------------------------------
num1=10
try:
    num2=int(input('숫자 입력 : '))
    print(num1/num2)

except ValueError as ve:            # 1) 하나씩 적기
    print('error 1',ve)               # => 에러별로 다른 동작 필요할때 사용

except ZeroDivisionError as ze:
    print('error 2',ze)
    # pass # 오류 무시

# except(ZeroDivisionError, ValueError) as e:  # 2) 여러개 같이 적기
#     print('error',e)

except Exception as e:  # 3) 전체 다 포함하는 예외 처리
    print('error',e)    

# print('end')  # finally 전에 그냥 실행문 하나 들어있으니까 오류남
 
finally: 
    print(f'항상실행')

print('end')


# ----------------------------------------------------------------------------------------------------------------------
FILE='a.txt'
try:
    fp=False # or None
    fp=open(FILE,mode='x',encoding='utf-8') 
    fp.write(12345)
except FileExistsError as e:
    print('이미 존재하는 파일',e)
except FileNotFoundError as e:
    print('존재하지 않는 파일',e)
except Exception as e:          # 큰 범위가 밑으로 가게 (위에서 부터 순서대로 처리함)
    print('오류발생',e)
finally:
    if fp: fp.close()
    print('파일닫기')
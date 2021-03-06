#if문 : 조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 사용

#if문의 기본 구조
'''
if 조건문 :
    수행할 문장 1
    수행할 문장 2
    ...
else :
    수행할 문장 A
    수행할 문장 B
    ...
else문은 if문 없이 독립적으로 사용할 수 없다.
들여쓰기(indentation) : if문에 속하는 모든 문장에 들여쓰기를 해야 한다. tab/공백 X4
콜론(:) : if 조건문 뒤에는 반드시 콜론(:)이 붙는다.
'''

#비교연산자 -> boolean 값으로 반환
print("-" * 10, "비교 연산자", "-" * 10)
'''
x < y   : x가 y보다 작다
x > y   : x가 y보다 크다
x == y  : z와 y가 같다
x != y  : x와 y가 같지 않다
x >=y   : x가 y보다 크거나 같다
x <= y  : x가 y보다 작거나 같다
'''
#비교연산자를 사용한 money 예시



# and / or / not 연산자
print("\n" + "-" * 10, "and / or / not", "-" * 10)
'''
x or y      : x와 y 둘 중에 하나만 참이어도 참
x and y     : x와 y 모두 참이어야 참
not x       : x가 거짓이면 참
'''
#and/or/not 연산자를 사용한 money or card 예시




# x in 튜플/리스트/문자열, x not in 튜플/리스트/문자열  -> boolean값 출력
# x in s 예시
print("\n" + "-" * 10, "x in s 예시", "-" * 10)




#조건문에서 아무 일도 하지 않게 설정하고 싶을 때  : pass
# pass 예시
print("\n" + "-" * 10, "pass 예시", "-" * 10)





#elif
#elif는 이전 조건문이 거짓일 때 수행되고, 개수에 제한 없이 사용할 수 있다.
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어 가라
# elif를 사용하지 않은 예시
print("\n" + "-" * 10, "elif를 사용하지 않은 예시", "-" * 10)







#elif를 사용한 예시
print("\n" + "-" * 10, "elif를 사용한 예시", "-" * 10)






#if문을 한 줄로 작성하기
print("\n" + "-" * 10, "if문을 한 줄로 작성하기", "-" * 10)



#조건부 표현식 (conditional experssion) : 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
print("\n" + "-" * 10, "조건부 표현식", "-" * 10)

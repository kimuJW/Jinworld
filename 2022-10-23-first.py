str = input().upper()
str2 = list(set(str))  # 입력받은 문자열에서 중복값을 제거
list = []
for i in str2 :
    strc = str.count(i)
    list.append(strc)  # count 숫자를 리스트에 append

if list.count(max(list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = list.index(max(list))  # count 숫자 최대값 인덱스(위치)
    print(str2[max_index])
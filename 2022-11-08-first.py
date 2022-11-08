str = input().upper()
str2 = list(set(str))  # 입력받은 문자열에서 중복값을 제거
cnt_list = []
for i in str2 :
    cnt = str.count(i)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
    print('?')
else :
    max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
    print(str2[max_index])
# 주민등록번호
# 920902-1111111
# abcdef-1111111
# 이메일주소
# bnbnac@naver.com
# bnbnac@naver@com
# 차량번호
# 11가1234
# 123가1234
# 가나다123라마
# ip주소
# 192.168.0.1
# 1000.2000.3000.4000       정규식(RE) : 올바른 형식인지 구별하기 위함

import re
# 차량번호판은 4자리의 문자로 이루어져있다고 가정
# 4자리 중 3자리만 기억날때
# ca?e
# care cafe case cave
# caae, cabe, cace, cade, ... 
# use RE!

p = re.compile("ca.e") 
# (.)점은 하나의 문자를 의미함. ///ca.e///  cafe, cave | caffe
# (^)삿갓은 문자열의 시작을 의미함. ///^de///   desk, destination | fade
# ($)달러는 문자열의 끝을 의미함. ///se$///   case, base | face
# m = p.match("case")
# m2 = p.match("caffe")


# print(m2.group())
def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환
        print("m.string:", m.string)# 일치하는 문자열 ######### 괄호가 없다#########
        print("m.string():", m.start())# 일치하는 문자열의 시작 index
        print("m.string():", m.end())# 일치하는 문자열의 끝 index
        print("m.string():", m.span())# 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않았습니다.")

# m = p.match("careless") # 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # 주어진 문자열 중에 일치하는 게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst) 
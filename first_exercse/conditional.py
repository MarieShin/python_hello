"""
if 문 외 테스트
성적이 주어지고 60점 이상이면 패스 나머지는 불합격
"""

# score = 55
#
# if score > 60:
#     print('pass')
#
# else:
#     print('not pass')
#
#
# print('the end')

def check_score(score):
    if score >= 60:
        return 'pass'
    else:
        return 'not pass'

print(check_score(58))

def greater_less_equal_5 (answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

"""
단어를 입력받아서 (from console)
1. 문자가 아니면 "invalid word"출력 프로그램 종료
2. 첫 글자를 마지막으로 옮기고 "ay"를 추가
    ex) hello world -> ello worldhay
    ex) LosAngeles -> osAngelesLay
"""


def convert_word(a_word):
    """ 단어를 입력받아서 적절히 변경 """
    if len(a_word) > 0 and a_word.replace(" ", "").isalpha():
        add_last = 'ay'
        first_word = a_word[0:1]
        rest_word = a_word[1:]
        word = rest_word + first_word + add_last
        return word
    else:
        return 'invalid word'


a_word = input('단어를 하나 입력해 주세요: ')
print(convert_word(a_word))

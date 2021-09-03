from random import *
n = 1 # default

quiz_ans = randint(1, 1000)
print("[up & down 퀴즈 프로그램]\n* 컴퓨터가 1부터 1000까지 무작위로 숫자 하나를 지정합니다.\n* 숫자를 입력하면 컴퓨터가 지정한 숫자와 비교하여\n숫자의 크기에 따라 up / down을 표기합니다.\n* 기회는 10번입니다.")


while True:
    if n <= 10:
        opportunity = 11 - n
        ans1 = int(input("기회는 %s번 남았습니다. 숫자를 입력하세요: " %(opportunity)))
        if ans1 == quiz_ans:
            print("정답입니다.")
            break
        elif ans1 >= quiz_ans:
            print("down")
            n += 1
            continue
        else:
            print("up")
            n += 1
            continue
    else:
        print("기회를 모두 사용하셨습니다.")
        break
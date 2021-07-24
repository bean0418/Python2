f = open("C:/Users/user/Desktop/읽은 책 목록.txt", 'a')

while True:
    ans1 = input("[독서 활동 확인 프로그램]\n바탕화면에 읽은 책 목록.txt 파일이 추가되었습니다.\n* 읽은 책을 추가하시려면 추가를 입력해주세요.\n* 종료를 원하시면 종료를 입력해주세요.\n(추가/종료): ")

    if ans1 == "추가":
        book = input("추가하실 책의 이름을 입력해주세요: ")
        print("읽은 책 목록에 %s이(가) 추가되었습니다." %(book))
        book = book + "\n"
        f.write(book)
        f.close
        break
        
    elif ans1 == "종료":
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 추가 또는 종료를 입력해주세요.")
        continue
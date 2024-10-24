def append():
    print("데이터를 추가합니다.")
def update():
    print("데이터를 갱신합니다.")
def delete():
    print("데이터를 삭제합니다.")

list = [append, update, delete]

res = int(input("조작 번호를 입력하세요.(0～2)"))

if 0 <= res and res < len(list):
    list[res]()

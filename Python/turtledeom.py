 #원본코드 설명 /분석
from turtle import * # Turtle 라이브러리 내 모든 변수, 함수를 사용할 수 있도록 선언
import random #랜덤 라이브러리 
class Block(Turtle): #Block 클래스 선언, Turtle 클래스를 상속받음, 배열내 정수의 크기를 나타내는 블록을 생성
    def __init__(self, size): #생성자
        self.size = size #입력된 정수를 클래스 내부에서 사용
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2) #블록의 크기를 설정
        self.fillcolor("black") #블록의 색을 검은색으로 설정
        self.st()
    def glow(self):#블록의 색을 빨간색으로 변경 (이동시에)
        self.fillcolor("red")
    def unglow(self):#블록의 색을 검정색으로 변경 (이동과정 종료시)
        self.fillcolor("black")
    def __repr__(self): #인스턴스를 Print로 출력시에 실행
        return "Block size: {0}".format(self.size)

class Shelf(list):
    #Shelf 클래스 선언, list 클래스를 상속받음, 블록들을 담는 선반을 생성
    #Block 클래스로 만들어진 블럭들을 선반에 담고 정렬시에 움직이는 과정을 보여줌
    def __init__(self, y): #생성자
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -150
    def push(self, d): #블록을 선반에 추가
        width, _, _ = d.shapesize()
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)
    def _close_gap_from_i(self, i): #블록이 움직일 때 빈 공간을 채우는 함수(i 이후의 원소들을 왼쪽으로 1칸씩 이동)
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)
    def _open_gap_from_i(self, i): #블록이 움직일 때 빈 공간을 만드는 함수 (i번째 원소부터오른쪽으로 1칸씩 이동)
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)
    def pop(self, key): #블록을 선반에서 제거
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b
    def insert(self, key, b): #블록을 삽입(list의 insert를 시각화)
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

def isort(shelf): #삽입정렬 함수
    length = len(shelf)
    for i in range(1, length):#두번째 블록부터 시작해서 각블록을 알맞은 위치에 삽입
        hole = i#현재블록을 삽입할 위치를 나타내는변수. 초기값은 현재 블록의 위치
        while hole > 0 and shelf[i].size < shelf[hole - 1].size: #삽입할 위치를 찾기위해 왼쪽으로 이동하면서비교
            hole = hole - 1 # 삽입 위치를 왼쪽으로 한 칸 이동
        shelf.insert(hole, shelf.pop(i))# 재블록을 찾은 위치에 insert와 pop을 이용해삽입
    return

def ssort(shelf): #선택정렬 함수
    length = len(shelf)
    for j in range(0, length - 1):#정렬되지않은 부분의 시작위치를 나타내는 변수
        imin = j # 현재 정렬되지 않은 부분에서 가장작은 블록의 인덱스를 저장하는 변수. 초기값은 시작위치
        for i in range(j + 1, length): #정렬되지 않은 부분에서 가장작은 블록을찾음
            if shelf[i].size < shelf[imin].size: #현재블록의 크기가 현재까지 찾은 가장작은블록의 크기보다 작으면
                imin = i #가장 작은 블록의 인덱스를 업데이트
        if imin != j:#현재 위치의 블록이 가장작은 블록이아니라면
            shelf.insert(j, shelf.pop(imin)) #가장 작은 블록을 insert와 pop을 이용해 이동

def partition(shelf, left, right, pivot_index): #퀵정렬의 분할진행 함수
    pivot = shelf[pivot_index] #피벗블록 선택
    shelf.insert(right, shelf.pop(pivot_index)) #피벗 오른쪽끝으로 이동(삭제후 삽입)
    store_index = left #피벗보다 작은블록 저장위치, 초기값은 왼쪽인덱스
    for i in range(left, right): #왼쪽부터 오른쪽 직전까지순회
        if shelf[i].size < pivot.size: #현재블록 크기가 피벗보다 작으면
            shelf.insert(store_index, shelf.pop(i)) #현재블록 store_index 위치로 이동(삭제후 삽입)
            store_index = store_index + 1 #store_index 증가, 다음 작은블록 저장 준비
    shelf.insert(store_index, shelf.pop(right)) #피벗 store_index 위치로이동(삭제후 삽입), 피벗왼쪽엔 작은블록, 오른쪽엔 큰블록
    return store_index #피벗 인덱스 반환

def qsort(shelf, left, right): #퀵정렬 함수
    if left < right: #정렬할부분 크기가 1보다 크면
        pivot_index = left #가장 왼쪽원소를 피벗으로설정
        pivot_new_index = partition(shelf, left, right, pivot_index) #피벗기준 분할, 새로운 인덱스 지정
        qsort(shelf, left, pivot_new_index - 1) #피벗 왼쪽 재귀정렬
        qsort(shelf, pivot_new_index + 1, right) #피벗 오른쪽 재귀정렬

def randomize(): #블록들을 섞는 함수
    disable_keys()#키입력을 받지 않도록 설정
    clear()#화면을 지움
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target): 
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def show_text(text, line=0): #화면에 텍스트를 출력하는 함수
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def start_ssort(): #선택정렬을 시작하는 함수
    disable_keys() #정렬진행중 키입력 방지
    clear() #화면상 텍스트 제거
    show_text("Selection Sort")
    ssort(s) #정렬 진행
    clear() #텍스트 제거
    show_text(instructions1) #초기화면 복귀
    show_text(instructions2, line=1)
    enable_keys()#다시 키입력 허용

def start_isort(): #삽입정렬을 시작하는 함수
    disable_keys()
    clear()
    show_text("Insertion Sort")
    isort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def start_qsort(): #퀵정렬을 시작하는 함수
    disable_keys()
    clear()
    show_text("Quicksort")
    qsort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def init_shelf(): #블록들을 선반에 추가하는 함수
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6) #정렬할 배열들
    for i in vals:
        s.push(Block(i)) #각 원소 Block클래스의 인스턴스로 변경 

def disable_keys(): #키 입력을 받지 않도록 하는 함수 (정렬과정 진행중에 키입력을 받지 않도록)
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")

def enable_keys(): #키입력 함수
    onkey(start_isort, "i")
    onkey(start_ssort, "s")
    onkey(start_qsort, "q")
    onkey(randomize, "r")
    onkey(bye, "space")

def main(): #메인함수
    getscreen().clearscreen() #화면 클리어
    ht(); penup() #이전터틀 제거, 펜 들기
    init_shelf() #shelf생성
    show_text(instructions1) #초기화면 구성
    show_text(instructions2, line=1)
    enable_keys() #키입력 진행
    listen() #입력 허용
    return "EVENTLOOP"
instructions1 = "press i for insertion sort, s for selection sort, q for quicksort"
instructions2 = "spacebar to quit, r to randomize"

if __name__=="__main__": #메인함수
    msg = main() #main함수 실행
    mainloop() #프로그램 실행
#전체 클래스 설명
#Block 클래스는 블록의 크기를 나타내는 정수를 받아 블록을 생성
#Shelf 클래스는 블록들을 담는 선반을 생성하고 정렬시에 움직이는 과정을 보여줌
#삽입정렬, 선택정렬, 퀵정렬 함수를 구현
#randomize 함수는 블록들을 섞는 함수
#show_text 함수는 화면에 텍스트를 출력하는 함수
#start_ssort, start_isort, start_qsort 함수는 정렬을 시작하는 함수
#init_shelf 함수는 블록들을 선반에 추가하는 함수
#disable_keys 함수는 키 입력을 받지 않도록 하는 함수
#enable_keys 함수는 키 입력 함수
#main 함수는 메인함수
#instructions1, instructions2는 텍스트 출력을 위한 변수
#main함수 실행

#원본코드 실행결과
#배열생성 -> Block클래스로 블록생성 
#Shelf클래스로 선반생성 -> 블록들을 선반에 추가 
#show_text함수로 텍스트 출력 -> enable_keys함수로 키입력 함수 실행
#키입력을 받아 정렬을 시작하는 함수 실행
#정렬을 시작하는 함수에서 정렬함수를 호출, 정렬이 끝나면 텍스트 출력
#mainloop()함수로 이벤트루프 실행
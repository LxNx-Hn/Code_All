from turtle import *

class Block(Turtle):
    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2)
        self.fillcolor("skyblue") #색변경진행
        self.st()  
        #정수 표시를 위한 레이블 생성, 기존코드는 배열을 크기로만 표시해서 크기차이가 1,2정도에서는 가시성이 떨어짐
        self.label = Turtle(visible=False)
        self.label.pu()
        self.update_label()
    def glow(self):
        self.fillcolor("red")  
    def unglow(self):
        self.fillcolor("skyblue")
    def set_color(self, color): # 색상을 설정하는 함수 추가
        self.fillcolor(color)    
    def __repr__(self):
        return f"Block size: {self.size}"#f스트링 사용
    
    def update_label(self): #블록의 크기를 레이블로 표시
        self.label.clear()
        block_height = self.size * 1.5 * 10
        self.label.goto(self.xcor(), self.ycor() - block_height - 15)
        self.label.color("black") 
        self.label.write(self.size, align="center", font=("Arial", 12, "normal"))

    def setx(self, x): #블록의 x좌표 설정,레이블추가에 필요
        Turtle.setx(self, x)
        self.update_label()
    def sety(self, y): #블록의 y좌표 설정,레이블추가에 필요
        Turtle.sety(self, y)
        self.update_label()
    def clear_label(self): #레이블 삭제
        self.label.clear()

class Shelf(list):
    def __init__(self, y):
        self.y = y
        self.x = -150
#정렬알고리즘에는 insert,pop보다 swap함수가 더 효율적
#EX) 10개원소중 2-3번 위치변경시 먼저 pop함수를 이용하여 2번 원소를 제거,
#glow로 표시후 close_gap_from_i 함수로 2번위치 이후의 모든원소를 왼쪽으로 한칸씩 이동시키며 빈공간을 채움, 
#open_gap_from_i함수로 3번 위치부터 모든원소를 오른쪽으로 한칸씩 밀어 빈공간을 만들고 
# insert함수로 2번 원소를 3번 위치에 삽입, glow헤제
# --> swap의 과정을 시각화할수있다는 장점이 있지만 
#리스트 자료구조에서 중간 요소 삽입/삭제는 평균적으로 O(n)의 시간 복잡도를 가짐       
    def swap(self, i, j):
        self[i].glow()
        self[j].glow()
        xpos_i, _ = self[i].pos()
        xpos_j, _ = self[j].pos() 
        self[i].setx(xpos_j)
        self[j].setx(xpos_i)
        self[i], self[j] = self[j], self[i]
        self[i].unglow()
        self[j].unglow()

    def push(self, d):
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
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()
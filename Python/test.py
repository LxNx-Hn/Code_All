from turtle import *
import random

class Block(Turtle):
    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2)
        self.fillcolor("skyblue")
        self.st()
        self.label = Turtle(visible=False)
        self.label.pu()
        self.update_label()

    def glow(self, color="red"):  # 색상 변경 기능 추가
        self.fillcolor(color)

    def unglow(self):
        self.fillcolor("skyblue")

    def __repr__(self):
        return f"Block size: {self.size}"

    def update_label(self):
        self.label.clear()
        block_height = self.size * 1.5 * 10
        self.label.goto(self.xcor(), self.ycor() - block_height - 15)
        self.label.color("black")
        self.label.write(self.size, align="center", font=("Arial", 12, "normal"))

    def setx(self, x):
        Turtle.setx(self, x)
        self.update_label()

    def sety(self, y):
        Turtle.sety(self, y)
        self.update_label()

    def clear_label(self):
        self.label.clear()

class Shelf(list):
    def __init__(self, y):
        self.y = y
        self.x = -150

    def swap(self, i, j):
        self[i].glow("yellow")  # 스왑되는 블록 강조
        self[j].glow("yellow")
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

def show_text(text, line=0):
    line = 20 * line
    goto(0, -250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def show_algorithm_info(name, complexity, description):
    goto(0, -300)
    color("black")
    write(f"{name} : 시간 복잡도 = {complexity}, \n설명 = {description}",
          align="center", font=("Courier", 12, "bold"))

def bubble_sort(shelf):
    complexity = "O(n²), Ω(n)"
    description = "인접한 두 원소를 비교하여 정렬."
    show_algorithm_info("버블 정렬", complexity, description)
    length = len(shelf)
    for i in range(length):
        for j in range(0, length - 1 - i):
            if shelf[j].size > shelf[j + 1].size:
                shelf.swap(j, j + 1)

def insertion_sort(shelf):
    complexity = "O(n²), Ω(n)"
    description = "각 원소를 정렬된 부분에 삽입하여 정렬."
    show_algorithm_info("삽입 정렬", complexity, description)
    length = len(shelf)
    for i in range(1, length):
        key = shelf[i]
        j = i - 1
        while j >= 0 and shelf[j].size > key.size:
            shelf.swap(j, j+1)
            j -= 1

def selection_sort(shelf):
    complexity = "O(n²), Ω(n²)"
    description = "최솟값을 찾아 맨 앞으로 이동."
    show_algorithm_info("선택 정렬", complexity, description)
    length = len(shelf)
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if shelf[j].size < shelf[min_idx].size:
                min_idx = j
        if min_idx != i:
            shelf.swap(i, min_idx)

def quick_sort_helper(shelf, low, high):  # 퀵정렬 함수, 안정성을 위해내부함수로 선언
    complexity = "O(n log n) (평균), O(n²) (최악)"
    description = "분할정복을 사용하여 피벗을 기준으로 정렬합니다."
    show_algorithm_info("퀵 정렬", complexity, description)

    def partition(low, high):
        pivot_index = random.randint(low, high)  # 무작위피벗 선택, 원래의코드에 기능추가
        shelf[pivot_index].glow("black")  # 피벗 블록 색상 변경 (glow)
        shelf.swap(high, pivot_index)  # 피벗을 맨오른쪽으로 이동
        pivot = shelf[high]
        i = low - 1
        for j in range(low, high):
            if shelf[j].size <= pivot.size:
                i += 1
                shelf.swap(i, j)
        shelf.swap(i + 1, high)
        shelf[high].unglow()  # 피벗 블록 색상 복원 (unglow)
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    _quick_sort(low, high)

    # 퀵 정렬: 분할정복 알고리즘을 사용하여 정렬
    # 배열에서 하나의 요소(pivot)를 선택 pivot을 기준으로 배열을 두 개의 하위 배열로 분할
    # pivot보다 작은 요소는 왼쪽,큰 요소는 오른쪽에 위치
    # 그후에는각 하위 배열에 대해 재귀적으로 퀵 정렬을 호출
    # 분할 과정(partition)에서의 성능이 퀵 정렬의 전체 성능을 좌우
    # 최악의 경우(정,역순 정렬)에는 O(n^2)의 시간 복잡도를 가질 수 있지만, 평균적으로 O(n log n)의 성능을 보장
    # 피벗선택에 따라 성능편차가 심함 -> 최악의 경우를 피하기위해 피벗을 랜덤으로 선택하도록 코드 개선

def merge_sort_helper(shelf, left, right):  # 병합정렬 함수, 안정성을 위해내부함수로 선언
    complexity = "O(n log n)"
    description = "분할 정복을 사용하여 병합 정렬합니다."
    show_algorithm_info("병합 정렬", complexity, description)

    def merge(left, mid, right):  # 병합정렬용 재귀호출함수
        # 분할된 영역 강조
        for i in range(left, right + 1):
            shelf[i].glow("green")
        left_half = shelf[left:mid + 1]
        right_half = shelf[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            left_half[i].glow("yellow") # 색상 변경
            right_half[j].glow("yellow") # 색상 변경

            if left_half[i].size <= right_half[j].size:
                shelf[k] = left_half[i]
                shelf[k].setx(shelf.x + 34 * k)
                i += 1
            else:
                shelf[k] = right_half[j]
                shelf[k].setx(shelf.x + 34 * k)
                j += 1
            k += 1
            if i > 0:
                left_half[i - 1].unglow()
            if j > 0:
                right_half[j - 1].unglow()

        while i < len(left_half):
            shelf[k] = left_half[i]
            shelf[k].setx(shelf.x + 34 * k)
            i += 1
            k += 1
            if i > 0:
                left_half[i - 1].unglow()

        while j < len(right_half):
            shelf[k] = right_half[j]
            shelf[k].setx(shelf.x + 34 * k)
            j += 1
            k += 1
            if j > 0:
                right_half[j - 1].unglow()

        # 분할된 영역 강조 해제
        for i in range(left, right + 1):
            shelf[i].unglow()

    def _merge_sort(left, right):  # 병합정렬함수
        if left < right:
            mid = (left + right) // 2
            _merge_sort(left, mid)
            _merge_sort(mid + 1, right)
            merge(left, mid, right)

    _merge_sort(left, right)

    # 병합 정렬: 분할 정복 알고리즘을 사용하여 정렬을 수행
    # 배열을 더 작은 하위 배열(크기가 1이될때까지)로 반복적으로 분할후에 하위 배열을 정렬
    # 정렬된 하위 배열을 다시 병합하여 새로운 정렬된 배열 생성
    # 항상 O(n log n)의 시간 복잡도를 보장하지만, 퀵 정렬에 비해 공간 복잡도가 높고, 구현이 다소 복잡함
    # 일정한 성능을 보장하지만, 퀵 정렬보다 느림
    # swap알고리즘을 사용하지않음, glow를 이용한 시각적효과를 직접 추가

def heap_helper(shelf, n, i):  # 힙 구조를 만드는 함수
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and shelf[i].size < shelf[left].size:
        largest = left

    if right < n and shelf[largest].size < shelf[right].size:
        largest = right

    if largest != i:
        shelf[i].glow("blue")  # 힙 구조 변경 블록 강조
        shelf[largest].glow("blue")
        shelf.swap(i, largest)
        shelf[i].unglow()
        shelf[largest].unglow()
        heap_helper(shelf, n, largest)

def heap_sort(shelf):  # 힙 정렬 함수
    complexity = "O(n log n)"
    description = "힙 자료 구조를 사용하여 정렬합니다."
    show_algorithm_info("힙 정렬", complexity, description)
    n = len(shelf)

    for i in range(n // 2 - 1, -1, -1):
        heap_helper(shelf, n, i)
    for i in range(n - 1, 0, -1):
        shelf.swap(0, i)
        heap_helper(shelf, i, 0)
    # 힙 정렬: 최대 힙 트리나 최소 힙 트리를 구성해 정렬하는 방법
    # 내림차순 정렬을 위해서는 최대 힙을 구성하고, 오름차순 정렬을 위해서는 최소 힙을 구성
    # heapify함수를 사용하여 힙 속성을 만족하는 subtree를 재구성
    # 힙 정렬은 퀵 정렬, 병합 정렬과 마찬가지로 O(n log n)의 시간 복잡도를 가짐

def randomize():
    complexity = "O(n)"
    description = "리스트의 순서를 임의로 섞습니다."
    show_algorithm_info("배열 섞기", complexity, description)
    disable_keys()
    clear()
    show_text("배열 섞는중...")
    for _ in range(len(s)):
        i, j = random.sample(range(len(s)), 2)
        s.swap(i, j)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_bubble_sort():
    disable_keys()
    clear()
    show_text("버블정렬 진행중")
    bubble_sort(s)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_insertion_sort():
    disable_keys()
    clear()
    show_text("삽입정렬 진행중")
    insertion_sort(s)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_selection_sort():
    disable_keys()
    clear()
    show_text("선택정렬 진행중")
    selection_sort(s)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_quick_sort():
    disable_keys()
    clear()
    show_text("퀵정렬 진행중")
    quick_sort_helper(s, 0, len(s) - 1)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_merge_sort():
    disable_keys()
    clear()
    show_text("병합정렬 진행중")
    merge_sort_helper(s, 0, len(s) - 1)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def start_heap_sort():
    disable_keys()
    clear()
    show_text("힙정렬 진행중")
    heap_sort(s)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

def init_shelf():
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "b")
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")
    onkey(None, "m")
    onkey(None, "h")
    onkey(None, "space")

def enable_keys():
    onkey(start_bubble_sort, "b")
    onkey(start_insertion_sort, "i")
    onkey(start_selection_sort, "s")
    onkey(start_quick_sort, "q")
    onkey(start_merge_sort, "m")
    onkey(start_heap_sort, "h")
    onkey(randomize, "r")
    onkey(bye, "space")

def main():
    getscreen().clearscreen()
    ht()
    penup()
    init_shelf()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()
    getscreen().listen()
    return "EVENTLOOP"

instructions1 = "i: 삽입정렬,  s: 선택정렬,  q: 퀵정렬"
instructions2 = "b: 버블정렬,  m: 병합정렬, h: 힙정렬 "
instructions3 = "r: 배열 섞기,  space: 종료"

if __name__=="__main__":
    msg = main()
    mainloop()
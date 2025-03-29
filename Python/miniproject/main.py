""" 
개선코드에는 변한부분에만 주석처리 진행
병합정렬,버블정렬,힙정렬렬추가
insert,pop기반 알고리즘을 swap기반 알고리즘으로 개선
UI한글화 진행,가독성을 위해 한줄추가
원소를 표시하는 블록아래에 레이블추가, 직관성 향상
가시성향상을 위해 블록색 변경, 각정렬에서 사용하는 여러방식에 맞게 추가설정정
퀵정렬에서 피벗선택을 가장 좌측원소 -> 무작위로 변경
정렬진행중에 해당 정렬알고리즘에대한 간략한 설명과 코드복잡도 추가
randominize함수 개선 """
from turtle import *
from classes import Block, Shelf
from functions import (show_text, bubble_sort, isort, selection_sort, 
                       quick_sort_helper, merge_sort_helper, heap_sort, randomize)

def disable_keys():
    onkey(None, "b") #버블정렬
    onkey(None, "s")
    onkey(None, "i")
    onkey(None, "q")
    onkey(None, "r")
    onkey(None, "m") #병합정렬
    onkey(None, "h")  #힙정렬
    onkey(None, "space")

def enable_keys():
    onkey(start_bubble_sort, "b") #버블정렬
    onkey(start_insertion_sort, "i")
    onkey(start_selection_sort, "s")
    onkey(start_quick_sort, "q")
    onkey(start_merge_sort, "m")#병합정렬
    onkey(start_heap_sort, "h") #힙정렬
    onkey(start_randomize, "r")
    onkey(bye, "space")

def init_shelf():
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))

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
    isort(s)
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

def start_randomize():
    disable_keys()
    clear()
    show_text("배열 섞는중...")
    randomize(s)
    clear()
    show_text(instructions1, line=0)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()

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

instructions1 = "i: 삽입정렬,  s: 선택정렬,  q: 퀵정렬" #한글화
instructions2 = "b: 버블정렬,  m: 병합정렬,  h: 힙정렬" #추가한 정렬들
instructions3 = "r: 배열 섞기,  space: 종료"

if __name__ == "__main__":
    msg = main()
    mainloop()
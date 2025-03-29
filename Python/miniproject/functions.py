import random
from turtle import *

# 텍스트 표시 함수
def show_text(text, line=0):
    line = 20 * line
    goto(0, -250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

#정렬진행중 정렬 알고리즘에대한 설명 추가 함수
def show_algorithm_info(name, complexity, description):
    goto(0, -300)
    color("black")
    write(f"{name} : 시간 복잡도 = {complexity}, \n설명 = {description}",
          align="center", font=("Courier", 12, "bold"))

def bubble_sort(shelf):
    complexity = "O(n²), Ω(n)"
    description = "인접한 두 원소를 비교하여 정렬. 구현이 제일 간단하지만 비효율적."
    show_algorithm_info("버블 정렬", complexity, description)
    length = len(shelf)
    for i in range(length): 
        # 이미 정렬된 부분 표시
        for j in range(length - i, length):
            shelf[j].set_color("lightgreen")
        #정렬 알고리즘
        for j in range(0, length - 1 - i):
            if shelf[j].size > shelf[j + 1].size:
                shelf.swap(j, j + 1)
                
        shelf[length - 1 - i].set_color("lightgreen")   
    # 모든 정렬이 끝나면 원래 색상으로 복원
    for i in range(length):
        shelf[i].set_color("skyblue")
    #버블정렬 :j번째 원소와 j+1번째 원소를 비교하여 정렬, j+1번째 원소가 더 작으면 swap
    #for j 구문이종료되면 가장큰 원소가 제일 뒤에 위치함
    #다음번 회전에서는 가장 큰 원소를 제외하고(length-1번째) 비교를 반복
    #최악의 경우(역순정렬)에는 n(n-1)/2번의 비교가 필요하므로 시간복잡도는 O(n^2)
    #최선의 경우(이미 정렬된 경우)에는 n-1번의 비교가 필요하므로 시간복잡도는 O(n)

def isort(shelf): #삽입정렬은 swap보다 기존방식이 더 알고리즘을 보여주기에 적합함
    complexity = "O(n²), Ω(n)"
    description = "각 원소를 이미 정렬된 부분에 삽입하여 정렬. 버블 정렬보다 약간 효율적."
    show_algorithm_info("삽입 정렬", complexity, description)
    
    length = len(shelf)
    for i in range(1, length):
        for k in range(i):
            shelf[k].set_color("lightgreen")
        hole = i
        while hole > 0 and shelf[i].size < shelf[hole - 1].size: 
            hole = hole - 1
        shelf.insert(hole, shelf.pop(i))
        shelf[hole].set_color("lightgreen")
    for i in range(len(shelf)):
        shelf[i].set_color("skyblue")
    #삽입정렬: i번째 원소를 0부터 i-1번째 원소들과 비교하여 올바른 위치에 삽입
    #key값을 배열에서 꺼낸 후, 배열을 탐색하며 key보다 큰 원소를 만나면 그 자리에 key를 삽입
    #최악의 경우(역순정렬)에는 n(n-1)/2번의 비교가 필요하므로 시간복잡도는 O(n^2)
    #최선의 경우(이미 정렬된 경우)에는 n-1번의 비교가 필요하므로 시간복잡도는 O(n)
    #버블,선택보다 빠르지만 배열이 길어질수록 효율성 하락 
     

def selection_sort(shelf): #insert,pop기반으로 구현되어있던 선택정렬 알고리즘 swap기반으로 변경
    complexity = "O(n²), Ω(n²)"
    description = "최솟값을 찾아 맨 앞으로 이동시키는 과정을 반복."
    show_algorithm_info("선택 정렬", complexity, description)
    for i in range(len(shelf)):
        for k in range(i):
            shelf[k].set_color("lightgreen")
        min_idx = i
        for j in range(i + 1, len(shelf)):
            if shelf[j].size < shelf[min_idx].size:
                min_idx = j
            else:
                shelf[j].set_color("skyblue")          
        if min_idx != i:
            shelf.swap(i, min_idx)
        shelf[i].set_color("lightgreen")
    for i in range(len(shelf)):
        shelf[i].set_color("skyblue")
    #선택정렬: i번째 원소를 i+1부터 n-1까지의 원소들과 비교하여 가장 작은 원소를 찾아 i번째 원소와 swap
    #i번째 원소를 제외한 나머지 원소들 중 가장 작은 원소를 찾아 i번째 원소와 swap
    #반복할때마다 앞에서부터 하나씩 정렬이 완료됨
    #최악의 경우(역순정렬)에는 n(n-1)/2번의 비교가 필요하므로 시간복잡도는 O(n^2)
    #최선의 경우(이미 정렬된 경우)에도 n(n-1)/2번의 비교가 필요하므로 시간복잡도는 O(n^2)


def quick_sort_helper(shelf, low, high): #퀵정렬 함수, 안정성을 위해내부함수로 선언
    complexity = "O(n log n) (평균), O(n²) (최악)"
    description = "분할정복을 사용하여 피벗을 기준으로 정렬."
    show_algorithm_info("퀵 정렬", complexity, description)

    def partition(low, high):
        # 분할 영역 표시
        for i in range(low, high + 1):
            shelf[i].set_color("lightblue")
        pivot_index = random.randint(low, high)  #무작위피벗 선택, 원래의코드에 기능추가
        shelf[pivot_index].set_color("purple")  # 피벗 표시
        shelf.swap(high, pivot_index)  # 피벗을 맨오른쪽으로 이동
        pivot = shelf[high]
        i = low - 1
        for j in range(low, high):
            shelf[j].set_color("orange")  # 현재 검사 중인 원소
            if shelf[j].size <= pivot.size:
                i += 1
                if i != j:  # 자기 자신과 swap하는 경우제외
                    shelf.swap(i, j)
            shelf[j].set_color("lightblue")  # 검사후 원래색상으로
        shelf.swap(i + 1, high)
        shelf[i + 1].set_color("green") # 분할 완료후 피벗위치 표시
        for k in range(low, high + 1):  # 분할 영역 원래색상으로 복원
            if k != i + 1:  # 피벗 위치 제외
                shelf[k].set_color("skyblue")
        return i + 1

    def _quick_sort(low, high):
        if low < high:
            # 현재 정렬 범위 표시
            for i in range(low, high + 1):
                shelf[i].set_color("black")     
            pi = partition(low, high)
            # 피벗 위치 복원
            shelf[pi].set_color("skyblue")
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)
    _quick_sort(low, high)
    # 모든 정렬이 끝나면 원래 색상으로 복원
    for i in range(low, high + 1):
        shelf[i].set_color("skyblue")
    #퀵 정렬: 분할정복 알고리즘을 사용하여 정렬
    #배열에서 하나의 요소(pivot)를 선택 pivot을 기준으로 배열을 두 개의 하위 배열로 분할
    #pivot보다 작은 요소는 왼쪽,큰 요소는 오른쪽에 위치
    #그후에는각 하위 배열에 대해 재귀적으로 퀵 정렬을 호출
    #분할 과정(partition)에서의 성능이 퀵 정렬의 전체 성능을 좌우
    #최악의 경우(정,역순 정렬)에는 O(n^2)의 시간 복잡도를 가질 수 있지만, 평균적으로 O(n log n)의 성능을 보장
    #피벗선택에 따라 성능편차가 심함 -> 최악의 경우를 피하기위해 피벗을 랜덤으로 선택하도록 코드 개선
           
def merge_sort_helper(shelf, left, right): #병합정렬 함수, 안정성을 위해내부함수로 선언
    complexity = "O(n log n)"
    description = "분할 정복을 사용하여 리스트를 병합 정렬합니다."
    show_algorithm_info("병합 정렬", complexity, description)

    def merge(left, mid, right): #병합정렬용 재귀호출함수
        # 병합 전 분할된 영역 표시 (왼쪽 부분은 초록색, 오른쪽 부분은 보라색으로 구분)
        for i in range(left, mid + 1):
            shelf[i].set_color("lightgreen")  # 왼쪽 부분 색상
        for i in range(mid + 1, right + 1):
            shelf[i].set_color("lavender")    # 오른쪽 부분 색상
        left_half = shelf[left:mid+1]
        right_half = shelf[mid+1:right+1]
        i = j = 0
        k = left

        while i < len(left_half) and j < len(right_half):
            left_half[i].set_color("red")
            right_half[j].set_color("red")
            
            if left_half[i].size <= right_half[j].size:
                shelf[k] = left_half[i]
                shelf[k].setx(shelf.x + 34 * k)
                shelf[k].set_color("skyblue")
                i += 1
            else:
                shelf[k] = right_half[j]
                shelf[k].setx(shelf.x + 34 * k)
                shelf[k].set_color("skyblue")
                j += 1
            k += 1

        while i < len(left_half): # 남은 왼쪽 처리
            left_half[i].set_color("orange")  # 남은 요소 강조
            shelf[k] = left_half[i]
            shelf[k].setx(shelf.x + 34 * k)
            shelf[k].set_color("skyblue")
            i += 1
            k += 1

        while j < len(right_half): # 남은 오른쪽 부분 처리
            right_half[j].set_color("orange")  # 남은 요소 강조
            shelf[k] = right_half[j]
            shelf[k].setx(shelf.x + 34 * k)
            shelf[k].set_color("skyblue")
            j += 1
            k += 1
        # 병합 완료 후 전체 영역 표시
        for i in range(left, right + 1):
            shelf[i].set_color("lightblue")  # 병합 완료된 영역을 밝은 파란색으로 표시
        # 색상 원래대로 복원
        for i in range(left, right + 1):
            shelf[i].set_color("skyblue")
    def _merge_sort(left, right):
        if left < right:
            for i in range(left, right + 1):  # 현재 정렬 범위 표시
                shelf[i].set_color("lightyellow")
            mid = (left + right) // 2
            _merge_sort(left, mid)
            _merge_sort(mid + 1, right)
            merge(left, mid, right)

    _merge_sort(left, right)
    #병합 정렬: 분할 정복 알고리즘을 사용하여 정렬을 수행
    #배열을 더 작은 하위 배열(크기가 1이될때까지)로 반복적으로 분할후에 하위 배열을 정렬
    #정렬된 하위 배열을 다시 병합하여 새로운 정렬된 배열 생성
    #항상 O(n log n)의 시간 복잡도를 보장하지만, 퀵 정렬에 비해 공간 복잡도가 높고, 구현이 다소 복잡함
    #일정한 성능을 보장하지만, 퀵 정렬보다 느림
    #swap알고리즘을 사용하지않음, glow를 이용한 시각적효과를 직접 추가  

def heap_helper(shelf, n, i): # 힙 구조를 만드는 함수
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 현재 노드, 왼쪽 자식, 오른쪽 자식 표시
    shelf[i].set_color("purple")  # 현재 노드
    
    if left < n:
        shelf[left].set_color("lightgreen")  # 왼쪽 자식
        if shelf[i].size < shelf[left].size:
            largest = left
    
    if right < n:
        shelf[right].set_color("lightyellow")  # 오른쪽 자식
        if shelf[largest].size < shelf[right].size:
            largest = right

    # 비교후 원래 색상으로 복원 (자식 노드)
    if left < n:
        shelf[left].set_color("skyblue")
    if right < n:
        shelf[right].set_color("skyblue")
        
    if largest != i:
        shelf[largest].set_color("orange") # 교환 필요시 표시
        shelf.swap(i, largest)
        # 교환 후 원래 색상으로
        shelf[i].set_color("skyblue")
        shelf[largest].set_color("skyblue")
        heap_helper(shelf, n, largest)
    else:
        shelf[i].set_color("skyblue") # 교환 불필요시 원래 색상으로

def heap_sort(shelf): # 힙 정렬 함수
    complexity = "O(n log n)"
    description = "힙 자료 구조를 사용하여 정렬. 최대 힙을 구성하고 루트를 차례대로 추출."
    show_algorithm_info("힙 정렬", complexity, description)  
    n = len(shelf)
    for i in range(len(shelf)): #힙 구성 단계 표시
        shelf[i].set_color("lightyellow")
    for i in range(n // 2 - 1, -1, -1): #최대 힙 구성
        heap_helper(shelf, n, i)
    
    for i in range(n - 1, 0, -1): #힙에서 요소를 하나씩 추출
        # 루트(최대값)와 마지막 요소 교환
        shelf[0].set_color("red")  #루트 표시
        shelf[i].set_color("green")  #교환할 요소 표시
        shelf.swap(0, i)
        shelf[i].set_color("lightgreen") # 교환 후 확정된 위치 표시
        heap_helper(shelf, i, 0) # 힙 속성 유지
    shelf[0].set_color("lightgreen")  # 모든 정렬이 끝나면 첫 번째 요소도 확정
    for i in range(n): # 정렬 완료 후 원래 색상으로 복원
        shelf[i].set_color("skyblue")
    #힙 정렬: 최대 힙 트리나 최소 힙 트리(완전이진트리)를 구성해 정렬하는 방법
    #내림차순 정렬을 위해서는 최대 힙을 구성하고, 오름차순 정렬을 위해서는 최소 힙을 구성
    #힙 정렬은 퀵 정렬, 병합 정렬과 마찬가지로 O(n log n)의 시간 복잡도를 가짐

# 배열 섞기
def randomize(shelf):
    complexity = "O(n)"
    description = "리스트의 순서를 임의로 섞습니다."
    show_algorithm_info("배열 섞기", complexity, description)

    for _ in range(len(shelf)): 
        i, j = random.sample(range(len(shelf)), 2) 
        shelf.swap(i, j)
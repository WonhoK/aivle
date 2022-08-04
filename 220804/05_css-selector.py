### CSS Selector ###
# CSS 스타일을 적용 시킬 HTML 엘리먼트를 선택하는 방법

# 1. Element Tag 이름으로 선택
# <div class="kt">
#     <div>python 1</div>
#     <p>python 2</p>
#     <span>python 3</span>
# </div>
# css selector : span : python 3 선택


# 2. Tag의 id 값으로 선택
# <div class="kt">
#     <p id="kt1">python 1</p>
#     <p id="kt2">python 2</p>
#     <p id="kt3">python 3</p>
# </div>
# css selector : #kt2 : python 2 선택


# 3. Tag의 class 값으로 선택
# <p class="kt kt1">python 1</p>
# <p class="kt kt2">python 2</p>
# <p class="kt kt3">python 3</p>
# css selector : .kt2 : python 2 선택
# css selector : .kt : python 1, python 2, python 3 선택


# 4. Tag의 attr 값으로 선택
# <p value="no1">python 1</p>
# <p value="no2">python 2</p>
# <p value="no3">python 3</p>
# css selector : [value="no1"] : python 1 선택


# 5. 여러개의 엘리먼트 선택
# <p class="py1">python 1</p>
# <p class="py2">python 2</p>
# <p class="py3">python 3</p>
# .py1, .py3 : python 1, python 3 선택

# <p class="no no1">python 1</p>
# <p class="no no2">python 2</p>
# <p class="no no3">python 3</p>
# class no 엘리먼트 모두 선택하고, no2 클래스를 갖는 엘리먼트만 제외
#    -> css selector : .no:not(.no2)

# <div>
#    <p class="py">python 1</p>
#    <p class="py">python 2</p>
#    <p class="py">python 3</p>
# </div>
# n번째 엘리먼트 선택
#    -> css selector : .py:nth-child(n)
# .py 엘리먼트 중에서 n번째 (X)
# n번째 엘리먼트 중에서 .py 클래스를 갖는 (O)


# 6. 계층적으로 엘리먼트 선택
# <div class="wrap">
#     <p>inner 1</p>
#     <div>
#         <p>inner 2</p>
#     </div>
# </div>
# .wrap > p : inner 1 선택
# .wrap p : inner 1, inner 2 선택

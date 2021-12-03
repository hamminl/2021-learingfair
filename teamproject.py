def 게임소개():
    print('캐릭터 키우기 게임:)')
    print('자신의 캐릭터를 하루 동안 키우는 게임입니다.')
    print('질문의 답에 대한 배점은 0,1,2로 점수가 5점이 넘어야 하루를 즐겁게 끝낼 수 있습니다.')
    
게임소개()

print('''.　　. ＼：／
　・･･･☆･･･・
. ⋀,,⋀. ∩.＼
(*・ω・)/
.(つ　 ﾉ
.しーＪ''')
name = input("캐릭터의 이름을 정해주세요: ")
score = 0
print()


for i in range(0,2,1):
    morning = {1:'''.　　∧,,∧
　(*＾ω＾) 🧽
　⊂　　つ))
(( ⊂、. /
　ミ ∪''', 2:'''.　∧,,∧
　(*＾ω＾) 공구르기~
　⊂　　つ))
(( ⊂、. /
　ミ ∪
　／￣＼
. |　　　 |
　＼＿／''' }  
    print(name+'이가 일어났습니다. 1번 세수하기와 2번 공구르기 중 일어나자마자 해야할 일은?(숫자 입력): ')
    morn = int(input())

    if morn == 1 :
        print(morning[1])
        score += 2
        break
    elif morn == 2 :
        print(morning[2])
        score += 1
        break
    else :
        print('실패. 다시 선택해주세요.')
        
print()       

for i in range(0,2,1):
    lunch = {1:'''. 　 ∧∧　      ∧∧
 　(´・ω・) 　(・ω・ `)
   ||(つ🍰D O🍰と)||
   ||￣|UU　 UU|￣||''', 2:'''. 　 ∧∧　      ∧∧
   (´・ω・) 　(・ω・ `)
   ||(つ☕D O☕と)||
   ||￣|UU　 UU|￣||'''}
    print(name+'이가 배가 고프다고 합니다. 1번 케이크와 2번 커피 중 친구와 먹을 것을 고르세요.(숫자 입력): ')
    meal = int(input())

    if meal == 1 :
        print(lunch[1])
        score += 2
        break
    elif meal == 2 :
        print(lunch[2])
        score += 1
        break
    else :
        print('실패. 다시 선택해주세요.')
    
print()

for i in range(0,2,1):
    act = {1:'''⊂_ヽ
　 ＼＼ Λ＿Λ
　　 ＼(　ˇωˇ)
　　　 >　⌒ヽ
　　　/ 　 へ＼
　　 /　　/　＼＼
　　 ﾚ　ノ　　 ヽ_つ
　　/　/
　 /　/|
　(　(ヽ
　|　|、＼
　| 丿 ＼ ⌒)
　| |　　) /
`ノ )　　Lﾉ
(_／''', 2:'''.　＼　.∧_∧ ＼＼
　＼　(`Д´；)、＼
　＼と∪∪_つ ＼＼
　　　 ／￣／ヽ＼
　　 /￣1￣ヽ／ヽ
　　/.￣ 2 ￣ヽ／ ヽ
　 /.￣￣3￣￣ヽ／ヽ
　/￣￣ 4￣￣￣ヽ／'''}
    print('이제 운동 할 시간입니다. 1번 춤추기와 2번 뜀틀 중', name+'이가 하게 될 운동은?(숫자 입력): ')
    sport = int(input())

    if sport == 1 :
        print(act[1])
        score += 1
        break
    elif sport == 2 :
        print(act[2])
        score += 2
        break
    else :
        print('실패. 다시 선택해주세요.')

print()

if score >= 5:
    print('점수는', score, '점으로', name+'이가 즐겁게 하루를 끝내는데 성공했습니다!')
    print('''
．     　∧ ∧
　 　　(´･ω･ ∩　성공！
　　　o.　　 ,ﾉ.
　 　　Ｏ＿ .ﾉ
　 　 　 　 (ノ
　 　 　　i｜|
　　　　  ━━     ''')
else :
    print('점수는', score, '점으로 좀 더 노력하세요!')
    print('''.∧,,∧
(；ω；) 
.∪　∪
し‐Ｊ''')
    

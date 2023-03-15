def main():
    player=0
    regist_user = {'kims4ok':'rlatjdwns@'}
    user_moeny ={'kims4ok': 99999999999}
    sw = True

    while sw:
        print('-----------------------------')
        print('1. 회원 아이디 생성')
        print('2. 비밀번호 변경')
        print('3. 전체 회원 아이디 목록 보기')
        print('4. 종료')
        print('5. 게임 플레이')
        print('-----------------------------\n')  

        select_no = int(input('번호 선택(1~4): '))

        if select_no == 1:
            id_result = make_id(regist_user)
            if id_result:
                regist_user[id_result[0]] = id_result[1]
                print(regist_user)

        if select_no == 2:
            uid = str(input('회원 아이디: '))
            if uid in regist_user:
                print(f'{uid} / {regist_user[uid]}')
                n_pwd = edit_password(uid, regist_user[uid])
                regist_user[uid] = n_pwd
                print('비밀번호 변경 완료!\n')
            else:
                print('등록된 아이디가 아닙니다.\n')
                continue

        if select_no == 3:
            for k, v in regist_user.items():
                print(f'id: {k} / pw: {v}')
            print()
    
        if select_no == 4:
            sw = False
        if select_no == 5:
            game_going = True
            while game_going:
                want_game = input("게임을 시작하시겠습니까? Y 아니면 N")
                if want_game == "Y":
                    print("게임을 시작합니다! 행운을 빕니다")
                    blackjack()
                else:
                    print("게임을 종료합니다.")
                    game_going = False
            # print('플레이어의 수를 입력하세요 : ')
            # player = int(input())
            # while player > 0:
            #     print('1번 참가자 로그인')
            #     print('아이디 : ')
            #     uid = str(input('회원 아이디: '))
            #     if uid in regist_user:
            #         print(f'{uid} / {regist_user[uid]}')
            #         n_pwd = edit_password(uid, regist_user[uid])
            #         regist_user[uid] = n_pwd
            #         print('비밀번호 변경 완료!\n')
            #     else:
            #         print('등록된 아이디가 아닙니다.\n')
            #         continue
            #     print('비밀번호 : ')
            #     player-=1

def make_id(regist_user):
    regist_id = []
    while True:
        uid = str(input('회원 아이디 입력: '))
        if uid in regist_user:
            print('이미 등록된 id입니다.')
            ex = input('메인 화면으로 이동하시겠습니까? (y/n): ')
            if ex == 'y' or ex == 'Y':
                return False
            else:
                continue
        else:
            res_id = chk_id(uid)
            if not res_id:
                continue
            else:
                regist_id.append(uid)
                break
    # print(regist_id)

    while True:
        pwd = str(input('비밀번호 입력: '))
        res_pwd = chk_password(pwd)
        if not res_pwd:
            continue
        else:
            regist_id.append(pwd)
            break
    # print(regist_id)
    return regist_id
import re

def chk_id(id):
    result = True
    reg = r'^[A-Za-z0-9_]{4,20}$'
    if not re.search(reg, id):
        print('아이디 생성 기준에 부적당합니다!')
        result = False
    return result


def chk_password(pwd):
    result = True
    reg = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%&*?])[A-Za-z\d!@#$%&*?]{8,20}$'
    if not re.search(reg, pwd):
        print('비밀번호 기준에 부적당합니다!')
        result = False
    return result
def edit_password(uid, pwd):
    n_pwd = ''
    while True:
        pw = str(input('새로운 비밀번호 입력: '))
        if pw == pwd:
            print(f'기존 비번하고 같음!')
            continue
        else:
            res_pwd = chk_password(pw)
            if not res_pwd:
                continue
            else:
                n_pwd = pw
                break
    print(f'id:{uid}, n_pwd:{n_pwd}')
    return uid, n_pwd

main()


def blackjack():
  # 카드 뽑기 
  import random
  list = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  my_pick = random.sample(list, 2)
  dealer_card = random.sample(list, 2)
  dealer_show_card = random.choice(dealer_card)

  print(f"나의 카드는 {my_pick}입니다")
  print("#딜러 카드는:", dealer_card)
  print(f"#딜러 카드 중 한 장은 {dealer_show_card}입니다")

  # 내 점수, 딜러 점수
  def score_sum(card_pick):
    sum=0
    for card in card_pick:
      sum +=card
    return sum

  my_score = score_sum(my_pick)
  dealer_score = score_sum(dealer_card)
  print(f"내 점수는 {my_score}입니다")
  print("#딜러 점수는:", dealer_score)

  # 딜러 점수[1~16] < 17이면 카드 한 장 더 받고 합계 다시 계산하기
  # 딜러 점수 >21이면, 만약 새로 받은 한 장이 에이스일 경우에는 에이스 점수를 1로 바꾸고 점수에 따라 와일문 돌리기! 
  if dealer_score < 17:
    a = True
    while a:
      one_more_card = random.sample(list, 1)
      dealer_card.extend(one_more_card)
      dealer_score = score_sum(dealer_card)
      print("#새로운 딜러의 카드:", dealer_card)
      print("#새로운 딜러 점수:", dealer_score)
      if dealer_score >16:
        if dealer_score >21:
          if one_more_card[0] == 11:
            dealer_card.remove(11)
            dealer_card.append(1)
            dealer_score = score_sum(dealer_card)
            print("#새로운 딜러의 카드:", dealer_card)
            print("#새로운 딜러 점수:", dealer_score)
            if dealer_score > 16:
              a = False
          else:
            a = False
        else:
          a = False

  # 승자 뽑기
  def winner(my_score, dealer_score):
    if my_score > dealer_score:
      if my_score == 21:
        print("블랙잭입니다.")
      print("이김")
    elif my_score == dealer_score:
      if my_score == 21:
        print("블랙잭입니다.")
      print("비김")
    else:
      if dealer_score == 21:
        print("블랙잭입니다.")
      print("짐")

  # stand? or hit?
  def decision(my_score, dealer_score):
    stand_hit = input("stand 할 것인가? hit 할 것인가?")
    keep_going = True
    while keep_going:
      if stand_hit == "stand":
        if dealer_score >21:
          print("이김")
          if my_score == 21:
            print("블랙잭입니다")
          keep_going = False
        else:
          winner(my_score, dealer_score)
          keep_going= False
      elif stand_hit == "hit":
        one_more_card = random.sample(list, 1)
        my_pick.extend(one_more_card)
        my_score = score_sum(my_pick)
        print(f"내가 가진 카드 리스트는 {my_pick}입니다")
        print(f"내 점수는 {my_score}입니다")
        if my_score > 21:
          if one_more_card[0] == 11:
            my_pick.remove(11)
            my_pick.append(1)
            my_score = score_sum(my_pick)
            print(f"내가 가진 카드 리스트는 {my_pick}입니다")
            print(f"내 점수는 {my_score}입니다")
            stand_hit = input("stand 할 것인가? hit 할 것인가?")
          else:
            print("짐")
            if dealer_score == 21:
              print("블랙잭입니다")
            keep_going = False
        else:
          stand_hit = input("stand 할 것인가? hit 할 것인가?")

  decision(my_score, dealer_score)



import random
# 게임의 승자는 3가지 간단한 규칙에 따라 결정된다.
# 1. 주먹은 가위를 이긴다.
# 2. 가위는 보를 이긴다.
# 3. 보는 주먹을 이긴다.

# 컴퓨터는 상대가 되어 주먹, 가위, 보 중 하나를 랜덤으로 낸다.
# 게임 내 상호작용은 콘솔을 통해 이루어진다.

# 플레이어는 가위, 바위, 보 중 하나를 선택할 수 있으며 잘못된 옵션을 입력하면 경고를 받아야한다.
# 각 라운드에서 플레이어는 목록에 있는 옵션 중 하나를 입력해야 하며 상대방과의 승리, 패배 또는 동점 여부를 알려야한다.
# 각 라운드가 끝날 때마다 플레이어는 다시 플레이할지 여부를 선택할 수 있다.
# 게임이 끝나면 플레이어의 점수를 표시
# 미니게임은 사용자 입력을 처리하여 이를 소문자로 입력하고 옵션이 유효하지 않은 경우 사용자에게 알려야 한다.

def get_user_choice():
    while True:
        user_choice = input("가위, 바위, 보 중 하나를 선택하세요: ").lower()
        if user_choice in ["가위", "바위", "보"]:
            return user_choice
        else:
            print("유효하지 않은 옵션입니다. 다시 입력해주세요.")

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "무승부"
    elif (player_choice == "가위" and computer_choice == "보") or \
         (player_choice == "바위" and computer_choice == "가위") or \
         (player_choice == "보" and computer_choice == "바위"):
        return "플레이어 승리"
    else:
        return "플레이어 패배"

def play_game():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_user_choice()
        computer_choice = random.choice(["가위", "바위", "보"])

        print(f"플레이어: {player_choice}")
        print(f"컴퓨터: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "플레이어 승리":
            player_score += 1
        elif result == "플레이어 패배":
            computer_score += 1

        play_again = input("다시 플레이하시겠습니까? (예/아니오): ").lower()
        if play_again != "예":
            break

    print(f"플레이어 점수: {player_score}")
    print(f"컴퓨터 점수: {computer_score}")

play_game()


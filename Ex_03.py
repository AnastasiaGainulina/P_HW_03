# Создайте программу для игры в ""Крестики-нолики""

board = list(range(1,10))

def paint_board(board):
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13)

def take_in(player_token):
    valid = False
    while not valid:
        player_answer=input('Куда ставим ' + player_token +'? ')

        try:
            player_answer=int(player_answer)
        except:
            print('Ошибка, убедитесь, что ввели число')
            continue
        if player_answer>=1 and player_answer <=9:
            if(str(board[player_answer-1])not in 'XO'):
                board[player_answer-1]=player_token
                valid =True
            else:
                print("позиция уже занята")
        else:
            print('введите число от 1 до 9')
def chec_w(board):
    win_variant= ((0 , 1 , 2), (3 , 4 , 5), (6 , 7 , 8), (0 , 3 , 6) , (1 , 4 , 7), (2 , 5 , 8), (0 , 4 , 8), (2 , 4 , 6))
    for every in win_variant:
        if board[every[0]]==board[every[1]]==board[every[2]]:
            return board[every[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        paint_board(board)
        if counter % 2 == 0:
            take_in('X')
        else:
            take_in('O') 
        counter += 1

        if counter>4:
            tmp = chec_w(board)
            if tmp:
                print(tmp, 'Победа')
                win=True
                break
        if counter==9:
            print('Ничья')
            break
    paint_board(board)
main(board)

from tkinter import *
import pygame

pygame.mixer.init()

place_sound = pygame.mixer.Sound('sounds\\place.mp3')
event_sound = pygame.mixer.Sound('sounds\\event.mp3')

WIN_WIDTH = 400
WIN_HEIGHT = 450
BG_COLOR = '#333344'
BUTTON_COLOR = '#404050'
WINNER_COLOR = '#22DD22'
FONT_NAME = 'consolas'

board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
player = players[0]

win = Tk()
win.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
win.title('TicTacToe')
win.resizable(False, False)
win.config(background=BG_COLOR)

main_label = Label(text=f'{player} TURN', font=(FONT_NAME, int(WIN_WIDTH/10)), bg=BG_COLOR, fg='#FFFFFF')
main_label.pack(side='top')

board_frame = Frame(win)
board_frame.pack()

turn = 0


def reset_board():

    global player, players, turn

    for y in board:
        for x in y:
            x['text'] = ''
            x.config(bg=BUTTON_COLOR)
    player = players[0]
    turn = 0
    place_sound.play()
    main_label.config(text=f'{player} TURN')


def check_board():
    
    global turn, player, players
    
    can_place = False

    if turn < 5:
        return None

    for row in range(3):
        if board[row][0]['text'] == '':
            continue
        if board[row][0]['text'] == board[row][1]['text'] and board[row][0]['text'] == board[row][2]['text']:
            board[row][0].config(bg=WINNER_COLOR)
            board[row][1].config(bg=WINNER_COLOR)
            board[row][2].config(bg=WINNER_COLOR)
            main_label.config(text=f'{board[row][0]["text"]} WINS')
            event_sound.play()
            return True
    for col in range(3):
        if board[0][col]['text'] == '':
            continue
        if board[0][col]['text'] == board[1][col]['text'] and board[0][col]['text'] == board[2][col]['text']:
            board[0][col].config(bg=WINNER_COLOR)
            board[1][col].config(bg=WINNER_COLOR)
            board[2][col].config(bg=WINNER_COLOR)
            main_label.config(text=f'{board[0][col]["text"]} WINS')
            event_sound.play()
            return True
    if board[0][0]['text'] == board[1][1]['text'] and board[0][0]['text'] == board[2][2]['text']:
        board[0][0].config(bg=WINNER_COLOR)
        board[1][1].config(bg=WINNER_COLOR)
        board[2][2].config(bg=WINNER_COLOR)
        main_label.config(text=f'{board[0][0]["text"]} WINS')
        event_sound.play()
        return True
    elif board[0][2]['text'] == board[1][1]['text'] and board[0][2]['text'] == board[2][0]['text']:
        board[0][2].config(bg=WINNER_COLOR)
        board[1][1].config(bg=WINNER_COLOR)
        board[2][0].config(bg=WINNER_COLOR)
        main_label.config(text=f'{board[0][2]["text"]} WINS')
        event_sound.play()
        return True
    for a in range(3):
        if can_place == True:
            break
        for b in range(3):
            if board[a][b]['text'] == '':
                can_place = True
                break
    if can_place == False:
        main_label.config(text="ITS A DRAW")
        event_sound.play()
        return False


def take_turn(row, col):

    global board, player, turn

    turn+=1

    if board[row][col]['text'] == '' and check_board() == None:
        board[row][col]['text'] = player
        player = players[1] if player == players[0] else players[0]
        main_label.config(text=f'{player} TURN')
    if check_board() == None:
        place_sound.play()

        
def main():

    global board, players, player

    for y in range(3):
        for x in range(3):
            board[y][x] = Button(board_frame, text='', font=(FONT_NAME, int(WIN_WIDTH/10)), 
                                 command=lambda row=y, col=x:take_turn(row, col),
                                 width=3, height=1, bg=BUTTON_COLOR, fg='#FFFFFF')
            board[y][x].grid(row=y, column=x)

    reset_button = Button(text='RESET BOARD', font=(FONT_NAME, int(WIN_WIDTH/20)), bg=BUTTON_COLOR, 
                          fg='#FFFFFF', command=lambda:reset_board())
    reset_button.pack(side='bottom', pady=10)

    win.mainloop()


if __name__ == '__main__':
    main()

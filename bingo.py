from random import randint
def get_user_input():
    count = 0
    user_list = ["  " for x in range(25)]
    enter_auto = input("Enter 0 to enter numbers automatically 1 to enetr numbers manually ")
    if enter_auto == 0:
        user_list = AI_play()
    else:
        while count < 25:
            pos = input("Enter the postion where you want to enter the number ")
            if user_list[pos-1] == '  ':
                user_list[pos-1] = input("Enter the number ")
                count += 1
            else:
                print "Postition already filled try again"
    return user_list

def print_bingo(arr):
    str2 = ''
    for x in range(len(arr)):
        if arr[x] < 10:
            str2 +=  "|" + str(arr[x]) + " |"
            if (x+1) % 5 == 0:
                str2 += "\n--------------------\n"
        else:
            str2 +=  "|" + str(arr[x]) + "|"
            if (x+1) % 5 == 0:
                str2 += "\n--------------------\n"
    print str2

def AI_play():
    ai_list = []
    counter = 0
    while counter < 25:
        num = randint(1,25)
        if num not in ai_list:
            ai_list.append(num)
            counter += 1
    return ai_list

def get_next_move(ai_list):
    x_list_row = []
    y_list_col = []
    counter = 0
    for x in range(0,25,5):
        for y in range(x,x+5):
            if ai_list[y] == 'X ':
                counter += 1
        if counter != 5:
            x_list_row.append(counter)
        else:
            x_list_row.append(-1)
        counter = 0
    
    x_row = x_list_row.index(max(x_list_row))

    for x in range(5):
        for y in range(x,25,5):
            if ai_list[y] == 'X ':
                counter += 1
        if counter != 5:
            y_list_col.append(counter)
        else:
            y_list_col.append(-1)
        counter = 0

    y_col = y_list_col.index(max(y_list_col))

    if max(x_list_row) >= max(y_list_col):
        for x in range(5*x_row,5*(x_row+1)):
            if ai_list[x] != 'X ':
                return ai_list[x]
    
    if max(y_list_col) > max(x_list_row):
        for x in range(y_col,25,5):
            if ai_list[x] != 'X ':
                return ai_list[x]

def check_win(list_):
    count = 0
    counter = 0

    for x in range(0,25,5):
        for y in range(x,x+5):
            if list_[y] == 'X ':
                counter += 1
        if counter == 5:
            count += 1
        counter = 0
    
    for x in range(5):
        for y in range(x,25,5):
            if list_[y] == 'X ':
                counter += 1
        if counter == 5:
            count += 1
        counter = 0
    
    if count >= 5:
        return True
    else:
        return False
        
def start_play(user_list, ai_list):
    print_bingo(user_list)
    num = ''
    toss = input("Pick Heads = 0 or Tails = 1 ")
    result = randint(0,1)
    if result == toss:
        print "User Starts First"
        while True:
            num = input("Enter number to cross out ")
            # num = get_next_move(user_list)
            user_list[user_list.index(num)] = 'X '
            if check_win(user_list):
                print "User Won User list"
                print_bingo(user_list)
                print "AI list"
                print_bingo(ai_list)
                break
            ai_list[ai_list.index(num)] = 'X '
            if check_win(ai_list):
                print "AI won Ai list"
                print_bingo(ai_list)
                print "User list"
                print_bingo(user_list)
                break
            print_bingo(user_list)
            num = get_next_move(ai_list)
            print "Number to cross out is",num
            ai_list[ai_list.index(num)] = 'X '
            if check_win(ai_list):
                print "AI won Ai list"
                print_bingo(ai_list)
                print "User list"
                print_bingo(user_list)
                break
            user_list[user_list.index(num)] = 'X '
            if check_win(user_list):
                print "User Won User list"
                print_bingo(user_list)
                print "AI list"
                print_bingo(ai_list)
                break
            print_bingo(user_list)
    else:
        print "AI starts First"
        while True:
            num = get_next_move(ai_list)
            print "Number to cross out is",num
            ai_list[ai_list.index(num)] = 'X '
            if check_win(ai_list):
                print "AI won Ai list"
                print_bingo(ai_list)
                print "User list"
                print_bingo(user_list)
                break
            user_list[user_list.index(num)] = 'X '
            if check_win(user_list):
                print "User Won User list"
                print_bingo(user_list)
                print "AI list"
                print_bingo(ai_list)
            print_bingo(user_list)
            num = input("Enter number to cross out ")
            # num = get_next_move(user_list)
            user_list[user_list.index(num)] = 'X '
            if check_win(user_list):
                print "User Won User list"
                print_bingo(user_list)
                print "AI list"
                print_bingo(ai_list)
            ai_list[ai_list.index(num)] = 'X '
            if check_win(ai_list):
                print "AI won Ai list"
                print_bingo(ai_list)
                print "User list"
                print_bingo(user_list)
                break
            print_bingo(user_list)
    
def main():
    user_list = get_user_input()
    ai_list = AI_play()
    start_play(user_list, ai_list)

if __name__ == "__main__":
    main()
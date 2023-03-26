from random import randint


def game():
    user_result = 0
    npc_result = 0
    count = 0

    while user_result < 2001 and npc_result < 2001:
        user_input = get_a_number()
        npc_number = randint(2, 12)
        print(user_input, npc_number)
        if count == 0:
            user_result += user_input
            count = 1
            npc_result += npc_number
        else:
            user_result = get_a_result(user_input, user_result)
            npc_result = get_a_result(npc_number, npc_result)
        print(f'Your actual result is: {user_result}\nYour opponent result is {npc_result}')

    if user_result > npc_result:
        print('User won!')
    elif user_result < npc_result:
        print('Computer won!')
    else:
        print('Draw')


def get_a_number():
    while True:
        try:
            user_input = int(input('Enter your dice: '))
        except ValueError:
            print('Enter a valid number')
        if user_input in range(2, 13):
            return user_input
        print('Enter a number between 2 and 12')


def get_a_result(input_, result_):
    if input_ == 7:
        result_ //= 7
    elif input_ == 11:
        result_ *= 11
    else:
        result_ += input_
    return result_


if __name__ == '__main__':
    game()

# coded by h4sski
'''
https://www.youtube.com/watch?v=th4OBktqK1I
This YT movie inspier me to try and code same /game/ by myself
'''
import random

MAX_BET_ROWS = 3
MAX_BET_VALUE = 100
MIN_BET_VALUE = 1

ROWS = 3
COLUMNS = 3

SYMBOLS ={
    'A' : 2, 
    'B' : 4, 
    'C' : 6, 
    'D' : 8
}
SYMBOLS_VALUES ={
    'A' : 6, 
    'B' : 4, 
    'C' : 3, 
    'D' : 2
}

def get_deposit():
    while True:
        depo = input('How many you want to deposit? ')
        if depo.isdigit():
            depo = int(depo)
            if depo > 0:
                break
            else:
                print('Value must be greater then 0.')
        else:
            print('Type a number.')
    return depo

def get_bet():
    while True:
        bid_value = input('How much you want to bid? ')
        if bid_value.isdigit():
            bid_value = int(bid_value)
            if MIN_BET_VALUE <= bid_value <= MAX_BET_VALUE:
                break
            else:
                print(f'Value must be between {MIN_BET_VALUE}-{MAX_BET_VALUE}.')
        else:
            print('Type a number.')
    return bid_value

def get_lines():
    while True:
        lines = input('How many lines you want to bid? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_BET_ROWS:
                break
            else:
                print(f'Value must be between 1 and {MAX_BET_ROWS}.')
        else:
            print('Type a number.')
    return lines

def get_symbols_pool():
    sym_pool = []
    for symbol, symbol_count in SYMBOLS.items():
        for _ in range(symbol_count):
            sym_pool.append(symbol)
    return sym_pool

def get_spin():
    symbols_pool = get_symbols_pool()
    local_symbols_pool = symbols_pool[:]
    spin = []
    for _ in range(COLUMNS):
        col = []
        for _ in range(ROWS):
            rand = random.choice(local_symbols_pool)
            local_symbols_pool.remove(rand)
            col.append(rand)
        spin.append(col)
    return spin

def get_total_bet(balance):
    print(f'Your balances is = {balance}')
    while True:
        lines = get_lines()
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You have to less monay. Your balance is {balance}.')
        else:
            print(f'You are betting = {total_bet}.')
            break
    return total_bet
            # spin_result = get_spin()
            # print(spin_result)
    
def print_spin(spin):
    print('---------------')
    for c in spin:
        for r in c:
            print(f'| {r} |', end = '')
        print()
    print('---------------')

def check_win(spin):
    win = []
    for c in spin:
        r_temp = c[0]
        # for r in c[1:]:
        #     if r_temp == r:
        #         win.append(r_temp)
        if c.count(c[0]) == len(c):
            win.append(c[0])
    return win

def main():
    balance = get_deposit()
    while balance >= MIN_BET_VALUE:
        bet = get_total_bet(balance)
        if bet <= balance:
            answer = input(f'For spin hit enter. Type q for quit ')
            if answer == 'q':
                break
            else:
                balance -= bet
                spin_result = get_spin()
                print_spin(spin_result)
                win_symbols = check_win(spin_result)
                if win_symbols != []:
                    print(f'\tYou won with row of {win_symbols}')
                    for win_symbol in win_symbols:
                        win_value = SYMBOLS_VALUES[win_symbol] * bet
                        balance += win_value
                        print(f'For win with {win_symbol} you earn {win_value}.')
        else:
            print('Your try bet more then you have in your balance. Try with lower bet value.')
    else:
        print(f'Sorry, but minimum bet value is {MIN_BET_VALUE}')
    print(f'You left with {balance}.')
                


if __name__ == '__main__':
    main()
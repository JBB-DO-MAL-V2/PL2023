import sys

def handle_number(char, state, number, counter):
    if char.isdigit() and state:
        number += char
    elif number != '':
        counter += int(number)
        number = ''
    return number, counter

def handle_on_off(char, on_off, state):
    if char.lower() == 'o':
        on_off = 'o'
    elif char.lower() == 'n' and on_off == 'o':
        state = True
        on_off = ''
    elif char.lower() == 'f' and on_off == 'o':
        on_off += 'f'
    elif char.lower() == 'f' and on_off == 'of':
        state = False
        on_off = ''
    else:
        on_off = ''
    return on_off, state

def main():
    state = True
    counter = 0
    number = ''
    on_off = ''
    
    for line in sys.stdin:
        for char in line:
            number, counter = handle_number(char, state, number, counter)
            on_off, state = handle_on_off(char, on_off, state)
            if char == '=':
                if number == '':
                    number = '0'
                counter += int(number)
                number = ''
                print(f"\nCounter: {counter}")
                on_off = ''
    
if __name__ == "__main__":
    main()

import re

def calculate_change(amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    result = "maq: \"troco= "
    
    for denomination in denominations:
        if amount >= denomination:
            count = amount // denomination
            amount %= denomination
            
            if count > 0:  
                coin = denomination // 100
                coin_suffix = 'e'
                
                if denomination not in denominations[:2]:
                    coin = denomination % 100
                    coin_suffix = 'c'
                    
                result += f'{count}x{coin}{coin_suffix}, '
                
    result += 'Volte sempre!"'
    result = result.replace(', V', '; V')
    
    return result


def process_coins(input_str, balance):
    total = 0
    invalid_coins = []
    coins = re.split(r', ', input_str)
    
    for coin in coins:
        if re.match(r'[125]0?c', coin):
            total += int(coin[:-1]) 
        elif re.match(r'[12]e', coin):
            total += int(coin[:-1]) * 100
        else:
            invalid_coins.append(coin)
            
    result = "maq: \""
    
    if len(invalid_coins) != 0:
        result += f"{invalid_coins} - inválido; "
        
    total_balance = balance + total
    
    result += f"saldo = {((total_balance) // 100)}e{((total_balance) % 100):02d}c\""
    print(result)
    
    return total_balance


def process_phone_number(input_str, balance):
    cost = 0
    
    if (len(input_str) == 9 and re.match(r'601|641', input_str) is None) or (len(input_str) == 11 and input_str[:2] == '00'):
        if re.match(r'00', input_str):
            cost = 150
        elif re.match(r'2', input_str):
            cost = 25
        elif re.match(r'808', input_str):
            cost = 10
            
        if cost <= balance:
            balance -= cost
            print(f"saldo = {((balance) // 100)}e{((balance) % 100):02d}c\"")
        else:
            print("maq: \"Saldo inválido!\"")
    else:
        print("maq: \"Esse número não é permitido neste telefone. Queira discar novo número!\"")
        
    return balance
    
    
balance = 0
state = ""

while state != "LEVANTAR":
    state = input()
    
print("maq: \"Introduza moedas.\"")

while state != "ABORTAR" and state != "POUSAR":
    state = input()
    
    if state[0] == 'M':
        balance = process_coins(re.sub(r'MOEDA ', '', state), balance)
    elif state[0] == 'T':
        balance = process_phone_number(re.sub(r'T=', '', state), balance)
        
print(calculate_change(balance))

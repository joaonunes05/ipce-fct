
import random
MAX_HILO = 1023

def initial_request(lo: int, hi: int):
    """ Start game. """
    print(f"Pense num número secreto entre {lo} e {hi}!")
    input("Já pensou? <ENTER> ")    # wait

def ask(guess: int) -> str:
    """ Read input until "<", ">" ou "=" """
    print(f'A minha tentativa é {guess}. ', end='')
    while True:
        rel = input('O número secreto é maior (>), menor (<) ou igual (=) ?  ')
        if rel in ['<', '>', '=']:
            break
    return rel

def ask_diff() -> int:
    diff = -1
    while diff not in [0, 1]:
        diff = int(input('Normal - 0, Dificil - 1: '))
    return diff

def final_message(lo: int, hi: int, attempts: int, guess: int):
    """ End game. """
    if lo > hi:
        print("Você é batoteiro!")
    else:
        print(f"Viva! Acertei em {attempts} tentativas! O número secreto era {guess}!")


def play_hilo_reverse(lo: int, hi: int):
    """ The classic HI-LO game in the closed range lo to hi. """
    initial_request(lo, hi)
    diff = ask_diff()
    attempts = 0
    low = lo
    high = hi
    rel = ''
    
    while rel != '=' and low <= high:
        if diff == 0:
            guess = random.randint(low, high)
        else:
            guess = (low + high) // 2
        rel = ask(guess)
        attempts += 1
        if rel == '<':
            high = guess - 1
        if rel == '>':
            low = guess + 1
    
    final_message(low, high, attempts, guess)

def main():
    print("JOGO HI-LO (REVERSE)")
    play_hilo_reverse(0, MAX_HILO)

main()
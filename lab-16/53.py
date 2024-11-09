def update_visible(visible: list[str], secret: str, c: str):
    """ Copy to 'visible' all the ocurrences of 'c' in 'secret'.
        Precondition: len(c) == 1
    """
    _ = 0
    for i in range(len(secret)):
        if c == secret[i]:
            visible[i] = c
            _ = 1
    if _ == 0: print(f"A letra '{c}' não faz parte do segredo.")

def print_visible(visible: list[str]):
    """ Show the current state of the discovery? """
    print(' '.join(visible))

def got_it_right(visible: list[str], secret: str) -> bool:
    """ Has discovered the secret yet? """
    return ''.join(visible) == secret

def input_letter(prompt: str) -> str:
    """ Input a letter (alphabetic char). """
    while True:
        s = input(prompt)
        if len(s) == 1 and s.isalpha():
            return s

def end_game(visible: list[str], secret: str, attempts: int) -> str:
    """ Action at the end of the game. """
    if got_it_right(visible, secret):
        print(f"Parabéns! Adivinhou em {attempts} tentativas o segredo '{secret}'!")
    else:
        print(f"Lamento, mas esgotou o número de tentativas. O segredo era '{secret}'.")

def interaction(secret: str, max_attempts: int):
    """ User interaction. """
    print("Bem-vindo ao Jogo da Forca!")
    visible = ['#'] * len(secret)   # é preciso usar uma lista mutável; uma string não serve
    attempts = 0
    print_visible(visible)
    for attempts in range(max_attempts):
        if got_it_right(visible, secret):
            break
        update_visible(visible, secret, input_letter(f'{(attempts + 1):02} - Adivinhe uma letra: '))
        print_visible(visible)
    end_game(visible, secret, attempts)

def main():
    MAX_ATTEMPTS = 10
    interaction("ananas", MAX_ATTEMPTS)

main()
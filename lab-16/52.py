type Atlas = dict[str, str]            # país -> capital

END_MARK = "fim"

def interaction(atlas: Atlas):
    """ User interaction. """
    while True:
        country = input("PAÍS: ")
        if country == "fim":
            break
        if country in atlas:
            print(f'{country} -> {atlas[country]}')
        else:
            atlas[country] = input(f'Não conheço a capital de {country}. Por favor ensine-me: ')

def main():  
    atlas = {"Portugal":"Lisboa", "Espanha":"Madrid", "França":"Paris"}
    interaction(atlas)

main()
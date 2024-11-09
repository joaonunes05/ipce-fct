type WordList = list[str]

def how_many_of_each(l:  WordList) -> dict[str, int]:
    """ Count the ocurrences of each word in the list l. """
    d = dict()      # cria dicionário vazio
    for s in l:
        if s in d:
            d[s] = d[s] + 1
        else:
            d[s] = 1
    return d

def main():
    a = ['a', 'mera', 'gnosiologia', 'explícita', 'ou', 'deliberadamente', 'divorciada', 'da',
         'axiologia', 'por', 'um', 'lado', 'e', 'da', 'ontologia', 'por', 'outro', 'não', 'se',
         'converte', 'sem', 'mais', 'em', 'fundamentação', 'deontológica', 'em', 'razão', 'do',
         'dever', 'ser']
    b = ['a', 'mera', 'gnosiologia', 'simples', 'afirmação', 'teorética', 'deliberadamente',
         'divorciada', 'da', 'axiologia', 'e', 'da', 'ontologia', 'não', 'nos', 'pode', 'fornecer',
         'uma', 'fundamentação', 'deontológica']
    c = ['a', 'axiologia', 'converte', 'da', 'deliberadamente', 'deontológica', 'dever', 'divorciada',
         'do', 'e', 'em', 'em', 'explícita', 'fundamentação', 'gnosiologia', 'lado', 'mais', 'mera',
         'não', 'ontologia', 'ou', 'outro', 'por', 'por', 'razão', 'se', 'sem', 'ser', 'um']    
    for wl in [a,b,c]:
        print(how_many_of_each(wl))

main()
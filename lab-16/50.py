type WordList = list[str]

def has_duplicates(l: WordList) -> bool:
    """ Has the list l any duplicate values? """
    return (len(set(l)) < len(l))

def same_words(a: WordList, b: WordList) -> bool:
    """ Do the lists a and b have  exactly the same words? """
    return (set(a) == set(b))

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
    l = [has_duplicates(wl) for wl in [a, b, c]]
    print(l)
    l = [same_words(wl1, wl2) for (wl1,wl2) in [(a,b), (a,c), (b,c)]]
    print(l)

main()
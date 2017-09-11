#Chester de Lang

voldoende_score = 15
ingegeven_score = eval(input('Geef je score: '))

if ingegeven_score > voldoende_score:
    print('Gefeliciteerd!')
    print('met een score van' + ' ' + str(ingegeven_score) + ' ' + 'ben je geslaagd!')
else:
    print('Je hebt het helaas niet gehaald')

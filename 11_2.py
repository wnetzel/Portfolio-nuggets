import re

# Standard fil til teståpning:
# tellefil = open('regex_sum_974545.txt')

filnavn = input("Hvilken fil? ")
if len(filnavn) < 1 : tellefil = open('regex_sum_974545.txt')
tellefil = open(filnavn)

telleverk = 0
antall = 0

for line in tellefil:
    napp = re.findall('[0-9]+', line)
    for tall in napp :
        tall = int(tall)
        telleverk = telleverk + tall
        antall += 1

print('Number of numbers:',antall)
print('Sum of numbers:',telleverk)

# Det er mulig å få til alt dette på 2 linjer kode, via 'list comprehension':
#
# import re
# print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

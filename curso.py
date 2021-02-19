

# recebe list

values = range(1, 100)
list = []
a = 10
print ( values)

for value in values :
    list.append(value)
    print(list)

# select only "odd" numbers
odd = []
for value in values :
    if (value % 2) == 0 :   # if remaider = 0 - odd
        odd.append(value)
        print( f'Odd : {odd}')
even = []
for value in values :
    if (value % 2) != 0 :
        even.append(value)
        print( f'Even : {even}')

soma = 0
for value in values :
    soma = soma + value

print(f'total sum of values, {soma}')
soma = 0
med = 0
tot_rep = len(values)
for value in values :
    soma = soma + value

med = soma / tot_rep

print(f'the average is :, {med}')

# fatorial
fator = int(10)
fatorial = 1

for value in range (1, fator) :
    fatorial = fatorial * value

print (fatorial)

word = 'Patricia'

count = 1
for i in range (len(word)-1) :
    count=1
    letter1 = word[i]
    #print(letter1)
    for z in range(len(word)-1,i,-1) :
        letter2 = word[z].lower()
        #print(letter2)
        if letter1 == letter2 :
            count = count + 1

    print(f'letter {word[i]} =  {count}')







"""    
    print(len(word))
    for z in range(len(word)-1,0,-1):
        print(word[z])
        if a == word[z]:
            count = count + 1

    print(f'letter {word[i]} = {count}')
"""














## Chp_3: Control Sequences

# if ----
if 2 + 2 == 4: #condition
    print('that was true') #outcome if true (if false, nothing happens)

if 2 + 2 == 5:
    print('that was true') #outcome if true
else:                       #outcome in any other case (e.g. when false)
    print('that was false')

if 2 + 2 == 4: #condition with multiple statements if true
    print('that was true') 
    print('...really true')

if 2 + 2 == 4: #1-statement block 
    print("that's true") #this is the outcome of conditional when true
print('or this....') #this is independent of conditional

if 2 + 2 == 5: #only else block executes
    print("this won't print")
else:
    print('but this will')
    print('...and so will this')

x = 'hat' #set a variable
if x[0] == 'a': #if word begins with "a"
    pass #empty outcome
else:
    print('doing something here....')

print('one','two',sep='-',end='!') #Digression in print


# for ----
for i in [1,2,3]: #iterates 'variable' over sequence 'in...'
    print(i) #block applied for each assignement

for i in [1,2,3]: #nothing requires we use the value i in the block.
    print('wow') #i assumes each value, but produces print

for i in [1,2,3]: 
    print("{} + 2 = {}".format(i, i+2))

for i in 'tone':
    print(i, end = ' ') #letters with spaces
print() #add return at end

# Recurssion using for
total = 0 #sets base variable
for i in range(5): #iterate 5 times (from 0 to 4)
    total = total + i #reassigns values of total and i
print(total) #prints only 'final' total (because not indented inside 'for')

# Morphological Recursion
prefix = 'anti' #initial prefix (i)
word = 'missile' #initial word
print(word) #print word

for i in range(3): #iterates 3 times
    word = prefix + "-" + word #reassigns value of 'word'
    print(word) #prints 'all' instances

# Define prefix and 3 words
prefix = 'anti'
words = ['missile','racism','music']
for word in words: #iterate over words
    print(word) #print word
    for i in range(3):
        word = prefix + "-" + word
        print(word)

# Sum numbers up to 10000
total = 0
for i in range(10000):
    total = total + i
print(total)


# Vowel Counter
vowels = 'aeiou'
vowelCount = 0
word = 'Appalachicola'
for letter in word:
    if letter in vowels:
        vowelCount += 1
print(vowelCount)

# Count Words if word is V-initial
vowels = 'aeiou'
letterCount = 0
word = 'Appalachicola'
if word[0].lower() in vowels:
    for letter in word:
        letterCount += 1
else:
    print('Not vowel-initial')
print(letterCount)

# while ----
count = 0
while count < 3: #while, followed by the test
    count += 1 #statement 1
    print(count)

# while within while
word = 'alphabet' #define word
count = 0 #define counter
#iterate while count is less than word length
while count < len(word):
    print(word[count]) #print current letter 
    count += 1 #increment counter
    othercount = 1 #start new counter
    #check if 2nd counter is less than 1st
    while othercount < count+1:
        #print ever larger prefixes
        print('\t',word[0:othercount])
        othercount += 1 #increment other counter

# if within while
word = 'alphabet'
vowels = 'aeiou'
count = 0
while count < len(word):
    letter = word[count]
    if letter not in vowels:
        print(letter)
    count += 1

# Difference between for and while
for i in [1,2,3]:
    print(i)

i = 1
while i < 4:
    print(i)
    i += 1

# Vowel counter
vowels = 'aeiou'
word = 'Winnepesaukee'
counter = 0
vowelCount = 0
while counter < len(word):
    if word[counter] in vowels:
        vowelCount += 1
    counter +=1
print('\n', '***There are',vowelCount, 'vowels in this word.***', '\n')


# use the range
print(range(3))
print(range(0,3))

# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N) :
    print(dates[i])
for i in range(len(dates)) :
    print(dates[i])

# Example of for loop
for i in range(0, 8):
    print(i)

# Exmaple of for loop, loop through list
for i in dates:
    print(i)

# for i in len(range(dates)) :
#     print(i)

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])



# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)

# while
count = 1
while count <= 5:
    print(count)
    count += 1

# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while (year != 1973):
    print(year)
    i = i + 1
    year = dates[i]
print("It took ", i, "repetitions to get out of loop.")

# for
for i in range(-5,6) :
    print(i)

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres :
    print(i)

squares=['red', 'yellow', 'green', 'purple', 'blue']
for i in squares :
    print(i)

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
count = 0
while ( PlayListRatings[count] >= 6 ) :
    print(PlayListRatings[count])
    count = count+1
print("less than 6")

# Write your code below and press Shift+Enter to execute
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(squares[i]=='orange') :
    new_squares.append(squares[i])
    i = i+1
print(new_squares)

for i in range (0,13) :
    print(6*i,7*i)

Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
A = []
i = 0
while(i < len(Animals)) :
    j = Animals[i]
    if(len(j)==7) :
        A.append(j)
    i=i+1
print(A)








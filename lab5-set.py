# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)

# Add element to seT
A.add("hi")
print(A)

# Try to add duplicate element to the set
A.add("hi")
print(A)

# Remove the element from set
A.remove('hi')
print(A)

# Verify if the element is in the set
print("AC/DC" in A)


# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
print(album_set1 , album_set2)


# Find the intersections
intersection = album_set1 & album_set2
print(intersection)
intersection = album_set1.intersection(album_set2)
print(intersection)

# Find the difference in set1 but not set2
album_set1.difference(album_set2)

# Find the union of two sets
album_set3 = album_set1.union(album_set2)

# Check if superset
print(set(album_set1).issuperset(album_set2) )
print(album_set1.issuperset(album_set2))

# Check if subset
set(album_set2).issubset(album_set1)
print(album_set1.issubset(album_set3))


#####list to set
A_list = ['rap','house','electronic music', 'rap']
A_set = set(A_list)
print(A_set)


A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print("the sum of A :" , sum(A))
print("the sum of B:" , sum(B))




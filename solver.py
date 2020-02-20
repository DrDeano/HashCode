import math

file_name = "a_example"

num_of_book = 0
num_of_libraries = 0
num_of_days = 0

book_scores = []
libraries = []

library_count = 0
with open(file_name + ".txt", "r") as in_file:
    line_number = 0
    for line in in_file:
        if line_number == 0:
            # Book, library, days
            first_line = line.split()
            num_of_book = int(first_line[0])
            num_of_libraries = int(first_line[1])
            num_of_days = int(first_line[2])
        elif line_number == 1:
            # Book scores
            second_line = line.split()
            book_scores = [int(b) for b in second_line]
        else:
            # Library stuff
            if line_number % 2 == 0:
                # First line of libray info
                libraries.append([int(b) for b in line.split()])
            else:
                # Second line
                libraries[library_count].append([int(b) for b in line.split()])
                library_count += 1
        line_number += 1

print("Number of books: ", num_of_book)
print("Number of libraries: ", num_of_libraries)
print("Number of days: ", num_of_days)

print("Book scores: ", book_scores)
print("Libraries: ", libraries)

for library in libraries:
    total_score = 0
    books = library[3]
    for book_index in books:
        total_score = total_score + book_scores[book_index]
    library.append(total_score)
    total_days = library[1] + math.ceil(library[0] / library[2])
    library.append(total_days)

print("Libraries: ", libraries)

# for day
#   if library not being setup:
#       Start library with highest score
#       add library to final list
#   else
#       decriment library that is being set up
#       if 0: no library set up next day
#   for each library that has been set up
#       send highest scoring book that another library hasn't sent
#       if none exist take library off, is done
#   
#   
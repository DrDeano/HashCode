file_name = "a_example"

num_of_book = 0
num_of_libraries = 0
num_of_days = 0

book_scores = []
libraries = {}

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
                libraries[library_count] = [int(b) for b in line.split()]
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

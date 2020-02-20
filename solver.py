import math

file_name = "a_example"

num_of_book = 0
num_of_libraries = 0
num_of_days = 0

book_scores = []
libraries = []

final_number_libraries = 0
final_libraries = []


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

def get_highest_book_index(lib):
    book_indexs = lib[3]
    max_book_score = -1
    max_book_scoring_index = -1
    for book_index in book_indexs:
        if book_scores[book_index] > max_book_score:
            max_book_score = book_scores[book_index]
            max_book_scoring_index = book_index
    return max_book_scoring_index

current_library_being_set_up = -1
libraries_sending_books = []

with open(file_name + ".out", "w") as solvedit:
    solvedit.write(str(final_number_libraries) + "\n")
    for i in final_libraries :
        sub = final_libraries[i]
        for j in sub :
            if j == 0:
                solvedit.write(str(sub[j]) + " ")
            elif j == 1:
                solvedit.write(str(sub[j]) + "\n")
            else :
                subsub = sub[j]
                for k in subsub:
                    if k == len(subsub) - 1 :
                        solvedit.write(str(subsub[k]) + "\n")
                    else :
                        solvedit.write(str(subsub[k]) + " ")

for day in range(num_of_days):
    if current_library_being_set_up == -1:
        current_lib = libraries[0]
        current_lib_index = -1
        for index, lib in enumerate(libraries):
            if lib[4] > current_lib[4]:
                current_lib = lib
                current_lib_index = index
        current_library_being_set_up = current_lib_index
        final_libraries.append([current_library_being_set_up])
        final_number_libraries += 1
    else:
        if libraries[current_library_being_set_up][1] == 1: # Pretend this is 0 mate
            libraries_sending_books.append(current_library_being_set_up)
            current_library_being_set_up = -1
    libraries[current_library_being_set_up][1] -= 1
    for lib_index in libraries_sending_books:
        lib = library[lib_index]
        lib_books =
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

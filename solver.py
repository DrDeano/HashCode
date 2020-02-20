import math

file_name = "b_read_on"

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

# print("Number of books: ", num_of_book)
# print("Number of libraries: ", num_of_libraries)
# print("Number of days: ", num_of_days)

# print("Book scores: ", book_scores)
# print("Libraries: ", libraries)

for library in libraries:
    total_score = 0
    books = library[3]
    for book_index in books:
        total_score = total_score + book_scores[book_index]
    library.append(total_score)
    total_days = library[1] + math.ceil(library[0] / library[2])
    library.append(total_days)

# print("Libraries: ", libraries)

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
libraies_that_have_been_set_up = []
for day in range(num_of_days):
    print(day)
    if current_library_being_set_up == -1:
        current_lib = [-1,-1,-1,-1,-1]
        current_lib_index = -1
        for index, lib in enumerate(libraries):
            if index not in libraies_that_have_been_set_up:
                if lib[4] > current_lib[4]:
                    current_lib = lib
                    current_lib_index = index
        current_library_being_set_up = current_lib_index
        final_libraries.append([current_library_being_set_up,0,[]])
        final_number_libraries += 1
    else:
        if libraries[current_library_being_set_up][1] == 1: # Pretend this is 0 mate
            libraries_sending_books.append(current_library_being_set_up)
            libraies_that_have_been_set_up.append(current_library_being_set_up)
            current_library_being_set_up = -1
        else:
            libraries[current_library_being_set_up][1] -= 1
    
    for lib_index in libraries_sending_books:
        lib = libraries[lib_index]
        for _ in range(lib[2]):
            book_index = get_highest_book_index(lib)
            if book_index != -1:
                for fin_lib in final_libraries:
                    if fin_lib[0] == lib_index:
                        fin_lib[2].append(book_index)
                        fin_lib[1] += 1
                        break

                for lib_2 in libraries:
                    try:
                        lib_2[3].remove(book_index)
                    except:
                        pass


for i in range(len(final_libraries)):
    if final_libraries[i][1] == 0:
        final_libraries.remove(final_libraries[i])
        i -= 1
        final_number_libraries -= 1

print("Final library number: ", final_number_libraries)
print("Final library array: ", final_libraries)

with open(file_name + ".out", "w") as solvedit:
    solvedit.write(str(final_number_libraries) + "\n")
    for i in final_libraries:
        #sub = final_libraries[i]
        sub = i
        for j in range(len(sub)):
            if j == 0:
                solvedit.write(str(sub[j]) + " ")
            elif j == 1:
                solvedit.write(str(sub[j]) + "\n")
            else:
                subsub = i[2]
                for k in range(len(subsub)):
                    if k == len(subsub) - 1:
                        solvedit.write(str(subsub[k]) + "\n")
                    else:
                        solvedit.write(str(subsub[k]) + " ")

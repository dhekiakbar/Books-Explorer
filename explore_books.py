import json
import lib as lib

# load file hasil scrap
with open("books.json") as file :
    books_data = json.load(file)

loop = True

lib.welcome()

while loop :
    loop = lib.menu(books_data)
    # count = 1
    # for books in books_data : #Sudah bisa ambil data berdasar kategori
    #     if books['category'] == "Religion":
    #         print(books["name"])
    #         print(count)
    #     count += 1
    # lib.filter_category(books_data, "Music")



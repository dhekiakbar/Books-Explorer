from pick import pick
import re

def welcome() :
    print("="*64)
    print("|| Hi, let's explore a bunch of books from books.toscrape.com ||")
    print("="*64)

def menu(data):
    title = "Select Your Menu Option"
    options = ["Filter by Category", "Filter by Price", "Filter by Keyword", "Customized  Filter", "Exit"]
    selected = pick(options, title, indicator="=>")

    if selected[0] == options[0] :
        category = input("Input Category Name : ")
        filtered_data = filter_category(data, category)


        count = 1
        print("=====================\nBooks Found : \n=====================")
        for books in filtered_data :
            print(f"[{count}] {books['title']}")
            print(f"==> price : {books['price']}, category : {books['category']}")
            count += 1
        
        input("\nPress Enter to continue...")

        return True
    
    elif selected[0] == options[1] :
        start = input("Start Price : ")
        if not re.match(r"^\d+(\.\d+)?$", start):
            print("Invalid start price")
            return
        start_price = float(start)
        end = input("End Price (type 0 if unlimited) : ")
        if not re.match(r"^\d+(\.\d+)?$", end):
            print("Invalid end price")
            return
        end_price = float(end)
        filtered_data = filter_price(data, start_price, end_price)    

        count = 1
        print("=====================\nBooks Found : \n=====================")
        for books in filtered_data :
            print(f"[{count}] {books['title']}")
            print(f"==> price : {books['price']}, category : {books['category']}")
            count += 1
        
        input("\nPress Enter to continue...")

        return True
    
    elif selected[0] == options[2] :
        keyword = input("Enter Keyword : ")
        filtered_data = filter_keyword(data, keyword)

        count = 1
        print("=====================\nBooks Found : \n=====================")
        for books in filtered_data :
            print(f"[{count}] {books['title']}")
            print(f"==> price : {books['price']}, category : {books['category']}")
            count += 1
        
        input("\nPress Enter to continue...")

        return True
    
    elif selected[0] == options[3] :
        title = "Select Your Filters, press Space to select and Enter if you done chosing : "
        options = ["Filter by Category", "Filter by Price", "Filter by Keyword"]
        selected = pick(options, title, multiselect=True, min_selection_count=2, indicator="=>")

        filtered_data = data
        for choice in selected :
            if choice[0] == options[0] :
                category = input("Input Category Name : ")
                filtered_data = filter_category(filtered_data, category)
            
            elif choice[0] == options[1] :
                start = input("Start Price : ")
                if not re.match(r"^\d+(\.\d+)?$", start):
                    print("Invalid start price")
                    return
                start_price = float(start)

                end = input("End Price (type 0 if unlimited) : ")
                if not re.match(r"^\d+(\.\d+)?$", end):
                    print("Invalid end price")
                    return
                end_price = float(end)
                filtered_data = filter_price(filtered_data, start_price, end_price)
            
            elif choice[0] == options[2]:
                keyword = input("Enter Keyword : ")
                filtered_data = filter_keyword(filtered_data, keyword)

        count = 1
        print("=====================\nBooks Found : \n=====================")
        for books in filtered_data :
            print(f"[{count}] {books['title']}")
            print(f"==> price : {books['price']}, category : {books['category']}")
            count += 1
        
        input("\nPress Enter to continue...")
        
        return True

   
    elif selected[0] == options[4] :
        return False

    else :
        print("Invalid Option")
        return True

def filter_category(data, selected_category):
    filtered_data = []
    for books in data:
        if selected_category.upper() in books['category'].upper():
            filtered_data.append(books)
    return filtered_data


def filter_keyword(data, keyword):
    filtered_data = []
    for books in data:
        if (keyword.upper() in books['category'].upper()) or \
           (keyword.upper() in books['title'].upper()):
            filtered_data.append(books)
    return filtered_data


def filter_price(data, start_price, end_price):
    filtered_data = []
    if end_price == 0:
        end_price = 99999999

    for books in data:
        price = float(books['price'].replace("£", "").strip())
        if price >= start_price and price <= end_price:
            filtered_data.append(books)

    return filtered_data
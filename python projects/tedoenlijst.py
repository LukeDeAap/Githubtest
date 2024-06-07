import time





#yes_no = input("Do you want to save something to your file? Yes(y) or No(n)")
#if yes_no == 'yes' or 'y':
#    yes_no == True
#else:
#    yes_no == False

to_do_list = []
count = 1
while True:
    
    print("1. Input contents in text file")
    print("2. See content of text file")
    print("3. delete content in text file")
    print("4. Quit")

    choice = input("Choose: 1, 2, 3, or 4  ")
    if choice == '1':
        count = 1
        while count == 1:
            item = input("Enter item: ")
            to_do_list.append(item)
            print("Item added to the list.")
            yes_or_no2 = str(input("Add another item? Y/N  "))
            if yes_or_no2 == 'n':
                count-=1
    elif choice == '2':
        if to_do_list:
            print("To-do Items:")
            print("---------")
            for index, item in enumerate(to_do_list, start=1):
                print(f'{index}. {item}')
            print("---------")
            time.sleep(3)
        else:
            print("To-do list is empty.")
    
    elif choice == '3':
        print("To-do Items:")
        print("---------")
        for index, item in enumerate(to_do_list, start=1):
                print(f'{index}. {item}')
        print("---------")
        item1 = input("Item that you want to remove: ")
        to_do_list.remove(item1)
        print(item1,"has been removed")
        print("New To-do list:")
        print("---------")
        for index, item in enumerate(to_do_list, start=1):
                print(f'{index}. {item}')
        print("---------")
    elif choice == '4':
        print("See ya later!")
        break
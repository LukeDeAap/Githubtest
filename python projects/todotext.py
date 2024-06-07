import time





#yes_no = input("Do you want to save something to your file? Yes(y) or No(n)")
#if yes_no == 'yes' or 'y':
#    yes_no == True
#else:
#    yes_no == False

to_do_list = open("todotext.txt", "r")
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
            File_object = open("todotext.txt", "a")
            item = File_object.write(input("Enter item: ")+'\n')
            File_object.close()
            print("Item added to the list.")
            yes_or_no2 = str(input("Add another item? Y/N  "))
            if yes_or_no2 == 'n':
                count-=1
            elif yes_or_no2 != 'n' and  yes_or_no2 != 'y':
                 print('\n'"invalid input..."'\n')
                 break
                
            
                 
    elif choice == '2':
        if to_do_list:
            to_do_list = open("todotext.txt", "r")
            print("To-do Items:")
            print("---------"+'\n')
            for index, item in enumerate(to_do_list, start=1):
                print(f'{index}. {item}')
            print("---------")
            to_do_list.close()
        else:
            print("To-do list is empty.")
    
    elif choice == '3':
        count = 1
        to_do_list = open("todotext.txt", "r")
        print("To-do Items:")
        print("---------"+'\n')
        for index, item in enumerate(to_do_list, start=1):
                print(f'{index}. {item}')
        print("---------")
        to_do_list.close()
        while count == 1:
            item1 = input("Item that you want to remove: ")
            with open("todotext.txt", "r") as f:
                data = f.readlines()
            with open("todotext.txt", "w") as f:
                for line in data:
                    if line.strip("\n") != item1:
                        f.write(line)
            print(item1,"has been removed")
            to_do_list = open("todotext.txt", "r")
            print("New To-do list:")
            print("---------"+'\n')
            for index, item in enumerate(to_do_list, start=1):
                    print(f'{index}. {item}')
            print("---------")
            yes_or_no3 = yes_or_no2 = str(input("Remove another item? Y/N  "))
            to_do_list = open("todotext.txt", "r")
            if yes_or_no2 == 'n':
                count-=1
            elif yes_or_no2 != 'n' and  yes_or_no2 != 'y':
                 print('\n'"invalid input..."'\n')
                 break
    elif choice == '4':
        print("See ya later!")
        break
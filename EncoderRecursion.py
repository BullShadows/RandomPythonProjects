userin = input("Enter in something you want to be encrypted")
asci_val = []
for i in userin:
    asci_val.append(ord(i))
print("Here is your encoded message")
for i in asci_val:
    print(i," ", end="")
decode = []
current_group = ""

userin2 = input("\nDo you want to decrypt a message?").lower()
new_list = []
final_list = []
if userin2 == "yes":
    decode_this = input("Enter in your message to decrypt")
    decode = decode_this.split()
    for i in decode:

        new_list.append(chr(int(i)))
    for i in new_list:
        if i != " ":
            current_group += i
        else:
            if current_group:
                final_list.append(current_group)
                current_group = ""
    if current_group:
        final_list.append(current_group)
        current_group = ""
    is_all_numbers = all(item.isdigit() for item in final_list)

    while is_all_numbers == True:
        new_list.clear()
        for i in final_list:
            new_list.append(i)
        final_list.clear()
        for i in new_list:
            final_list.append(chr(int(i)))
        new_list.clear()
        for i in final_list:
            if i != " ":
                current_group += i
            else:
                if current_group:
                    new_list.append(current_group)
                    current_group = ""
        if current_group:
            new_list.append(current_group)
            current_group = ""
            final_list.clear()
        for i in new_list:
            final_list.append(i)
        is_all_numbers = all(item.isdigit() for item in final_list)
        if is_all_numbers == False:
            break


    """
    while is_all_numbers == True:
        new_list = final_list
        print(new_list[0])
        print(type(new_list[0]))
        for item in new_list:
            #print(item)
            #print(type(item))
            final_list.append(chr(121))
        is_all_numbers = False
        is_all_numbers = all(item.isdigit() for item in final_list)
        """
for i in final_list:
    print("Here is your decoded message: ",i,end="")
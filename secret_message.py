
print("Secret Message Generator\n")

guest_name = input("Enter the recipient's name: \n").strip()
print()
message = input("Enter your secret party message: \n").strip()

cleaned_message = message.strip()
uppercase_version = cleaned_message.upper()
reverse_version = cleaned_message[::-1]
char_count = len(cleaned_message)
print()
print("Which format of your message would you like to see?\n")
print(f"1) Uppercase message: {uppercase_version}")
print(f"2) Reversed message: {reverse_version}")
print(f"3) Number of characters: {char_count}")
print()
user_choice = input("Please enter 1, 2, or 3 to choose the format of your message: \n")
print()
if user_choice == "1":
    print(f"Hey {guest_name}, here's your secret code: {uppercase_version}\n")
elif user_choice == "2":
    print(f"Hey {guest_name}, here's your secret code: {reverse_version}\n")
elif user_choice == "3":
    print(f"Hey {guest_name}, here's your secret code: {char_count}\n")
else:
    print("Please enter 1, 2, or 3\n")

print("Do you accept this message?")
print("Y) Yes")
print("N) No\n")
user_accept = input("Enter Y for Yes. Enter N for No: ")
if user_accept == "Y":
    print("Awesome! Enjoy the party!")
else:
    print("Sorry, we couldn't help you")

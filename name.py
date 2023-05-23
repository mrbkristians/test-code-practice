from name_function import get_formatted_name

print("\nEnter 'q' at any time to quit.")

while True:
    first = input("\nEnter your first name: ")
    if first == 'q':
        break
    last = input("Eenter your last name: ")
    if last == 'q':
        break
    middle = input("Enter your middle name(optional): ")
    if middle = 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tHello, {formatted_name}")
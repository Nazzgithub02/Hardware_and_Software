def display_menu():
    menu_dict = {
        'A':'Apple',
        'B':'Banana',
        'C':'Cherry'
    }
    for items, values in menu_dict.items():
        print(items+". "+ values)
def main():
    display_menu()

if __name__ == "__main__":
    main()
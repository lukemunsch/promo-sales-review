import gspread
from google.oauth2.service_account import Credentials
from collections import OrderedDict

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('promo-sales-review')


def password_request():
    """
    This will set up the functions for specific requests by the admins
    The user will need to specifically state their intention
    """
    while True:
        print("You must input the 'password' to authorize the update.")
        print("***NOTE: the password is case sensitive.***\n")

        password = input("Please enter your password: \n")

        if validate_password(password):
            print("Loading systems...")
            break


def validate_password(value):
    """
    This is used to make sure the input from user is the correct value
    by making the format and type of input matches exact request.
    """
    try:
        if value != "MAGIC":
            raise ValueError
    except ValueError:
        print("Invalid Password, please try again.\n")
        return False
    else:
        print("You are authorised.\n")
        return True


def get_sales_data():
    """
    Gets the original sales data to then build on later in
    other functions
    """
    print("Retrieving all the sales information...")
    data = SHEET.worksheet('sales')
    print("Compilation complete!\n")
    return data


def get_new_list(data, column):
    """
    This will build a new list for the required sections:
    - advisor list
    - items list
    - values list
    """
    a_list = data.col_values(column)
    del a_list[0]
    return a_list


def count_total_sales(value):
    """
    This will count the total number of sales
    based on one of the lists
    """
    count = len(value)
    print(f"We have found a total of {count} sale(s).\n")
    return count


def count_sales_value(value1, value2):
    """
    This will calculate the total value of the sales made so far
    as well as the average sales value.
    """
    print("Calculating the TOTAL and AVERAGE sales values...")
    total_val = sum(value1)
    avg_val = sum(value1) / value2
    print("We have finished calculations.\n")
    print(f"Total value of sales: £{total_val:.2f}.")
    print(f"Average value of sales: £{avg_val:.2f}.\n")


def create_unique_value_list(value):
    """
    The function to find only unique values in a list;
    needed for items and advisors
    """
    my_set = set(value)
    new_list = list(my_set)
    new_list.sort()
    return new_list


def print_list(value):
    """
    This will print a list of the advisors who have sold something
    """
    print(*value, ", ")


def create_dict_count(value):
    """
    this will count the number of occurances of all items in a list
    """
    counted = OrderedDict([(i, value.count(i)) for i in value])

    for key, value in counted.items():
        print(key, ' : ', value)
    print("")
    return counted


def find_max_key_val(value):
    most_sold = max(value, key=value.get)
    keys_val = value.get(most_sold)
    print(f"We can see the most sold item is {most_sold},")
    print(f"with a total of {keys_val} sale(s).\n")
    return keys_val


def sale_call(data):
    """
    Calls all functions for displaying calculated values when called in menu
    """
    print('-' * 80)
    print("")
    print("This is the Sales review.\n")
    items_tally = get_new_list(data, 4)
    total_sales = count_total_sales(items_tally)
    sales_vals = get_new_list(data, 5)
    values_tally = [int(num) for num in sales_vals]
    count_sales_value(values_tally, total_sales)
    exit_call = continue_exit(data)
    if exit_call:
        return True
    else:
        return False


def item_call(data):
    """
    Calls all functions related to item sales
    """
    print('-' * 80)
    print("")
    print("This is the Item Review.\n")
    items_tally = get_new_list(data, 4)
    create_unique_value_list(items_tally)
    item_sale_count = create_dict_count(items_tally)
    find_max_key_val(item_sale_count)
    exit_call = continue_exit(data)
    if exit_call:
        return True
    else:
        return False


def adv_call(data):
    """
    Calls all functions related to advisor performance
    """
    print('-' * 80)
    print("")
    print("This is the Advisor Review.")
    advisor_tally = get_new_list(data, 3)
    create_unique_value_list(advisor_tally)
    print("Here is the total sales for the advisors.\n")
    adv_sale_count = create_dict_count(advisor_tally)
    find_max_key_val(adv_sale_count)
    exit_call = continue_exit(data)
    if exit_call:
        return True
    else:
        return False


def menu(data):
    """
    This will allow the terminal to choose what is needed to display
    - sales values
    - item sales
    - advisor performance
    """
    print('-' * 80)
    while True:
        print("Please choose which section you would like to review.")
        print("""
        1. Sales Review
        2. Item Review
        3. Advisor Review
        4. Exit/Quit
        """)

        review = input("Please type your choice NUMBER and press ENTER: \n")
        if validate_input(review):
            if review == '1':
                print(f"You typed '{review}', Sales Data will be compiled...\n")
                exit_call = sale_call(data)
                if exit_call:
                    print("Reload Complete!")
                else:
                    return False
            elif review == '2':
                print(f"You typed '{review}', We are now loading the Items Data...\n")
                exit_call = item_call(data)
                if exit_call:
                    print("Reload Complete!")
                else:
                    return False
            elif review == '3':
                print(f"You typed '{review}', We are now taking you to the Advisor Data...\n")
                exit_call = adv_call(data)
                if exit_call:
                    print("Reload Complete!")
                else:
                    return False
            else:
                print(f"You typed {review}, You have chosen to leave the programme...\n")
                print("The programme will now terminate...\n")
                print("Have a nice day! :-)")
                print('-' * 80)
                return False
                


def validate_input(value):
    try:
        values = ['1', '2', '3', '4']
        if value not in values:
            raise ValueError
    except ValueError:
        print(f"Invalid selection, you typed '{value}'. Please try again.\n")
        print('-' * 80)
        return False
    else:
        return True


def continue_exit(data):
    """
    Requests input from user to return to menu or exit programme
    """
    print('-' * 80)
    print("You can return to the main menu to review a different section,")
    print("or you can terminate the programme.\n")
    result = input("Would you like to continue? 'y'/'n': \n")

    while True:
        if validate_choice(result):
            if result == 'y':
                print(f"You typed {result}, we will return you to the main menu.")
                print("Reloading menu...")
                print("")
                print('-' * 80)
                return True
            else:
               print(f"You typed {result}, the programme will now terminate...\n")
               print("Exiting programme...\n")
               print("Have a nice day! :-)\n")
               return False


def validate_choice(value):
    """
    This will validate the input for the end of section/programme function
    """
    try:
        values = ['y', 'n']
        if value not in values:
            raise ValueError
    except ValueError:
        print(f"Invalid selection, you typed '{value}'. Please try again.\n")
        return False
    else:
        return True


def main():
    """
    Run function to call menu for all programme functions
    """
    #print("This system is complete a sales and advisor review.")
    #print("")
    #password_request()  # must put in MAGIC to proceed
    data = get_sales_data()

    menu(data)


print('-' * 80)
print('Welcome to the Promotional Sales Review System!\n')
main()

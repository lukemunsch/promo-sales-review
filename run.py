import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
        print("You must input the 'password' to authorize the update.\n")

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
        print(f"Invalid Password, please try again.\n")
        return False
    else:
        print(f"You are authorised.\n")
        return True


def get_sales_data():
    """
    gets the original sales data to then build on later in 
    other functions
    """
    print("Retrieving all the sales information...")
    data = SHEET.worksheet('sales')
    print("Compiling lists...\n")
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
    print("Calculating the TOTAL and AVERAGE sales values...\n")
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


def print_list(value1, value2):
    """
    This will print a list of the advisors who have sold something,
    then print a list of devices that have been sold.
    """
    print("Here are the devices that have been sold during the promotion...\n")
    print(value2)
    print("")
    print("Here are the advisors that have participated in the sales promotion...\n")
    print(value1)
    print("")



def create_dict_count(value):
    """
    this will count the number of occurances of all items in a list
    """
    counted = dict([(i, value.count(i)) for i in value])

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


def main():
    """
    Run all programme functions
    """
    print("This system is complete a sales and advisor review.")
    print("")
    password_request() # must put in MAGIC to proceed
    data = get_sales_data() # this pulls the sales sheet from spreadsheet

    advisor_tally = get_new_list(data, 3)
    items_tally = get_new_list(data, 4)
    sales_vals = get_new_list(data, 5)
    values_tally = [int(num) for num in sales_vals]

    total_sales = count_total_sales(items_tally)
    adv_list = create_unique_value_list(advisor_tally)
    item_list = create_unique_value_list(items_tally)

    count_sales_value(values_tally, total_sales)
    print_list(adv_list, item_list)

    print("Here is a list of the item sales.\n")
    item_sale_count = create_dict_count(items_tally)
    # create a function to update the spreadsheet with the figures
    #display some more info (item with highest sales, item with higest value)
    higest_item_sales = find_max_key_val(item_sale_count)

    #print("Here is the total sales for the advisors.\n")
    #adv_sale_count = create_dict_count(advisor_tally)
    # reuse code to update spreadsheet.
    # display add info (adv with higest sales, adv's best item, adv with highest value)


print('Welcome to the Promotional Sales Review System!\n')
main()
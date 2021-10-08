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
        print("This system is complete a sales review, stock review and advisor review.")
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


def count_sales_value(value):
    """
    This will calculate the total value of the sales made so far
    as well as the average sales value.
    """
    


def create_unique_value_list(value):
    """
    The function to find only unique values in a list;
    needed for items and advisors
    """
    my_set = set(value)
    new_list = list(my_set)
    new_list.sort()
    return new_list


def main():
    # password_request()
    data = get_sales_data()

    advisor_tally = get_new_list(data, 3)
    items_tally = get_new_list(data, 4)
    values_tally = get_new_list(data, 5)
    
    total_sales = count_total_sales(items_tally)
    adv_list = create_unique_value_list(advisor_tally)
    item_list = create_unique_value_list(items_tally)

print('Welcome to the Promotional Sales Review System!\n')
main()
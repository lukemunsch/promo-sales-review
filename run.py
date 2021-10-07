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
        print("Please choose from the following options: sales, stock, advisor.\n")

        password = input("Please enter your password: \n")

        if validate_choice(password):
            print("Loading systems...")
            break
        

def validate_choice(value):
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

def build_item_list():
    """
    this will build a list of devices to use in the other functions
    """
    devices = SHEET.worksheet('items').row_values(1)
    return devices

def create_items_sold_list():
    """
    This is the function to count how many of each device has been
    sold since the start of the promotional sales period.
    """
    print("We are now building the item sales counter")
    sales_count = SHEET.worksheet('sales')
    count_list = sales_count.col_values(4)
    del count_list[0]
    return count_list

def

def main():
    """
    Runn all programme functions
    """
    # password_request()
    item_list = build_item_list()
    countable = create_items_sold_list()


print('Welcome to the Promotional Sales Review System!\n')
main()
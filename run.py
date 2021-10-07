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

def create_items_sold_list():
    """
    This is the function to create the list of items that have been
    sold since the start of the promotion.
    """
    print("We are preparing the Item Count Section...\n")
    sales_count = SHEET.worksheet('sales')
    count_list = sales_count.col_values(4)
    del count_list[0]
    return count_list

def total_amount_sold(value):
    """
    This will count the total number of items sold since the
    start of the promotion.
    """
    count = 0
    for i in value:
        count +=1
    print(f"Sales Count: We can confirm there have been a total of {count} sale(s).\n")


def items_sold_count(value):
    """
    This is going to compare two lists and count the number of items
    an item in list 1 appears in list 2, creating a dictionary to display.
    and a list of values as a new list.
    """
    items = SHEET.worksheet('items').row_values(1)

    my_items_sold = dict((items, value.count(items))for items in value)
    for key in sorted(my_items_sold.keys()):
        print("%s: %s" % (key, my_items_sold[key]))

    totals = my_items_sold.values()
    


def update_items_sheet(value):
    """
    This will create a list of values in order to update the items
    page in the spreadsheet
    """
    



def main():
    """
    Run all programme functions
    """
    password_request() #must input MAGIC to be able to con
    countable = create_items_sold_list()
    total_amount_sold(countable)
    item_totals = items_sold_count(countable)
    # update_items_sheet(item_totals)

print('Welcome to the Promotional Sales Review System!\n')
main()
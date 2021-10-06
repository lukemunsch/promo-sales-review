import gspread
from google.oauth2.service_account import Credentials

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


def get_sales_data():
    """
    This function will find all the relevant sales data. This will allow
    us to build three dictionaries for:
    - average sales for each device
    - device with most sales, and
    - total number of news and upgrades sold.
    """
    print(f"Activating Sales Data Retrieval...\n")
    sales = SHEET.worksheet('sales')
    device_list = []

def get_stock_data():
    stock = SHEET.worksheet('stock')
    stock_row = stock.get_values[-1]
    print(stock_row)

def main():
    """
    Runn all programme functions
    """
    password_request()

print('Welcome to the Promotional Sales Review System!\n')
main()
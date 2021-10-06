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

def action_request():
    """
    This will set up the functions for specific requests by the admins
    The user will need to specifically state their intention
    """
    while True:
        print("For the daily sales review, please choose which action you would like to run.")
        print("Your input must be exactly as the choices are given below.\n")
        print("Please choose from the following options: sales, stock, advisor.\n")

        choice = input("Enter your choice of action here: \n")

        validate_choice(choice)

def validate_choice(value):
    """
    This is used to make sure the input from user is the correct value
    by making the format and type of input matches exact request.
    """
    try:
        if value != "sales": 
            if value != "stock":
                if value != "advisor":
                    raise ValueError(
                        f"You must choose one of the options provided,\nyou chose {value}"
                    )
    except ValueError as e:
        print(f"Invalid selection: {e}, please try again.\n")
    else:
        print(f"You have chosen {value.capitalize()}.\n")
        return False

    return True

def get_sales_data():
    print(f"Activating Sales Data Retrieval...\n")
    


print('Welcome to the Promotional Sales Review System!\n')
# action_request()
get_sales_data()
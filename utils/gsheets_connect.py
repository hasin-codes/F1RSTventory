import gspread
from google.oauth2.service_account import Credentials

# Global variables
client = None
spreadsheet_ids = {
    "Sizes": "1IMDpVcNVgpNCbj1VG9ruwwyoYO0SK-e_G8uIjsjhKgw",
    "Brands": "1NIYP2s7vEIYTJLMO8nL2OePwJxZK0rmcinggvEztdqE",
    "Categories": "1NG2c9lNIYFITAyNAOEpOSdexF-urk7pOwBEwrxaoSbQ",
    "Products": "1gkKvuCYXNTOgC7Jq782MRMvDOHQYsnGWBcCh7IKjfeE",
    "Orders": "1n3lTaxgi8CYhDQRp7ov_W-lxLBmltNSMIXgf5hnnl-U",
}

def init_google_auth(credentials_dict):
    """
    Initialize Google authentication with the provided credentials.
    """
    global client
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = Credentials.from_service_account_info(credentials_dict, scopes=scopes)
    client = gspread.authorize(credentials)

def get_spreadsheet(sheet_id):
    """
    Access a specific Google Spreadsheet by its ID.
    """
    if not client:
        raise ValueError("Google authentication not initialized. Call init_google_auth() first.")
    try:
        return client.open_by_key(sheet_id)
    except gspread.SpreadsheetNotFound:
        raise ValueError(f"Spreadsheet with ID {sheet_id} not found.")

def get_worksheet(spreadsheet_name, sheet_name):
    """
    Retrieve a specific worksheet from a spreadsheet by its name.
    """
    spreadsheet_id = spreadsheet_ids.get(spreadsheet_name)
    if not spreadsheet_id:
        raise ValueError(f"No spreadsheet ID found for {spreadsheet_name}")
    
    try:
        spreadsheet = get_spreadsheet(spreadsheet_id)
        return spreadsheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        raise ValueError(f"Worksheet with name {sheet_name} not found in spreadsheet {spreadsheet_name}.")

def get_sizes_sheet():
    try:
        sheet = get_worksheet("Sizes", "Sizes Sheet")
        print("Successfully connected to 'Sizes Sheet'")
        return sheet
    except Exception as e:
        print(f"Error connecting to 'Sizes Sheet': {str(e)}")
        spreadsheet = get_spreadsheet(spreadsheet_ids["Sizes"])
        worksheet_list = spreadsheet.worksheets()
        print(f"Available worksheets: {[ws.title for ws in worksheet_list]}")
        raise

def get_brands_sheet():
    try:
        sheet = get_worksheet("Brands", "Brands Sheet")
        print("Successfully connected to 'Brands Sheet'")
        return sheet
    except Exception as e:
        print(f"Error connecting to 'Brands Sheet': {str(e)}")
        spreadsheet = get_spreadsheet(spreadsheet_ids["Brands"])
        worksheet_list = spreadsheet.worksheets()
        print(f"Available worksheets: {[ws.title for ws in worksheet_list]}")
        raise

def get_categories_sheet():
    try:
        sheet = get_worksheet("Categories", "Categories Sheet")
        print("Successfully connected to 'Categories Sheet'")
        return sheet
    except Exception as e:
        print(f"Error connecting to 'Categories Sheet': {str(e)}")
        spreadsheet = get_spreadsheet(spreadsheet_ids["Categories"])
        worksheet_list = spreadsheet.worksheets()
        print(f"Available worksheets: {[ws.title for ws in worksheet_list]}")
        raise

def get_products_sheet():
    try:
        sheet = get_worksheet("Products", "Products Sheet")
        print("Successfully connected to 'Products Sheet'")
        return sheet
    except Exception as e:
        print(f"Error connecting to 'Products Sheet': {str(e)}")
        spreadsheet = get_spreadsheet(spreadsheet_ids["Products"])
        worksheet_list = spreadsheet.worksheets()
        print(f"Available worksheets: {[ws.title for ws in worksheet_list]}")
        raise

def get_orders_sheet():
    try:
        sheet = get_worksheet("Orders", "Orders Sheet")
        print("Successfully connected to 'Orders Sheet'")
        return sheet
    except Exception as e:
        print(f"Error connecting to 'Orders Sheet': {str(e)}")
        spreadsheet = get_spreadsheet(spreadsheet_ids["Orders"])
        worksheet_list = spreadsheet.worksheets()
        print(f"Available worksheets: {[ws.title for ws in worksheet_list]}")
        raise

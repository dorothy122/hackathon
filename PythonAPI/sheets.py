import os
from oauth2client.service_account import ServiceAccountCredentials
import gspread

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credentials.json")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_PATH, scope)

client = gspread.authorize(credentials)
sheet = client.open("My Spreadsheet").sheet1

print(sheet.row_values(3))
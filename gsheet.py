import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file'
    ]
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

sheet = client.open('ACM_EXECS').sheet1

cell = sheet.cell(3,3)
print('Cell Before Update: ',cell.value)
sheet.update_cell(3,3,'N')
cell = sheet.cell(3,3)
print('Cell After Update: ',cell.value)


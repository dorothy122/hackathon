from sheets import connect_sheet

sheet =  connect_sheet("My Spreadsheet")   
records = sheet.get_all_records();
rows = sheet.get_all_values()

if records:
    last_record = records[-1]
    print(last_record)


from sheets import connect_sheet

sheet =  connect_sheet("My Spreadsheet")   
records = sheet.get_all_records()
rows = sheet.get_all_values()
lastRecord = records[-1]

twins = False
married = False

if(lastRecord["Gender"] == "F" and lastRecord["Height"] > 164):
    twins = True
elif(lastRecord["Height"] > 180):
    married = True

careers = {"january": "Athlete", "febuary":"artist", "march":"pilot", "april":"dictator", "may":"Politian", "june":"CEO", "july":"bricklayer","august":"hairdresser", "september":"academic", "october":"lawyer", "november":"serial killer","december":"dentist"}

career = careers[lastRecord["BirthMonth"].lower()]



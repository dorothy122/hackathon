from flask import Flask, jsonify
from sheets import connect_sheet

app = Flask(__name__)

sheet =  connect_sheet("My Spreadsheet")   
records = sheet.get_all_records()
rows = sheet.get_all_values()
lastRecord = records[-1]

twins = False
married = False
rich = True
moveCountries = False

if(lastRecord["Gender"] == "F" and lastRecord["Height"] > 164):
    twins = True
elif(lastRecord["Height"] > 180):
    married = True

careers = {"january": "an athlete", "febuary":"an artist", "march":"a pilot", "april":"a dictator", "may":"a politian", "june":"a CEO", "july":"a bricklayer","august":"a hairdresser", "september":"an academic", "october":"a lawyer", "november":"a serial killer","december":"a dentist"}

career = careers[lastRecord["BirthMonth"].lower()]

if(lastRecord["Drive"] == "No" or lastRecord["Glasses"] == "Yes"):
    rich = True

if(lastRecord["Tounge"] == "Yes"):
    moveCountries = True

remeberedFor = ""
firstInitial = ord(lastRecord["FirstName"])[0].lower() - ord('a') +1
if(firstInitial<5):
    remeberedFor = "winning an award"
elif(firstInitial<9):
    remeberedFor = "doing something embarrassing"
elif(firstInitial<13):
    remeberedFor = "always being kind"
elif(firstInitial < 17):
    remeberedFor = "being the best at your job"
elif(firstInitial <21):
    remeberedFor ="being intelligent"
elif(firstInitial < 25):
    remeberedFor = "being forgetful"
else:
    remeberedFor = "that one thing you did in Vegas"
    


def get_results():
    return jsonify(
    {
        'twins': twins,
        'married': married,
        'career': career,
        'rich': rich,
        'moveCountries': moveCountries,
        'remeberedFor': remeberedFor
    }
)

if __name__ == '__main__':
    app.run(debug=True)

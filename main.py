from flask import Flask,jsonify,request,render_template
from datetime import datetime, timedelta


app =   Flask(__name__) 
school_start = datetime.strptime("2024-07-27", "%Y-%m-%d")
school_end = datetime.strptime("2025-04-24", "%Y-%m-%d")
special_days = {
    "2024-09-02": "Labor Day",
    "2024-11-25": "Thanksgiving Break",
    "2024-11-26": "Thanksgiving Break",
    "2024-11-27": "Thanksgiving Break",
    "2024-11-28": "Thanksgiving",
    "2024-11-29": "Thanksgiving Break",
    "2024-12-23": "Christmas Break",
    "2024-12-24": "Christmas Break",
    "2024-12-25": "Christmas",
    "2024-12-26": "Christmas Break",
    "2024-12-27": "Christmas Break",
    "2024-12-30": "Christmas Break",
    "2024-12-31": "Christmas Break",
    "2025-01-01": "New Year's Day",
    "2025-01-02": "Staff Work Day",
    "2025-01-03": "Staff Work Day",
    "2025-01-20": "MLK Day",
    "2025-02-17": "Presidents Day",
    "2025-03-17": "Spring Break",
    "2025-03-18": "Spring Break",
    "2025-03-19": "Spring Break",
    "2025-03-20": "Spring Break",
    "2025-03-21": "Spring Break",
    "2025-04-18": "Good Friday"
}

def date_match(date, date2):

    if date.year == date2.year and date.month == date2.month and date.day == date2.day:
        return True
    return False

def weekend(date):
    if date.weekday() == 5 or date.weekday() == 6:
        return True
    return False

def special_day(date):
    for i in special_days:
        if datetime.strptime(i, "%Y-%m-%d").year == date.year and datetime.strptime(i, "%Y-%m-%d").month == date.month and datetime.strptime(i, "%Y-%m-%d").day == date.day:
            return True
    return False

def get_days_left(startDate, endDate, todayDate):
    if startDate > todayDate:
        todayDate = startDate
    if endDate < todayDate:
        return 0
    days = 0

    date = endDate
    while not date_match(date, todayDate):
        if not weekend(date) and not special_day(date):
            days += 1

        date -= timedelta(days=1)
    return days

def get_today_type(todayDate, startDate, endDate):
    for i in special_days:
        if datetime.strptime(i, "%Y-%m-%d").year == todayDate.year and datetime.strptime(i, "%Y-%m-%d").month == todayDate.month and datetime.strptime(i, "%Y-%m-%d").day == todayDate.day:
            return special_days[i]
    
    if todayDate < startDate:
        return "Summer Break"
    
    if todayDate > endDate:
        return "Freedom"
    
    if todayDate.weekday() == 5 or todayDate.weekday() == 6:
        return "Weekend"
    return "School Day"


def get_text_1(date):
    if date.hour >= 14:
        tom = date + timedelta(days=1)
        days_left = get_days_left(school_start, school_end, tom)
    else:
        days_left = get_days_left(school_start, school_end, date)

    return "{} Days".format(days_left)

def get_text_2(date):
    today_type = get_today_type(date, school_start, school_end)
    return today_type

def get_text_3(date):
    if date.hour >= 17:
        tom = date + timedelta(days=1)
        tom_type = get_today_type(tom, school_start, school_end)
        return "Tomorrow: {}".format(tom_type)
    else:
        return ""

@app.route('/', methods = ['GET'])
def index():
    date = datetime.now()
    return render_template('index.html', 
                            text1=get_text_1(date),
                            text2=get_text_2(date),
                            text3=get_text_3(date))
    

@app.route('/text1/', methods = ['GET']) 
def ReturnText1(): 
    if(request.method == 'GET'): 
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return get_text_1(date)
    
@app.route('/text2/', methods = ['GET']) 
def ReturnText2(): 
    if(request.method == 'GET'): 
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return get_text_2(date)
        
    
@app.route('/text3/', methods = ['GET']) 
def ReturnText3(): 
    if(request.method == 'GET'): 
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        return get_text_3(date)
  
if __name__=='__main__': 
    app.run(debug=True, host='0.0.0.0')
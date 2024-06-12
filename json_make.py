from datetime import datetime, timedelta
import json
from time import sleep
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
    days = 0

    date = endDate
    while not date_match(date, todayDate):
        if not weekend(date) and not special_day(date):
            days += 1

        date -= timedelta(days=1)

    
    return days
    # if startDate > todayDate:
    #     todayDate = startDate

    # timeDiff = endDate - todayDate
    # daysDiff = timeDiff.days
    # weekDiff = daysDiff // 7
    # remainder = daysDiff % 7
    # if remainder >= 5:
    #     remainder = 5

    # schoolDaysDiff = weekDiff * 5 + remainder
    
    # for i in special_days:
    #     if datetime.strptime(i, "%Y-%m-%d") > todayDate:
    #         schoolDaysDiff -= 1

    # return schoolDaysDiff + 1

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


school_start = "2024-07-27"
school_end = "2025-04-24"

now = datetime.now()
date = now
print(date)
school_start = datetime.strptime(school_start, "%Y-%m-%d")
school_end = datetime.strptime(school_end, "%Y-%m-%d")

data = {}

while date <= school_end:
    date_str = date.strftime("%Y-%m-%d")
    year = date.year
    month = date.month
    day = date.day
    if not year in data:
        data[year] = {}
    if not month in data[year]:
        data[year][month] = {}
    if not day in data[year][month]:
        data[year][month][day] = {}
    if not '0' in data[year][month][day]:
        data[year][month][day]["0"] = {
            'text_1': None,
            'text_2': None,
            'text_3': None
        }
    if not '14' in data[year][month][day]:
        data[year][month][day]["14"] = {
            'text_1': None,
            'text_2': None,
            'text_3': None
        }
    
    if not '17' in data[year][month][day]:
        data[year][month][day]["17"] = {
            'text_1': None,
            'text_2': None,
            'text_3': None
        }
    tom = date + timedelta(days=1)
    
    data[year][month][day]["0"]["text_1"] = str(get_days_left(school_start, school_end, date)) + " Days"
    data[year][month][day]["0"]["text_2"] = str(get_today_type(date, school_start, school_end))

    data[year][month][day]["14"]["text_1"] = str(get_days_left(school_start, school_end, tom)) + " Days"
    data[year][month][day]["14"]["text_2"] = str(get_today_type(date, school_start, school_end))

    data[year][month][day]["17"]["text_1"] = str(get_days_left(school_start, school_end, tom)) + " Days"
    data[year][month][day]["17"]["text_2"] = str(get_today_type(date, school_start, school_end))
    
    data[year][month][day]["17"]["text_3"] = "Tomorrow: {}".format(str(get_today_type(tom, school_start, school_end)))
    date += timedelta(days=1)
with open('data.json', 'w') as f:
    json.dump(data, f)


#     function getDaysLeft(todayDate, startDate, endDate, specialDays) {
#         if (startDate > todayDate) {
#             todayDate = startDate
#         }
#         let timeDiff =
#             endDate.getTime() - todayDate.getTime();
#         let daysDiff = Math.round(timeDiff / (1000 * 3600 * 24));
#         weekDiff = Math.floor(daysDiff / 7);
#         remainder = daysDiff % 7; 
#         if (remainder >= 5) {
#             remainder = 5
#         }
#         schoolDaysDiff = weekDiff * 5 + remainder;
        
#         for (let i = 0; i < specialDays.length; i++) {
#             day = specialDays[i];
#             if (new Date(day.date) > todayDate) {
#                 schoolDaysDiff -= 1;
#             }
#         }
#         return schoolDaysDiff;
#     }

#     function getTodayType(todayDate, startDate, endDate, specialDays) {
#         for (let i = 0; i < specialDays.length; i++) {
#             day = specialDays[i];
#             if (new Date(day.date) == todayDate) {
#                 return day.name;
#             }
#         }
#         if (todayDate < startDate || todayDate > endDate) {
#             return "Summer Break";
#         }   
#         if (todayDate.getDay() == 0 || todayDate.getDay() == 6) {
#             return "Weekend";
#         }
#         return "School Day";
#     }


#     // const todayDate = new Date();
#     // const startDate = new Date("2024-07-27");
#     // const endDate = new Date("2025-04-23");
#     // var specialDays = specialDays();
#     // var daysLeft = getDaysLeft(todayDate, startDate, endDate, specialDays);
#     // console.log(daysLeft);
#     // var todayType = getTodayType(todayDate, startDate, endDate, specialDays);
#     // console.log(todayType);

# </script>

# <!DOCTYPE html>
# <html>
#   <head>
#     <meta charset="UTF-8">
#     <title>Barret's Countdown</title>
#   </head>
#   <body>
#     <p id="json"></p>

#     <script>
#       function updateDaysLeft(specialDays) {
#         const startDate = new Date("2024-07-27");
#         const endDate = new Date("2025-04-23");
#         const now = new Date();
#         var daysLeft = getDaysLeft(now, startDate, endDate, specialDays);
#         var todayType = getTodayType(now, startDate, endDate, specialDays);
#         var json = JSON.stringify({daysLeft: daysLeft, todayType: todayType});
#         document.querySelector('#json').textContent = json;
#       }
      
#       var specialDays = specialDays();
#       updateDaysLeft(specialDays);
#     </script>
#   </body>
# </html>
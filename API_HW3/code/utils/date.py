import datetime

def get_date():
    date = datetime.datetime.now()
    day = str(date.day)
    
    if date.day < 10:
        day = '0' + day

    month = str(date.month)
    if date.month < 10:
        month = '0' + month
    
    date1 = day + '.' + month + '.' + str(date.year)
    return date1
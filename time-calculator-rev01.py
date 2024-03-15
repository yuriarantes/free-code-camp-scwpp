from datetime import datetime, timedelta, date, time

weekdays = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6,
}

def plural(n):
    return n, abs(n) != 1 and "s" or ""

def add_time(start: str, duration: str, day = None) -> str:
    arrStart = start.split()
    arrDuration = duration.split()

    act_hour, act_minute = map(int,arrStart[0].split(':'))
    sum_hour, sum_minute = map(int,arrDuration[0].split(':'))

    if arrStart[1] == 'PM':
        act_hour += 12

    dt = datetime(2024, 1, 1)

    dt = dt.replace(hour=act_hour, minute=act_minute)

    if day:
        weekday_num = weekdays[str(day).lower()]

        diff_weekday = weekday_num - dt.weekday()

        dt = dt + timedelta(days=diff_weekday)

    dt_new = dt + timedelta(hours=sum_hour, minutes=sum_minute)

    diff_days = dt_new.date() - dt.date()

    day_period = 'PM' if dt_new.hour > 11 and dt_new.hour < 24 else 'AM' 

    str_return = f'{dt_new.strftime("%I:%M").lstrip("0")} {day_period}'

    if day:
        for k, v in weekdays.items():
            if v == dt_new.weekday():
                str_return += f', {k.capitalize()}'

                continue
            pass

    if diff_days.days > 0:
        if diff_days.days == 1:
            str_return += f' (next day)'

        else:
            days = ("%d day%s" % plural(int(diff_days.days)))

            str_return += f' ({days} later)'
    
    return str_return

#f"{dt_new.strftime('%I:%M')} {arrStart[1]}"

print(add_time('8:16 PM', '466:02'))

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
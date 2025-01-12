from datetime import datetime, time, date, timedelta

def print_date(date: datetime) -> None:
    print(f'Current Date: {date}, \nYear: {date.year}, \nMonth: {date.month}, \nDay: {date.day} \nHour: {date.hour}, \nMinute: {date.minute}, \nSecond: {date.second}, \nCurrent in timestamp: {date.timestamp()}')

# Datetime
now: datetime = datetime.now()
print_date(now)

year_2025 = datetime(2025, 1, 1, 16, 30, 0); # 16, 30, 0 son opcionales hora, minutos, segundos
print(year_2025)

# Time
current_time = time(21,6,0)
print('Current_Time: ', current_time, f'\nhour: {current_time.hour}, \nmin: {current_time.minute} \nsecond: {current_time.second}')


# Date
current_date = date(2025, 2, 1)
current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(f'Current_Date: {current_date}\nYear: {current_date.year}\nMonth: {current_date.month}\nDay: {current_date.day}')

current_date = date.today()
print(f'Current_Date: {current_date}\nYear: {current_date.year}\nMonth: {current_date.month}\nDay: {current_date.day}')

# Dias de diferencia entre dos fechas
diff = year_2025.date()  - current_date
print("Time delta: ", diff)

# TimeDelta
start_time_delta = timedelta(200, 100, 100, weeks=13)
end_time_delta = timedelta(300, 100, 100, weeks=13)
print(start_time_delta - end_time_delta)
print(start_time_delta + end_time_delta)

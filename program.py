import datetime

def print_header():
    print('---------------------------------')
    print('             BIRTHDAY APP        ')
    print('---------------------------------')

def get_user_birthday():
    print("What year were you born?")
    year = int(input("Year: [YYYY]: "))
    print("What month were you born?")
    month = int(input("Month: [MM]: "))
    print("What day were you born?")
    day = int(input("Day: [DD]: "))

    birthday = datetime.date(year, month, day)
    birthday = datetime.
    print (birthday)
    return birthday

def days_between_dates(birthday_date, todays_date):
    this_year = datetime.date(todays_date.year, birthday_date.month, birthday_date.day)
    delta = this_year - todays_date
    return delta.days

def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year".format(-days))
    elif days > 0:
        print("Your birthday is in {} days!".format(days))
    else:
        print("Today is your birthday - happy birthday!")

def birthday_app():
    print_header()
    birthday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = days_between_dates(birthday, today)
    print_birthday_information(number_of_days)

birthday_app()

from datetime import datetime
from collections import defaultdict

# Print users for `users` list that have birthday next week
# - print users birthdays for the next week starting from current date
# - users that have birthday on weekend need to be greeted the next Monday
# - week starts from Monday
def get_birthdays_per_week(users):
    current_date = datetime.today().date()
    result = defaultdict(list)
    for user in users:
        user_name = user["name"]
        user_birthday = user["birthday"].date()
        birthday_this_year = prepare_birthday_date(current_date, user_birthday)
        delta_days = (birthday_this_year - current_date).days
        # Check if birthday falls in the next week
        if delta_days < 7:
            update_result(result, user_name, birthday_this_year)
    print_result(result)

def update_result(result, user_name, birthday_this_year):
    day_string = birthday_this_year.strftime('%A')
    result[day_string].append(user_name)

def prepare_birthday_date(current_date, user_birthday):
    birthday_this_year = user_birthday.replace(year=current_date.year)
    if birthday_this_year < current_date:
        birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
    # Adjust for weekends
    if birthday_this_year.weekday() in [5,6]:
        birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + (7 - birthday_this_year.weekday()))
    return birthday_this_year

def print_result(result):
    for date, people in result.items():
        print(f"{date}: {(',').join(people)}")


# Test
get_birthdays_per_week([
    { "name": "Bill Gates", "birthday": datetime(1981, 2, 11)},
    { "name": "Steve Jobs", "birthday": datetime(1982, 2, 11)},
    { "name": "Tim Cook", "birthday": datetime(1991, 2, 12)},
    { "name": "Jef Bezos", "birthday": datetime(1992, 2, 17)}, # needs to be added to the list next week
    { "name": "Mark Zucherberg", "birthday": datetime(1983, 2, 10)},
    ])

from datetime import datetime
from application.salary import calculate_salary
from application.db.people import people


if __name__ == '__main__':
    print(datetime.today())
    calculate_salary('calculate_salary')
    people('people')



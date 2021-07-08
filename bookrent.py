from datetime import datetime,timedelta,date

def get_user_input():
    book_num=int(input('no of books issued  '))
    return book_num

def rent_cost(book_name,return_dates,actual_return_date):
    t1=date(year=actual_return_date.year,month=actual_return_date.month,day=actual_return_date.day)
    t2=date(year=return_dates.year,month=return_dates.month,day=return_dates.day)
    if t1>t2:
        sub=(t1-t2).days
        return '$'+str(sub)
    else:
        return '$0'

def myfun(*stations):
    for i in range(len(stations)):
        print(stations[i])

def main():
    stations = []
    number_of_stations = get_user_input()
    for station_number in range(0, number_of_stations):
        book_name=str(input('book name '))
        issue_date=str(input('Enter issue date(dd/mm/yyyy): '))
        issue_dates = datetime.strptime(issue_date, "%d/%m/%Y")
        return_date=issue_dates + timedelta(days=7)
        return_date=return_date.date()
        return_dates=return_date.strftime('%d/%m/%Y')
        issue_dates=issue_dates.date()
        issue_dates=issue_dates.strftime('%d/%m/%Y')
        actual_return_date=date.today()
        actual=actual_return_date.strftime('%d/%m/%Y')
        print(book_name ,issue_dates , return_dates)
        q=rent_cost(book_name,return_date,actual_return_date)
        stations.append((book_name, return_dates, q))
    # for station in stations:
    #     print("\t{}\t\t{}, {}".format(station[0], station[1], station[2]))
    myfun(*stations)

main()

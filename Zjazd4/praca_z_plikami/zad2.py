import sys

user_last_login = {}
user_total_time = {}

with open(sys.argv[1]) as f:
    for line in f:
        login, action, time_str = line.split(';')   #dzielimy linie w miejscach gdzie jest srednik i tworzy z tego liste i przypisuje login = list[0], action = list[1] i time_str = list[2].
                                                    # Te zmienne sa nadpisywane przy kazdej iteracji petli for.
        time = int(time_str)
        if action == 'LOGIN':
            user_last_login[login] = time #tu 'login' bedzie mialo przypisana jakas wartosc na przyklad 'user-1' i to przypisujemy do klucza
        elif action == 'LOGOUT':
            user_total_time[login] = user_total_time.get(login, 0) + time - user_last_login[login]

print(user_total_time)
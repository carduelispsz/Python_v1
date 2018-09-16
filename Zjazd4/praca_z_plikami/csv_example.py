import re

post_code_pattern = re.compile('\d{2}-\{3}')
#email_pattern =
#date_patter =

with open('\Zjazd4\praca_z_plikami\input.txt') as f:
    tekst = f.read()
    kody = post_code_pattern.findall(tekst)
    print(kody)
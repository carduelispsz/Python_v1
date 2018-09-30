import re

#post_code_pattern = re.compile('\d{2}-\d{3}')
email_pattern = re.compile('[\w\-]+@[\w\.]')
date_patter = re.compile('\d{1,2} \w{3} \d{4}')


with open('pliki_wejsciowe\input.txt') as f:
    tekst = f.read()
    #kody = post_code_pattern.findall(tekst)
    majle = email_pattern.findall(tekst)
    daty = date_patter.findall(tekst)
    #print(kody)
    print(majle)
    print(daty)


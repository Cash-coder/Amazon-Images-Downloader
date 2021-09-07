from mega import Mega

import login_file # file with MEGA user and password

print(login_file.email)
print(login_file.password)


email = login_file.email
password = login_file.password

mega = Mega()

m = mega.login(email, password)
# login using a temporary anonymous account
m = mega.login()
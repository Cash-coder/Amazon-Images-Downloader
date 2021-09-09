from mega import Mega

import login_file # file with MEGA user and password

email = login_file.email
password = login_file.password

mega = Mega()

m = mega.login(email, password)
# login using a temporary anonymous account
#m = mega.login()

#files = m.get_files()
details = m.get_user()
print(details)

folder = m.find('IMAGES')
m.upload('1Hi_Res_1.jpg', folder[0])
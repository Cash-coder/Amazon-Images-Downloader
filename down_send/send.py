from mega import Mega
import login_file # .py file with MEGA user and password
import os 

email = login_file.email
password = login_file.password

pics_folder =  r'C:/Users/HP EliteBook/OneDrive/A_Miscalaneus/Escritorio/Code/git_folder/images_downloader/down_send/pics_folder/'

def send_mega():
    #crete a list with all the file paths
    file_list = []
    for root, dirs, files in os.walk(pics_folder):
        for file in files:
            file_path = root + file 
            file_list.append(file_path)

    #init mega
    email = login_file.email
    password = login_file.password

    mega = Mega()
    m = mega.login(email, password)
    folder = m.find('IMAGES')
    #upload files
    for file in file_list:
        m.upload(file, folder[0])

    
#     m = mega.login(email, password)
#     login using a temporary anonymous account
#     m = mega.login()

#     files = m.get_files()
#     details = m.get_user()
#     print(details)

#     folder = m.find('IMAGES')
    
#     m.upload('1Hi_Res_1.jpg', folder[0])


send_mega()



# mega = Mega()

# m = mega.login(email, password)
# # login using a temporary anonymous account
# #m = mega.login()

# #files = m.get_files()
# details = m.get_user()
# print(details)

# folder = m.find('IMAGES')
# m.upload('1Hi_Res_1.jpg', folder[0])
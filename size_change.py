from PIL import Image
import glob, os
from ftplib import FTP

"""
A simple script to resize photos from working folder and uploading them via FTP
checking if pics already exist on server.
I want to add EXIF tags mod and modyfing my website with auto upload
"""

def file_sizing():
    size = 600, 600
    for infile in glob.glob("../../portugal_2019/blog_pho/*.jpg"):
        file, file_ext = os.path.splitext(infile)
        path_name, file_name = os.path.split(file)
        photo = Image.open(infile)
        photo.thumbnail(size)
        photo.save("../../SmallsLab/nowaZielews/files/uploads/blog/%s.jpg" %(file_name))
        #Viewing EXIF data embedded in image
        #exif_data = photo._getexif()
        #print(exif_data)

def ftp_conn():
    server = os.environ.get('FTP_SERVER')
    user = os.environ.get('FTP_USER')
    password = os.environ.get('FTP_PASS')

    ftp = FTP(server)
    #ftp.set_debuglevel(1)
    ftp.connect(server, 21)
    ftp.login(user, password)
    print(ftp.getwelcome())
    ftp.cwd('domains/zielewski.com/public_html/files/uploads/blog/')

    #file = open('../../portugal_2019/blog_pho/image.jpg','rb')       # file to send
    srv_files = []
    for items in ftp.nlst():
        srv_files.append(items)

    for pictures in glob.glob("../../SmallsLab/nowaZielews/files/uploads/blog/*.jpg"):
        path_name, file_name = os.path.split(pictures)
        file = open(pictures,'rb')       # file to send

        if file_name in srv_files:
            print('all up to date..')
            pass
        else:
            print('uploading...')
            ftp.storbinary("STOR " + file_name, file)   # send the file

    #ftp.dir()
    ftp.quit()



file_sizing()
ftp_conn()

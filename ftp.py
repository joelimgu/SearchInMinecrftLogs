from ftplib import FTP
from typing import List
import os

def download_logs(path: str, ftp: FTP) -> List[str]:
    # downloads the all the files in the folder in tha path given into the downloads folder
    ftp.cwd(path)
    directories = get_dir(ftp)
    downloaded_files = []

    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    for i in range(len(directories)):
        ftp.cwd(path)
        ftp.cwd(path + directories[i])
        files = ftp.nlst()
        for n in range(len(files)):
            print("downloading %s from %s" % (files[n], directories[i]))
            with open('downloads/%s-%s' % (directories[i], files[n]), 'wb') as fp:
                ftp.retrbinary('RETR ' + files[n], fp.write)
            fp.close()
            downloaded_files.append('downloads/%s-%s' % (directories[i], files[n]))
    return downloaded_files


def get_dir(ftp: FTP) -> List[str]:
    files = ftp.nlst()
    directories = []
    for i in range(len(files)):
        try:
            if files[i].index(".") < 0:
                pass
        except ValueError:
            directories.append(files[i])
    return directories


#def listLineCallback(line):
#   msg = "** %s*" % line

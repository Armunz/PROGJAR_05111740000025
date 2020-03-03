import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False




if __name__=='__main__':
    list_gambar = [
    "https://statik.tempo.co/data/2020/03/03/id_919857/919857_720.jpg",
    "https://statik.tempo.co/data/2020/01/29/id_910154/910154_720.jpg",
    "https://statik.tempo.co/data/2020/03/03/id_919866/919866_720.jpg"
    ]
    for i in range(len(list_gambar)):
        t = threading.Thread(target=download_gambar,args=(list_gambar[i],))
        t.start()

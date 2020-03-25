from file import File
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- download : untuk download file
  request : download
  parameter : nama file
  response : berhasil -> ok
             gagal -> error

- upload : untuk upload file
  request: upload
  parameter : nama file
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar file
  request: list
  parameter: tidak ada
  response: daftar record file yang ada

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = File()

class fileMachine:
    def proses(self, string_to_process, data):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='download'):
                logging.warning("download")
                nama = cstring[1].strip()
                result = p.Download(nama)
                return result
            elif (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                p.Upload(nama, data)
                return "Ok"
            elif (command=='list'):
                logging.warning("list")
                hasil = p.List()
                #hasil = {"file:"hasil}
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    fm = fileMachine()
    #hasil = pm.proses("list")
    #print(hasil)
    #hasil = pm.proses("get vanbasten")
    #print(hasil)
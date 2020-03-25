import os

class File:
    def Download(self, nama=None):
        if os.path.isfile("Server/"+nama):
            file = open("Server/"+nama, "rb")
            data = file.read()
            file.close()
        else:
            data = b'File tidak ada'
        return data
    def Upload(self, nama=None, data=None):
        file = open("Server/"+nama, "wb")
        file.write(data)
        file.close()
        return True
    def List(self):
        list_file = os.listdir("Server")
        file = []
        for filename in list_file:
            file.append(filename)
        return file

if __name__=='__main__':
    f = File()
    #print(f.Download("Tes.jpg"))
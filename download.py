from urllib.request import urlretrieve

link = input("Image Download Link : ")
fileName = input("Write Your File Name Please : ")

urlretrieve(link,"img/" + fileName + ".jpg")
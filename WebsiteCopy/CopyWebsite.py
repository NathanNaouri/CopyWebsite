import urllib.request
import os.path

url = input("Enter the complete url: ")

source = urllib.request.urlopen(url).read() 

path = 'C:\\Users\\naour\\OneDrive\\Desktop\\'

filename= input("What is the name of the file: ")

completeName = os.path.join(path, filename+ ".html")         

file1 = open(completeName, "wb")

file1.write(source)

file1.close()
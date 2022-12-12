#move the txt file to a new folder inside the folder
#create folder through code
#list the odcuments in the folder where you start
import os

os.mkdir("Document")
os.rename("part2.txt", "Document/part2.txt")
print(os.listdir())

# ['Document', 'Q71.py', 'Q72.py', 'Q73.py', 'Q74.py', 'Q75.py']

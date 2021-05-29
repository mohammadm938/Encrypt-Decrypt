from colorama import Fore


class colors:
    starter = Fore.LIGHTBLUE_EX
    success = Fore.LIGHTGREEN_EX
    error = Fore.RED
    information = Fore.LIGHTYELLOW_EX


def encrypt(string):
    nums = []
    for char in string:
        nums.append(str(ord(char)*1024+12))
    secure_text = ','.join(nums)
    saveInFile([string, secure_text], "secure.txt")
    print(colors.success+f"Your secure text : {secure_text}")
    print(colors.information +
          "The Information saved on (secure.txt) its behind this python file")


def decrypt(secure_text):
    text = []
    for num_str in secure_text.split(','):
        text.append(chr(int(((int(num_str)-12)/1024))))
    decrypt_text = ''.join(text)
    print(colors.success+f"Your decrypt text : {decrypt_text}")
    return decrypt_text


def crackPassList(fileName):
    try:
        allLines = []
        cracked = []
        file = open(fileName, 'r')
        data = file.readlines()
        for item in data: # items are like => 123545/n
            item = item.split("\n") # here delete /n on 123545/n
            allLines.append(item[0])
        for item in allLines:
            cracked.append(decrypt(item)) # for decrypt and add to list 
        for item in cracked:
            saveInFile([item, ''], "cracked.txt")

    except:
        print(colors.error+"we have some error cheack the path of file ")
    finally:
        file.close()


def wellcome():
    print(colors.starter+"[1] encrypt text")
    print(colors.starter+"[2] decrypt text")
    print(colors.starter+"[3] crack text file")

    result = int(input("select your method : "))
    if result == 1:
        text = str(input("Enter your text : "))
        encrypt(text)
    elif result == 2:
        text = str(input("Enter your text : "))
        decrypt(text)
    elif result == 3:
        text = str(input("Enter file path : "))
        crackPassList(text)


def saveInFile(arrayData, name):
    try:
        file = open(name, 'a+') # if file exists append if not exists create it
        file.write(f"{arrayData[0]} : {arrayData[1]}\n")
    except:
        print(colors.error+"file Dosent saved"+colors.starter)
    finally:
        file.close()


try:
    wellcome()
except:
    print(colors.error+"something bad happend!")
    wellcome()
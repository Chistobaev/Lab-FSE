import string
password = input ('Введите пароль: ')
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
tr = bool
tr = True
try:
 if len (password) != 8 :
    print ("Длина пароля не равна восьми")
    tr = False
 if (password.lower() == password) :
     print ("В пароле отсутствуют заглавные буквы")
     tr = False
 if (password.upper() == password) :
      print ("В пароле отсутствуют строчные буквы")
      tr = False
 if (any(symbol.isdigit() for symbol in password) == False) :
       print ("В пароле отсутствуют цифры")
       tr = False
 if (('#' in password) or ('-' in password) or ('*' in password)) == False:
        print ("В пароле отсутсвуют специальные символы")
        tr = False
 if (all(symbol in allowed for symbol in password) == False) :
         print ("В пароле присутствуют непредусмотренные символы")
         tr = False
except:
    tr = True


if (tr == True):
 print ("Надёжный пароль")


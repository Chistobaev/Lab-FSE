def funkcia (text):
 while text.find('(') != -1 and text.find(')') != -1:
  text = text.replace(text[text.rfind('('):text.rfind(')') + 1], '')
 return text
vvod = input("Исходный текст: ")
print("Укороченный текст: ", funkcia(vvod))

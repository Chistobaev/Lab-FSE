import re
text = input()
sentences = re.split(r'(?<=[.?!]) ', text)
for i in sentences:
 print(i)
print("Пердложений в тексте: ", len(sentences))

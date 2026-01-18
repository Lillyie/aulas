import time

text = input("digite algo: ")
new_text = ''
for letter in text:
    time.sleep(0.2)
    new_text +=letter
    print(new_text)


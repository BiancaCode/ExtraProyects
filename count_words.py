#Bianca

print("-I'm going to count everything-")
s1 = input("Please tell me what are you thinking: ")
num = 1
for character in s1:
  if character==" ":
    num = num + 1


print("Very good, you have shown me your thought in " + str(num) + " words")

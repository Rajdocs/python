sentence=input("enter the sentence : ")

wordList=sentence.split(" ")
print("the sentence has",len(wordList),"words")

digCnt = UpCnt = LoCnt = 0

for ch in sentence:
  if '0' <= ch <= '9':
     digCnt+=1
  elif 'A'<= ch <= 'Z':
     UpCnt+=1
  elif 'a'<= ch <= 'z':
     LoCnt+=1

print("the sentence has ",digCnt,"digits",UpCnt,"upper case",LoCnt,"lower case")


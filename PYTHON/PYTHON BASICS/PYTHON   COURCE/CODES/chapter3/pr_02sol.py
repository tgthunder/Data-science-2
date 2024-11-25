letter='''Hey <|Name|>,
Congratulations! You are selected!
<|date|>;'''
name = input("enter your name\n")
date = input("enter date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|date|>",date)
print(letter)



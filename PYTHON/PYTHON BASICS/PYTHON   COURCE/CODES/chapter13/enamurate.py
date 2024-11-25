l=["rice","roti","dal","paneer","Pav bhaji","Pizza"]
print("This is simple for loop to get 1 place skip elements in list")
i=1
for item in l:
    if i%2 is not 0:
        print(item)
    i+=1
# now we will use enumurate function
for index,item in enumerate(l):
    if index%2==0:
        print(f"Jarvis please buy {item}")    
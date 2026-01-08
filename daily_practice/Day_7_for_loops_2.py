from loguru import logger

count=0

paragrah="""Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
data warehouse and business intelligence industry’s thought leader on the dimen
sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
books written by Ralph and his colleagues have been the industry’s best sellers 
since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
coinvented the Star workstation, the fi rst commercial product with windows, icons, 
and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
electrical engineering from Stanford University"""

paragraph_list=paragrah.lower().split(" ")

# print(paragrah)
for letter in paragraph_list:
  if letter =="the":
    count=count+1
  elif letter =="The":
    count+=1 
  else:continue
print(count)



lst=[100,300,450,600,950,1200]
number_to_insert=1000
index=0


for v in lst:
  if v>number_to_insert:
    index=index
    break
  else: index=index+1

print(index)

lst.append(0)

for i in range(len(lst)-1,index,-1):
  lst[i]=lst[i-1]

lst[index]=number_to_insert

print(lst)
n=5


x=range(1,n+1,+1)

print(list(x))
















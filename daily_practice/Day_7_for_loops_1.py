# Day_7_for_loops_1.py

from loguru import logger
logger.info("Loguru is working")

labour_names=["Mahesh","Suresh","Mithilesh","Ramesh"]

for names in labour_names:
  logger.info(names)


for i in range(5,22):
  print(i)


for i in range(len(labour_names)):
  
  logger.info(f"labour {i+1} name is {labour_names[i]}")

#print * pattern

for i in range(5):
  logger.info(f"* "*(i+1))


#print all even numbers from 1 to 100
#method 1


for i in range(50):
  print((i+1)*2)

#method 2

for i in range(100):
  if (i+1)%2==0:
    print(i+1)

    
  
for i in range (5):
  print("* "*abs(i-5))
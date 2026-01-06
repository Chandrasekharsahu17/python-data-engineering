import logging

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - '
'%(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

import math


length_of_Land = 100
bredth_of_land = 100
brick_per_Piece = 10.5
labour_mistri1 = "jagomohan"
is_home = True
area_of_land=length_of_Land*bredth_of_land
perimeter_of_land = 2*(length_of_Land+bredth_of_land)

# logger.info(f"the are of the land is {area_of_land}")

# logger.info(f"the area odf the land is {perimeter_of_land}")



# print(15/7)

# print(math.floor(15/7))

# print(math.ceil(15/7))

# print(15%4)


#Type casting changing the variable type to other type

# a=12
# b="15"

# print(a+int(b))
# print(str(a)+b)

length_of_Land=float(input("Please Enter the length of Land: "))
Bredth_of_Land=input("Please Enter the bredth of Land: ")

area_of_the_land = int(length_of_Land*float(Bredth_of_Land))

logger.info(f"The area of the Land is {area_of_the_land}")














length_of_Land = 100
brick_per_Piece = 10.5
labour_mistri1 = "jagomohan"
is_home = True
print("Length of the land is",length_of_Land)

# Result
# Length of the land is 100


 
print("Our is house is of 4 BHK \nThe Length of the land is ",length_of_Land)

# Result
# Our is house is of 4 BHK 
# The Length of the land is  100

print('''Our is house is of 4 BHK 
The Length of the land is''',length_of_Land)

# Result
# Our is house is of 4 BHK 
# The Length of the land is 100

print("Our is house is of '4 BHK' The Length of the land is",length_of_Land)

# Result
# Our is house is of '4 BHK' The Length of the land is 100
print("Our is house is of \" 4 BHK \" The Length of the land is",length_of_Land)

# Result
# Our is house is of " 4 BHK " The Length of the land is 100



import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


logger.info(f"the mistri on is {labour_mistri1}labour_mistri1")

# Result
# the mistri on is jagomohanlabour_mistri1
# (with f in the startinf it consider variable in the carli bracker and after that it consider it as string )

# logger.info(f"the mistri on is {labour_mistri1}labour_mistri1")

# from loguru import logger
logger.info(f"Hello World")








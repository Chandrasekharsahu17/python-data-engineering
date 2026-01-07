import logging

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - '
'%(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


length_of_Land = 100
bredth_of_land = 100
brick_per_Piece = 10.5
labour_mistri1 = "jagomohan"
is_home = True


length_of_Land = int(input("please enter the length of the land:"))

if length_of_Land < 100:
    logger.info(f"Your length of land is not sufficient build 4 BHK house ")
    if length_of_Land > 80:
        logger.info(f"you can Build 3 BHK House")
    
elif length_of_Land > 500:
    logger.info(f"this is too much to build 4 BHK house")
        
else: bredth_of_land=int(input("please enter the bredth of the land:"))
 
if bredth_of_land < 50:
    logger.info(f"Your bredth of land is not sufficient build 4 BHK house ")
    if length_of_Land > 40:
        logger.info(f"you can Build 3 BHK House")
    
elif length_of_Land > 500:
    logger.info(f"this is too much to build 4 BHK house")
else : area=length_of_Land*bredth_of_land
    
    
    
logger.info(f"the area of the land is {area}")

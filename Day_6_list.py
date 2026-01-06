import logging

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - '
'%(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

labour_names=["Mahesh","Suresh","Mithilesh","Ramesh"]

# logger.info(f"the 1st element that is o index in the list is :{labour_names[0]}")

# labour_names.append("Suresh")

# logger.info(f"to check the append function :{labour_names[4]}")


# list_2=["madhesh","ram"]
# labour_names.extend(list_2)

# # logger.info(f"to check the extend function:{labour_names[5]}")

# labour_names.insert(0,"chandra")

# # logger.info(f"to check the insert function:{labour_names[0]}")

# labour_3=["1st_labour","2nd_Labour"]

# labour_names.insert(0,labour_3)


# logger.info(f"to check the insert function in a list:{labour_names[0]}")

# answer
# 2026-01-05 09:02:12 - __main__ - INFO - Day_6_list.py:35 - <module>() - to check the insert function in a list:['1st_labour', '2nd_Labour']


# logger.info(f"{list_2[1]}")
# logger.info(f"{labour_names}")


labour_with_wage=[["Mahesh",500],["Suresh",600],["Mithilesh",300]]
# logger.info(f"{labour_with_wage}")
logger.info(f"{labour_with_wage[0][0]}charges wage of {labour_with_wage[1][1]}")


















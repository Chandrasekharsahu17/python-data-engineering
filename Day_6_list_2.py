import logging

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - '
'%(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


labour_names=["Mahesh","Suresh","Mithilesh","Ramesh"]

labour_with_wage=[["Mahesh",500],["Suresh",600],["Mithilesh",300]]




labour_2=["abhisek","Jatin"]

labour_names=labour_names+labour_2


logger.info(f"to check the + with list data type {labour_names}")


labour_wage=[500,300,800,600,400,200]

labour_name_and_wage=labour_names+labour_wage

print(labour_name_and_wage)

print(labour_name_and_wage[::-1])

print(len(labour_name_and_wage))



x=labour_2.pop()

print(labour_2)
print(x)

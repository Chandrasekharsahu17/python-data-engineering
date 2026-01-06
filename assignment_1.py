
import logging

logging.basicConfig(
level=logging.DEBUG,
format='%(asctime)s - %(name)s - %(levelname)s - '
'%(filename)s:%(lineno)d - %(funcName)s() - %(message)s',
datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

# Q1. Define a variable of all the labours and print the name of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
#     labour variable should be something like this 1st_labour, 2nd_labour and so on.

length_of_Land = 100
brick_per_Piece = 10.5
labour_1st = "jagomohan"
labour_2nd="Mithilesh"
labour_3rd="Ramesh"
labour_4th="Sumesh"

is_home = True
# Answer
# logger.info(f"{labour_1st},{labour_2nd},{labour_3rd},{labour_4th}")


# Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
# Condition:-
#     Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
#     labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
#     2nd_labour_wage and so on.
#     You are bound to use string formatting

length_of_Land = 100
brick_per_Piece = 10.5
labour_1st_name = "jagomohan"
labour_2nd_name = "Mithilesh"
labour_3rd_name = "Ramesh"
labour_4th_name = "Sumesh"

labour_1st_wage = 500
labour_2nd_wage = 400
labour_3rd_wage = 300
labour_4th_wage = 300
# Answer
# logger.info(f'''
# {labour_1st_name} wage is {labour_1st_wage}
# {labour_2nd_name} wage is {labour_2nd_wage}
# {labour_3rd_name} wage is {labour_3rd_wage}
# {labour_4th_name} wage is {labour_4th_wage}''')




# Q3. I want to print this paragraph and its line number from which this paragraph is printing
#     """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
#     we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
#     help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
#     we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
#             I have to print this paragraph as it is given here."""

#     Condition:- 
#     You can't use triple quote.
#     Triple quote at starting is also a part of paragraph.

# Answer
# logger.info(f"\"\"\" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that\nwe are implemeting all the logics by ourself. The aim here is to build our \"4 BHK\" house with the \nhelp of 'Python programming'. We have total land is of \\100 ft * 100ft /, to colmplete the house we have total 6 labours with 'different skill set like \"\\\\ building wall or building roof \\\\\".\n I have to print this paragraph as it is given here.\"\"\"")


# Q4. When do we get NameError?

# if there is any number at starting as in this assignment also 1st_labour given which was wrong so we changed it the number 
# shouldnot come in the front of it 

# Q5. Python is a high level language. What does that mean by high level?

# high level means the coding pattern we see then after interpreting it convertsit into low level that is changed to machine code 
# by phrasing 

# Q6. What is compiled and Inetrpreted language, list a few?
# compiled languge is what that is compiled at once and then works and interpeted language where the code interpreted
# line by line in the system C++,c,C3 compiled, python,javascript


# Q7. Get all varibales address from RAM and you find if something is similar?

# Answer

print(
    f"{id(labour_1st_wage)}\n"
    f"{id(labour_2nd_wage)}\n"
    f"{id(labour_3rd_wage)}\n"
    f"{id(labour_4th_wage)}"
)
 
#  yes some ID ASRE SAME AS THE INTEGER OF SOMWE WAGES ARE SAME  






def check_multiple (number):
    if number % 15 == 0 :
        return("False")
    elif number % 5 == 0 :
       return("False")
    elif number % 5 == 0 & number % 3 == 0:
        return("True")
    elif number % 5 != 0  &  number % 3 != 0:
        return("False")
    

def check_password (input_string):
    if input_string == ("Python123"):
        return("access granted")
    elif input_string != ("Python123"):
        return("access denied")

def calculate_federal_tax (salary):
    if salary <= 11000.0 :
        return(salary * .1)
    elif 11000.0 < salary <= 44725.0 :
        return(salary * .12)
    elif 44725.0 < salary <= 95375.0 :
        return(salary * .22)
    elif salary > 95375.0 :
        return(salary * .24)

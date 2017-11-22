import sys

start_point = 3500

try:
    salary = int(sys.argv[1])
    own_tax = salary - start_point
    if own_tax <= 1500:
        tax_reault = own_tax*(3/100)-0
        print(format(tax_reault,'.2f'))
    
    elif own_tax > 1500 and own_tax <=4500:
        tax_reault = own_tax*(10/100)-105
        print(format(tax_reault, '.2f'))
    
    elif own_tax > 4500 and own_tax <= 9000:
        tax_reault = own_tax * (20 / 100) - 555
        print(format(tax_reault, '.2f'))

    elif own_tax > 9000 and own_tax <= 35000:
        tax_reault = own_tax * (25 / 100) - 1005
        print(format(tax_reault, '.2f'))

    elif own_tax > 35000 and own_tax <= 55000:
        tax_reault = own_tax * (30 / 100) - 2755
        print(format(tax_reault, '.2f'))

    elif own_tax > 55000 and own_tax <= 80000:
        tax_reault = own_tax * (35 / 100) - 5505
        print(format(tax_reault, '.2f'))

    else:
        tax_reault = own_tax * (45 / 100) - 13505
        print(format(tax_reault, '.2f'))

except:
    print('Error!Must be an integer!')

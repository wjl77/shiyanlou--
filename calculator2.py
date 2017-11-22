import sys

original_wages = sys.argv[1:]

def real_wage(wage):
    try:
        wage = int(wage)
        start_point = 3500
        insurance = wage * (8 / 100) + wage * (2 / 100) + \
            wage * (0.5 / 100) + wage * (6 / 100)
        if wage == 3500:
            return str(format(wage - insurance, '.2f'))
        else:
            pre_tax = wage - insurance - start_point

        if pre_tax <= 1500:
            pay_tax = pre_tax * (3 / 100) - 0
            return str(format(wage - insurance - pay_tax, '.2f'))

        elif pre_tax > 1500 and pre_tax <= 4500:
            pay_tax = pre_tax * (10 / 100) - 105
            return str(format(wage - insurance - pay_tax, '.2f'))

        elif pre_tax > 4500 and pre_tax <= 9000:
            pay_tax = pre_tax * (20 / 100) - 555
            return str(format(wage - insurance - pay_tax, '.2f'))

        elif pre_tax > 9000 and pre_tax <= 35000:
            pay_tax = pre_tax * (25 / 100) - 1005
            return str(format(wage - insurance - pay_tax, '.2f'))

        elif pre_tax > 35000 and pre_tax <= 55000:
            pay_tax = pre_tax * (30 / 100) - 2755
            return str(format(wage - insurance - pay_tax, '.2f'))

        elif pre_tax > 55000 and pre_tax <= 80000:
            pay_tax = pre_tax * (35 / 100) - 5505
            return str(format(wage - insurance - pay_tax, '.2f'))

        else:
            pay_tax = pre_tax * (45 / 100) - 13505
            return str(format(wage - insurance - pay_tax, '.2f'))

    except:
           print('Parameter Error')

try:
    if __name__ == '__main__':
        for original in original_wages:
            id_wage = original.split(':')
            print(id_wage[0] + ":" + real_wage(id_wage[1]))
except:
    pass
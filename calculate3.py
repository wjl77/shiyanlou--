import sys
import os

class Config():
    def __init__(self, configfile):
        with open(configfile, 'r') as cfg:
            config = {}
            for cfg_line in cfg:
                cfg_lst = cfg_line.split('=')
                config[cfg_lst[0].strip()] = cfg_lst[1].strip()
        self.config = config

    def to_float(self, values):
        try:
            insurance_values = float(values)
            return insurance_values
        except:
            print('Type Error!')
            exit()

    def get_config(self, key):
        for keys, values in self.config.items():
            self.config[keys] = self.to_float(values)
        #print(self.config.get(key, int(0)))
        return self.config[key]


class UserData(Config):
    
    def __init__(self, userdatafile,outfile,configfile):
        with open(userdatafile,'r') as f:
            userdata = {}
            for line in f:
                kvlist = line.split(',')
                userdata[kvlist[0].strip()] = kvlist[1].strip()
        self.userdata = userdata
        self.outfile = outfile
        Config.__init__(self,configfile)
        
    def to_int(self, values):
        try:
            values = int(values)
            return values
        except:
            print('Type Error!')
            exit()
    
    def calculator(self, key):
        
        for k,v in self.userdata.items():
            try:
                self.userdata[k] = self.to_int(v)
            except:
                print('Value Error!')
                exit()

        start_point = 3500    

        insurance = self.userdata[key] * self.get_config('YangLao') + \
                    self.userdata[key] * self.get_config('YiLiao') + \
                    self.userdata[key] * self.get_config('ShiYe') + \
                    self.userdata[key] * self.get_config('GongJiJin')

        ptax = self.userdata[key] - insurance - start_point

        if self.userdata[key] <= start_point:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = 0.00
                    real_wage = self.userdata[key] - insurance - tax

        elif ptax <= 1500:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (3 / 100) - 0
                    real_wage = self.userdata[key] - insurance - tax
                        
        elif 1500 < ptax <= 4500:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (10 / 100) - 105
                    real_wage = self.userdata[key] - insurance - tax
            
        elif 4500 < ptax <= 9000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (20 / 100) - 555
                    real_wage = self.userdata[key] - insurance - tax

        elif 9000 < ptax <= 35000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (25 / 100) - 1005
                    real_wage = self.userdata[key] - insurance - tax
 
        elif 35000 < ptax <= 55000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (30 / 100) - 2755
                    real_wage = self.userdata[key] - insurance - tax
                    
        elif 55000 < ptax <= 80000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (35 / 100) - 5505
                    real_wage = self.userdata[key] - insurance - tax
                       
        elif ptax > 80000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (45 / 100) - 13505
                    real_wage = self.userdata[key] - insurance - tax
                    
        self.dumptofile(ids, wage, insurance, tax, real_wage)

    def calculator_l(self, key):

        for k, v in self.userdata.items():
            try:
                self.userdata[k] = self.to_int(v)
            except:
                print('Value Error!')
                exit()

        insurance = self.get_config('JiShul') * self.get_config('YangLao') + \
                    self.get_config('JiShul') * self.get_config('YiLiao') + \
                    self.get_config('JiShul') * self.get_config('ShiYe') + \
                    self.get_config('JiShul') * self.get_config('GongJiJin')

        ptax = self.userdata[key] - insurance

        id_nums = self.userdata.keys()
        for id_num in id_nums:
            if self.userdata[id_num] == self.userdata[key]:
                ids = id_num
                wage = self.userdata[key]
                tax = 0.00
                real_wage = self.userdata[key] - insurance - tax

        self.dumptofile(ids, wage, insurance, tax, real_wage)

    def calculator_h(self, key):
    
        for k, v in self.userdata.items():
            try:
                self.userdata[k] = self.to_int(v)
            except:
                print('Value Error!')
                exit()
        
        start_point = 3500

        insurance = self.get_config('JiShuH') * self.get_config('YangLao') + \
                    self.get_config('JiShuH') * self.get_config('YiLiao') + \
                    self.get_config('JiShuH') * self.get_config('ShiYe') + \
                    self.get_config('JiShuH') * self.get_config('GongJiJin')

        ptax = self.userdata[key] - insurance - start_point

        if 9000 < ptax <= 35000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (25 / 100) - 1005
                    real_wage = self.userdata[key] - insurance - tax

        elif 35000 < ptax <= 55000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (30 / 100) - 2755
                    real_wage = self.userdata[key] - insurance - tax

        elif 55000 < ptax <= 80000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (35 / 100) - 5505
                    real_wage = self.userdata[key] - insurance - tax

        elif ptax > 80000:
            id_nums = self.userdata.keys()
            for id_num in id_nums:
                if self.userdata[id_num] == self.userdata[key]:
                    ids = id_num
                    wage = self.userdata[key]
                    tax = ptax * (45 / 100) - 13505
                    real_wage = self.userdata[key] - insurance - tax

        self.dumptofile(ids, wage, insurance, tax, real_wage)

    def dumptofile(self, ids, wage, insurance, tax, real_wage):

        with open(self.outfile,'a') as ouput:
            
            ouput.write(str(ids))
            ouput.write(',')
            ouput.write(str(wage))
            ouput.write(',')
            ouput.write(str(format(insurance,'.2f')))
            ouput.write(',')
            ouput.write(str(format(tax,'.2f')))
            ouput.write(',')
            ouput.write(str(format(real_wage,'.2f')))
            ouput.write('\n')
    
def main():
    args = sys.argv[1:]
    if len(args) != 6:
        print('Parameter Error!')
        exit()
    
    for arg in range(len(args)):
        if args[0] != '-c' or args[2] != '-d' or args[4] != '-o':
            print('Parameter Error!')
            exit()
    
    c_index = args.index('-c')
    configfile = args[c_index + 1]

    d_index = args.index('-d')
    userdatafile = args[d_index + 1]

    o_index = args.index('-o')
    outfile = args[o_index + 1]
    
    user = UserData(userdatafile,outfile,configfile)
    JiShul = user.get_config('JiShul')
    JiShuH = user.get_config('JiShuH')

    if not os.path.isfile(configfile):
        print('Parameter Error!')
        exit()

    if not os.path.isfile(userdatafile):
        print('Parameter Error!')
        exit()

    if not os.path.isfile(outfile):
        print('Parameter Error')
        exit()

    with open(userdatafile,'r') as f:
        for line in f:
            k,v = line.split(',')
            if JiShul < float(v) < JiShuH:
                user.calculator(k.strip())
            elif float(v) <= JiShul:
                user.calculator_l(k.strip())
            elif float(v) >= JiShuH:
                user.calculator_h(k.strip())

if __name__ == '__main__':
    main()

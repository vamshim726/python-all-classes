


class Calc:

    company ='CASIO'
    registration_id ='RID1234'

    def __init__(self,id,manf_date):
        self.id=id
        self.manf_date=manf_date

    def add(self,a , b):
        return a+b
    
    def sub(self, a,b):
        return a-b


class AdvCalc(Calc):
    def __init__(self,id,manf_date):
        super().__init__(id,manf_date)


    def log(self,a):
        return 5
    
class SuperCalc(AdvCalc):
    
    def __init__(self,id,manf_date):
        super().__init__(id,manf_date)
        
    def integration(self,a,b):
        return 'integration done'
    


# calc1= AdvCalc()
# print(calc1.company)
# print(calc1.registration_id)
# print(calc1.add(10,20))
calc2= SuperCalc('201','14 july')
print(calc2.integration(1,2))
print(f"id is: {calc2.id}, manf date {calc2.manf_date}")

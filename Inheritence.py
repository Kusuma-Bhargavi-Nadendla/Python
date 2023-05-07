class Time(object):
    """Represents Indian Standard time
    Attributes:hour,minute,second"""
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return '%.2d:%.2d:%.2d '%(self.hour,self.minute,self.second)
    def cal_time(self,other):
        duration=Time()
        duration.hour=abs(self.hour-other.hour)
        duration.monute=abs(self.minute-other.minute)
        duration.second=abs(self.second-other.second)
        return duration
class Date(object):
    """Represents Standard Date
    Attributes:Day,Month,Year"""
    def __init__(self,day=0,month=0,year=0):
        self.day=day 
        self.month=month 
        self.year=year 
    def __str__(self):
        return '%.2d/%.2d/%.4d'%(self.day,self.month,self.year)
    def cal_days(self,other):
        diff=Date()
        diff.year=abs(self.year-other.year)
        diff.month=abs(self.month-other.month)
        diff.day=abs(self.day-other.day)
        return diff
class Employee(Date,Time):
    """Represents Some basic details of an Employee
    Attributes:Name,Age,Experience,Working_Hours"""
    def __init__(self,name,joinDate,untilDate,time1,time2,dob):
        self.name=name
        self.whours=time1.cal_time(time2) 
        self.experience=joinDate.cal_days(untilDate)
        self.age=dob.cal_days(untilDate).year
    def __str__(self):
        return 'Name:%s\nAge:%d\nExperience:%1.d years %.2d Months\nWorking Hours:%1d'%(self.name,self.age,self.experience.year,self.experience.month,self.whours.hour)
n=input('Enter Employee name :')
jd=Date(*tuple(map(int,(input('Enter Joining Date :').split('/')))))
wd=Date(*tuple(map(int,(input('Enter Today Date :').split('/')))))
db=Date(*tuple(map(int,(input('Enter Date of Birth:').split('/')))))
t1=Time(*tuple(map(int,input('Entry time for office:').split(':'))))
t2=Time(*tuple(map(int,input('Exit time from office:').split(':'))))
emp=Employee(n,jd,wd,t1,t2,db)
print('Using Multiple Inheritence Job Details of Employee are')
print(emp)







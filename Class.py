""" Chapter 18. Class and object """
#!/usr/bin/python
from __builtin__ import False
class Employee:
    '''Common base class for all employees
        this class is the base class
    '''
    empCount=0
        
    'initialize function with name, salaary'
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        self.__employID=Employee.empCount        
        Employee.empCount+=1
    
    def displayCount(self):
        print "Total Employee %d" %Employee.empCount

    def displayEmployee(self):
        print "Name:",self.name,", Salary:",self.salary
    
    def get_EmployeeID(self):
        return self.__employID;


class USAEmployee(Employee):
    ''' Employee's of USA branch
    
    '''
    USEmpCount=0
    def __init__(self,name,salary,vacation):
        self.name=name
        self.salary=salary
        self.vacation=vacation
        self.__employID=Employee.empCount        
        Employee.empCount+=1
        USAEmployee.USEmpCount+=1        
        return
    
    def displayEmployee(self):
        print "Name:",self.name,", Salary:",self.salary,"Vacation:",self.vacation
        self.displayCount()
        self.displayUSEmployeeCount()
        return
    
    def displayUSEmployeeCount(self):
        print "Total USEmployee:",USAEmployee.USEmpCount;
        
    
def print_emp1():
    emp1=Employee("Zara",2000)
    emp2=Employee("Manni",5000)
    
    print id(emp1), id(emp2)
    
    emp1.displayEmployee()
    print "emp1 ID:", emp1.get_EmployeeID()
    
    emp2.displayEmployee()
    print "emp2 ID:", emp2.get_EmployeeID()
        
    print "Total Employee %d" %Employee.empCount
    if hasattr(emp1,'age'):
        print "Emp1 Age : %s" %getattr(emp1,'age')
    else:
        setattr(emp1,'age',20)
        print "Emp1 Age : %s" %getattr(emp1,'age')
    if hasattr(emp1,'name'):
        print "Emp1 name: %s" %getattr(emp1,'name')
    if hasattr(emp1,'salary'):
        print "Emp1 salary:%d" %getattr(emp1,'salary')
            
    print ("Emp1 __dict__:",emp1.__dict__)
    print ("Emp1 __doc__:",emp1.__doc__)
    print ("Emp1 __module__:",emp1.__module__)
    
    
#print ("Emp1 __bases__:",emp1.__bases__)
#print ("Emp1 __name__:",emp1.__name__)

def print_USAEmp1():
    emp1 = USAEmployee("Snoopy",3000,10)
    print "USA emp1 ID:", emp1.get_EmployeeID()    
    emp2 = USAEmployee("Candy",5000,15)
    print "USA emp2 ID:", emp2.get_EmployeeID()    
    emp1.displayEmployee()
    emp2.displayEmployee()
    
class MYPoint:
    def __init__(self,x=0, y=0):
        self.x=x
        self.y=y
        
    def displayPoint(self):
        print "x=%d y=%d"%(self.x,self.y)
        
    def __del__(self):
        class_name=self.__class__.__name__
        print class_name,"destroyed"

def del_point():
    pt1=MYPoint(5,10)
    pt2=pt1
    pt3=pt1
    
    pt1.displayPoint()
    pt2.displayPoint()
    pt3.displayPoint()
    
    print id(pt1),id(pt2),id(pt3)
    
    del pt1
    del pt2
    del pt3

class MyVector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "MyVector (%d,%d)" %(self.a,self.b)
    
    def __add__(self,other):
        return MyVector(self.a+other.a,self.b+other.b)
    
    def __cmp__(self,other):
        if(self.a>other.a):
            return True
        elif(self.a==other.a):
            if(self.b>=other.b):
                return True
            else:
                return False
        else: #self.a< self.b 
            return False

def MyVector_Test():
    a= MyVector(20,20)
    b= MyVector(20,20)
    c= a+b
    print "MyVector a", a
    print "MyVector b", b
    print "MyVector c=a+b", c
    
    if(a>b):
        print"Class a is bigger than b"
    else:
        print"Class a is smaller than b"
    
    return


def main():
    print_emp1()
    del_point()
    print_USAEmp1()
    MyVector_Test()
    
    
if __name__=='__main__':
    main()
    
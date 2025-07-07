import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CURDporject.settings')
import django
django.setup()
from testapp.models import employee
from random import *
from faker import Faker
faker=Faker()

def populate(n):
    for i in range(n):
        feid=randint(1,100)
        fename=faker.name()
        fesal=randint(15000,30000)
        feaddress=faker.city()
        emp_record=employee.objects.get_or_create(
            eid=feid,
            ename=fename,
            esal=fesal,
            eaddress=feaddress
        )
n=int(input("Enter a How Many Generate:"))
populate(n)
print(f'{n} inserted record successfully...........')
class Student:
    pass
s1=Student()
s2=Student()
s1.name="saurabh"  ## attribute
s1.roll=2      ## attribute

##get attributes's value
print(s1.name)

##gives all aatribute ob that object in dictionary format
## that is {key:value}
print(s1.__dict__)


##check if attributes is present or not,return boolean value
print(hasattr(s1,'name'))

##get attribute's value .If attribute isn't present it will give attribute error
print(getattr(s1,'name'))

## to avoid attribute error we can pass third argument so that if attribute isn't present
## we will get default value
print(getattr(s2,'roll',69))

## delete the attribute
delattr(s1,'name')
print(hasattr(s1,'name'))   ### returns falsy value

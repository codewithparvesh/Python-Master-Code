from this import d
from traceback import print_tb


def new_func():
# dicatonary
#orderd changanble and it allow the supliaceta value
    dic = {
    "name" : " Parvesh",
    "age" : 20,
    "year" : 2002
  }

    print(dic)
    print(type(dic))

    employe = {
        "Nmae" : "parvesh",
        "Age" : 20,
        "Company" : "Let's Learn Finance Market",
        "Postion" : "Founder and CEO"
    }
    print(employe)

    #differnet type of key value
    employe = {
        "Nmae" : "parvesh",
        "Age" : 20,
        "Company" : "Let's Learn Finance Market",
        "Postion" : "Founder and CEO",
        "Make" : True,
        "Options" : ["TVCS", "GOOGLE"]

    }
    print(employe)

    demo = {
        "Nmae" : "parvesh",
        "Age" : 20,
        "Company" : "Let's Learn Finance Market",
        "Postion" : "Founder and CEO",
        "Make" : True,
        "Options" : ["TVCS", "GOOGLE"],
        "Age" : 852 # IT WILL PRINT THE LATEST VALUSE 
    }

    print(demo)987654;
    print(demo)
    demo.upda
    print(demo["Age"])
    print(demo.keys())
    print(demo.values())
    print(demo.items())
    demo["Age"]=te({"Age" : 123})
    print(demo)
    demo["add"]=5464    # use to add in the dictonary
    print(demo)
    demo.pop("add")
    print(demo)
    del demo["Age"]
    print(demo)


    # nested Dicitonaries
    dic ={
        "dic1" :{
            "Name": 'Parvesh'
        },
        "Age" : 15
    }
    print(dic)
new_func()
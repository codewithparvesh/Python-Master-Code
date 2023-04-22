def new_func():
    name =("parvesh", "panda", "swati")
    a = [" parvesh ","  ", "jangra", "manisha"]
    print(type(name))
    print(type(a))

    a=("parvesh")
    b=("jangra",)
    print(type(a))
    print(type(b))

    name = ("parvesh", "parvesh", "jangra", 25)
    print(name)
    #name[0]="jangra"

    name = ("parvesh", "parvesh", "jangra", 25)
    print(type(name))
    # tuple to list 
    b=list(name)
    print(type(b))
    b[1]="Jangra"
    name=tuple(b)
    print(name)


    name = ("parvesh", "parvesh", "jangra", 25)
    #name.apend("kiran")  # this will fgave you error
    #b so if you want ot add so you have to convert to list
    print(name)

    a=("parvesh",)
    b=("jangra",)
    print(a+b)
    a+=b
    print(a)

    
new_func()
Usr=[]
def user(first_name= "pradeep",mid_name ="chandra",last_name="behara"):
    Usr.append(first_name+ mid_name + last_name)
    Usr.append(first_name + mid_name)
    Usr.append(first_name[0] + mid_name[0]+ last_name)
    Usr.append(first_name+ mid_name[0]+ last_name)
    Usr.append(first_name + mid_name[:1])
    Usr.append(first_name + last_name)
    Usr.append(first_name[:1] + last_name)
    Usr.append(first_name + last_name[:1])
    Usr.append(first_name + '_'+ last_name)
    Usr.append(first_name + '.'+ last_name)
    Usr.append(first_name[0] + mid_name[0]+'.'+ last_name)
    Usr.append(first_name+ mid_name+ last_name[:1])
    Usr.append(first_name+ last_name[:1])
    Usr.append(first_name + last_name)           # johndoe
    Usr.append(last_name + first_name)           # doejohn
    Usr.append(first_name + "." + last_name)     # john.doe
    Usr.append(last_name + "." + first_name)     # doe.john
    Usr.append(last_name + first_name[0])        # doej
    Usr.append(first_name[0] + last_name)        # jdoe
    Usr.append(last_name[0] + first_name)        # djoe
    Usr.append(first_name[0] + "." + last_name)  # j.doe
    Usr.append(last_name[0] + "." + first_name)  # d.john

user()

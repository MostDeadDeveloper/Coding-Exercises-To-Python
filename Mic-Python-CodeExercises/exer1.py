import time
name = []
email = []
for x in range(5):
    n = input("Enter Name #%d: " % (x+1))
    name.append(n)
    e = input("Enter %s's Email Address: " % n)
    email.append(e)
    print('\n')

print('\nNames and Email Addresses\n')
for x in range(5):
    print("%s : %s\n" % (name[x], email[x]))
    
time.sleep(5)

#def spam(divideBy):
#    return 42 / divideBy

#print (spam(0))

#def spam(bagi):
#    try:
#        return 42/bagi
#    except ZeroDivisionError: #the code must go on
#        print ('Error brader')

#print (spam(2))
#print (spam(0))
#print (spam(1))

def spam(bagi):
    return 42/bagi

try:
    print (spam(2))
    print (spam(0)) #disiini udah error, yang 1 jadi ga kebaca langsung loncat ke except
    print (spam(1))
except ZeroDivisionError: #the code must go on
        print ('Error brader')

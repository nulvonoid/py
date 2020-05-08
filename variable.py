#def spam ():
#    eggs = 'spam local'
#    print (eggs)

#def bacon ():
#    eggs = 'bacon local'
#    print (eggs)
#    spam()  #dia kerjain yang spam dulu
#    print (eggs) #value eggs nya reset, karena spam udah kelar

#eggs = 'eggs global' # ini variabel global
#bacon () #dia kerja bacon dulu, tapi begitu bacon selesai, eggs balik jadi var globalnya
#print (eggs) # print eggs global

#global statement
#def spam ():
#    global eggs #define eggs globally
#    eggs = 'spam'
#    print (eggs)

#def bacon ():
#    eggs = 'bacon' #define eggos=bacon, local

#def ham ():
#    print (eggs) # eggs globalnya masih yg di spam()

#eggs = 'not spam'
#spam ()
#bacon()
#ham()
#print (eggs)

#eggs = 'global'
#def spam():
#    print(eggs) # ERROR!
#    eggs = 'spam local'
#spam()

#import sys
#sys.exit()

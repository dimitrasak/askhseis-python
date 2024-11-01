def fibo(x):
    i=1
    j=1
    for k in range(x-2): #το k το χρησιμοποιώ ως μετρητή
        tmp=i #μεταβλητή,προκειμένου να κρατήσω προσωρινά την τιμή του i
        i=i+j #αλλάγή της τιμής του i
        j=tmp #το j παίρνει την παλιά τιμή του i
    return i

print("Καταχωρίστε τον όρο της ακολoυθίας Fibonacci:")
p = int(input()) #βάζει ο χρήστης τον όρο της ακολουθίας
print("O όρος της ακολουθίας Fibonacci είναι o:",p)
print("Η τιμή της ακολουθίας Fibonacci είναι: ",fibo(p))

import random

check = 0 #αρχικοποίηση της τιμής 0

for k in range(20): #χρησιμοποιώ το k ως μετρητή,η παρακάτω διαδικασία επαναλαμβάνεται 20 φορές
    a=random.randint(1,1000)#επιλέγει μια τυχαία τιμή ανάμεσα στο 1 και στο 1000
    #print("a:",a)
    if (a**p)%p==a%p:
        continue
    else: #έστω ότι δεν ισχύει για έναν αριθμό η παραπάνω ισότητα
        check = 1
        print("False: Δεν είναι πρώτος.") #εκτύπωνει ότι είναι ψέμα
        break #σταματάει την επανάληψη

if check == 0:
    print("True: Είναι πρώτος.")

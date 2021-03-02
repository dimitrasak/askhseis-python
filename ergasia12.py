import re

def reverse(string): #δημιουργία συνάρτησης για την αντιστροφή του κειμένου και των λέξεων
    reversed_string = ""  #αρχικοποίηση
    for i in string:
        reversed_string = i + reversed_string
    print("The reversed ascii text is: " + reversed_string) #εκτυπώνει το αντεστραμμένο κείμενο
    for c in reversed_string: #για κάθε χαρακτήρα του αντεστραμμένου κειμένου
        s = ord(c)
        #print(s)
        #print(type(s)) επιστρέφει int
        kat = chr(128 - s) #επιστρέφει string,εν΄ώ στις () δέχεται μόνο int
        kat1 = kat.split() #μετατρέπω το kat σε λίστα ώστε να μου εμφανιστούν οι κατοπτρικοί αριθμοί
        #print(type(kat))
        #kat1 = int(kat)
        print(kat1, end=" ") #χωρίζω με το κενό

userinput = input("Enter the name of the ascii file: ") #ο χρήστης καταχωρεί το αρχείο ascii
#print(type(userinput))
myfile = open(userinput) #ανοίγει το αρχείο
info = myfile.read() #διαβάζει το αρχείο
#print(info)
myfile.close

processed_text = re.sub('(@[A-Za-z0-9]+)|([^A-Za-z \t])|(\w+:\/\/\S+)', '', info)  #καθαρίζει το κείμενο από άχρηστους χαρακτήρες
processed_text = " ".join(processed_text.split())
print(processed_text)
processed_text1 = processed_text.split() #μετατρέπω το επεξεργασμένο κείμενο σε λίστα
#print(processed_text1)

reverse(processed_text) #καλώ την συνάρτηση η οποία αντριστρέφει το επεξεργασμένο κείμενο και έπειτα εμφανίζει τους κατοπτρικούς χαρακτήρες

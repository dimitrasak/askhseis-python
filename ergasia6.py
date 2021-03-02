import tweepy  # εισαγωγή του module
import re #βιβλιοθήκη για regular expressions

# ορίζω τα κλειδιά που πήρα από το twitter αντίστοιχα
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

# έγκριση του consumer key και του consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_secret)

# καλώ το api
api = tweepy.API(auth)

userID = input("Καταχωρίστε το username του χρήστη:") #ο χρήστης δηλώνει τον λογαριασμό που θέλει να πάρει τα 10 tweets
tweets = api.user_timeline(screen_name=userID,
                           count=100,
                           include_rts=False, #απαραίτητο για να αποσπάσει ολόκληρο το κείμενο και όχι μόνο τις πρώτες 140 λέξεις
                           tweet_mode="extended"
                           )

for info in tweets[:10]: #παίρνει τα 10 τελευταία tweets
    #print("ID:{}".format(info.id))
    print(info.created_at) #δείχνει την ημερομηνία που έγινε το tweet
    s = info.full_text
    print(s) #εκτυπώνει το tweet
    tweets1 = str(s) #μετατρέπω το s σε string
    processed_text = re.sub('(@[A-Za-z0-9]+)|([^A-Za-z \t])|(\w+:\/\/\S+)', '', tweets1)  #καθαρίζει τα tweets από υπερσυνδέσμους,tags,emojis και από άχρηστους χαρακτήρες γενικά
    processed_text = " ".join(processed_text.split())
    #print(processed_text) #εκτυπώνει το επεξεργασμένο tweet!
    tmp = processed_text.split() #χωρίζω τα tweets με το κενό
    #print(tmp) #εκτυπώνει την λίστα των λέξεων
    small = large = tmp[0]
    smallist = [] #ορίζω 2 λίστες:1 για τις μικρότερες λέξεις και 1 για τις μεγαλύτερες
    largelist = []
    smallist = tmp.copy() #αντιγ΄ραφω τα περιεχόμενα της λίστας tmp
    largelist = tmp.copy()
    #print(smallist)
    #print(largelist)

    for l in range(5): #επανάληψη για να βρω τις 5 λέξεις
        indexsmall = 0
        indexlarge = 0

        lensmall = len(smallist[0])
        lenlarge = len(largelist[0])

        for k in range(0,len(smallist)):
            if(lensmall > len(smallist[k])):
                lensmall = len(smallist[k])
                indexsmall = k
        for m in range(0,len(largelist)):
            if(lenlarge < len(largelist[m])):
                indexlarge = m
                lenlarge = len(largelist[m])

        print("H "+str(l+1)+"η "+ "μικρότερη λέξη είναι:" + smallist[indexsmall])
        print("Η "+str(l+1)+"η "+ "μεγαλύτερη λέξη είναι:" + largelist[indexlarge])
        smallist.remove(smallist[indexsmall])
        largelist.remove(largelist[indexlarge])
        if len(smallist) == 0:
            break
    print("\n") #ετυπώνει μια γραμμή κενό ανάμεσα από τα tweets

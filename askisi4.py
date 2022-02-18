#Έστω ένα τετράγωνο 3*3 στο οποίο τοποθετείται καπάκια.Έχετε στην 
#κατοχή σας 27 καπάκια,9 για κάθε μέγεθος(μίκρο,μεσαίο,μεγάλο).
#Μια τριάδα που τερματίζει το παιχνίδι γίνεται οριζόντια,κάθετα ή διαγωνια
#Η τριάδα αποτελείται απο καπάκια είτε του ίδιου μεγέθους είτε απο 
#το μικρό  προς το μεγαλύτερο.Επειδή έχετε καπάκια,ένα καπάκι μπορεί
#να μπει σε οποιαδήποτε τετράγωνο,αρκεί να είναι ελεύθερο ή να μην
#υπάρχει εκεί μικρότερο καπάκι.Γράψτε ένα πρόγραμμα το οποίο 
#παίζει τυχαία το παιχνίδι 100 φορες και επιστρέφει το μέσο όρο 
#των βημάτων για να λήξει το παιχνίδι. 
import random

def check_seira(TAMP):
    x = random.randint(0,8)
    while True:
        if TAMP[x] == 0:
            choose = TAMP[x]
            break
    return TAMP

#elegxos orizontia
def check_horiz():
    seira1 = TAMP[0] == TAMP[1] == TAMP[2] !=0
    seira2 = TAMP[1] == TAMP[4] == TAMP[7] !=0
    seira3 = TAMP[6] == TAMP[7] == TAMP[8] !=0

    seira1a = TAMP[0] < TAMP[1] < TAMP[2] !=0
    seira2a = TAMP[3] < TAMP[4] < TAMP[5] !=0
    seira3a = TAMP[6] < TAMP[7] < TAMP[8] !=0

    seira1b = TAMP[0] > TAMP[1] > TAMP[2] !=0
    seira2b = TAMP[3] > TAMP[4] > TAMP[5] !=0
    seira3b = TAMP[6] > TAMP[7] > TAMP[8] !=0

    if seira1:
        return True
    elif seira2:
        return True
    elif seira3:
        return True
    if seira1a:
        return True
    elif seira2a:
        return True
    elif seira3a:
        return True
    if seira1b:
        return True
    elif seira2b:
        return True
    elif seira3b:
        return True
#elegxoume ka8eta
def check_vert():
    seira1 = TAMP[0] == TAMP[3] == TAMP[6] !=0
    seira2 = TAMP[1] == TAMP[4] == TAMP[7] !=0
    seira3 = TAMP[2] == TAMP[5] == TAMP[8] !=0

    seira1s = TAMP[0] < TAMP[3] < TAMP[6] !=0
    seira2s = TAMP[1] < TAMP[4] < TAMP[7] !=0
    seira3s = TAMP[2] < TAMP[5] < TAMP[8] !=0

    seira1e = TAMP[0] > TAMP[3] > TAMP[6] !=0
    seira2e = TAMP[1] > TAMP[4] > TAMP[7] !=0
    seira3e = TAMP[2] > TAMP[5] > TAMP[8] !=0

    if seira1:
        return True
    elif seira2:
        return True
    elif seira3:
        return True
    elif seira1s:
        return True
    elif seira2s:
        return True
    elif seira3s:
        return True
    elif seira1e:
        return True
    elif seira2e:
        return True
    elif seira3e:
        return True

def check_diag():
    diag1 = TAMP[0] == TAMP[4] == TAMP[8]
    diag2 = TAMP[2] == TAMP[4] == TAMP[6]

    diag1t = TAMP[0] < TAMP[4] < TAMP[8]
    diag2t = TAMP[2] < TAMP[4] < TAMP[6]

    if diag1:
        return True
    elif diag2:
        return True
    elif diag1t:
        return True
    elif diag2t:
        return True

counter = 0
for i in range (100):
    TAMP=[0]*9
    logiki = True
    metrisi = 0
    while logiki:
        metrisi +=1
        counter +=1
        check_seira(TAMP)
        if metrisi >=3:
            if check_horiz():
                logiki = False
            elif check_vert():
                logiki = False
            elif check_diag():
                logiki = False

counter=counter/100
print(counter)     

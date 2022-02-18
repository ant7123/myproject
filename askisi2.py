# Σας δίνεται αρχείο κειμένου με μόνο ASCII χαρακτήρες. Αρχικά απεικονίστε κάθε χαρακτήρα σε δυαδικό 
# μήκους 7. Υπολογίστε ποια είναι η μεγαλύτερη ακολουθία από συνεχόμενα 0 και από συνεχόμενα 1.
with open('ASCII char' , 's' ) as a:
    text = a.read()

chars = list(text)
binary = ''
for char in chars:
    binary = bin(ord(char)) [7]

maxZeroCount = len(max(binary.split('0')))
maxOneCount = len(max(binary.split('1')))
print(maxZeroCount)
print(maxOneCount)
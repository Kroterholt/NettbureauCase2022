from email import message
from multiprocessing import context
import sys
import pandas as pd
import smtplib, ssl

df = pd.read_csv("Postnummerregister.csv")
postalNumbers = df["Postnummer"]

def main():
    schema = sys.argv[1]
    schema = argToList(schema)

    if verifyData(schema): sendMail(schema) # TODO sende varsel på epost
    else: print("Not verified")
    
"""
Splitting schema into a list, indexes should look like this:
[0] = Navn
[1] = E-post
[2] = Telefon
[3] = Postnummer
[4] = Kommentar
"""
def argToList(schema):
    return schema.split(";")

"""
This function gets called when the schema is verified
Sends a confirmation email
Based my code on the tutorial found here: https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development 
"""
def sendMail(schema):
    senderEmail = "nettbureauTest@gmail.com" # Insert adress of sender
    password = input("Type password for " + senderEmail + ": ")

    recieverEmail = "io@nettbureau.no" # Insert adress of reciever
    message = """\
        Subject: Skjema godkjent

        Skjemaet er godkjent.
        """

    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("nettbureauTest@gmail.com", password)
        server.sendmail(senderEmail, recieverEmail, message)
    

"""
Seperate check for each important field
"""
def verifyData(schema):
    isValid = True
    if len(schema) == 5: # Checks if all fields are represented
        if not verifyEmail(schema[1]):
            print("E-Mail not verified")
            isValid = False

        if not verifyPhoneNumber(schema[2]):
            print("Phone number not verified")
            isValid = False

        if not verifyPostal(int(schema[3])): 
            print("Postal code not verified")
            isValid = False
    else: 
        isValid = False
        print("Not enough inputs")

    return isValid

"""
True if email satisfies conditions
"""
def verifyEmail(str):
    if "@" in str: # Emails needs to contain @
        nameAndDomain = str.split("@")
        if len(nameAndDomain) == 2: # Make sure there are not multiple @ in the adress
            if "." in nameAndDomain[1]: # Domain needs to contain .
                return True
    else: return False

"""
True if phone number satisfies conditions
Assuming the forms only allow Norwegian private numbers
"""
def verifyPhoneNumber(phoneNumber):
    legalStartingDigits = ["2","4","5","6","8","9"] # Norwegian private numbers start with these digits
    if len(phoneNumber) == 8: # Phone number must be 8 digits long
        if phoneNumber[:1] in legalStartingDigits:
            return True
    return False

"""
True if given number exist in postalNumbers
"""
def verifyPostal(n):
    if n in postalNumbers: return True
    else: return False

if __name__== "__main__":
    main()

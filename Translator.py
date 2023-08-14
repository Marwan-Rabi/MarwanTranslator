from deep_translator import GoogleTranslator
    
#input the from and to 
print("Welcome to Translator Program")
while True: 
    fro= input("From: ")
    to =input("To: ")
    text = input("Enter The Text: ")
    # translate 
    try:
        translated_text = GoogleTranslator(source=fro,target=to).translate(text)
        print(translated_text)
    except:
        print("The language is not correct, Please enter the correct language")

    # close or return
    close = input("Click (r) to return or any another key to close: ")

    if close != 'r':
        quit()
    

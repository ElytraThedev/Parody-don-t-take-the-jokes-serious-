import webbrowser
import winsound 

def getOpen1():
    url = "https://youtu.be/-GpiF8J4j9U"
    webbrowser.open(url)

def getOpen2():
    urll = "https://www.youtube.com/watch?v=MuwfR9YrNp4&pp=ygUFRXJpa2E%3D"
    webbrowser.open(urll)

def getOpen3():
    urlb = "https://www.youtube.com/shorts/b9N1JMF-hFk?feature=share"
    webbrowser.open(urlb)

def getOpen4():
    urlb = "https://www.youtube.com/watch?v=wU-490g1d3c"
    webbrowser.open(urlb)


while True:
    inp = input(">> ")

    if inp == "/hack":
      print('>> '+"\033[36m"+"hacking successful, the antivirus was made in china "+"\033[0m")
      winsound.MessageBeep(winsound.MB_ICONASTERISK)


    if inp == "/reboot microsoft":
      getOpen1()

    if inp == "/i like messi":
        print("WTF")
        winsound.Beep(1000, 1500)  
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

    if inp == "/hail Hitler":
       getOpen2()

    if inp == "SUS":
       getOpen3()

    if inp == "Communism op":
       getOpen4()

    if inp == "/quit":
       print("hamse nahi miloge kya -salmon bhai")
       break
       
       


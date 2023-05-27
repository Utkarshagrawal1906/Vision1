import speech_recognition as sr
import webbrowser as wb
import pyttsx3,datetime,openai
from urllib.request import urlopen
import main1
from AppOpener import open,close
from mysql.connector import connection
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
con=connection.MySQLConnection(user='root',host='localhost',database='vision',port='3307',password='utkag')
cursor=con.cursor()

options=Options()
options.add_argument('--user-data-dir=C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\User Data\\')
driver=uc.Chrome
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',160)
hour=int(datetime.datetime.now().hour)
minute=int(datetime.datetime.now().minute)
user="Utkarsh"
openai.api_key = "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"
dicts=one=face=False

class Voice:
    def __init__(self):
        global one
        one=True
    def gpt(self,ask):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=ask,
            temperature=0.5)
        return response['choices'][0]['text'].strip()
    def fone(self):
        global one
        one=False
    def greet(self):
        ext=""
        global user,driver
        if face:
            main1.img()
            user=main1.face().title()
            if user=="Unknown":
                user=""
                ext=", but I didn't recognized you"
            cursor.execute(f"select * from data where name='{user}';")
            r=cursor.fetchall()
            print(r[0][1])
            try:
                options.add_argument(f'--profile-directory={r[0][1]}')
            except Exception as e:
                print(e)
        if 0 <= hour < 12:
            return "Good Morning "+user+" Sir"+ext
        elif 12 <= hour < 18:
            return "Good Afternoon "+user+" Sir"+ext
        else:
            return "Good Evening "+user+" Sir"+ext

    def speak(audio):
        if one and dicts:
            engine.say(audio)
            engine.runAndWait()

    def voice(self):
        print("k")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio,language="en-in")
                print(text)
                text=text.lower()
                if face:
                    global user
                    user=main1.face()
                    print(user)
                return text
            except Exception as e:
                print(e)
                return "sorry"

    def search(self, text):
        if "open" in text:
            text = text.replace(" ", "")
            a=open(text[4:], match_closest=True)
            print(a,"hi")
            if a!=None:
                return "Opening " + text[4:]
            else:
                try:
                    urlopen("https://www." + text[4:])
                    wb.get().open_new("https://www." + text[4:])
                    return "Opening " + text[4:]
                except:
                    try:
                        urlopen("https://www." + text[4:] + ".in")
                        wb.get().open_new("https://www." + text[4:] + ".in")
                        return "Opening " + text[4:] + ".in"
                    except:
                        try:
                            urlopen("https://www." + text[4:] + ".com")
                            wb.get().open_new("https://www." + text[4:] + ".com")
                            return "Opening " + text[4:] + ".com"
                        except:
                            try:
                                urlopen("https://www." + text[4:] + ".org")
                                wb.get().open_new("https://www." + text[4:] + ".org")
                                return "Opening " + text[4:] + ".org"
                            except:
                                try:
                                    urlopen("https://www." + text[4:] + ".gov")
                                    wb.get().open_new("https://www." + text[4:] + ".gov")
                                    return "Opening " + text[4:] + ".gov"
                                except:
                                    return "page not found"
        elif "close" in text:
            text = text.replace(" ", "")
            a = close(text[5:], match_closest=True)
            return "Closing " + text[4:]
        elif "search" in text or " on " in text:
            a = text.split()
            s = ""
            for i in a:
                if i == "search":
                    continue
                elif i == "on":
                    if a[-1] == "google":
                        wb.get().open_new("https://www.google.com/search?q=" + text)
                        return "Searching query on Google"
                    if a[-1]=="bing":
                        wb.get().open_new("https://www.bing.com/search?q=" + text)
                        return "Searching query on Bing"
                    elif a[-1] == "youtube":
                        wb.get().open_new("https://www.youtube.com/results?search_query=" + s.lstrip())
                        return "Opening "+s.lstrip()+" on Youtube"
                    elif a[-1] == "linkedin":
                        wb.get().open_new("https://www.linkedin.com/search/results/all/?keywords=" + s.lstrip() + "&origin=GLOBAL_SEARCH_HEADER&sid=n2m")
                        return "Opening "+s.lstrip()+" on Linkedin"
                    elif a[-1] == "amazon":
                        wb.get().open_new(f"https://www.amazon.com/s?k={s.lstrip()}&crid=162S3P6U3ZRZ9&sprefix={s.lstrip()}%2Caps%2C713&ref=nb_sb_noss_1")
                        return "Opening "+s.lstrip()+" on Amazon"
                    elif a[-1] == "flipkart":
                        wb.get().open_new(f"https://www.flipkart.com/search?q={s.lstrip()}&as-type=RECENT&requestId=dc8d1d33-9ccb-4d0e-a67d-96ae30812fb5&as-backfill=on")
                        return "Opening "+s.lstrip()+" on Flipkart"
                    elif a[-1] == "hackerrank":
                        wb.get().open_new(f"https://www.hackerrank.com/{s.lstrip()}?h_r=internal-search&hr_r=1")
                        return "Opening "+s.lstrip()+" on HackerRank"
                    elif a[-1] == "facebook":
                        wb.get().open_new(f"https://www.facebook.com/search/top/?q={s.lstrip()}")
                        return "Opening "+s.lstrip()+" on Facebook"
                    elif a[-1] == "wikipedia":
                        wb.get().open_new(f"https://en.wikipedia.org/w/index.php?go=Go&search={s.lstrip()}&title=Special%3ASearch&ns0=1")
                        return "Opening "+s.lstrip()+" on Wikipedia"
                else:
                    s += " " + i
            else:
                wb.get().open_new("https://www.google.com/search?q=" + s)
                return "Searching query on Google"
        else:
            try:
                print('nk')
                v=Voice.gpt(Voice,text)
                print(v,len(v))
                if v==None:
                    raise "Not Found"
                return v
            except Exception as e:
                print(e)
                wb.get().open_new("https://www.google.com/search?q=" + text)
                return "Searching query on Google"
import random

class story:
    tipe = ["legend", "fairytale", "history"]
    tokoh = ["kancil", "harimau", "buaya"]
    tempat = ["surabaya", "bandung", "semarang", "jakarta"]
    kota = random.choice(tempat)
    tokoh = random.choice(tokoh)

    def __init__(self, storyType, place):
        self.storyType = storyType
        self.place = place
        
class gnrtStory1(story):

    def __init__(self, storyType, place):
        super().__init__(storyType, place)
        #Legenda
        if storyType == story.tipe[0]:
            print("Pada zaman dahulu terdapat kisah legenda yang berasal dari kota {} yang mengisahkan tentang ....".format(story.kota))
        #Dongeng
        elif storyType == story.tipe[1]:
            print("Pada suatu hari hiduplah seekor {} ditengah hutan yang lebat ...".format(story.tokoh))

class gnrtStory2(story):

    def __init__(self, storyType, place):
        super().__init__(storyType, place)
        if storyType == story.tipe[2] and place == story.tempat[0]:
            print("Pada suatu hari, pada tanggal 10 November 1945 merupakan hari paling bersejarah \nbagi masyarakat Indonesia khususnya kota Surabaya ...")
        elif storyType == story.tipe[2] and place == story.tempat[1]:
            print("Pada suatu hari, pada tanggal 23 Maret 1946 merupakan peristiwa yang kita kenal \ndengan Bandung lautan api ...")
        elif storyType == story.tipe[2]  and place == story.tempat[2]:
            print("Pada suatu hari, pada tanggal 15 - 19 Oktober 1945 terjadi peristiwa bersejarah \nyang dikenal dengan peristiwa pertempuran 5 hari di Semarang ...")
        elif storyType == story.tipe[2]  and place == story.tempat[3]:
            print("Pada suatu hari, pada tanggal 17 Agustus 1945 merupakan peristiwa paling bersejarah bagi bangsa Indonesia. \nPada tanggal tersebut merupakan hari kemerdekaan bangsa Indonesia ...")

print("Welcome to the story generator game \nit's time to generate a story based on your preference")
nameReader = input("First of all could you tell me your name ? Y/N : ").upper()
if nameReader == "Y":
    name = input("What's your name : ")
    print("Great! Hello {} let's begin this game".format(name))
    print("=====================================")
else :
    print("It's ok, I will make you anonymous, so you can still play this game :) ")
    print("=====================================")
tipe = input("Enter the type of story you want to read \n(Legend/Fairytale/History): ").lower()
print("=====================================")
if tipe != "history":
    cerita1 = gnrtStory1(tipe, "None")
    print(cerita1)
else :
    kota = input("Enter the origin of the historical story you want to read \n(Surabaya/Bandung/Semarang/Jakarta) : ").lower()
    print("=====================================")
    cerita2 = gnrtStory2(tipe,kota)
    print(cerita2)
    
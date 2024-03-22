import  tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import random

MAIN_PAGE=Tk()
MAIN_PAGE.configure(bg="black")
I_FULL=PhotoImage(file="unnamed1.png")
LABEL_I_FULL=tkinter.Label(MAIN_PAGE,image=I_FULL,bg='BLACK')
LABEL_I_FULL.place(x=0, y=0,relwidth=1, relheight=1)

WOULDU=tkinter.Label(MAIN_PAGE,bg="gray13",text='WOULD YOU RATHER',fg="white",font=("white",53,"bold")).place(x=420,y=60)
OR1=tkinter.Label(MAIN_PAGE,text='OR',bg='gray15',fg="white",font=("white",53,"bold")).place(x=705,y=415)


def randomgame():
    try:
        randomgame.A1.destroy()
        randomgame.B1.destroy()
    except:
        pass
    
    r=random.randrange(1,101)
    
        
    if r==1:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have an incredibly\n annoying high-pitched\n voice',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have a really deep\n manly voice',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==2:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have a full-blown\n moustache for a year',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have a Permanently\n hairy legs for\n ten years',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==3:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Give up your phone',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Only wear Crocs for the\n rest of your life',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==4:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Clog the toilet on a\n first date',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Clog the toilet on\n first day at a new job',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==5:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have an abnormally\n big toe',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='An abnormally big ear',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==6:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='To be naked at work\n for an hour ',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be dropped off two\n miles from your\n house whilst you are\n naked',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==7:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be three feet tall',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be Eight feet tall',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==8:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Smell like rotten\n cheese',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A hamster cage which\n has not been cleaned',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==9:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be a mad genius',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Popular but dim',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==10:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have a nose that never\n stops growing',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Ears that never stop\n growing',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==11:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Cheat on someone',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be cheated on',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==12:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have your hair pulled',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Your back scratched',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==13:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Cheat in a test',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Fail in a test',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==14:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Relive the worst part\n of your life',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Become 20 years older',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==15:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have telekinesis',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have telepathy',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==16:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Lose your sight',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Lose your memories',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==17:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Give up social media',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Eat the same dinner\n for the rest of\n your life',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==18:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have no taste',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be colorblind',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==19:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Know the date\n of your death',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Know the cause of\n your death',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==20:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Win $25,000',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have your best friend\n win $100,000',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==21:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Work a high-paying\n job that you hate',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Your dream job with\n only enough money for\n basic necessities',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==22:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Live in the\n Antarctic',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Live in the\n Sahara',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==22:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Always be 20 minutes\n late for important events',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Always be 2 hours early\n to everything else',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==23:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Talk to animals',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Speak all human\n languages',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==24:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be reborn into\n the past',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be reborn into\n the future',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==25:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be able to run\n 200 miles an hour',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be able to fly\n 20 miles an hour',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==26:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Give up your favorite\n food',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Give up phone',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==27:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Eat dinner alone\n for a year',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have to take showers\n at a public gym\n for a year',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==28:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Die before your spouse',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Die after your spouse',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==29:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Get stranded on\n Antarctica',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Get stranded in\n the desert',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==30:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Give up brushing\n your teeth',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Give up brushing\n your hair',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==31:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Never age physically',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Never age mentally',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==32:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be able to play every\n musical instrument',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Master every type\n of sport',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==33:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be a vegetarian',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Only be able to eat meat',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==34:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have no friends\n but be rich',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have lots of friends\n but be dirt poor',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==35:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Marry the person\n of your dreams',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have the job of\n your dreams',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==36:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have to spend a night\n inside an asylum full\n of crazy people',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have to spend a night\n in a haunted hotel',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==37:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have a pause button\n in your life',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A rewind button',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==38:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have your parents walk\n in on you while you\n were doing it',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Accidentally walk in on\n them doing it',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==39:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Fart out loud during\n a presentation',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Snort while laughing on\n a great first date',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==40:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Always be overdressed',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Always be underdressed',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==41:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Drown to death',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Burned to death',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==42:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Constantly itch',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be in excruciating pain\n for a whole day\n once a year',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==43:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Save 5 of the greatest\n friends you could\n ever have',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Make 5 new friends that\n pay you 20$ a month',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==44:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have uncontrollable gas\n for an entire month',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Wet yourself at work',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==45:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Make out with your\n celebrity crush',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Get paid $5,000',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==46:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Never shower again",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Never talk to anyone\n again',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==47:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Save 100% of the\nworld but not be\nrecognized",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text="Save 25% of the\nworld but be\npraised by them",font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==48:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Drink a glass of\n vomit once',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Burp every time \nsomeone says\n your name',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==49:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Wear the same pair of\n underwear for a week',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text="Wear your mother’s\n clean underwear for\n a day",font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==50:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be able to\n shapeshift',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be able to teleport',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==51:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Meet any celebritiy\n at any time',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Meet any fictional\n character once',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==52:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Live forever',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Die in the next\n five minutes',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==53:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Have everything you’ve\n ever wanted but you\n die in one year",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Live your life as\n it is now',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==54:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be an ugly genius',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A hot moron',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==55:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be filthy rich but\n suffer depression',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be poor but happy',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==56:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be a vampire',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A wizard',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==57:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be in a real version\n of The Walking Dead',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be in a real version\n of The Jurassic Park',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==58:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have 20 kids over\n the course of your\n life',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Never be able to have\n or adopt children',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==59:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Die happy in five\n years',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Die unhappy in sixty\n years',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==60:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have an interesting\n conversation',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='An interesting life',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==61:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Pick a fun way\n to die',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Never to die at all',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==62:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Eat dinner with Donald\n Trump',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Eat dinner with Hitler',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==63:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Not be able to taste\n ice cream',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Not be able to taste\n Pizza',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==64:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be asked the same\n question every\n morning',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Hear the same song\n every morning',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==65:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Wear wet socks',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Wear wet underwear',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==66:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Lose your phone',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Lose your wallet',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==67:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Watch your favorite\n television couple\n break up forever',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Recite their wedding\n vows',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==68:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Ability to heal others\nand not\nyourself',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Ability to heal\nyourself but not\nothers',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==69:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Huge tattoo of your\n partner’s name across\n your chest",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A tiny tattoo of their\n face on your arm',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==70:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Live in the same\nhouse with someone\n you hate',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Temporarily get married\n to them in Vegas',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==71:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be immune to hangovers\n forever',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Never have to go to\n the dentist ever again',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==72:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Tell someone that their\n new baby is ugly',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Tell someone that their\n spouse is ugly',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==73:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be the top dog at\n a shitty company',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be the worst employee\n at the best company\n in the world',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==74:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Never wash your sheets\n ever again',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Only be able to shower\n once every two weeks',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==75:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be absolutely adored\n by everyone',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have unlimited power',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==76:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have to permanently\n give up salts',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have to permanently\n give up sweets',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==77:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have a straight,\n flawless smile with\n super yellow teeth',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Super crooked teeth\n that are pearly white',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==78:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Post an extremely\n unflattering photo that\n gets hundreds of likes',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A super flattering photo\n that only gets one\n like in total',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==79:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have an elaborate,\n expensive wedding',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='A small, private wedding',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==80:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Find a dead body',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be a witness to\n a deadly assault',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==78:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be strong but\n look rail thin',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be weak but\n look buff',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==78:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be in love with your\n best friend',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have your best friend\n be in love with you',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==81:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Faint at your wedding',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Faint at your\n graduation',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==82:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Live without music for\n the rest of your life',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Live without movies for\n the rest of your life',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==83:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Experience life in\n slow motion',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Experience life in\n fast forward',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==84:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Never be able to go\n to anyone’s wedding\n (your own included)",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have to go to a\n funeral every day',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==85:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text="Have a dog with\n a cat’s personality",font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have a cat with\n a dog’s personality',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==86:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Continue with your life',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Restart it',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==87:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be able to talk your\n way out of any\n situation',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Punch your way out\n of any situation',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==88:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have free Wi-Fi\n wherever you go',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have free coffee\n where/whenever\n you want',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==89:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Get away with\n lying every time',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Always know that\n someone is lying',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==90:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Live in an amusement\n park',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Live in a zoo',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==91:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Visit 100 years in\n the past',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Visit 100 years in\n the future',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==92:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Sit alone in the\n house on the weekend',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Go and hang out with\n the most boring person\n in the world',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==93:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Let people read\n your mind whenever\n they want',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Let them know your\n deepest darkest\n secrets',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==94:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Want to have a\n photogenic face',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have photoshop skills',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==95:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be imprisoned for one\n year in a maximum\n security prison with\n the most hardcore\n criminals',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be imprisoned for ten\n years in a low\n security prison with\n Wall Street type of\n criminals',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==96:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Have the ability to\n watch the top 5% best\n movies only',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Only be able to watch\n the remaining 95%\n of movies',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==97:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Be known all over\n the world and\n widely mocked',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Be normal but only\n known within your\n neighborhood',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==98:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Lose the ability to\n speak or understand\n language',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Lose the ability to\n understand written\n words',font=('Comic Sans MS',40))
        B.place(x=890,y=309)
        
    elif r==99:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Your head become as\n big as a watermelon',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='As small as a tennis\n ball',font=('Comic Sans MS',40))
        B.place(x=890,y=309)

    elif r==100:
        A=tkinter.Label(MAIN_PAGE,bg="ORANGERED3",text='Spend a year in jail',font=('Comic Sans MS',40))
        A.place(x=40,y=309)
        B=tkinter.Label(MAIN_PAGE,bg="skyblue2",text='Have that year reduced\n from your life',font=('Comic Sans MS',40))
        B.place(x=890,y=309)



    randomgame.A1=A
    randomgame.B1=B





    


I_RED=PhotoImage(file="unnamedA.png")
ButtonA=tkinter.Button(MAIN_PAGE,image=I_RED,bg='ORANGERED3',borderwidth = 0,command=randomgame).place(x=16,y=169)

    
I_BLUE=PhotoImage(file="unnamedB.png")
ButtonB=tkinter.Button(MAIN_PAGE,image=I_BLUE,bg='skyblue2',borderwidth = 0,command=randomgame).place(x=883,y=169)


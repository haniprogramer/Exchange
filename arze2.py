import requests
from tkinter import *

root = Tk()
root.title('arze')
root.geometry('480x423')
root.resizable(width=False, height=False)


trackfram1=LabelFrame(root,font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white')
trackfram1.place(x=0,y=0,width=480,height=239)

trackfram2=LabelFrame(root,font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white')
trackfram2.place(x=0,y=238,width=480,height=120)

trackfram3=LabelFrame(root,font=('Arial',15,'bold'),bg='turquoise',bd=5,fg='white')
trackfram3.place(x=0,y=358,width=480,height=65)


def arze():
    x=e1.get()
    x1='http://api.navasan.tech/latest/?api_key='+ x

    response=requests.get(x1)
    res=response.json()
    y=e2.get()
    global v1
    global v2

    global v4
    y2=res[y]
    v1=str(y2['value'])
    v2=str(y2['change'])

    v4=str(y2['date'])
    global a
    global vv
    vv ='  name : '+e2.get() +'     Price :'+v1 +'     Price change : '+v2+'     Update time : '+ v4 + '\n'
    a=list1.insert(END,vv)

    with open("arz.txt", mode="a") as w:
        w.write(vv)
        w.close()


# --------LABEL----------
l1 = Label(trackfram2, text='Plese Enter Key',bg='turquoise',font=('Arial',10,'bold'))
l1.place(x=10,y=15)

l2 = Label(trackfram2, text='Plese Enter Your Data Key',bg='turquoise',font=('Arial',10,'bold'))
l2.place(x=10,y=47)

ll1 = Label(trackfram3, text='To get the key   :   https://www.navasan.tech/api/',bg='turquoise',font=('Arial',10,'bold'))
ll1.place(x=0,y=1)

l3 = Label(trackfram3, text='Send Telegram.bot : @badboys007_bot ',bg='turquoise',font=('Arial',10,'bold'))
l3.place(x=0,y=25)


# ---------Entries---------
e1 = Entry(trackfram2,width=39)
e1.place(x=220,y=15)

e2 = Entry(trackfram2,width=39)
e2.place(x=220,y=47)

# -------------------------------------------------------------------

def send_msg():
    requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", params=
    {
        "UrlBox": f"https://api.telegram.org/؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟/sendMessage?chat_id=؟؟؟؟؟؟؟؟؟؟؟؟؟؟؟={vv}&parse_mode=HTML",
    "AgentList" : "Mozilla Firefox" ,
    "MethodList" : "POST" ,

    }
                  )


# ---------------------------Button-----------------------------------

b1 = Button(trackfram2, text='Search', width=12,command=arze,bg="Sky blue")
b1.place(x=264,y=78)

b7 = Button(trackfram2, text='Close', width=12,command=root.destroy,bg="red")
b7.place(x=368,y=78)

b8 = Button(trackfram2, text='Send', width=12,command=send_msg,bg="Sky blue")
b8.place(x=159,y=78)



# -------------------------------------list--------------------------------------

list1 = Listbox(trackfram1, width=66, height=14)
list1.pack(fill=BOTH)




root.mainloop()
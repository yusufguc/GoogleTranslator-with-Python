#TranslateWithPython
from tkinter import *
from tkinter import ttk,messagebox
import googletrans
from googletrans import Translator,LANGUAGES


root=Tk()
root.title("Google Translator")
root.geometry("1080x400")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)



def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c3 = combo2.get()

        if not text_:
            messagebox.showwarning("Warning", "Please enter the text to be translated!")
            return

        if c3 == "SELECT LANGUAGE":
            messagebox.showwarning("Warning", "Please select the target language!")
            return

        translator = Translator()
        detected_lang = translator.detect(text_).lang 
        lan_ = None

        
        for lang_code, lang_name in LANGUAGES.items():
            if lang_name.lower() == c3.lower():
                lan_ = lang_code
                break

        if lan_:
            translated_text = translator.translate(text_, src=detected_lang, dest=lan_).text
            text2.delete(1.0, END)
            text2.insert(END, translated_text)
        else:
            messagebox.showerror("Error", "Selected language not found!") 

    except Exception as e:
        messagebox.showerror("Google Translate Error", f"Please try again!\nError: {e}")


#İCON(

image_icon=PhotoImage(file="C:\\Users\\uzayv\\Downloads\\icons8-translation-50.png")
root.iconphoto(False,image_icon)

#ARROW
arrow_image=PhotoImage(file="C:\\Users\\uzayv\\Downloads\\icons8-double-arrow-64.png")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)

language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 14",state="readonly")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Red",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



combo2=ttk.Combobox(root,values=languageV,font="RobotoV 14",state="readonly")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)


f1=Frame(root,bg="Red",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#Translate button 
translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground="purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()

root.configure(bg="white")
root.mainloop()

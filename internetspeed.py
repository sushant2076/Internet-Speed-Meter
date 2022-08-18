from tkinter import *
import speedtest

def speedcheck():
	sp = speedtest.Speedtest()
	sp.get_servers()
	down = str(round(sp.download()/(10**6))) + "Mbps"
	up = str(round(sp.upload()/(10**6))) + "Mbps"
	lab3.config(text=down)
	lab5.config(text=up)


sp = Tk()
sp.title("INTERNET SPEED METER")
sp.geometry("500x500")
sp.config(bg = "Blue")
lab1 = Label(sp, text="INTERNET SPEED METER", font=("Normal", 20, "bold"), bg = "Blue", fg = "White")
lab1.place(x="80",y="40", height ="50", width ="380")


lab2 = Label(sp, text="Download Speed", font=("Normal", 20, "bold"))
lab2.place(x="80",y="90", width ="360")

lab3 = Label(sp, text="0", font=("Normal", 20, "bold"))
lab3.place(x="80",y="140", width ="360" )

lab4 = Label(sp, text="Upload Speed", font=("Normal", 20, "bold"))
lab4.place(x="80",y="190", width ="360")

lab5 = Label(sp, text="0", font=("Normal", 20, "bold"))
lab5.place(x="80",y="240", width ="360")

button = Button(sp, text= "CHECK SPEED", font = ("Normal", 20, "bold"), relief = RAISED, bg = "Yellow", command = speedcheck)
button.place(x="80",y="300", width ="360")

sp.mainloop() #creates window
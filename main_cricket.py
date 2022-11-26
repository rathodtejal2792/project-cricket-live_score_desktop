from tkinter import *
import tkinter as tk
from turtle import width
from boto import BUCKET_NAME_RE
import mysql.connector
import tkinter.messagebox as tmsg
from tkinter import ttk

mydb = mysql.connector.connect(
    host="localhost", user="root", password="Shailesh@2701", database="cricket")
mycursor = mydb.cursor()

root = Tk()
root.geometry("1000x1000")
root.minsize(300, 300)

root.wm_iconbitmap("board.ico")
root.title("WININD")

can1 = Canvas(root, width=700, height=700)
can1.grid(row=0, column=0)

scroll = Scrollbar(root)
scroll.grid(row=700, column=800)
scroll.config(command=can1.yview)
can1.config(yscrollcommand=scroll.set)

image1 = PhotoImage(file="cricket_PNG12.png")
can1.create_image(400, 420, image=image1)

image3 = PhotoImage(file="logo_lab.png")
lab4 = Label(root, image=image3, height=100, width=300)
lab4.place(x=570, y=00)

image2 = PhotoImage(file="username.png")
lab4 = Label(root, image=image2, height=200, width=300)
lab4.place(x=650, y=150)

lab2 = Label(root, text="Email", font=("bold", 10))
lab2.place(x=600, y=350)

lab3 = Label(root, text="Password", font=("bold", 10))
lab3.place(x=600, y=400)

mail = StringVar()
passw = StringVar()
ent1 = Entry(root, textvariable=mail, width=33)
ent1.place(x=700, y=350)

ent1 = Entry(root, textvariable=passw, show="*" ,width=33)
ent1.place(x=700, y=400)


def signup():

    mycursor.execute("select mail from login_data")
    result = mycursor.fetchall()
    print(result)
    new_result = []
    print(" i am for git hub ")
    

    for m in result:
        new_result.append(m[0])
    print(new_result)

    new_mail = mail.get()

    if new_mail in new_result:
        tmsg.showinfo(
            "Login", "Kindly use other mail , this mail already in use")
    else:
        mycursor.execute(
            "insert into login_data(mail,password) values(%s,%s)", (mail.get(), passw.get()))
        mydb.commit()
        value = tmsg.showinfo("Success", "Registerd Successfull ")
        home_page()
        # chk=tmsg.showinfo("Again","Kindly Login")


def home_page():
    global child

    home = tk.Toplevel()
    home.wm_iconbitmap("board.ico")
    home.geometry("570x500")
    home.maxsize(600, 500)
    home.title("WININD")
    fondov = tk.PhotoImage(file="pngwing.png")
    label2 = tk.Label(home, image=fondov)
    label2.image = fondov
    label2.place(x=0, y=0)

    def feature_match():

        past = tk.Toplevel()
        past.wm_iconbitmap("board.ico")
        past.geometry("1000x1000")
        past.title("FEATURE-WININD")
        fondov_p = tk.PhotoImage(file="past_1.png")
        label2_p = tk.Label(past, image=fondov_p)
        label2_p.image = fondov_p
        label2_p.place(x=0, y=0)

        def myfun(x):
            print("my number is ",x)
            
            mycursor.execute("select team1,team2,toss_winner from tornament where srno={tab} group by srno".format(tab=x))
            all_p = mycursor.fetchall()
            col1_p = all_p[0][0]
            col2_p = all_p[0][1]
            col3_p = all_p[0][2]
            

            team1_label_p = Label(label2_p, text=col1_p,fg="blue")
            team1_label_p.place(x=250, y=220)

            won_label_p2= Label(label2_p, text=col3_p ,bg="blue",fg="orange")
            won_label_p2.place(x=400, y=220)

            team2_label_p2 = Label(label2_p, text=col2_p,fg="blue")
            team2_label_p2.place(x=650, y=220)
            
            mytree_past = ttk.Treeview(label2_p, selectmode="browse")
            s = ttk.Style(past)
            s.theme_use("clam")
            s.configure(".", font=("Helvetica", 11))  # give font
            s.configure("Treeview.Heading", foreground="red", font=(
                "Helvetic", 11, "bold"), width=300)   # give font heading

            mytree_past.place(x=250, y=250)

            mytree_past["show"] = "headings"  # to delete extra empty row
            mytree_past["columns"] = ("1", "2", "3")
            mytree_past.column("1", width=30, anchor="c")
            mytree_past.column("2", width=100, anchor="c")
            mytree_past.column("3", width=50, anchor="c")

            mytree_past.heading("1", text="Name.", anchor="c")
            mytree_past.heading("2", text="Runs", anchor="c")
            mytree_past.heading("3", text="Balls", anchor="c")

            mytree_past2 = ttk.Treeview(label2_p, selectmode="browse")
            s = ttk.Style(past)
            s.theme_use("clam")
            s.configure(".", font=("Helvetica", 11))  # give font
            s.configure("Treeview.Heading", foreground="red", font=("Helvetic", 11, "bold"), width=300)   # give font heading
            mytree_past2.place(x=650, y=250)

            mytree_past2["show"] = "headings"  # to delete extra empty row
            mytree_past2["columns"] = ("1", "2", "3")
            mytree_past2.column("1", width=30, anchor="c")
            mytree_past2.column("2", width=100, anchor="c")
            mytree_past2.column("3", width=50, anchor="c")

            mytree_past2.heading("1", text="Name.", anchor="c")
            mytree_past2.heading("2", text="Runs", anchor="c")
            mytree_past2.heading("3", text="Balls", anchor="c")


            mycursor.execute("select team1_name,sum(team1_run),sum(team1_ball) from tornament where srno={tab} and team1_name is not null group by team1_name".format(tab=x))
            result_past = mycursor.fetchall()
            print(result_past)
            runs_p = 0
            balls_p = 0
            for data in result_past:
                print(data)
                mytree_past.insert("", 'end', iid=data[0], values=(data[0], data[1], data[2]))
                runs_p = runs_p+data[1]
                balls_p = balls_p+data[2]

            print("runs:", runs_p)
            print("balls:", balls_p)
            print("over:", int(balls_p/6))
#--------------------------------------------
            mycursor.execute("select sum(coalesce(extra1,0)),sum(coalesce(out11,0)) from tornament where srno={tab}".format(tab=x))
            ex_ot_p1 = mycursor.fetchall()
            print("i am total",ex_ot_p1)
            
            ex_p = ex_ot_p1[0][0]
            ot_p= ex_ot_p1[0][1]
            total_run = ex_p+runs_p

            total_run_p = "Runs: "+str(total_run)+"/"+str(ot_p)
            run_label_p= Label(label2_p, text=total_run_p, width=20)
            run_label_p.place(x=250, y=500)

            #----------------------------------------------
            to_p=0
            for i in range (1,int(balls_p+1)):
                to_p=to_p+0.1

                a_p=str(round(to_p,1))
                print(a_p)
                if str(a_p[-1])=="6":
                    to_p=int(to_p)+1
    


            print("hello",round(to_p,1))


            #-----------------------------------------------------------


            total_ball_p= "Balls: " + str(balls_p)+" ("+str(round(to_p, 1))+" Overs)"
            ball_label_p= Label(label2_p, text=total_ball_p, width=20)
            ball_label_p.place(x=250, y=520)

            ext_run_p= "Extra Runs: "+str(ex_p)
            ext_label_p = Label(label2_p, text=ext_run_p, width=20)
            ext_label_p.place(x=250, y=550)

#------------------------------------------
            
            mycursor.execute("select team2_name,sum(team2_run),sum(team2_ball) from tornament where srno={tab} and team2_name is not null group by team2_name".format(tab=x))
            result_past2 = mycursor.fetchall()
            print(result_past2)


            runs_p2 = 0
            balls_p2 = 0
            for data in result_past2:
                print(data)
                mytree_past2.insert("", 'end', iid=data[0], values=(data[0], data[1], data[2]))
                runs_p2= runs_p2+data[1]
                balls_p2 = balls_p2+data[2]

            print("runs:", runs_p2)
            print("balls:", balls_p2)
            print("over:", int(balls_p2/6))

#***************************************************************

            mycursor.execute("select sum(coalesce(extra2,0)),sum(coalesce(out2,0)) from tornament where srno={tab}".format(tab=x))
            ex_ot_p2 = mycursor.fetchall()
            print(ex_ot_p2)
            ex_p2 = ex_ot_p2[0][0]
            ot_p2 = ex_ot_p2[0][1]

            total_run_p2 = ex_p2+runs_p2

           
            total_run_lab_p2 = "Runs: "+str(total_run_p2)+"/"+str(ot_p2)
            run_labelp2 = Label(label2_p, text=total_run_lab_p2, width=20)
            run_labelp2.place(x=650, y=500)

 #----------------------------------------------
            to_p2=0
            for i in range (1,int(balls_p2+1)):
                to_p2=to_p2+0.1

                a_p2=str(round(to_p2,1))
                print(a_p2)
                if str(a_p2[-1])=="6":
                    to_p2=int(to_p2)+1
    


            print("hello",round(to_p2,1))


            #-----------------------------------------------------------


            total_ball2_p = "Balls: " + str(balls_p2)+" ("+str(round(to_p2, 1))+" Overs)"
            ball_label2p = Label(label2_p, text=total_ball2_p, width=20)
            ball_label2p.place(x=650, y=520)

            ext_runp2 = "Extra Runs: "+str(ex_p2)
            ext_labelp2 = Label(label2_p, text=ext_runp2, width=20)
            ext_labelp2.place(x=650, y=550)


#*********************************************************************************

       

            '''
            hsb_p = ttk.Scrollbar(past, orient="vertical")
            hsb_p.configure(command=mytree_past.yview)
            mytree_past.configure(yscrollcommand=hsb_p.set)
            hsb_p.grid(sticky="we")

            hsb_p2 = ttk.Scrollbar(past, orient="vertical")
            hsb_p2.configure(command=mytree_past.yview)
            mytree_past2.configure(yscrollcommand=hsb_p.set)
            hsb_p2.grid(sticky="we")'''

            mycursor.execute(" select match_winner from tornament  where srno ={tab} and match_winner is not null group by match_winner".format(tab=x))
            matchwin_fea = mycursor.fetchall()
            print(matchwin_fea[0][0])
            
            if matchwin_fea[0][0]=="NULL":
                ''
                
            else:
                today_match_winner = Label(label2_p, text=matchwin_fea[0][0], width=50,bg="blue",height=5,fg="white")
                today_match_winner.place(x=300, y=600)
            
        mycursor.execute("select match_date,team1,team2,srno from tornament where srno is not null group by srno ")
        group = mycursor.fetchall()
        print("group:", group)
        i = 200
        for pair in group:
            
            but_name = str(pair[0])+" "+pair[1]+" Vs "+pair[2]
            but=Button(past, text=but_name, command=lambda k=pair[3]: myfun(k))
            but.place(x=40, y=i)
            print("but1")
            i = i+40
           
           

        past.mainloop()

    def live_match():

        live = tk.Toplevel()
        live.wm_iconbitmap("board.ico")
        live.geometry("1000x1000")

        live.title("LIVE-WININD")
        fondov1 = tk.PhotoImage(file="live.png")
        label_live = tk.Label(live, image=fondov1)
        label_live.image = fondov1
        label_live.place(x=0, y=0)

        

        def Today_live():
            mycursor.execute("select *from tosswon")
            all = mycursor.fetchall()
            col1 = all[0][0]
            col2 = all[0][1]
            col3 = all[0][2]
            col4 = all[0][3]

            team1_label = Label(live, text=col2)
            team1_label.place(x=200, y=230)

            won_label = Label(live, text=col4 ,bg="blue",fg="orange")
            won_label.place(x=480, y=200)

            team2_label = Label(live, text=col3)
            team2_label.place(x=700, y=230)

            mytree1 = ttk.Treeview(label_live, selectmode="browse")

            t = ttk.Style(label_live)
            t.theme_use("clam")
            t.configure(".", font=("Helvetica", 11))  # give font
            t.configure("Treeview.Heading", foreground="red", font=(
                "Helvetic", 11, "bold"), width=300)   # give font heading

            mytree1.place(x=200, y=250)

            mytree1["columns"] = ("1", "2", "3")
            mytree1["show"] = "headings"  # to delete extra empty row
            mytree1.column("1", width=100, anchor="c")
            mytree1.column("2", width=100, anchor="c")
            mytree1.column("3", width=50, anchor="c")

            mytree1.heading("1", text="Name", anchor="c")
            mytree1.heading("2", text="Run", anchor="c")
            mytree1.heading("3", text="Balls", anchor="c")


            mytree2 = ttk.Treeview(label_live, selectmode="browse")
            mytree2.place(x=700, y=250)

            mytree2["columns"] = ("1", "2", "3")
            mytree2["show"] = "headings"  # to delete extra empty row
            mytree2.column("1", width=100, anchor="c")
            mytree2.column("2", width=100, anchor="c")
            mytree2.column("3", width=50, anchor="c")

            mytree2.heading("1", text="Name", anchor="c")
            mytree2.heading("2", text="Run", anchor="c")
            mytree2.heading("3", text="Balls", anchor="c")



            '''hsb1 = ttk.Scrollbar(live, orient="vertical")
            hsb1.configure(command=mytree1.yview)
            mytree1.configure(yscrollcommand=hsb1.set)
            hsb1.grid(sticky="we")'''

            mycursor.execute("select team1_name,sum(coalesce(team1_run,0)),sum(coalesce(team1_ball,0)) from tornament where srno={tab} and team1_name is not null group by team1_name".format(tab=col1))
            result = mycursor.fetchall()
            print(result)

            
            runs = 0
            balls = 0
            for data in result:
                print(data)
                mytree1.insert("", 'end', iid=data[0], values=(
                    data[0], data[1], data[2]))
                runs = runs+data[1]
                balls = balls+data[2]

            print("runs:", runs)
            print("balls:", balls)
            

            mycursor.execute("select sum(coalesce(extra1,0)),sum(coalesce(out11,0)) from tornament where srno={tab}".format(tab=col1))
            ex_ot = mycursor.fetchall()
            print("i am total",ex_ot)
            
            ex = ex_ot[0][0]
            ot = ex_ot[0][1]
            total_run = ex+runs

            total_run = "Runs: "+str(total_run)+"/"+str(ot)
            run_label = Label(label_live, text=total_run, width=20)
            run_label.place(x=250, y=500)

            print("ballss:",balls)
            #-------------------------
    
            to=0
            for i in range (1,int(balls+1)):
                to=to+0.1

                a=str(round(to,1))
                print(a)
                if str(a[-1])=="6":
                    to=int(to)+1
    


            print("hello",round(to,1))
            

            #---------------------------
            
            total_ball = "Balls: " + str(balls)+" ("+str(round(to, 1))+" Overs)"
            ball_label = Label(label_live, text=total_ball, width=20)
            ball_label.place(x=250, y=520)

            ext_run = "Extra Runs: "+str(ex)
            ext_label = Label(label_live, text=ext_run, width=20)
            ext_label.place(x=250, y=550)

            
            
            
            '''hsb2 = ttk.Scrollbar(live, orient="vertical")
            hsb2.configure(command=mytree2.yview)
            mytree2.configure(yscrollcommand=hsb2.set)
            hsb2.grid(sticky="we")'''
            
            

            mycursor.execute(
                "select team2_name,sum(coalesce(team2_run,0)),sum(coalesce(team2_ball,0)) from tornament where srno={tab} and team2_name is not null group by team2_name".format(tab=col1))
            result2 = mycursor.fetchall()
            print(result2)

            runs2 = 0
            balls2 = 0
            for data in result2:
                print(data)
                mytree2.insert("", 'end', iid=data[0], values=(
                    data[0], data[1], data[2]))
                runs2 = runs2+data[1]
                balls2 = balls2+data[2]

            print("runs:", runs2)
            print("balls:", balls2)
            print("over:", int(balls2/6))
 
            mycursor.execute("select sum(coalesce(extra2,0)),sum(coalesce(out2,0)) from tornament where srno={tab}".format(tab=col1))
            ex_ot2 = mycursor.fetchall()
            print(ex_ot2)
            ex2 = ex_ot2[0][0]
            ot2 = ex_ot2[0][1]

            total_run2 = ex2+runs2

           
            total_run22 = "Runs: "+str(total_run2)+"/"+str(ot2)
            run_label2 = Label(label_live, text=total_run22, width=20)
            run_label2.place(x=700, y=500)

            #---------------------------------
            to2=0
            for i in range (1,int(balls2+1)):
                to2=to2+0.1

                a2=str(round(to2,1))
                print(a2)
                if str(a2[-1])=="6":
                    to2=int(to2)+1

            #-----------------------------------

            total_ball2 = "Balls: " + \
                str(balls2)+" ("+str(round(to2, 1))+" Overs)"
            ball_label2 = Label(label_live, text=total_ball2, width=20)
            ball_label2.place(x=700, y=520)

            ext_run2 = "Extra Runs: "+str(ex2)
            ext_label2 = Label(label_live, text=ext_run2, width=20)
            ext_label2.place(x=700, y=550)

            mycursor.execute(" select match_winner from tornament  where srno ={tab} and match_winner is not null group by match_winner".format(tab=col1))
            matchwin = mycursor.fetchall()
            print(matchwin[0][0])
            
            if matchwin[0][0]=="NULL":
                ''
            else:
                today_match_winner = Label(label_live, text=matchwin[0][0], width=50,bg="yellow")
                today_match_winner.place(x=400, y=600)
            


        mycursor.execute("select team1,team2 from tosswon")
        two_team = mycursor.fetchall()
        print(two_team)
        first_team = two_team[0][0]+" Vs "+two_team[0][1]
        print(first_team)
        child_but1 = Button(live, text=first_team,width=30, command=Today_live)
        child_but1.place(x=40, y=150)



        live.mainloop()

    def future_match():
        
        future = tk.Toplevel()
        future.wm_iconbitmap("board.ico")
        future.geometry("1000x1000")

        future.title("UPCOMING MATCHES-WININD")
        fondovf = tk.PhotoImage(file="past2.png")
        label_future = tk.Label(future, image=fondovf)
        label_future.image = fondovf
        label_future.place(x=0, y=0)

        tit_srno=Label(label_future,text="SRNO",bg="blue",fg="white",width=6,height=2)
        tit_srno.place(x=150,y=185)
        
        tit_date=Label(label_future,text="DATE , TIME",bg="blue",fg="white",width=20,height=2)
        tit_date.place(x=200,y=185)

        tit_team1=Label(label_future,text="TEAMS",bg="blue",fg="white",width=34,height=2)
        tit_team1.place(x=350,y=185)
        
        tit_venue=Label(label_future,text="VENUE",bg="blue",fg="white",width=34,height=2)
        tit_venue.place(x=600,y=185)
        
        mycursor.execute("select srno,date_time,team1,team2,venue from upcoming_match")
        fu_group = mycursor.fetchall()
        print("group:", fu_group)
        i = 220
        for pair in fu_group:
            
            team_name_fu = pair[2]+" Vs "+pair[3]
            srno_lab=Label(label_future, text=pair[0],width=6,height=2,bg="cyan")
            srno_lab.place(x=150, y=i)

            date_lab=Label(label_future, text=pair[1],width=20,height=2,bg="cyan")
            date_lab.place(x=200, y=i)

            team_lab=Label(label_future, text=team_name_fu,width=34,height=2,bg="cyan")
            team_lab.place(x=350, y=i)
    
            venue_lab=Label(label_future, text=pair[4],width=34,height=2,bg="cyan")
            venue_lab.place(x=600, y=i)

            i = i+40


        future.mainloop()

    child_but1 = Button(home, text="FEATURED MATCH",
                        width=30, command=feature_match)
    child_but1.place(x=40, y=150)

    child_but2 = Button(home, text="LIVE MATCH", width=30, command=live_match)
    child_but2.place(x=40, y=200)

    child_but3 = Button(home, text="UPCOMING MATCH",
                        width=30, command=future_match)
    child_but3.place(x=40, y=250)

    home.mainloop()


def admin():
    global Team1
    admin_data = tk.Toplevel()
    admin_data.geometry("1000x1000")
    admin_data.wm_iconbitmap("board.ico")
    admin_data.title("ADMIN-WININD")

    def toss_update():

        print(Team1.get(), Team2.get(), tosswon.get())
        # team1=Team1.get()
        # team2=Team2.get()
        match_name = tosswon.get()
        mycursor.execute("truncate table tosswon")
        mycursor.execute("insert into tosswon(srno,team1,team2,winner) values(%s,%s,%s,%s)",
                         (match_no.get(), Team1.get(), Team2.get(), match_name))
        mydb.commit()

        wonn = tosswon.get()
        mycursor.execute("insert into tornament(match_date,srno,team1, team2, toss_winner) values(%s,%s,%s,%s,%s)",
                         (match_date.get(),match_no.get(), Team1.get(), Team2.get(), wonn))
        mydb.commit()



    match_date = StringVar()
    match_date.set("dd/mm/yyyy")
    match = Label(admin_data, text="Match date:")
    match.place(x=250, y=10)
    match_box = Entry(admin_data, textvariable=match_date, width=20)
    match_box.place(x=350, y=10)

    match_no = IntVar()
    match = Label(admin_data, text="Match No:")
    match.place(x=250, y=30)
    match_box = Entry(admin_data, textvariable=match_no, width=20)
    match_box.place(x=350, y=30)

    Team1 = StringVar()
    team1 = Label(admin_data, text="Team1:")
    team1.place(x=10, y=10)
    team_box = Entry(admin_data, textvariable=Team1)
    team_box.place(x=80, y=10)

    Team2 = StringVar()
    team2 = Label(admin_data, text="Team2:")
    team2.place(x=550, y=10)
    team_box2 = Entry(admin_data, textvariable=Team2)
    team_box2.place(x=650, y=10)

    tosswon = StringVar()
    toss = Label(admin_data, text="Toss Won")
    toss.place(x=250, y=50)
    toss_box = Entry(admin_data, textvariable=tosswon)
    toss_box.place(x=350, y=50)

    update1 = Button(admin_data, text="Update", command=toss_update)
    update1.place(x=300, y=70)

    vs = Label(admin_data, text="VS")
    vs.place(x=500, y=10)

    play1 = StringVar()
    run1 = IntVar()
    ball1 = IntVar()

    player1 = Label(admin_data, text="Player1:", bg="red")
    player1.place(x=10, y=50)
    player_box1 = Entry(admin_data, textvariable=play1)
    player_box1.place(x=80, y=50)

    play_run1 = Label(admin_data, text="Player1 Run:", bg="red")
    play_run1.place(x=10, y=90)
    play_run_box1 = Entry(admin_data, textvariable=run1)
    play_run_box1.place(x=80, y=90)

    play_ball1 = Label(admin_data, text="Player1 ball:", bg="red")
    play_ball1.place(x=10, y=130)
    play_ball_box1 = Entry(admin_data, textvariable=ball1)
    play_ball_box1.place(x=80, y=130)

    def player1_update():
        print(play1.get(), run1.get(), ball1.get())

        mycursor.execute("insert into tornament(srno,team1,team1_name,team1_run,team1_ball) values(%s,%s,%s,%s,%s)",
                         (match_no.get(), Team1.get(), play1.get(), run1.get(), ball1.get()))
        mydb.commit()
    play1_up = Button(admin_data, text="Player1-Update",
                      command=player1_update)
    play1_up.place(x=220, y=130)

    # player 2

    play2 = StringVar()
    run2 = IntVar()
    ball2 = IntVar()

    player2 = Label(admin_data, text="Player2:", bg="yellow")
    player2.place(x=10, y=170)
    player_box2 = Entry(admin_data, textvariable=play2)
    player_box2.place(x=80, y=170)

    play_run2 = Label(admin_data, text="Player2 Run:", bg="yellow")
    play_run2.place(x=10, y=210)
    play_run_box2 = Entry(admin_data, textvariable=run2)
    play_run_box2.place(x=80, y=210)

    play_ball2 = Label(admin_data, text="Player2 ball:", bg="yellow")
    play_ball2.place(x=10, y=250)
    play_ball_box2 = Entry(admin_data, textvariable=ball2)
    play_ball_box2.place(x=80, y=250)

    def player2_update():
        print(play2.get(), run2.get(), ball2.get())
        mycursor.execute("insert into tornament(srno,team1,team1_name,team1_run,team1_ball) values(%s,%s,%s,%s,%s)",
                         (match_no.get(), Team1.get(), play2.get(), run2.get(), ball2.get()))
        mydb.commit()

    play2_up = Button(admin_data, text="Player2-Update",
                      command=player2_update)
    play2_up.place(x=220, y=250)

    extra_run = IntVar()
    extra_run.set(0)
    extra_run = Label(admin_data, text="Extra Runs:")
    extra_run.place(x=10, y=290)
    extra_run = Entry(admin_data, textvariable=extra_run)
    extra_run.place(x=80, y=290)

    def extra1_run():
        print(extra_run.get())
        mycursor.execute("insert into tornament(srno,team1,extra1) values(%s,%s,%s)",
                         (match_no.get(), Team1.get(), extra_run.get()))
        mydb.commit()
    extra1 = Button(admin_data, text="Extra Team1", command=extra1_run)
    extra1.place(x=220, y=290)

    out1 = IntVar()
    out1.set(0)
    out_lab1 = Label(admin_data, text="out:")
    out_lab1.place(x=10, y=350)
    out_ent1 = Entry(admin_data, textvariable=out1)
    out_ent1.place(x=80, y=350)

    def call_out1():
        print(out1.get())
        mycursor.execute("insert into tornament(srno,team1,out11) values(%s,%s,%s)",
                         (match_no.get(), Team1.get(), out1.get()))
        mydb.commit()

    out2_but = Button(admin_data, text="out1", command=call_out1)
    out2_but.place(x=220, y=350)

    play21 = StringVar()
    run21 = IntVar()
    ball21 = IntVar()

    player21 = Label(admin_data, text="Player1:", bg="red")
    player21.place(x=550, y=50)
    player_box21 = Entry(admin_data, textvariable=play21)
    player_box21.place(x=650, y=50)

    play_run21 = Label(admin_data, text="Player1 Run:", bg="red")
    play_run21.place(x=550, y=90)
    play_run_box21 = Entry(admin_data, textvariable=run21)
    play_run_box21.place(x=650, y=90)

    play_ball21 = Label(admin_data, text="Player1 ball:", bg="red")
    play_ball21.place(x=550, y=130)
    play_ball_box21 = Entry(admin_data, textvariable=ball21)
    play_ball_box21.place(x=650, y=130)

    def player21_update():
        print(play21.get(), run21.get(), ball21.get())
        mycursor.execute("insert into tornament(srno,team2,team2_name,team2_run,team2_ball) values(%s,%s,%s,%s,%s)",
                         (match_no.get(), Team2.get(), play21.get(), run21.get(), ball21.get()))
        mydb.commit()

    play21_up = Button(admin_data, text="Player1-Update",
                       command=player21_update)
    play21_up.place(x=800, y=130)

    play22 = StringVar()
    run22 = IntVar()
    ball22 = IntVar()

    player22 = Label(admin_data, text="Player2:", bg="yellow")
    player22.place(x=550, y=170)
    player_box2 = Entry(admin_data, textvariable=play22)
    player_box2.place(x=650, y=170)

    play_run22 = Label(admin_data, text="Player2 Run:", bg="yellow")
    play_run22.place(x=550, y=210)
    play_run_box22 = Entry(admin_data, textvariable=run22)
    play_run_box22.place(x=650, y=210)

    play_ball22 = Label(admin_data, text="Player2 ball:", bg="yellow")
    play_ball22.place(x=550, y=250)
    play_ball_box22 = Entry(admin_data, textvariable=ball22)
    play_ball_box22.place(x=650, y=250)

    def player22_update():
        mycursor.execute("insert into tornament(srno,team2,team2_name,team2_run,team2_ball) values(%s,%s,%s,%s,%s)",
                         (match_no.get(), Team2.get(), play22.get(), run22.get(), ball22.get()))
        mydb.commit()
        print(play22.get(), run22.get(), ball22.get())

    play22_up = Button(admin_data, text="Player2-Update",
                       command=player22_update)
    play22_up.place(x=800, y=250)

    # extra run team2
    extra_run2 = IntVar()
    extra_lab2 = Label(admin_data, text="Extra Runs:")
    extra_lab2.place(x=550, y=290)
    extra_ent2 = Entry(admin_data, textvariable=extra_run2)
    extra_ent2.place(x=650, y=290)

    def extra2():
        print(extra_run2.get())
        mycursor.execute("insert into tornament(srno,team2,extra2) values(%s,%s,%s)",
                         (match_no.get(), Team1.get(), extra_run2.get()))
        mydb.commit()

    extra_but2 = Button(admin_data, text="Extra Team2", command=extra2)
    extra_but2.place(x=800, y=290)

    out2 = IntVar()
    out_lab2 = Label(admin_data, text="out:")
    out_lab2.place(x=550, y=350)
    out_ent2 = Entry(admin_data, textvariable=out2)
    out_ent2.place(x=650, y=350)

    def call_out2():
        print(out2.get())
        mycursor.execute("insert into tornament(srno,team2,out2) values(%s,%s,%s)",
                         (match_no.get(), Team2.get(), out2.get()))
        mydb.commit()

    out2_but = Button(admin_data, text="out2", command=call_out2)
    out2_but.place(x=800, y=350)


    
    match_win = StringVar()
    match_win_lab = Label(admin_data, text="Match Winner")
    match_win_lab.place(x=250, y=450)
    match_win_ent = Entry(admin_data, textvariable=match_win)
    match_win_ent.place(x=350, y=450)
    
    def match_winner():
        print(match_win.get())
        mycursor.execute("insert into tornament(srno,team1,team2,match_winner) values(%s,%s,%s,%s)",
                         (match_no.get(), Team1.get(), Team2.get(),match_win.get()))
        mydb.commit()
        

    match_win_but = Button(admin_data, text="winner", command=match_winner)
    match_win_but.place(x=500, y=450)

    fu_match= Label(admin_data, text="*****UPCOMING MATCHES*****",bg="blue",fg="white",width=140)
    fu_match.place(x=10, y=550)

    fu_srno= Label(admin_data, text="Match No.:")
    fu_srno.place(x=10, y=600)
    fu_match_no=StringVar()
    fu_ent_srno = Entry(admin_data, textvariable=fu_match_no)
    fu_ent_srno.place(x=80, y=600)

    fu_date= Label(admin_data, text="Match Dt.& Time:")
    fu_date.place(x=260, y=600)
    fu_match_date=StringVar()
    fu_match_date.set("dd/mm/yyyy 00:00:00 am/pm")
    fu_ent_date = Entry(admin_data, textvariable=fu_match_date)
    fu_ent_date.place(x=360, y=600)

    fu_venu= Label(admin_data, text="Venue:")
    fu_venu.place(x=550, y=600)
    fu_match_venue=StringVar()
    fu_ent_venue= Entry(admin_data, textvariable=fu_match_venue)
    fu_ent_venue.place(x=600, y=600)

    fu_team1= Label(admin_data, text="Team1:")
    fu_team1.place(x=10, y=650)
    fu_match_team1=StringVar()
    fu_ent_team1= Entry(admin_data, textvariable=fu_match_team1)
    fu_ent_team1.place(x=80, y=650)

    fu_team2= Label(admin_data, text="Team2:")
    fu_team2.place(x=260, y=650)
    fu_match_team2=StringVar()
    fu_ent_team2= Entry(admin_data, textvariable=fu_match_team2)
    fu_ent_team2.place(x=360, y=650)

    def upcoming_match():

        mycursor.execute("insert into upcoming_match(srno,date_time,team1,team2,venue) values(%s,%s,%s,%s,%s)",(fu_match_no.get(),fu_match_date.get(), fu_match_team1.get(), fu_match_team2.get(),fu_match_venue.get()))
        mydb.commit()
        
        
    fu_match_up = Button(admin_data, text="update", command=upcoming_match)
    fu_match_up.place(x=550, y=650)


    admin_data.mainloop()


def admin_login():
    mycursor.execute("select mail, password from admin_data")
    answer = mycursor.fetchall()
    print(answer)

    new_mail = (mail.get(), passw.get())

    if new_mail in answer:
        a = tmsg.showinfo("Success", "Successful login")
        admin()
    else:
        tmsg.showinfo("Not Admin", " Email/Password is Invalid")


def login():

    mycursor.execute("select mail, password from login_data")
    answer = mycursor.fetchall()
    print(answer)

    new_mail = (mail.get(), passw.get())

    if new_mail in answer:
        a = tmsg.showinfo("Success", "Successful login")
        home_page()
    else:
        tmsg.showinfo("Not Register",
                      "This mail is not register Or Email/Password is Invalid")


button1 = Button(text="Sign Up", width=5, command=signup)
button1.place(x=700, y=450)

button2 = Button(text="Login", width=5, command=login)
button2.place(x=750, y=450)

button3 = Button(text="Admin", width=5, command=admin_login)
button3.place(x=950, y=0)

root.mainloop()

from tkinter import *

########################## INCIO DA TABELA SAC ################################
def btcS():
    janela = Tk()

    v = float(valor.get())
    p = int(parcela.get())
    tx = float(taxa.get())
    t = (tx / 100)
    amor = v / p
    jt=0;


    for j in range(1, p + 1):

        nparcelas=Label(janela,text=(j))
        nparcelas.place(x=93, y=45+30*j)


        vj = v * t
        vjuros = Label(janela, text="R$")
        vjuros.place(x=585 - 30, y=45 + 30 * j)
        vjuros = Label(janela, text=(round(vj,2)))
        vjuros.place(x=585, y=45 + 30 * j)


        vamor = Label(janela, text="R$")
        vamor.place(x=430 - 30, y=45 + 30 * j)
        vamor = Label(janela, text=(round(amor,2)))
        vamor.place(x=430, y=45 + 30 * j)


        pre = amor + vj
        valpres = Label(janela, text="R$")
        valpres.place(x=248-30, y=45 + 30 * j)
        valpres = Label(janela, text=(round(pre,2)))
        valpres.place(x=248, y=45 + 30 * j)


        saldodev = v - amor
        sdev = Label(janela, text="R$")
        sdev.place(x=736 - 30, y=45 + 30 * j)
        sdev = Label(janela, text=(round(saldodev,2)))
        sdev.place(x=736, y=45 + 30 * j)

        jt+=vj
        v = saldodev



    esc = Label(janela, text="SAC ",font="Arial 20")
    esc.place(x=407, y=5)


    totalpago = Label(janela, text="Juros totais pagos:  R$",font="Arial 12")
    totalpago.place(x=607, y=8)
    totalpago = Label(janela, text=(round(jt,2)),fg="red",font="Arial 11")
    totalpago.place(x=770, y=8)


    par = Label(janela, text="Parcela: ")
    par.place(x=80, y=50)


    vpr = Label(janela, text="Valor da prestação: ")
    vpr.place(x=210, y=50)


    amo = Label(janela, text="Amortização: ")
    amo.place(x=400, y=50)


    jr = Label(janela, text="Juros: ")
    jr.place(x=573, y=50)


    sd = Label(janela, text="Saldo devedor: ")
    sd.place(x=700, y=50)


    janela.geometry("900x600+250+50")
    janela.mainloop()


################# FIM DA JANELA SAC #####################


################# INCIO DA JANELA PRICE #################


def btcP():
    janela = Tk()

    v = float(valor.get())
    p = int(parcela.get())
    tx = float(taxa.get())
    t = (tx / 100)
    pm = v / ((1 + t) ** p - 1) * ((1 + t) ** p * t)
    jt=0

    for j in range(1, p + 1):

        nparcelas = Label(janela, text=(j))
        nparcelas.place(x=93, y=45 + 30 * j)

        vj = v * t
        vjuros = Label(janela, text="R$")
        vjuros.place(x=585 - 30, y=45 + 30 * j)
        vjuros = Label(janela, text=(round(vj, 2)))
        vjuros.place(x=585, y=45 + 30 * j)


        valpres = Label(janela, text="R$")
        valpres.place(x=248 - 30, y=45 + 30 * j)
        valpres = Label(janela, text=(round(pm, 2)))
        valpres.place(x=248, y=45 + 30 * j)


        amo = pm - v * t
        vamor = Label(janela, text="R$")
        vamor.place(x=430 - 30, y=45 + 30 * j)
        vamor = Label(janela, text=(round(amo, 2)))
        vamor.place(x=430, y=45 + 30 * j)


        saldodev = v - amo
        sdev = Label(janela, text="R$")
        sdev.place(x=736 - 30, y=45 + 30 * j)
        sdev = Label(janela, text=(round(saldodev, 2)))
        sdev.place(x=736, y=45 + 30 * j)


        jt += vj
        v = saldodev


    esc = Label(janela, text="PRICE",font="Arial 20")
    esc.place(x=394, y=5)

    totalpago = Label(janela, text="Juros totais pagos:  R$", font="Arial 12")
    totalpago.place(x=607, y=8)
    totalpago = Label(janela, text=(round(jt, 2)), fg="red", font="Arial 11")
    totalpago.place(x=770, y=8)


    par = Label(janela, text="Parcela: ")
    par.place(x=80, y=50)

    vpr = Label(janela, text="Valor da prestação: ")
    vpr.place(x=210, y=50)

    amo = Label(janela, text="Amortização: ")
    amo.place(x=400, y=50)

    jr = Label(janela, text="Juros: ")
    jr.place(x=573, y=50)

    sd = Label(janela, text="Saldo devedor: ")
    sd.place(x=700, y=50)

    janela.geometry("900x600+250+50")
    janela.mainloop()

############################## FIM DA JANELA PRICE ###########################

############################## INICIO DA JANELA DADOS ########################
janela = Tk()


valor = Entry(janela,width=20)
valor.place(x=140,y=70)

parcela = Entry(janela,width=20)
parcela.place(x=390,y=70)

taxa = Entry(janela,width=20)
taxa.place(x=640,y=70)



legvalor = Label(janela, text="Valor do Empréstimo:")
legvalor.place(x=138,y=49)

legpre = Label(janela, text="Número de prestações:")
legpre.place(x=387,y=49)

legtaxa = Label(janela, text="Valor da taxa de juros:")
legtaxa.place(x=638,y=49)

pr = Label(janela, text="%")
pr.place(x=764,y=69)

esc = Label(janela, text="<=   Escolha o sistema financeiro desejado  =>",font=10)
esc.place(x=300,y=170)



btS=Button(janela,width=20,text="SAC",command=btcS)
btS.place(x=138,y=170)

btP=Button(janela,width=18,text="PRICE",command=btcP)
btP.place(x=638,y=170)



janela.geometry("900x300+250+50")
janela.mainloop()
##################################### FIM DA JANELA DADOS ##############################
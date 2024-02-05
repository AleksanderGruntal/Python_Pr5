nimed=["Mati","Kati","Mati","Mati","Kadri"]
while True:
    valik=input("Andmete lisamine-add\nAndmete nätamine-show\nAndmete kustutamine-del\nJärjendi pööramine-rev\nAndmete kustutamine-clear\nAndmete sortimine-sort\nAndmete otsing-ots\n")
    if valik=="add":
        valik=input("Kas lisame mitu inimest või positsioonile (pos)").lower
        if valik=="mitu":
            mitu=int(input("Mitu inimest liseme? "))
            for i in range(mitu):
               nimi=input("Sisesta nimi: ")
               nimed.append(nimi)
        else:
            indeks=int(input("Kuhu lisamine? ")).lower
            nimi=input("Mis nimi: ")
            nimed.insert(indeks-1,nimi).dict
    elif valik=="show":
        valik=input("Kas kustutame nimi(nimi) või indeksi järgi (ind)?")
        if valik=="nimi":
            nimi=input("Mis nimi on vaja kustutada? ")
            kogus=nimed.count(nimi)
            if kogus>0:
                for i in range(kogus):
                    nimed.remove(nimi)
            else:
                print(f"Nimi {nimi} ei ole nimekirjas")
        else:
            indeks=int(input("Mis on järjekorranumber?"))
            nimed.pop(indeks-1)
        print(nimed)
    elif valik=="show":
        print(nimed)
    elif valik=="rev":
        nimed.reverse()
        print(nimed)
    elif valik=="sort":
        nimed.sort()
        print(nimed)
    elif valik=="clear":
        nimed.clear()
        print(nimed)
    elif valik=="ots":
        ind=-1
        nimi=input("Mis nimi otsime? ")
        if nimed.count(nimi)>0:
            for nim in nimed:
                if nim==nimi:
                    ind=nimed.index(nimi,ind+1)
                    print(f"{nimi} on indeksiga {ind}")
        else:
            print(f"{nimi} ei ole nimekirjas")
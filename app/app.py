import psycopg2
conn = None
try:
    while conn == None:
        try:
            conn = psycopg2.connect(
                    user='mkrawiec',
                    password='password',
                    host='10.0.10.3',
                    port='5432',
                    database='mkrawiec_db',
                    )    
        except:
            continue
except:
    pass
print("Połączono\n")
cur = conn.cursor()
imie_1 = "Jan"
nazwisko_1 = "Kowalski"
imie_2 = "Adam"
nazwisko_2 = "Malinowski"
imie_3 = "Zbigniew"
nazwisko_3 = "Wodecki"
table = False
try:
    while table == False:
        try:
            create_table = 'CREATE TABLE IF NOT EXISTS "Uzytkownicy" (id SERIAL PRIMARY KEY, "Imie" varchar(30) NOT NULL, "Nazwisko" varchar(30) NOT NULL);'
            select = 'SELECT * FROM "Uzytkownicy";'
            cur.execute(create_table)
            conn.commit()
            table = True
        except:
            continue
except:
    print("error")
print("Utworzono tabele\n")
try:    
    cur.execute('INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko") VALUES (%s, %s);', (imie_1, nazwisko_1))
    conn.commit()
    cur.execute('INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko") VALUES (%s, %s);', (imie_2, nazwisko_2))
    conn.commit()
    cur.execute('INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko") VALUES (%s, %s);', (imie_3, nazwisko_3))
    conn.commit()
    print("Dodano 3 rekordy do bazy\n")
except:
    print("error")
number = '0'
while number!=5:
    print("1 - dodaj uzytkownika 2 - usun uzytkownika 3-aktualizuj dane uzytkownika 4-wyswietl uzytkownikow 5-koniec")
    number = int(input())
    
    if number == 1:
        try:
            imie = input("Imie: ")
            nazwisko = input("Nazwisko: ")
            cur.execute('INSERT INTO "Uzytkownicy" ("Imie", "Nazwisko") VALUES (%s, %s);',(imie, nazwisko))
            conn.commit()
            print("Dodano uzytkownika\n")
        except: 
            print("error")
    elif number == 2:
        try:
            id = input("Id uzytkownika: ")
            cur.execute('DELETE FROM "Uzytkownicy" WHERE id=%s;', id)
            conn.commit()
            print("Usunieto uzytkownika o id = %s",id)
        except:
            print("error")
        
    elif number ==3:
        try:
            id = input("Id uzytkownika: ")
            imie = input("Nowe imie: ")
            nazwisko = input("Nowe nazwisko: ")
            cur.execute('UPDATE "Uzytkownicy" SET "Imie"=%s, "Nazwisko"=%s WHERE id=%s;', (imie, nazwisko, id))
            conn.commit()
            print("Zaktualizowano dane uzytkownikao id = %s",id)
        except: 
            print("error")
    elif number == 4:
        try:
            cur.execute(select)
            users = cur.fetchall()
            for u in users:
                print("Id = ", u[0], )
                print("Imie = ", u[1])
                print("Nazwisko  = ", u[2], "\n")
        except: 
            print("error")

cur.close()
conn.close()

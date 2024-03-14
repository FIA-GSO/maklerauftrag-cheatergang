#Kopf des Formulars
print("Bitte füllen Sie den Kopf aus")
print("Mitarbeitername:")
name = input();
print("Wohnungsname:")
objekt = input();
print("Datum:")
datum = input();

###Rechnenblock##
###Gesamt variablen werden benutzt um außerhalb der Schleifen die Werte zu speicher
###Erste Schleife, um die Anzahl der Räume zu wiederholen
###Zweite Schleife, um komplexe Räume zu berechnen, indem man die einzelnen Vierecke zusammen rechnet
print("Anzahl der Räumlichkeiten:")
gesamt0 = 0 #Variable außerhalb der Schleifen um die Gesamtfläche zu berechnen, damit sie von der Schleife nicht zurückgesetzt wird
gesamt1 = 0 #Variable außerhalb der Schleifen um die Gesamtfläche zu berechnen, damit sie von der Schleife nicht zurückgesetzt wird
gesamt2 = 0 #Variable außerhalb der Schleifen um die Gesamtfläche zu berechnen, damit sie von der Schleife nicht zurückgesetzt wird
Listeräume = [] #Leere Liste
rooms = int(input());
for i in range (rooms): #Schleifen anfang
    print("In welchen Raum befinden Sie sich?")
    raumname = input();
    gesamt4 = 0 #Variable, welche zurück auf 0 gesetzt werden soll, durch jeden neuen Raum
    gesamt5 = 0 #Variable, welche zurück auf 0 gesetzt werden soll, durch jeden neuen Raum
    print("Ist der Raum komplex? 'ja','nein'")
    raum0 = input(); 
    if raum0 == "ja": #Anfang der Verzweigung, ob der Raum komplex ist oder nicht
        print("Anzahl der Vierecke:")
        vierecke = int(input()); 
        for i in range (vierecke): # Zweite Schleife für die Anzahl der Vierecke, für den jeweiligen Raum 
            print("Länge:")
            länge = int(input());
            print("Breite:")
            breite = int(input());
            gesamt1 = gesamt1 + (länge * breite) #Rechnung für die Gesamtgröße
            gesamt4 = gesamt4 + (länge * breite) #Rechnung für die Raumgröße
            print(f"Gesamtfläche",raumname,":",{gesamt4},"m^2") #Ausgabe für den Raum
    else: #Zweite Verzweigung, ob der Raum nicht komplex ist
        if raum0 == "nein":
            print("Länge:")
            länge1 = int(input());
            print("Breite:")
            breite1 = int(input());
            gesamt0 = gesamt0 + (länge1 * breite1) #Rechnung für die Gesamtgröße
            gesamt5 = länge1 * breite1 #Rechnung für den einzelnen Raum
            print(f"Gesamtfläche",raumname,":",{gesamt5},"m^2") #Ausgabe für den Raum
    gesamt6 = gesamt4 + gesamt5 #Zusammenfassen der Varibalen Raumkomplex, nicht komplex
    zusammenfassung = raumname, gesamt6 #zusammenfassen der Varibalen Raum, gesamt6 für die Liste
    Listeräume.append(zusammenfassung) #Eintrag in der Liste
gesamt2 = gesamt1 + gesamt0 #Rechnung für die Gesamtgröße
durchschnitt = gesamt2/rooms #Rechnung für die durchschnittliche Größe
print(f"Gesamtfläche der Wohnung",{gesamt2},"m^2")
print("Die durchschnittliche Fläche pro Raum betragt:",durchschnitt,"m^2")
print(Listeräume)

     
        
        

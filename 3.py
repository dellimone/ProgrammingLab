#il programma apre il file shampoo_sales.csv, prende i valori di soldi e li mette in una lista, si sommano i valori della lista e si printa il totale

#apro il file shampoo_sales.csv
my_file = open('shampoo_sales.csv', 'r')

#creo una lista vuota dove metterò i valori da sommare
value_list=[]

#creo un ciclo che mi permette di operare su ciascuna linea del file testo singolarmente
for line in my_file:
    
    #splitto ogni linea per "," ottenendo una lista temporanea di due elementi del file testo
    my_list = line.split(",")

    #controllo che il la linea non sia l'intestazione della tabella
    if my_list[0]!="Date":

         #aggiungo il valore numerico alla mia lista dei valori
        value_list.append(float(my_list[1]))

my_file.close()

#sommo e stampo il totale utilizzando i valori selezionati nel ciclo
print(sum(value_list))
#definisco una classe CSVFile

class CSVFile():

    #inizializzo la classe
    def __init__(self,name):

        self.name = name

    #definisco un metodo get_data che ritorna una lista composta da liste del tipo [data,valore]
    def get_data(self):
        
        #apro il file e lo assegno a file_csv
        file_csv = open(self.name,'r')
        
        #creo la lista di coppie di valori che dovrà essere ritornata
        list_of_couple = []
        
        #ciclo che permette di operare sulla singola linea del file csv
        for line in file_csv:
            
            #creo una lista temporanea contentente i valori della linea splittati per "," 
            tmp_list = line.split(",")

            #escludo la linea di intestazione
            if tmp_list[0]!="Date":

                #pulisco il valore del carattere escape \n
                tmp_list[1] = (tmp_list[1])[0:-1]

                #aggiungo la coppia [data,valore] alla lista da ritornare
                list_of_couple.append(tmp_list)
        
        #n.b entrambe le coppie di valori sono stringhe
        return list_of_couple

file = CSVFile('shampoo_sales.csv')

data_list = file.get_data()

print(data_list)
            



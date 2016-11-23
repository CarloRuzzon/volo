#calcoliamo il tempo di volo di un aereo carburante = 1480 galloni, consumo_h = 320

consumotot=1480.0/320.0
consumotot=consumotot*1000
int(consumotot)
secondi=consumotot%10
int(secondi)
consumotot/=10
int(consumotot)
minuti=consumotot%100
int(minuti)
consumotot=consumotot/100

if (minuti>59):
   consumotot+=1
   minuti=minuti-59
secondi1=minuti%10
minuti/=10
int(minuti)

print "L'aereo puo viaggiare per ", int(consumotot), " ore, ", int(minuti), " minuti, ",int(secondi1),int(secondi), " secondi"



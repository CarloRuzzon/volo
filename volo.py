#calcoliamo il tempo di volo di un aereo carburante = 1480 galloni, consumo_h = 320

carb=1460.
consumo_h=320.

consumotot=carb/consumo_h
ore=int(consumotot)
resto=float(consumotot-int(consumotot))
minuti=int(resto*60)
minuti1=resto*60
secondi1 = minuti1 - minuti
secondi = int (secondi1*60)

print"L'aereo puo' volare per massimo ",ore, " ore, ",minuti, "minuti, ", secondi, "secondi"

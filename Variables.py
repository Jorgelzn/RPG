
# Escenarios y ventanas:
map1 = (1600, 1290)
map2 = (2000, 2000)
ventana = (1200, 900)
objects=[]
# Colores:
agua = (50, 120, 240)
hierba = (50, 220, 50)

#Sonidos
soundtrack1 ="sonidos/ost/Moki_Town.mp3"
soundtrack2 ="sonidos/ost/abyss.mp3"
flute ="sonidos/ost/Saria song.mp3"
# Otros:
FPSPRITE = 10 # frames por sprite (personaje)
#saving variables
f=open("save.txt","r")
lines=f.readlines()
pjx=int(lines[0])
pjy=int(lines[1])
mapaG=int(lines[2])
objects.append(eval(lines[3]))

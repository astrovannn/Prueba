capitales=[]
proflos=[]
op=int(input("Hola, ingrese cuantas operaciones hizo el dia de hoy "))

for i in range(op):
    n = int(input(f"¿Cuál fue el capital de la operación {i+1}? "))
    capitales.append(n)
    sum(capitales)

for i in range(op):
    pl = int(input(f"¿Cuál fue el beneficio/perdida de la operación {i+1}? "))
    proflos.append(pl)
    sum(proflos)

Tproflos = sum(proflos)
Tcapitales = sum(capitales)
R = (Tproflos/Tcapitales)*100
print("Su rentabilidad es del", R,"%") 
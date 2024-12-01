from pickle import APPEND
from os.path import basename
import random

flechaHorizontalDobleCabeza = "\u2194;" # ↔
flechaVerticalDobleCabeza = "\u2195;"   #↕   ## primero las pase al codigo asci
flechas=[flechaHorizontalDobleCabeza,flechaVerticalDobleCabeza] ## las agrupe en un arreglo para un mejor manejp
import random
n = int (input("Ingresa la cantidad de bits con la que quieres trabajar ,ejemplo puedes usar 1,2,3,..... 00 bits para trabajar : ")) ## aqui el usuario agrega los bits a trabajr
def generar_bits(n):
    # Crear una lista con n elementos aleatorios de 0 y 1
    binarios = [str(random.randint(0, 1)) for _ in range(n)]

    # Mezclar la lista de binarios
    random.shuffle(binarios)

    return ''.join(binarios)

# Ejemplo de uso
##n = 4  # Número de dígitos
                                                                                                                                                    ###proceso alice
resultado = generar_bits(n)
print("....................APARTADO ALICE .............")
print("---------------------bases y bits generados de manera aleatoria---------------")
print("\n")
print(resultado)   ##1010001111


def generar_bases(z):
  bases = [random.choice(flechas)for _ in range(z)] ## aqui manejamos las bases de modo aleatorio con .choice maneja el arreglo flechas
  random.shuffle(bases) ## mezcla el arreglo
  return bases
##z = n

basearray0= generar_bases(n)

print(basearray0)    ##↕;↔;↕;↔;↔;↔;↔;↕;↔;↔;



bitsarray= [int(bit) for bit in resultado]


print("\n")
print("---------comparador------- ")
print("bases:",basearray0)
print("bits:",bitsarray)
print("Cantidad de bits:", len(bitsarray))
print("Cantidad de bases:", len(basearray0))
print("\n")
qubitsAlice= [];
##while len(basearray0)!= 0 and len(bitsarray) !=0:
for i in range(len(basearray0)):
    bit = bitsarray[i]
    base = basearray0[i]

    if bit == 0 and base == flechaVerticalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|0>")
              qubitsAlice.append("|0>");
    elif bit == 1 and base == flechaVerticalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|1>")
              qubitsAlice.append("|1>");
    elif bit == 1 and base == flechaHorizontalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|->")
              qubitsAlice.append("|->");
    elif bit == 0 and base == flechaHorizontalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|+>")
              qubitsAlice.append("|+>");
    else:
              print("\n")
              print("No se cumple ninguna condición.")


print("--------Qubit para Alice---------",qubitsAlice)
print("\n")

print(".......Apartado bob, cargando ............")
print("\n")
def generar_basesbob(x):
  bases = [random.choice(flechas)for _ in range(x)] ## aqui manejamos las bases de modo aleatorio con .choice maneja el arreglo flechas
  random.shuffle(bases) ## mezcla el arreglo
  return ''.join(bases)
x = n
QubitsBob=[]
xresultado=generar_bases(n)
print("base en bob")
print(xresultado)


print(resultado)
for i in range( len(xresultado)):
    bit = bitsarray[i]
    base = xresultado[i]


    if bit == 0 and base == flechaVerticalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|0>")
              QubitsBob.append("|0>");
    elif bit == 1 and base == flechaVerticalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|1>")
              QubitsBob.append("|1>");
    elif bit == 1 and base == flechaHorizontalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|->")
              QubitsBob.append("|->");
    elif bit == 0 and base == flechaHorizontalDobleCabeza:
              print("\n")
              print("qubit obtenido ------- " + "|+>")
              QubitsBob.append("|+>");
    else:
              print("\n")
              print("No se cumple ninguna condición.")


print("--------Qubit para Bob--------",QubitsBob)
print("\n")
print("comparador de bases ALICE Y BOB ................CARGANDO..........CAEGANDO .........")
baseCorroborada= []
qubitsvivos=[]
for i in  range (len (basearray0)):
 basealice = basearray0[i]
 basebob =   xresultado[i]
 ali = qubitsAlice[i]
 bob= QubitsBob[i]
 if basealice == flechaVerticalDobleCabeza and basebob == flechaVerticalDobleCabeza:
    print("las bases son las mismas ")
    qubitsvivos.append(ali)
    baseCorroborada.append(basealice)
 elif basealice == flechaHorizontalDobleCabeza and basebob == flechaHorizontalDobleCabeza:
    print("las bases son las mismas ")
    baseCorroborada.append(basealice)
    qubitsvivos.append(ali)
 elif basealice == flechaHorizontalDobleCabeza and basebob == flechaVerticalDobleCabeza:
    print("las bases son diferentes ")
 elif basealice == flechaVerticalDobleCabeza and basebob == flechaHorizontalDobleCabeza:
    print("las bases son diferentes ")
print("Base Depurada ,bases que coinciden en Alice y Bob: ",baseCorroborada)


print("........los qubits vivos son :",qubitsvivos)
print("\n")
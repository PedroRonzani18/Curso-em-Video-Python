""" 
tendo uma tupla',' mostrar
1. 5 colocados
2. ultimos 4 colocados
3. ordenados
4. posicao do c
"""

times = ('a','f','g','g','yh','u','h','v','x','z','s','e','dc','c','e','t','y','u','n','v','f')

print("5 primeiros colocados: ",end='')
for i in range(0,5): print(f"{times[i]} ",end='') 

print("\nUltimos 4 colocados: ",end='')
for i in range (-1,-5,-1): print(f"{times[i]} ",end='')

print(f"\nTimes ordenados: {sorted(times)}")

print(f"Posição do c: {times.index('c')+1}")



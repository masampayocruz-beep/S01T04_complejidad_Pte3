import time 

valores_tabla = [100, 500, 1000, 1500, 2000, 2500, 3000, 3500]

for n in valores_tabla:
    #maraca de tiempo 
    timestamp_01 = time.time()
    
    total_sum = 0
    # ciclo for
    for number in range (1,n+1):
        total_sum =  total_sum + number
        #1: linea de codigo <- 0+1
        #suma = 1
        #2: sum<- 1 + 2
        #suma = 3
    print(f"La suma de 1 hasta {n} es : {total_sum}")

    #Tomando el tiempo final
    timestamp_02 =  time.time()

    #Tomando el timepo del tiempo de ejecuicion
    print(f"Timepo de ejecicion para n={n}: {(timestamp_02 - timestamp_01) * 1e6:.2f}  µs")
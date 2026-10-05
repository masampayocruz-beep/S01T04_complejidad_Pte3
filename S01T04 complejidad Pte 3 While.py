import time 

# La lista de valores que el profe tiene en su pantalla
valores_n = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]

for n_objetivo in valores_n:
    n = n_objetivo
    the_sum = 0
    
    # Tomando el t1
    timestamp_01 = time.time()
    
    # El mismo ciclo while que ya arreglamos
    while n > 0:
        the_sum = the_sum + n 
        n -= 1 
       
    # Tomamos el t2
    timestamp_02 = time.time()
    
    # Calculando tiempo
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
    
    # Imprimiendo el formato exacto del profe: (n, tiempo, suma)
    print(f"({n_objetivo}, {elapsed_time}, {the_sum})")
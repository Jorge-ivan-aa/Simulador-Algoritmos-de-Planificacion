class Proceso:
    def __init__(self, id, llegada, burst, memoria=None, prioridad=None):
        self.id = id
        self.llegada = llegada
        self.burst = burst
        self.memoria = memoria  # Requisito de memoria del proceso
        self.prioridad = prioridad
        self.tiempo_espera = 0
        self.tiempo_retorno = 0

    def fcfs(procesos):
        tiempo_actual = 0
        orden = "Orden de ejecución: "
        for p in sorted(procesos, key=lambda x: x.llegada):
            orden += str(p.id) + " -> "
            p.tiempo_espera = tiempo_actual - p.llegada
            tiempo_actual += p.burst
            p.tiempo_retorno = tiempo_actual - p.llegada

        orden = orden[:-3]

        return (procesos, orden)

    def sjf(procesos):
        tiempo_actual = 0
        orden = "Orden de ejecución: "
        cola = sorted(procesos, key=lambda x: (x.llegada, x.burst))
        while cola:
            p = next((p for p in cola if p.llegada <= tiempo_actual), None)
            if not p:
                tiempo_actual += 1
                continue
            
            orden += str(p.id) + " -> "
            p.tiempo_espera = tiempo_actual - p.llegada
            tiempo_actual += p.burst
            p.tiempo_retorno = tiempo_actual - p.llegada
            cola.remove(p)

        orden = orden[:-3]
        return (procesos, orden)

    def round_robin(procesos, quantum):
        tiempo_actual = 0
        cola = list(procesos)
        orden = "Orden de ejecución: "
        while cola:
            p = cola.pop(0)
            if p.burst > quantum:
                tiempo_actual += quantum
                p.burst -= quantum
                cola.append(p)
            else:
                orden += str(p.id) + " -> "
                tiempo_actual += p.burst
                p.tiempo_retorno = tiempo_actual - p.llegada
                p.tiempo_espera = p.tiempo_retorno - p.burst

        orden = orden[:-3]
        return (procesos, orden)

    def prioridad(procesos):
        tiempo_actual = 0
        cola = []  # Usaremos esta lista para manejar los procesos pendientes
        procesos_restantes = procesos.copy()
        orden = "Orden de ejecución: "
    
        while procesos_restantes or cola:
            # Agregar a la cola todos los procesos que hayan llegado hasta el tiempo_actual
            nuevos_procesos = [p for p in procesos_restantes if p.llegada <= tiempo_actual]
            for p in nuevos_procesos:
                cola.append(p)
                procesos_restantes.remove(p)
        
            if not cola:
                # Si no hay procesos listos, avanzar el tiempo al próximo proceso
                tiempo_actual = min(p.llegada for p in procesos_restantes)
                continue
        
            # Seleccionar el proceso de MAYOR prioridad (menor número)
            cola.sort(key=lambda x: x.prioridad)  # Ordenar por prioridad
            p = cola[0]  # Tomar el más prioritario
        
            orden += f"{p.id} -> "
            p.tiempo_espera = tiempo_actual - p.llegada
            tiempo_actual += p.burst
            p.tiempo_retorno = tiempo_actual - p.llegada
            cola.remove(p)
    
        orden = orden[:-4]  # Eliminar el último " -> "
        return (procesos, orden)

    def fms(procesos, memoria_total):
        tiempo_actual = 0
        cola = sorted([p for p in procesos if p.memoria <= memoria_total], key=lambda x: x.llegada)  # Filtrar procesos imposibles
        memoria_disponible = memoria_total
        procesos_ejecutados = []
        orden = "Orden de ejecución: "
    
        while cola:
            # Buscar el primer proceso que llegó y cabe en memoria
            proceso_elegido = None
            for p in cola:
                if p.llegada <= tiempo_actual and p.memoria <= memoria_disponible:
                    proceso_elegido = p
                    break
        
            if not proceso_elegido:
                # Si no hay procesos válidos, avanzar tiempo al próximo evento relevante
                if not cola:
                    break  # No hay más procesos
            
                # Calcular el próximo tiempo de llegada o de liberación de memoria
                proxima_llegada = min(p.llegada for p in cola if p.llegada > tiempo_actual)
                tiempo_actual = proxima_llegada
                continue
        
            # Ejecutar el proceso
            orden += str(p.id) + " -> "
            memoria_disponible -= proceso_elegido.memoria
            proceso_elegido.tiempo_espera = tiempo_actual - proceso_elegido.llegada
            tiempo_actual += proceso_elegido.burst
            proceso_elegido.tiempo_retorno = tiempo_actual - proceso_elegido.llegada
            memoria_disponible += proceso_elegido.memoria  # Liberar memoria
            cola.remove(proceso_elegido)
            procesos_ejecutados.append(proceso_elegido)
    
        orden = orden[:-3]
        return (procesos_ejecutados, orden)
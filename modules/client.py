from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Slot
from .gui import Ui_MainWindow
from .proceso import Proceso

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
       
        # Configurar la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.procesos = []
        self.memoria_disponible = 0
        self.quantum = 2
        self.configurar_controles()
        self.conectar_senales()
    
    def configurar_controles(self):
        """Configura los valores iniciales de los controles"""
        self.ui.id.setRange(1, 100)
        self.ui.llegada.setRange(0, 100)
        self.ui.burst.setRange(0, 100)
        self.ui.memoria.setRange(100, 1000)
        self.ui.prioridad.setRange(0, 100)
        self.ui.memoria_disponible.setRange(300, 2000)
        self.ui.quantum.setRange(1, 10)

        # Valores por defecto
        self.ui.id.setValue(0)
        self.ui.llegada.setValue(0)
        self.ui.burst.setValue(0)
        self.ui.memoria.setValue(100)
        self.ui.prioridad.setValue(0)
        self.ui.memoria_disponible.setValue(300)
        self.ui.quantum.setValue(2)
    
    def conectar_senales(self):
        """Conecta las señales de los botones a sus slots"""
        self.ui.memoria_disponible.valueChanged.connect(self.actualizar_memoria)
        self.ui.quantum.valueChanged.connect(self.actualizar_quantum)
        self.ui.agregar_proceso.clicked.connect(self.agregar_proceso)
        self.ui.eliminar_ultimo.clicked.connect(self.eliminar_ultimo_proceso)
        self.ui.simular.clicked.connect(self.ejecutar_simulacion)
    
    @Slot()
    def actualizar_memoria(self):
        self.memoria_disponible = self.ui.memoria_disponible.value()

    @Slot()
    def actualizar_quantum(self):
        self.quantum = self.ui.quantum.value()

    @Slot()
    def eliminar_ultimo_proceso(self):
        
        try:
            del self.procesos[-1]
            texto_actual = self.ui.preview.toPlainText()
            nuevo_texto = self.eliminar_ultima_linea(texto_actual)
            self.ui.preview.setPlainText(nuevo_texto)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo eliminar el ultimo proceso:\n{str(e)}")


    def eliminar_ultima_linea(self, texto: str) -> str:
        lineas = texto.splitlines()
        if len(lineas) <= 1:
            return ""  # o texto si prefieres mantener la única línea
        return '\n'.join(lineas[:-1])


    @Slot()
    def agregar_proceso(self):
        """Agrega un nuevo proceso a la lista"""
        try:
            # Crear nuevo proceso
            proceso = Proceso(
                id=self.ui.id.value(),
                llegada=self.ui.llegada.value(),
                burst= self.ui.burst.value(),  # Valor por defecto (puedes añadir un QSpinBox para esto)
                memoria=self.ui.memoria.value(),
                prioridad=self.ui.prioridad.value(),
            )
            
            self.quantum = self.ui.quantum.value()
            self.procesos.append(proceso)
            
            # Actualizar el área de preview
            texto_actual = self.ui.preview.toPlainText()
            nuevo_texto = f"{texto_actual}\n{proceso.id}, {proceso.llegada}, {proceso.burst}, {proceso.memoria}, {proceso.prioridad}"
            self.ui.preview.setPlainText(nuevo_texto.strip())

            # Manejar la memoria
            self.memoria_disponible = self.ui.memoria_disponible.value()

            # Preparar para el siguiente proceso
            self.ui.id.setValue(self.ui.id.value() + 1)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo agregar el proceso:\n{str(e)}")
    
    @Slot()
    def ejecutar_simulacion(self):
        """Ejecuta todos los algoritmos de planificación"""
        if not self.procesos:
            QMessageBox.warning(self, "Advertencia", "No hay procesos para simular")
            return
        
        try:
            resultado = "=== RESULTADOS DE SIMULACIÓN ===\n\n\n"
            
            # FCFS
            resultado += "FCFS (First Come First Served):\n"
            resultado += self.ejecutar_algoritmo(Proceso.fcfs)
            
            # SJF
            resultado += "\nSJF (Shortest Job First):\n"
            resultado += self.ejecutar_algoritmo(Proceso.sjf)
            
            # Round Robin (quantum=2)
            resultado += f"\nRound Robin, (Quantum={self.quantum}) :\n"

            resultado += self.ejecutar_algoritmo(lambda p: Proceso.round_robin(p, self.quantum))
            
            # Prioridad
            resultado += "\nPrioridad:\n"
            resultado += self.ejecutar_algoritmo(Proceso.prioridad)
            
            # FMS (First Memory Served)
            resultado += f"\nFMS (First Memory Served), (Memory={self.memoria_disponible}) :\n"
            resultado += self.ejecutar_algoritmo(lambda p: Proceso.fms(p, self.memoria_disponible))
            
            # Mostrar resultados
            self.ui.resultado.setPlainText(resultado)
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error en la simulación:\n{str(e)}")
    
    def ejecutar_algoritmo(self, algoritmo):
        """Ejecuta un algoritmo y devuelve resultados formateados"""

        res = algoritmo(self.procesos.copy())
        procesos = res[0]
        orden_ejecucion = res[1]

        ts_espera = 0
        ts_retorno = 0

        for p in procesos:
            ts_espera += p.tiempo_espera
            ts_retorno += p.tiempo_retorno
        
        prom_espera = round(ts_espera/len(self.procesos), 2)
        prom_retorno = round(ts_retorno/len(self.procesos), 2)

        return (
            "\n".join(
                f"\tProceso {p.id}: Espera={p.tiempo_espera}, Retorno={p.tiempo_retorno}"
                for p in procesos
            )
            + f"\n\n\tPromedio Tiempo espera: {prom_espera}"
            + f"\n\tPromedio Tiempo retorno: {prom_retorno}"
            + f"\n\t{orden_ejecucion}\n\n"
        )

    @staticmethod
    def create_app(args):
        """Método estático para crear la aplicación"""
        app = QApplication(args)
        app.setStyle('Fusion')  # Configurar estilo visual
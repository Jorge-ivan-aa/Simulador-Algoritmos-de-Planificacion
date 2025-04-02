import sys
from modules.client import MainWindow
from PySide6.QtWidgets import QApplication

def main():
    # Actividad: Simulación de Planificación de Procesos y
    # Gestión de Memoria
    #
    # Estudiante: Jorge Iván Acosta Aristizábal
    
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Configurar estilo visual
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
# Simulador de Algoritmos de Planificación de Procesos

Este es un simulador de algoritmos de planificación de procesos que permite visualizar y analizar el comportamiento de diferentes estrategias de planificación, como FCFS, SJF, Round Robin, Prioridad y FMS.

## Requisitos

Antes de ejecutar el simulador, asegúrate de tener instalado Python (versión 3.8 o superior) y los siguientes paquetes:

```txt
PySide6==6.8.3
PySide6_Addons==6.8.3
PySide6_Essentials==6.8.3
setuptools==78.1.0
shiboken6==6.8.3
```

## Instalación

1. **Clona el repositorio o descarga el código fuente**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_PROYECTO>
   ```

2. **Crea un entorno virtual (opcional pero recomendado)**:

   ```bash
   python -m venv venv
   # Para activarlo:
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el simulador, ejecuta el siguiente comando:

```bash
python init.py
```

Esto abrirá la interfaz gráfica del simulador donde podrás agregar
los datos de prueba y ver el resultado con cada algoritmo de
planificación.
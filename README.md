# AI-IQRS
## Sistema Inteligente para la Liberación Automatizada de Calidad mediante Inteligencia Artificial

AI-IQRS (Artificial Intelligence Intelligent Quality Release System) es un sistema de visión artificial desarrollado para asistir el proceso de inspección de calidad de kits médicos vasculares mediante Inteligencia Artificial.

El proyecto utiliza **YOLOv8**, **Python** y **OpenCV** para detectar automáticamente los componentes presentes en un kit médico e identificar aquellos que hacen falta antes de su liberación, reduciendo errores humanos y mejorando la eficiencia del proceso de inspección.

> **Nota:** Este proyecto corresponde a un prototipo académico desarrollado como parte de la Maestría en Inteligencia Artificial y no representa una solución lista para producción.

---

# Objetivo del Proyecto

El objetivo principal es desarrollar un sistema inteligente capaz de:

- Detectar automáticamente los componentes de un kit médico.
- Comparar los componentes detectados con la configuración esperada.
- Identificar componentes faltantes.
- Generar una decisión de inspección **PASS** o **FAIL**.
- Servir como herramienta de apoyo para los inspectores de calidad.

---

# Tecnologías Utilizadas

- Python 3.11
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- NumPy
- Label Studio
- Apple Silicon (MPS)
- macOS

---

# Dataset

El conjunto de datos fue construido específicamente para este proyecto mediante imágenes reales de kits médicos.

## Distribución del Dataset

| Conjunto | Cantidad |
|----------|----------|
| Entrenamiento | 245 |
| Validación | 31 |
| Pruebas | 30 |
| **Total** | **306 imágenes** |

Todas las imágenes fueron etiquetadas manualmente utilizando **Label Studio** y exportadas en formato **YOLO**.

---

# Clases Detectadas

El modelo fue entrenado para reconocer diez tipos de componentes médicos:

- Catheter
- Griplock
- Guidewire
- Micro-Claves
- Needle
- Needle Protector
- Ruler
- Scalpel
- Syringe
- Tearaway

---

# Modelo Seleccionado

Después de evaluar diferentes arquitecturas de detección de objetos, se seleccionó **YOLOv8s** por ofrecer el mejor equilibrio entre precisión, velocidad de inferencia y facilidad de implementación para este caso de estudio.

## Parámetros de entrenamiento

- Modelo: YOLOv8s
- Épocas: 100
- Tamaño de imagen: 1024 × 1024
- Batch Size: 8
- Optimizador: AdamW
- Learning Rate: 0.001
- Patience (Early Stopping): 50
- Cosine Learning Rate Scheduler
- Apple MPS Acceleration

---

# Estrategias para Reducir el Overfitting

Durante el entrenamiento se implementaron diversas técnicas para mejorar la capacidad de generalización del modelo.

## Data Augmentation

- Rotaciones leves
- Traslaciones
- Escalado
- Ajuste HSV
- Mosaic = 0.2
- MixUp deshabilitado
- Flip horizontal deshabilitado
- Flip vertical deshabilitado

## Otras estrategias

- Incremento progresivo del dataset hasta 306 imágenes.
- Separación entre entrenamiento, validación y prueba.
- Early Stopping.
- Validación continua durante el entrenamiento.
- Ajuste fino de hiperparámetros.

Estas estrategias permitieron disminuir el riesgo de sobreajuste y mejorar el desempeño del modelo sobre imágenes no vistas.

---

# Flujo General del Sistema

```
Captura de Imagen
        │
        ▼
Detección mediante YOLOv8
        │
        ▼
Identificación de Componentes
        │
        ▼
Motor de Reglas (Rules Engine)
        │
        ▼
Comparación con Componentes Esperados
        │
        ▼
Componentes Faltantes
        │
        ▼
Resultado Final
PASS / FAIL
```

---

# Interfaz Gráfica

La interfaz desarrollada muestra en tiempo real:

- Imagen capturada por la cámara.
- Componentes detectados.
- Componentes faltantes.
- Estado de inspección (READY, PASS o FAIL).

La interfaz fue diseñada para enfocarse únicamente en la detección de componentes faltantes, facilitando la interpretación por parte del operador.

---

# Estructura del Proyecto

```
AI-IQRS
│
├── dataset
│   ├── images
│   ├── labels
│   └── data.yaml
│
├── runs
│
├── camera.py
├── detector.py
├── gui.py
├── rules_engine.py
├── config.py
├── main.py
│
└── README.md
```

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/AI-IQRS.git
```

## Crear entorno virtual

```bash
python3 -m venv venv
```

## Activar entorno

### macOS

```bash
source venv/bin/activate
```

### Windows

```cmd
venv\Scripts\activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Entrenamiento del Modelo

```bash
yolo detect train \
model=yolov8s.pt \
data=dataset/data.yaml \
epochs=100 \
imgsz=1024 \
batch=8
```

---

# Ejecución del Sistema

```bash
python main.py
```

## Controles

| Tecla | Acción |
|--------|--------|
| Espacio | Ejecutar inspección |
| ESC | Salir |

---

# Resultados

El sistema identifica automáticamente los componentes presentes en el kit médico y determina si existen componentes faltantes.

Ejemplo de salida:

```
STATUS

PASS

Componentes Detectados

Catheter: 1
Guidewire: 1
Needle: 1

Componentes Faltantes

Ninguno
```

o

```
STATUS

FAIL

Componentes Faltantes

• Syringe
• Tearaway
```

---

# Trabajo Futuro

Las siguientes mejoras permitirán incrementar la robustez del sistema:

- Aumentar el dataset a más de 1000 imágenes.
- Incorporar nuevas configuraciones de kits médicos.
- Mejorar la detección de objetos pequeños.
- Implementar inspección completamente en tiempo real.
- Integrar lectores de códigos de barras.
- Generar reportes automáticos de inspección.
- Desplegar el sistema en hardware industrial.
- Optimizar aún más la velocidad de inferencia.

---

# Autor

**Juan Castañeda**

Proyecto desarrollado como parte de la **Maestría en Inteligencia Artificial**.

---

# Licencia

Este repositorio fue desarrollado con fines académicos y de investigación. No está destinado para uso clínico ni para ambientes de producción.

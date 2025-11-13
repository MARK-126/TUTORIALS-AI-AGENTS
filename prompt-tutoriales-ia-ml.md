# PROYECTO: Tutoriales Interactivos de IA/ML en Jupyter Notebooks

## OBJETIVO GENERAL
Crear una serie educativa completa en formato mono-repositorio que cubra desde Machine Learning 
clásico hasta Agentic AI (incluyendo RL clásico y LLM-based agents), con énfasis en comprensión 
profunda mediante matemática, visualizaciones y ejercicios prácticos.

## AUDIENCIA
- Desarrolladores con conocimientos de Python
- Estudiantes de ingeniería/CS con bases de matemática universitaria
- Profesionales que quieren transicionar a ML/AI
- Nivel: Intermedio (conocen programación y matemática básica)

## ESTRUCTURA DEL REPOSITORIO

```
ml-ai-tutorials/
├── README.md                       # Mapa general + instrucciones
├── environment.yml                 # Conda environment
├── requirements.txt                # Pip dependencies (TensorFlow, plotly, sklearn, etc.)
│
├── shared/                         # Recursos compartidos
│   ├── utils/
│   │   ├── visualization.py       # Funciones de visualización (plotly/matplotlib)
│   │   ├── testing.py             # Tests para ejercicios
│   │   └── datasets.py            # Helpers para cargar datos
│   └── datasets/                   # Datasets pequeños compartidos
│
├── rutas/
│   ├── 01-ml-clasico/
│   │   ├── README.md              
│   │   ├── 01-regresion-lineal.ipynb
│   │   ├── 02-gradient-descent.ipynb
│   │   ├── 03-regresion-logistica.ipynb
│   │   ├── 04-regresion-softmax.ipynb
│   │   ├── 05-arboles-decision.ipynb
│   │   ├── 06-random-forests.ipynb
│   │   ├── 07-boosting.ipynb
│   │   ├── 08-svm.ipynb
│   │   ├── 09-kmeans.ipynb
│   │   ├── 10-pca.ipynb
│   │   └── datasets/              
│   │
│   ├── 02-rl-clasico/
│   │   ├── README.md
│   │   ├── 01-fundamentos-agentes.ipynb
│   │   ├── 02-mdp-bellman.ipynb
│   │   ├── 03-q-learning.ipynb
│   │   ├── 04-deep-q-networks.ipynb
│   │   ├── 05-policy-gradients.ipynb
│   │   ├── 06-actor-critic.ipynb
│   │   └── environments/          # Ambientes custom
│   │
│   └── 03-llm-agents/
│       ├── README.md
│       ├── 01-intro-llm-agents.ipynb
│       ├── 02-prompting-agentico.ipynb
│       ├── 03-react-reasoning-acting.ipynb
│       ├── 04-tool-use-function-calling.ipynb
│       ├── 05-memory-systems.ipynb
│       ├── 06-multi-agentes.ipynb
│       └── ejemplos/
│
└── proyectos/                      # Proyectos integradores (futuro)
    ├── proyecto-1-clasificador-completo.ipynb
    └── proyecto-2-agente-autonomo.ipynb
```

## PRINCIPIOS PEDAGÓGICOS FUNDAMENTALES

1. **Motivación primero**: Cada notebook empieza con un problema real o pregunta intrigante
2. **Intuición antes que formalismo**: Visualizaciones y ejemplos antes de ecuaciones
3. **Construcción gradual**: Implementar desde cero (numpy) antes de usar frameworks
4. **Interactividad**: Ejercicios para completar con tests automáticos
5. **Conexión entre conceptos**: Cada notebook referencia el anterior y prepara el siguiente
6. **Rigor sin pedantería**: Matemática explicada paso a paso con ejemplos numéricos

## FORMATO ESTÁNDAR DE CADA NOTEBOOK

### 1. Header (celda markdown)
```markdown
# [Número]. [Título Descriptivo]

**Nivel:** [🟢 Principiante / 🟡 Intermedio / 🔴 Avanzado]  
**Tiempo estimado:** [30-90 minutos]  
**Prerequisitos:** [Link a notebook(s) previo(s)]

## 🎯 Objetivos de Aprendizaje
Al finalizar este notebook, podrás:
- [Objetivo concreto y medible 1]
- [Objetivo concreto y medible 2]
- [Objetivo concreto y medible 3]
```

### 2. Sección: Motivación (5-10% del notebook)
- Problema del mundo real
- Por qué este tema importa
- Qué limitaciones resuelve vs métodos anteriores
- Pregunta guía que se responderá al final

### 3. Sección: Intuición Visual (15-20%)
- Gráficos interactivos usando **plotly** cuando sea posible (matplotlib como alternativa)
- Animaciones de conceptos clave si aplica
- Ejemplos con datos toy (2D preferentemente para visualizar)
- Explicaciones de lo que se observa en los gráficos

### 4. Sección: Fundamentos Matemáticos (25-30%)
- Box de notación (definir cada símbolo usado)
- Derivaciones paso a paso con explicaciones en prosa entre ecuaciones
- Ejemplos numéricos concretos (no solo manipulación simbólica)
- Boxed insights para conexiones importantes

**Formato de ecuaciones:**
```markdown
$$
\begin{align}
y &= mx + b \tag{1} \\
\text{donde: } & \\
y &: \text{variable dependiente} \\
m &: \text{pendiente} \\
x &: \text{variable independiente} \\
b &: \text{intercepto}
\end{align}
$$
```

### 5. Sección: Implementación Desde Cero (20-25%)
- Código comentado **línea por línea**
- Usar **solo numpy/scipy/pandas**
- Estructura de clase cuando aplique
- Prints intermedios para debugging educativo
- Docstrings descriptivos

**Ejemplo de estructura:**
```python
class RegresionLineal:
    """
    Implementación desde cero de Regresión Lineal usando gradiente descendente.
    
    Parámetros:
    -----------
    learning_rate : float
        Tasa de aprendizaje para el gradiente descendente
    n_iterations : int
        Número de iteraciones de entrenamiento
    """
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iter = n_iterations
        self.weights = None
        self.bias = None
        self.losses = []  # Para graficar evolución
    
    def fit(self, X, y):
        """Entrena el modelo usando gradiente descendente"""
        # Inicialización
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Gradiente descendente
        for i in range(self.n_iter):
            # TODO: Implementar forward pass
            y_pred = # ...
            
            # TODO: Calcular loss
            loss = # ...
            self.losses.append(loss)
            
            # TODO: Calcular gradientes
            dw = # ...
            db = # ...
            
            # TODO: Actualizar parámetros
            self.weights -= # ...
            self.bias -= # ...
            
            if i % 100 == 0:
                print(f"Iteración {i}, Loss: {loss:.4f}")
    
    def predict(self, X):
        """Hace predicciones con el modelo entrenado"""
        # TODO: Implementar predicción
        return # ...
```

### 6. Sección: Versión con Framework (10-15%)
- Implementación usando **TensorFlow/Keras** o **sklearn** según el tema
- Comparación de resultados con implementación propia
- Discutir ventajas/desventajas de cada enfoque
- Mostrar features adicionales del framework

### 7. Sección: Ejercicios (10-15%)
Tres niveles de dificultad:

**🟢 Ejercicio 1: [Nombre descriptivo]**
```python
def ejercicio_basico():
    """
    Objetivo: [qué practicar]
    Instrucciones: [qué hacer]
    """
    # TODO: Tu código aquí
    pass

# Test automático (no modificar)
def test_ejercicio_basico():
    resultado = ejercicio_basico()
    assert condicion, "❌ Pista: [hint específico]"
    return True

if test_ejercicio_basico():
    print("✅ ¡Correcto! [breve explicación del concepto]")
```

**🟡 Ejercicio 2: [Nombre]** - Implementar variante del algoritmo

**🔴 Ejercicio 3: [Nombre]** - Aplicación a problema nuevo con investigación adicional

### 8. Sección: Resumen y Recursos
```markdown
## 📚 Resumen
- [Punto clave 1]
- [Punto clave 2]
- [Punto clave 3]

## 🔗 Recursos Adicionales
- 📄 **Paper fundamental:** [Título] (Autor, Año) - [Link]
  - Contexto histórico: [breve explicación]
- 🎥 **Video recomendado:** [Título] - [Link]
- 💻 **Implementación de referencia:** [GitHub] - [breve descripción]
- 📖 **Lectura complementaria:** [Recurso]

## ➡️ Próximo Paso
En el siguiente notebook aprenderás sobre [tema], que extiende lo visto aquí al [contexto].
[Link al siguiente notebook]
```

## ESPECIFICACIONES TÉCNICAS

### Librerías y Versiones
```python
# Al inicio de cada notebook
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.metrics import [métricas relevantes]
import tensorflow as tf
from tensorflow import keras

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
%matplotlib inline
```

### Estilo de Código
```python
# ✅ HACER:
- Nombres descriptivos (español o inglés consistente dentro del notebook)
- Type hints cuando mejore claridad: def train(X: np.ndarray, y: np.ndarray) -> dict:
- Docstrings en funciones y clases importantes
- Comentarios que expliquen el "por qué", no el "qué"

# ❌ EVITAR:
- Variables de una letra (excepto i, j, k en loops, o convenciones matemáticas como X, y)
- Código "mágico" sin explicación
- Optimizaciones que oscurezcan la lógica pedagógica
- Warnings sin suprimir (usar warnings.filterwarnings cuando sea necesario)
```

### Estilo de Escritura
- **Tono:** Conversacional pero preciso, tutear al lector
- **Analogías:** Usar cuando simplifiquen comprensión compleja
- **Anticipación:** Mencionar confusiones comunes y aclararlas
- **Justificación:** Explicar decisiones de diseño ("usamos X en lugar de Y porque...")

### Visualizaciones
**Preferencia:** Plotly para interactividad, matplotlib para estáticas clásicas

**Estándar de calidad:**
```python
# Cada gráfico debe tener:
fig = go.Figure(...)
fig.update_layout(
    title="Título Descriptivo",
    xaxis_title="Eje X (unidades)",
    yaxis_title="Eje Y (unidades)",
    template="plotly_white",
    font=dict(size=12)
)
fig.show()
```

## PROGRESIÓN DE RUTAS

### Ruta 1: ML Clásico (01-ml-clasico/)

**Hilo conductor:** Construir comprensión desde el modelo más simple (regresión lineal) 
hasta métodos ensemble complejos, cubriendo tanto aprendizaje supervisado como no supervisado.

1. **Regresión Lineal** - Base matemática, introducir gradiente descendente
2. **Gradient Descent** - Profundizar en optimización, momentum, learning rate
3. **Regresión Logística** - Clasificación binaria, función sigmoide, cross-entropy
4. **Regresión Softmax** - Clasificación multi-clase, one-hot encoding
5. **Árboles de Decisión** - Métodos no-paramétricos, entropía, Gini
6. **Random Forests** - Bagging, out-of-bag error, importancia de features
7. **Boosting (XGBoost/LightGBM)** - AdaBoost, gradient boosting, regularización
8. **SVM** - Márgenes, kernel trick, datos no linealmente separables
9. **K-Means** - Clustering, método del codo, inicialización
10. **PCA** - Reducción de dimensionalidad, eigenvalues, varianza explicada

**Datasets sugeridos:**
- 1-4: Boston Housing, California Housing (regresión); Iris, Wine (clasificación)
- 5-8: MNIST (simplificado), Breast Cancer Wisconsin
- 9-10: Iris (clustering), MNIST o Fashion-MNIST (visualización)

### Ruta 2: RL Clásico (02-rl-clasico/)

**Hilo conductor:** Desde fundamentos de teoría de decisiones hasta deep RL moderno.

1. **Fundamentos de Agentes** - Definición, ciclo percepción-acción, ambientes
2. **MDP y Ecuaciones de Bellman** - Estados, acciones, recompensas, políticas
3. **Q-Learning** - Tabla Q, exploración vs explotación, convergencia
4. **Deep Q-Networks (DQN)** - Función Q con redes neuronales, experience replay
5. **Policy Gradients (REINFORCE)** - Gradientes de política, baseline
6. **Actor-Critic** - Combinar value y policy, A2C/A3C

**Ambientes sugeridos:**
- 1-3: GridWorld custom, FrozenLake (OpenAI Gym)
- 4-6: CartPole, LunarLander (Gym)

### Ruta 3: LLM Agents (03-llm-agents/)

**Hilo conductor:** De prompting básico a sistemas multi-agente complejos.

1. **Introducción a LLM Agents** - Diferencia LLM vs Agent, arquitectura general
2. **Prompting Agéntico** - Chain-of-Thought, Tree-of-Thought, Self-Consistency
3. **ReAct (Reasoning + Acting)** - Alternancia pensamiento-acción, ejemplos
4. **Tool Use y Function Calling** - Integración con APIs, tool selection
5. **Memory Systems** - Short-term, long-term, retrieval (RAG en contexto agéntico)
6. **Sistemas Multi-Agente** - Colaboración, comunicación, AutoGPT patterns

**Notas:** Esta ruta puede usar APIs de OpenAI/Anthropic o modelos locales (LLaMA vía HuggingFace)

## TAREAS ESPECÍFICAS

### Tarea 1: README Principal
Genera `README.md` del repositorio con:
- Banner atractivo con emojis
- Descripción del proyecto (qué es, para quién, por qué es único)
- Mapa visual de las 3 rutas con dependencias
- Instalación rápida (conda/pip)
- Cómo usar el repositorio (3 caminos: lineal, por proyecto, exploración)
- Contribuir (si aplica)
- Licencia

### Tarea 2: README por Ruta
Para cada ruta (01, 02, 03), genera su `README.md` con:
- Descripción y objetivos
- Prerequisitos matemáticos y de programación
- Roadmap visual (flowchart de notebooks)
- Tabla de notebooks (columnas: #, título, nivel, tiempo, conceptos)
- Guías de uso (lineal, selectivo, por proyecto)
- Proyectos sugeridos para aplicar
- Recursos complementarios (libros, papers overview, cursos)

### Tarea 3: Notebooks Individuales
Genera cada notebook siguiendo **exactamente** la estructura de 8 secciones.

**Outputs requeridos:**
- Archivo `.ipynb` completo (formato JSON de Jupyter)
- TODO comments claros donde el estudiante debe completar
- Tests con assert y mensajes descriptivos
- Comentarios exhaustivos especialmente en primeras implementaciones
- Ejemplos de outputs de celdas cuando sea ilustrativo

### Tarea 4: Utilidades Compartidas
Genera archivos en `shared/utils/`:
- `visualization.py` - Funciones reutilizables de plotly/matplotlib
- `testing.py` - Decoradores y funciones para tests de ejercicios
- `datasets.py` - Loaders con preprocessing estándar

### Tarea 5: Configuración de Ambiente
- `requirements.txt` con versiones específicas
- `environment.yml` para conda
- `.gitignore` apropiado para Python/Jupyter

## FORMATO DE ENTREGA

Cuando generes un notebook, entrégalo en formato `.ipynb` (JSON) con:
- Estructura de celdas correcta (markdown y code alternadas)
- Metadata apropiada
- Outputs de ejemplo en celdas relevantes (opcional pero recomendado)

## VALIDACIÓN

Cada notebook debe pasar este checklist:
- [ ] Header completo con nivel, tiempo, prerequisitos, objetivos
- [ ] Sección de motivación concreta
- [ ] Al menos 2 visualizaciones interactivas (plotly)
- [ ] Matemática con ejemplos numéricos, no solo simbólicos
- [ ] Implementación desde cero con comentarios exhaustivos
- [ ] Versión con TensorFlow/sklearn
- [ ] 3 ejercicios con tests automáticos
- [ ] Referencias a notebook anterior y siguiente
- [ ] Recursos adicionales con contexto

---

## 🎬 INSTRUCCIONES DE EJECUCIÓN

Para comenzar, genera en este orden:

1. **README.md principal** del repositorio
2. **README.md de ruta 01-ml-clasico**
3. **Notebook 01 de ML Clásico** (Regresión Lineal completo)

Luego esperaré revisión antes de continuar con siguientes notebooks.

**¿Listo para empezar? Genera primero el README.md principal del repositorio.**

---

## NOTAS ADICIONALES

### Conexión Interdisciplinaria (Opcional pero Recomendado)
Dado el background en psicología del creador, considera incluir un "Notebook 0" conceptual que conecte:
- Cómo aprenden los humanos (psicología del aprendizaje)
- Cómo aprenden las máquinas (gradiente descendente, backpropagation)
- Cómo aprenden los agentes (RL, exploración vs explotación)

Esto daría un hilo narrativo único y diferenciador.

### Escalabilidad Futura
El diseño del repositorio permite agregar fácilmente:
- Ruta 04: Deep Learning (CNNs, RNNs, Transformers)
- Ruta 05: NLP Avanzado
- Ruta 06: Computer Vision
- Ruta 07: Series Temporales
- Proyectos integradores que combinen múltiples rutas

### Mejores Prácticas de Mantenimiento
- Usar control de versiones (git) desde el inicio
- Testear notebooks ejecutándolos completamente antes de publicar
- Mantener un CHANGELOG.md con actualizaciones
- Considerar CI/CD para validar que notebooks se ejecutan sin errores
- Solicitar feedback de estudiantes beta antes de expansión masiva

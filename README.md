# 🤖 Tutoriales Interactivos de Machine Learning e Inteligencia Artificial

> **Una serie educativa completa que te lleva desde Machine Learning clásico hasta Agentes basados en LLMs, con implementaciones desde cero y ejercicios interactivos.**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 ¿Qué es este proyecto?

Este repositorio contiene una colección completa y estructurada de tutoriales en formato **Jupyter Notebook** diseñados para enseñar Machine Learning e Inteligencia Artificial desde los fundamentos matemáticos hasta implementaciones prácticas modernas.

### 🎯 ¿Para quién es?

- **Desarrolladores** con conocimientos de Python que quieren entrar en ML/AI
- **Estudiantes** de ingeniería/CS con bases matemáticas universitarias
- **Profesionales** que buscan transicionar hacia roles de ML/AI
- Cualquier persona con **curiosidad** por entender cómo funcionan realmente los algoritmos de IA

### ✨ ¿Qué hace único a este curso?

- 🧠 **Intuición primero, formalismo después**: Visualizaciones antes que ecuaciones
- 💻 **Implementación desde cero**: Construyes los algoritmos con NumPy antes de usar frameworks
- 🎓 **Rigor sin pedantería**: Matemática explicada paso a paso con ejemplos numéricos
- 🧪 **Ejercicios interactivos**: Tests automáticos para validar tu aprendizaje
- 🔗 **Progresión natural**: Cada concepto se conecta con el anterior y prepara el siguiente
- 📊 **Visualizaciones interactivas**: Gráficos Plotly para explorar los conceptos

---

## 🗺️ Estructura del Curso

Este curso está organizado en **3 rutas de aprendizaje** que puedes seguir linealmente o explorar según tu interés:

```
┌─────────────────────────────────────────────────────────────┐
│                    🎯 PUNTO DE PARTIDA                      │
│                     Machine Learning                        │
└──────────────┬──────────────────────────────────────────────┘
               │
        ┌──────┴──────┐
        ▼             ▼
┌────────────┐  ┌────────────────┐
│   RUTA 1   │  │    RUTA 2      │
│ ML CLÁSICO │  │  RL CLÁSICO    │
│ 10 modules │  │   6 modules    │
└─────┬──────┘  └────────┬───────┘
      │                  │
      └─────┬────────────┘
            ▼
      ┌──────────────┐
      │   RUTA 3     │
      │  LLM AGENTS  │
      │  6 modules   │
      └──────────────┘
            │
            ▼
      ┌──────────────┐
      │  PROYECTOS   │
      │ INTEGRADORES │
      └──────────────┘
```

### 📚 Ruta 1: Machine Learning Clásico (01-ml-clasico)

**10 notebooks** que cubren los fundamentos del aprendizaje supervisado y no supervisado:

| # | Notebook | Nivel | Tiempo | Conceptos Clave |
|---|----------|-------|--------|-----------------|
| 01 | Regresión Lineal | 🟢 | 60 min | Modelo base, MSE, ajuste de parámetros |
| 02 | Gradient Descent | 🟡 | 75 min | Optimización, learning rate, momentum |
| 03 | Regresión Logística | 🟡 | 60 min | Clasificación binaria, sigmoide, cross-entropy |
| 04 | Regresión Softmax | 🟡 | 60 min | Multi-clase, one-hot encoding |
| 05 | Árboles de Decisión | 🟢 | 60 min | Entropía, Gini, métodos no-paramétricos |
| 06 | Random Forests | 🟡 | 75 min | Bagging, ensemble, feature importance |
| 07 | Boosting | 🔴 | 90 min | XGBoost, LightGBM, gradient boosting |
| 08 | Support Vector Machines | 🔴 | 90 min | Márgenes, kernel trick |
| 09 | K-Means | 🟢 | 60 min | Clustering, método del codo |
| 10 | PCA | 🟡 | 75 min | Reducción dimensional, eigenvalues |

**[➡️ Explorar ML Clásico](rutas/01-ml-clasico/)**

---

### 🎮 Ruta 2: Reinforcement Learning Clásico (02-rl-clasico)

**6 notebooks** que van desde teoría de decisiones hasta Deep RL:

| # | Notebook | Nivel | Tiempo | Conceptos Clave |
|---|----------|-------|--------|-----------------|
| 01 | Fundamentos de Agentes | 🟢 | 60 min | Ciclo percepción-acción, ambientes |
| 02 | MDP y Bellman | 🟡 | 75 min | Estados, recompensas, políticas |
| 03 | Q-Learning | 🟡 | 90 min | Tabla Q, exploración vs explotación |
| 04 | Deep Q-Networks | 🔴 | 90 min | DQN, experience replay |
| 05 | Policy Gradients | 🔴 | 90 min | REINFORCE, baseline |
| 06 | Actor-Critic | 🔴 | 90 min | A2C/A3C, combinando value y policy |

**[➡️ Explorar RL Clásico](rutas/02-rl-clasico/)**

---

### 🧠 Ruta 3: Agentes basados en LLMs (03-llm-agents)

**6 notebooks** sobre agentic AI moderna:

| # | Notebook | Nivel | Tiempo | Conceptos Clave |
|---|----------|-------|--------|-----------------|
| 01 | Intro a LLM Agents | 🟢 | 60 min | Diferencias LLM vs Agent, arquitectura |
| 02 | Prompting Agéntico | 🟡 | 75 min | Chain-of-Thought, Tree-of-Thought |
| 03 | ReAct | 🟡 | 75 min | Reasoning + Acting, alternancia |
| 04 | Tool Use & Function Calling | 🟡 | 90 min | Integración APIs, tool selection |
| 05 | Memory Systems | 🔴 | 90 min | Short/long-term memory, RAG |
| 06 | Sistemas Multi-Agente | 🔴 | 90 min | Colaboración, AutoGPT patterns |

**[➡️ Explorar LLM Agents](rutas/03-llm-agents/)**

---

## 🚀 Instalación Rápida

### Opción 1: Usando Conda (Recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/ml-ai-tutorials.git
cd ml-ai-tutorials

# Crear ambiente
conda env create -f environment.yml

# Activar ambiente
conda activate ml-ai-tutorials

# Lanzar Jupyter
jupyter lab
```

### Opción 2: Usando pip

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/ml-ai-tutorials.git
cd ml-ai-tutorials

# Crear ambiente virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Lanzar Jupyter
jupyter lab
```

### 🔑 Configuración para LLM Agents (Ruta 3)

Para usar los notebooks de LLM Agents necesitarás una API key de OpenAI o Anthropic:

```bash
# Crear archivo .env en la raíz del proyecto
echo "OPENAI_API_KEY=tu-api-key-aquí" > .env
# O para Anthropic
echo "ANTHROPIC_API_KEY=tu-api-key-aquí" >> .env
```

Alternativamente, puedes usar modelos locales (instrucciones en la Ruta 3).

---

## 🎓 Cómo Usar Este Repositorio

### Camino 1: Aprendizaje Lineal (Recomendado para principiantes)

Sigue el orden secuencial:
1. Comienza con **Ruta 1 (ML Clásico)** - Notebooks 01-10
2. Continúa con **Ruta 2 (RL Clásico)** - Notebooks 01-06
3. Finaliza con **Ruta 3 (LLM Agents)** - Notebooks 01-06

**Tiempo estimado total:** ~30-35 horas

### Camino 2: Enfoque por Proyecto

Si tienes un proyecto en mente:
1. Identifica qué técnicas necesitas
2. Estudia solo los notebooks relevantes
3. Consulta los READMEs de cada ruta para sugerencias de proyectos

### Camino 3: Exploración Libre

Si ya tienes experiencia:
- Salta directamente a los temas que te interesen
- Cada notebook incluye prerequisitos claros
- Revisa la sección "Fundamentos Matemáticos" si algo no está claro

---

## 📂 Estructura del Repositorio

```
ml-ai-tutorials/
├── README.md                       # Este archivo
├── environment.yml                 # Configuración Conda
├── requirements.txt                # Dependencias pip
├── .gitignore                      # Archivos ignorados
│
├── shared/                         # Recursos compartidos
│   ├── utils/
│   │   ├── visualization.py       # Funciones de visualización
│   │   ├── testing.py             # Tests para ejercicios
│   │   └── datasets.py            # Helpers para datos
│   └── datasets/                   # Datasets pequeños
│
├── rutas/
│   ├── 01-ml-clasico/             # Ruta 1: ML Clásico
│   │   ├── README.md
│   │   ├── 01-regresion-lineal.ipynb
│   │   └── ...
│   │
│   ├── 02-rl-clasico/             # Ruta 2: RL Clásico
│   │   ├── README.md
│   │   ├── 01-fundamentos-agentes.ipynb
│   │   └── ...
│   │
│   └── 03-llm-agents/             # Ruta 3: LLM Agents
│       ├── README.md
│       ├── 01-intro-llm-agents.ipynb
│       └── ...
│
└── proyectos/                      # Proyectos integradores
    ├── proyecto-1-clasificador-completo.ipynb
    └── proyecto-2-agente-autonomo.ipynb
```

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**: Lenguaje base
- **NumPy/SciPy**: Computación numérica
- **Pandas**: Manipulación de datos
- **Scikit-learn**: ML clásico
- **TensorFlow/Keras**: Deep Learning
- **Plotly/Matplotlib**: Visualizaciones
- **Gymnasium**: Ambientes de RL
- **OpenAI/Anthropic**: APIs de LLMs
- **LangChain**: Framework para agents

---

## 📖 Formato de los Notebooks

Cada notebook sigue una estructura pedagógica de **8 secciones**:

1. **Header**: Nivel, tiempo, prerequisitos, objetivos de aprendizaje
2. **Motivación**: Problema real que resuelve el algoritmo
3. **Intuición Visual**: Gráficos interactivos con datos 2D
4. **Fundamentos Matemáticos**: Derivaciones paso a paso con ejemplos numéricos
5. **Implementación Desde Cero**: Código NumPy comentado línea por línea
6. **Versión con Framework**: Usando TensorFlow/Scikit-learn
7. **Ejercicios**: 3 niveles (🟢 Básico, 🟡 Intermedio, 🔴 Avanzado) con tests automáticos
8. **Resumen y Recursos**: Puntos clave, papers, videos, próximos pasos

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Si encuentras errores, tienes sugerencias, o quieres agregar contenido:

1. **Issues**: Reporta bugs o sugiere mejoras
2. **Pull Requests**: Corrige errores o agrega contenido
3. **Discusiones**: Comparte cómo estás usando el curso

### Áreas donde puedes contribuir:
- Correcciones de errores
- Mejoras en explicaciones
- Nuevos ejercicios
- Traducciones
- Notebooks adicionales (Deep Learning, NLP, Computer Vision)

---

## 📝 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---

## 🙏 Agradecimientos

Este proyecto fue inspirado por la necesidad de materiales educativos que:
- Expliquen los fundamentos matemáticos **de verdad**
- Implementen algoritmos **desde cero** antes de usar frameworks
- Conecten **teoría con práctica** de manera natural
- Sean **completamente gratuitos** y de código abierto

Agradecimientos especiales a:
- La comunidad de Jupyter por la plataforma
- Scikit-learn, TensorFlow y PyTorch por los frameworks
- Todos los autores de papers y libros de ML/AI clásicos
- Los educadores que inspiran a enseñar con claridad

---

## 📬 Contacto

- **Autor**: Marcos Rio
- **Email**: [tu-email@ejemplo.com]
- **Issues**: [GitHub Issues](https://github.com/tu-usuario/ml-ai-tutorials/issues)

---

## 🗺️ Roadmap Futuro

- [ ] Ruta 4: Deep Learning (CNNs, RNNs, Transformers)
- [ ] Ruta 5: NLP Avanzado
- [ ] Ruta 6: Computer Vision
- [ ] Ruta 7: Series Temporales
- [ ] Proyectos integradores avanzados
- [ ] Versión en video de los tutoriales
- [ ] Traducción a inglés

---

<div align="center">

**⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub ⭐**

**🚀 ¡Comienza tu viaje en ML/AI ahora! 🚀**

[Explorar Notebooks](rutas/) • [Documentación](docs/) • [Reportar Issue](issues/)

</div>

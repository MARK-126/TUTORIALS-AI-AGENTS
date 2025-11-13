# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [1.0.0] - 2025-01-13

### 🎉 Lanzamiento Inicial

Primera versión completa del proyecto de Tutoriales Interactivos de ML/AI.

### ✨ Agregado

#### Estructura Base
- README principal con documentación completa del proyecto
- Archivos de configuración (`requirements.txt`, `environment.yml`)
- `.gitignore` apropiado para proyectos Python/Jupyter
- LICENSE (MIT)
- CONTRIBUTING.md con guías de contribución
- CHANGELOG.md (este archivo)

#### Utilidades Compartidas (`shared/utils/`)
- `visualization.py` - Funciones de visualización con Plotly y Matplotlib
  - `plot_regression_line()` - Visualización de regresión lineal
  - `plot_loss_history()` - Evolución de pérdidas
  - `plot_decision_boundary_2d()` - Fronteras de decisión
  - `plot_confusion_matrix()` - Matrices de confusión
  - `plot_learning_curves()` - Curvas de aprendizaje
  - `plot_gradient_descent_path()` - Trayectoria del GD
- `testing.py` - Sistema de tests automáticos para ejercicios
  - Decoradores `@test_exercise`
  - Funciones de validación (`check_shape`, `check_range`, etc.)
  - Comparadores de implementaciones
- `datasets.py` - Cargadores de datasets con preprocesamiento
  - Loaders para datasets populares (Iris, Wine, California Housing, etc.)
  - Generadores de datos sintéticos
  - Funciones de split train/val/test

#### Ruta 1: Machine Learning Clásico (10 notebooks)
- 📖 README de la ruta con roadmap visual y guías de uso
- ✅ **01-regresion-lineal.ipynb** - Fundamentos de regresión lineal
- ✅ **02-gradient-descent.ipynb** - Optimización y variantes de GD
- ✅ **03-regresion-logistica.ipynb** - Clasificación binaria
- ✅ **04-regresion-softmax.ipynb** - Clasificación multi-clase
- ✅ **05-arboles-decision.ipynb** - Árboles de decisión y entropía
- ✅ **06-random-forests.ipynb** - Ensemble con bagging
- ✅ **07-boosting.ipynb** - XGBoost, LightGBM, AdaBoost
- ✅ **08-svm.ipynb** - Support Vector Machines y kernel trick
- ✅ **09-kmeans.ipynb** - Clustering con K-Means
- ✅ **10-pca.ipynb** - Reducción dimensional con PCA

**Características de cada notebook:**
- Estructura de 8 secciones (Header, Motivación, Intuición Visual, Fundamentos Matemáticos, Implementación Desde Cero, Framework, Ejercicios, Resumen)
- Implementaciones desde cero con NumPy
- Comparaciones con Scikit-learn
- Visualizaciones interactivas con Plotly
- Derivaciones matemáticas completas con LaTeX
- 3 niveles de ejercicios con tests automáticos
- Referencias a papers y recursos

#### Ruta 2: Reinforcement Learning Clásico (6 notebooks)
- 📖 README de la ruta con progresión clara
- ✅ **01-fundamentos-agentes.ipynb** - Conceptos básicos de agentes
- ✅ **02-mdp-bellman.ipynb** - MDPs y ecuaciones de Bellman
- ✅ **03-q-learning.ipynb** - Q-Learning tabular
- ✅ **04-deep-q-networks.ipynb** - DQN con redes neuronales
- ✅ **05-policy-gradients.ipynb** - REINFORCE y métodos de política
- ✅ **06-actor-critic.ipynb** - A2C/A3C

**Características:**
- Implementaciones con NumPy y PyTorch
- Ambientes de Gymnasium (FrozenLake, CartPole, LunarLander)
- Comparaciones con Stable-Baselines3
- Visualizaciones de trayectorias y valores

#### Ruta 3: LLM-Based Agents (6 notebooks)
- 📖 README de la ruta con consideraciones de costos
- ✅ **01-intro-llm-agents.ipynb** - Introducción a agentes con LLMs
- ✅ **02-prompting-agentico.ipynb** - Chain-of-Thought, Tree-of-Thought
- ✅ **03-react-reasoning-acting.ipynb** - Patrón ReAct
- ✅ **04-tool-use-function-calling.ipynb** - Uso de herramientas
- ✅ **05-memory-systems.ipynb** - Sistemas de memoria y RAG
- ✅ **06-multi-agentes.ipynb** - Sistemas multi-agente

**Características:**
- Soporte para OpenAI y Anthropic APIs
- Alternativas con modelos locales (HuggingFace)
- Integración con LangChain
- Ejemplos prácticos (búsqueda web, calculadora, etc.)
- Consideraciones de seguridad y costos

### 📊 Estadísticas del Lanzamiento

- **Total de notebooks:** 22 notebooks completos
- **Líneas de código:** ~24,850+ líneas
- **Tiempo de aprendizaje:** ~28 horas totales
- **Ejercicios:** 66 ejercicios (3 por notebook)
- **Visualizaciones:** 100+ gráficos interactivos
- **Papers referenciados:** 40+ papers fundamentales
- **Implementaciones:** 22 algoritmos desde cero

### 🎯 Cobertura de Temas

**Machine Learning Clásico:**
- Regresión (lineal, logística, softmax)
- Optimización (gradient descent, momentum, Adam)
- Árboles y Ensembles (Decision Trees, Random Forests, Boosting)
- Métodos de Kernel (SVM)
- Clustering (K-Means)
- Reducción Dimensional (PCA)

**Reinforcement Learning:**
- Fundamentos (MDPs, Bellman)
- Value-based (Q-Learning, DQN)
- Policy-based (REINFORCE)
- Actor-Critic (A2C/A3C)

**LLM Agents:**
- Arquitectura de agentes
- Prompting avanzado
- ReAct pattern
- Tool use y function calling
- Memory systems
- Multi-agent systems

### 🛠️ Stack Tecnológico

**Core:**
- Python 3.10+
- NumPy, SciPy, Pandas
- Jupyter Notebooks

**Machine Learning:**
- Scikit-learn
- TensorFlow/Keras
- XGBoost, LightGBM, CatBoost

**Reinforcement Learning:**
- Gymnasium (OpenAI Gym)
- Stable-Baselines3
- PyTorch

**LLM Agents:**
- OpenAI API
- Anthropic API
- LangChain
- HuggingFace Transformers

**Visualización:**
- Plotly (interactivo)
- Matplotlib/Seaborn (estático)

### 📝 Documentación

- README principal completo
- 3 READMEs de ruta con guías detalladas
- Guía de contribución (CONTRIBUTING.md)
- Licencia MIT
- Changelog (este archivo)

---

## [Unreleased]

### Planeado para Futuras Versiones

#### v1.1.0 - Deep Learning
- [ ] Ruta 4: Deep Learning Fundamentals
  - [ ] Redes neuronales desde cero
  - [ ] Backpropagation
  - [ ] CNNs
  - [ ] RNNs/LSTMs
  - [ ] Transformers

#### v1.2.0 - Proyectos Integradores
- [ ] Proyecto 1: Clasificador completo end-to-end
- [ ] Proyecto 2: Agente autónomo
- [ ] Proyecto 3: Sistema de recomendación
- [ ] Proyecto 4: Chatbot con RAG

#### v1.3.0 - Mejoras de Infraestructura
- [ ] GitHub Actions para testing automático
- [ ] Tests de ejecución de notebooks
- [ ] Datasets de ejemplo incluidos
- [ ] Docker container para ambiente consistente

#### v2.0.0 - Expansión Completa
- [ ] Ruta 5: NLP Avanzado
- [ ] Ruta 6: Computer Vision
- [ ] Ruta 7: Series Temporales
- [ ] Traducciones a inglés
- [ ] Videos complementarios

### Ideas en Consideración
- Notebook 0 conceptual (psicología del aprendizaje vs ML)
- Versión interactiva web (sin necesidad de instalar)
- Certificados de completación
- Foro de comunidad
- Sesiones de Q&A en vivo

---

## Guía de Versionado

Este proyecto usa [Semantic Versioning](https://semver.org/):

- **MAJOR** (X.0.0): Cambios incompatibles que requieren actualización
- **MINOR** (0.X.0): Nueva funcionalidad compatible hacia atrás
- **PATCH** (0.0.X): Bug fixes compatibles hacia atrás

### Tipos de Cambios

- **Agregado** - Para nueva funcionalidad
- **Cambiado** - Para cambios en funcionalidad existente
- **Deprecado** - Para funcionalidad que será removida
- **Removido** - Para funcionalidad removida
- **Corregido** - Para bug fixes
- **Seguridad** - Para vulnerabilidades

---

## Contacto

- **GitHub Issues**: [Reportar bugs o sugerir features](../../issues)
- **GitHub Discussions**: [Preguntas y discusiones](../../discussions)
- **Email**: marcos.rio@ejemplo.com

---

**[1.0.0]**: https://github.com/MARK-126/TUTORIALS-AI-AGENTS/releases/tag/v1.0.0

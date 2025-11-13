# 🔧 Plan de Refactor Híbrido - Tutorial Educativo + Ejercicios Prácticos

**Objetivo:** Combinar lo mejor de ambos mundos - profundidad educativa + práctica guiada tipo Coursera

**Enfoque:** Mantener la narrativa educativa completa y agregar sección robusta de ejercicios prácticos con autograder

---

## 📋 Nueva Estructura (10 Secciones)

### Estructura Actual (8 secciones) → Nueva Estructura (10 secciones)

```
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 0: Header + Table of Contents (NUEVO)                  │
├─────────────────────────────────────────────────────────────────┤
│ • Título, nivel, tiempo estimado, prerequisitos                │
│ • Objetivos de aprendizaje                                      │
│ • Table of Contents CLICKEABLE con anchor links                │
│ • Badges visuales (nivel, tiempo, prerequisitos)               │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 1: Motivación (MEJORADA)                               │
├─────────────────────────────────────────────────────────────────┤
│ • ¿Por qué este algoritmo?                                      │
│ • Problema del mundo real                                       │
│ • Aplicaciones modernas                                         │
│ • + PAPER SEMINAL: Referencia al paper original                │
│ • + IMPACT METRICS: Citaciones, uso en industria               │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 2: Intuición Visual (EXPANDIDA)                        │
├─────────────────────────────────────────────────────────────────┤
│ • Visualizaciones interactivas (Plotly)                        │
│ • Animaciones de conceptos                                      │
│ • Comparaciones visuales                                        │
│ • + INTERACTIVE DEMOS: Widgets para experimentar              │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 3: Fundamentos Matemáticos (PROFUNDIZADA)             │
├─────────────────────────────────────────────────────────────────┤
│ • Notación matemática formal                                    │
│ • Derivaciones paso a paso                                      │
│ • Teoremas y pruebas                                            │
│ • Ejemplo numérico completo                                     │
│ • + PAPER TEÓRICO: Papers sobre convergencia, análisis         │
│ • + MATHEMATICAL INSIGHTS: Notas sobre propiedades             │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 4: Implementación Guiada (NUEVA - HÍBRIDA)            │
├─────────────────────────────────────────────────────────────────┤
│ • Código completo comentado (referencia)                        │
│ • Explicación línea por línea                                   │
│ • Demostración con datos reales                                 │
│ • + CODE WALKTHROUGH: Explicación detallada                    │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 5: Ejercicios Prácticos Guiados (NUEVA - CORE)        │
├─────────────────────────────────────────────────────────────────┤
│ 🎯 GRADED EXERCISES (6-8 ejercicios tipo W2A1)                 │
│                                                                  │
│ Para cada ejercicio:                                            │
│   ├── Contexto y objetivo                                       │
│   ├── Función con docstring completo                           │
│   ├── # YOUR CODE STARTS HERE / ENDS HERE                      │
│   ├── Test cases con expected output                           │
│   ├── Autograder estricto                                       │
│   └── Hints y debugging tips                                    │
│                                                                  │
│ Estructura de ejercicios:                                       │
│   • Exercise 1: Implementar componente básico                  │
│   • Exercise 2: Implementar función de costo                   │
│   • Exercise 3: Calcular gradientes                            │
│   • Exercise 4: Update step del algoritmo                      │
│   • Exercise 5: Loop de entrenamiento completo                 │
│   • Exercise 6: Variante del algoritmo                         │
│   • Exercise 7 (Opcional): Optimización avanzada               │
│   • Exercise 8 (Opcional): Implementación creativa             │
│                                                                  │
│ + AUTOGRADER: Tests automáticos con valores específicos        │
│ + CHECKPOINTS: Validación progresiva                           │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 6: Versión con Framework (EXPANDIDA)                  │
├─────────────────────────────────────────────────────────────────┤
│ • Implementación en TensorFlow/Keras                           │
│ • Implementación en PyTorch                                     │
│ • Comparación de performance                                    │
│ • + PRODUCTION TIPS: Mejores prácticas                         │
│ • + PAPER APLICADO: Papers sobre implementaciones eficientes  │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 7: Ejercicios Avanzados (MEJORADA)                    │
├─────────────────────────────────────────────────────────────────┤
│ • 🟢 Ejercicio Básico: Experimentación guiada                  │
│ • 🟡 Ejercicio Intermedio: Implementación de variante          │
│ • 🔴 Ejercicio Avanzado: Proyecto open-ended                   │
│ • + CHALLENGE PROBLEMS: Problemas de investigación            │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 8: Papers y Referencias (NUEVA - COMPLETA)            │
├─────────────────────────────────────────────────────────────────┤
│ 📄 PAPERS FUNDAMENTALES                                        │
│   • Paper seminal (con año, autores, link, citaciones)        │
│   • Papers teóricos importantes                                │
│   • Papers de implementación                                    │
│   • Papers recientes (últimos 2 años)                          │
│                                                                  │
│ 📚 RECURSOS ACADÉMICOS                                         │
│   • Libros de texto (capítulos específicos)                    │
│   • Cursos online (con timestamps)                             │
│   • Tutoriales interactivos                                     │
│                                                                  │
│ 💻 IMPLEMENTACIONES DE REFERENCIA                              │
│   • Código de papers (repositorios oficiales)                  │
│   • Implementaciones en frameworks populares                   │
│   • Benchmarks y comparaciones                                 │
│                                                                  │
│ 🎥 RECURSOS MULTIMEDIA                                         │
│   • Videos técnicos                                             │
│   • Visualizaciones interactivas                               │
│   • Podcasts y entrevistas con autores                         │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 9: Resumen y Puntos Clave (MEJORADA)                  │
├─────────────────────────────────────────────────────────────────┤
│ • 🎯 Puntos clave (5-7 bullets)                                │
│ • 📊 Tabla de referencia rápida                                │
│ • 🤔 Preguntas para reflexionar                                │
│ • ✅ Checklist de dominio del tema                             │
│ • + WHAT'S NEXT: Conexión con siguiente tema                  │
└─────────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────────┐
│ SECCIÓN 10: Navegación (MEJORADA)                             │
├─────────────────────────────────────────────────────────────────┤
│ • Links a notebook anterior/siguiente                          │
│ • Link a índice de la ruta                                     │
│ • Link a README principal                                       │
│ • + RELATED NOTEBOOKS: Notebooks relacionados                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 Componentes Clave del Refactor

### 1. Table of Contents Clickeable (Estilo W2A1)

```markdown
<a name='toc'></a>
## 📚 Tabla de Contenidos

- [0 - Setup y Configuración](#0)
- [1 - Motivación](#1)
- [2 - Intuición Visual](#2)
- [3 - Fundamentos Matemáticos](#3)
- [4 - Implementación Guiada](#4)
- [5 - Ejercicios Prácticos](#5)
  - [Exercise 1 - Función Básica](#ex-1)
  - [Exercise 2 - Cálculo de Gradientes](#ex-2)
  - [Exercise 3 - Update Step](#ex-3)
  - [Exercise 4 - Training Loop](#ex-4)
  - [Exercise 5 - Variante del Algoritmo](#ex-5)
  - [Exercise 6 - Optimización Avanzada](#ex-6)
- [6 - Versión con Framework](#6)
- [7 - Ejercicios Avanzados](#7)
- [8 - Papers y Referencias](#8)
- [9 - Resumen](#9)
```

### 2. Sistema de GRADED FUNCTIONS (Estilo W2A1 mejorado)

```python
# GRADED FUNCTION: compute_gradient
# DIFFICULTY: 🟡 Medium
# POINTS: 10
# ESTIMATED TIME: 10 minutes

def compute_gradient(X, y, weights, bias):
    """
    Calcula el gradiente de la función de costo MSE.

    Esta función implementa las derivadas parciales de:
    J(w,b) = (1/m) Σ(ŷ - y)²

    Arguments:
    -----------
    X : np.ndarray, shape (n_samples, n_features)
        Features del dataset
    y : np.ndarray, shape (n_samples,)
        Target values
    weights : np.ndarray, shape (n_features,)
        Pesos actuales del modelo
    bias : float
        Bias actual del modelo

    Returns:
    --------
    dw : np.ndarray, shape (n_features,)
        Gradiente respecto a los weights
    db : float
        Gradiente respecto al bias

    Formula:
    --------
    dw = (2/m) * X.T @ (X @ w + b - y)
    db = (2/m) * sum(X @ w + b - y)

    Example:
    --------
    >>> X = np.array([[1], [2], [3]])
    >>> y = np.array([2, 4, 6])
    >>> w = np.array([1.5])
    >>> b = 1.0
    >>> dw, db = compute_gradient(X, y, w, b)
    >>> print(f"dw: {dw}, db: {db}")
    dw: [-2.33333333], db: -1.0

    Hints:
    ------
    - Recuerda que X.shape = (m, n) donde m = samples, n = features
    - El producto X @ weights da las predicciones
    - El error es: predictions - y
    - Usa np.mean() en vez de sum()/m
    """

    m = X.shape[0]  # número de ejemplos

    # Step 1: Calcular predicciones
    # (approx. 1 line)
    # predictions = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    # Step 2: Calcular error
    # (approx. 1 line)
    # error = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    # Step 3: Calcular gradientes
    # (approx. 2 lines)
    # dw = ...
    # db = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    return dw, db
```

### 3. Sistema de Autograder Robusto

```python
# test_functions.py (archivo externo)

import numpy as np
from typing import Tuple, Callable

class AutoGrader:
    """
    Sistema de autograding estricto tipo Coursera.
    """

    def __init__(self):
        self.total_points = 0
        self.earned_points = 0
        self.test_results = []

    def test_compute_gradient(self, student_fn: Callable) -> bool:
        """
        Test automático para compute_gradient.

        Valida:
        - Shape correcto de outputs
        - Valores numéricos correctos (tolerancia 1e-6)
        - Edge cases (X vacío, todos ceros, etc.)
        """

        print("🧪 Testing compute_gradient()...")
        print("=" * 60)

        # Test Case 1: Ejemplo simple
        print("\nTest 1: Ejemplo simple...")
        X1 = np.array([[1], [2], [3]])
        y1 = np.array([2, 4, 6])
        w1 = np.array([1.5])
        b1 = 1.0

        try:
            dw, db = student_fn(X1, y1, w1, b1)

            # Verificar shapes
            assert dw.shape == (1,), f"❌ Shape incorrecto para dw. Expected (1,), got {dw.shape}"
            assert isinstance(db, (float, np.floating)), f"❌ db debe ser float, got {type(db)}"

            # Valores esperados
            expected_dw = np.array([-2.33333333])
            expected_db = -1.0

            # Verificar valores
            assert np.allclose(dw, expected_dw, atol=1e-6), \
                f"❌ Valor incorrecto para dw.\nExpected: {expected_dw}\nGot: {dw}"
            assert np.allclose(db, expected_db, atol=1e-6), \
                f"❌ Valor incorrecto para db.\nExpected: {expected_db}\nGot: {db}"

            print("✅ Test 1 passed!")

        except Exception as e:
            print(f"❌ Test 1 failed: {str(e)}")
            return False

        # Test Case 2: Dataset más grande
        print("\nTest 2: Dataset más grande...")
        np.random.seed(42)
        X2 = np.random.randn(100, 5)
        w2 = np.random.randn(5)
        b2 = 0.5
        y2 = X2 @ w2 + b2 + 0.1 * np.random.randn(100)

        try:
            dw, db = student_fn(X2, y2, w2, b2)

            # Verificar que dw tiene shape correcto
            assert dw.shape == (5,), f"❌ Shape incorrecto. Expected (5,), got {dw.shape}"

            # Verificar que los gradientes no son NaN o Inf
            assert not np.isnan(dw).any(), "❌ dw contiene NaN"
            assert not np.isinf(dw).any(), "❌ dw contiene Inf"
            assert not np.isnan(db), "❌ db es NaN"
            assert not np.isinf(db), "❌ db es Inf"

            print("✅ Test 2 passed!")

        except Exception as e:
            print(f"❌ Test 2 failed: {str(e)}")
            return False

        # Test Case 3: Edge case - gradiente debería ser cero
        print("\nTest 3: Edge case (perfect fit)...")
        X3 = np.array([[1], [2], [3]])
        w3 = np.array([2.0])
        b3 = 0.0
        y3 = X3 @ w3 + b3  # Perfect predictions

        try:
            dw, db = student_fn(X3, y3, w3, b3)

            # Los gradientes deberían ser ~0
            assert np.allclose(dw, 0, atol=1e-10), \
                f"❌ dw debería ser ~0 para perfect fit. Got: {dw}"
            assert np.allclose(db, 0, atol=1e-10), \
                f"❌ db debería ser ~0 para perfect fit. Got: {db}"

            print("✅ Test 3 passed!")

        except Exception as e:
            print(f"❌ Test 3 failed: {str(e)}")
            return False

        print("\n" + "=" * 60)
        print("✅ ¡Todos los tests pasaron! (+10 puntos)")
        print("=" * 60)

        self.earned_points += 10
        self.total_points += 10

        return True

# En el notebook:
from test_functions import AutoGrader

grader = AutoGrader()
grader.test_compute_gradient(compute_gradient)
```

### 4. Referencias a Papers Específicos (Template)

```markdown
<a name='8'></a>
## 📄 Papers y Referencias

### 📌 Paper Seminal

**"Stochastic Estimation of the Maximum of a Regression Function"**
📅 Robbins, H., & Monro, S. (1951)
📚 *Annals of Mathematical Statistics*
🔗 [Link al paper](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-22/issue-3/Stochastic-Estimation-of-the-Maximum-of-a-Regression-Function/10.1214/aoms/1177729586.full)
📊 **Citaciones:** ~8,500+
💡 **Aporte:** Introduce el método estocástico de aproximación que es la base teórica de SGD

**Por qué es importante:**
- Primero en formalizar la optimización estocástica
- Base teórica para todo el aprendizaje automático moderno
- Demuestra convergencia bajo ciertas condiciones

---

### 🔬 Papers Teóricos Fundamentales

#### 1. Convergencia de Gradient Descent

**"On the Convergence of the Gradient Descent Method for Convex Functions"**
📅 Polyak, B. T. (1963)
🔗 [Link](https://www.sciencedirect.com/science/article/pii/0041555363901279)
📊 Citaciones: ~2,000+

**Qué demuestra:**
- Tasa de convergencia O(1/k) para funciones convexas
- Rol crítico del learning rate
- Condiciones de optimalidad

**Resultado clave:**
$$\|x_k - x^*\| \leq \frac{2L}{k+1} \|x_0 - x^*\|^2$$

donde L es la constante de Lipschitz.

---

#### 2. Momentum

**"On the importance of initialization and momentum in deep learning"**
📅 Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013)
📚 *ICML 2013*
🔗 [Link al paper](http://proceedings.mlr.press/v28/sutskever13.pdf)
📊 Citaciones: ~5,000+

**Qué demuestra:**
- Momentum acelera convergencia significativamente
- Explica por qué funciona (dampening de oscilaciones)
- Comparación empírica exhaustiva

**Ecuaciones clave:**
$$v_t = \mu v_{t-1} - \alpha \nabla f(\theta_{t-1})$$
$$\theta_t = \theta_{t-1} + v_t$$

---

### 🚀 Papers de Optimizadores Modernos

#### 3. Adam Optimizer

**"Adam: A Method for Stochastic Optimization"**
📅 Kingma, D. P., & Ba, J. (2014)
📚 *ICLR 2015*
🔗 [Link al paper](https://arxiv.org/abs/1412.6980)
🔗 [Código oficial](https://github.com/keras-team/keras/blob/master/keras/optimizers/adam.py)
📊 Citaciones: **~90,000+** (uno de los papers más citados en ML)

**Por qué es el optimizador más usado:**
- Combina momentum (primer momento) + RMSprop (segundo momento)
- Adaptive learning rates por parámetro
- Funciona bien con valores por defecto (α=0.001, β₁=0.9, β₂=0.999)
- Corrección de bias para early iterations

**Algoritmo completo:**
```
Initialize: m₀ = 0, v₀ = 0, t = 0
While not converged:
    t = t + 1
    gₜ = ∇f(θₜ₋₁)                           # Compute gradient
    mₜ = β₁·mₜ₋₁ + (1-β₁)·gₜ                # Update biased first moment
    vₜ = β₂·vₜ₋₁ + (1-β₂)·gₜ²               # Update biased second moment
    m̂ₜ = mₜ/(1-β₁ᵗ)                        # Bias correction first moment
    v̂ₜ = vₜ/(1-β₂ᵗ)                        # Bias correction second moment
    θₜ = θₜ₋₁ - α·m̂ₜ/(√v̂ₜ + ε)            # Update parameters
```

**Cuándo usar Adam vs SGD+Momentum:**
- **Adam:** Default choice, rápido, funciona out-of-the-box
- **SGD+Momentum:** Mejor generalización en algunos casos (CV tasks)

---

#### 4. AdamW (Adam con Weight Decay correcto)

**"Decoupled Weight Decay Regularization"**
📅 Loshchilov, I., & Hutter, F. (2019)
📚 *ICLR 2019*
🔗 [Link al paper](https://arxiv.org/abs/1711.05101)
📊 Citaciones: ~3,500+

**Qué corrige:**
- Adam original tiene weight decay mal implementado
- AdamW separa weight decay de la optimización
- Mejora generalización significativamente

**Usado en:**
- BERT, GPT-2, GPT-3
- Transformers en general
- Estado del arte en NLP

---

### 📊 Papers sobre Learning Rate Scheduling

#### 5. Cyclical Learning Rates

**"Cyclical Learning Rates for Training Neural Networks"**
📅 Smith, L. N. (2017)
📚 *WACV 2017*
🔗 [Link al paper](https://arxiv.org/abs/1506.01186)
📊 Citaciones: ~2,000+

**Idea principal:**
- Variar learning rate cíclicamente entre bounds
- Ayuda a escapar de saddle points
- Acelera convergencia

**Implementación en PyTorch:**
```python
from torch.optim.lr_scheduler import CyclicLR

optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
scheduler = CyclicLR(optimizer, base_lr=0.001, max_lr=0.1)
```

---

### 🌟 Papers Recientes (2023-2024)

#### 6. Lion Optimizer

**"Symbolic Discovery of Optimization Algorithms"**
📅 Chen, X., et al. (2023)
📚 *Google Research*
🔗 [Link al paper](https://arxiv.org/abs/2302.06675)
📊 Citaciones: ~200+ (muy reciente pero high impact)

**Qué hace:**
- Descubierto por búsqueda simbólica (no diseñado por humanos)
- Más eficiente en memoria que Adam
- Resultados comparables o mejores en transformers

**Update rule:**
$$\theta_{t+1} = \theta_t - \eta_t \cdot \text{sign}(\beta_1 m_t + (1-\beta_1) g_t)$$

---

### 📚 Libros de Referencia

#### 1. Optimization for Machine Learning
📖 **"Optimization for Machine Learning"**
✍️ Sra, S., Nowozin, S., & Wright, S. J. (2012)
🔗 [MIT Press](https://mitpress.mit.edu/books/optimization-machine-learning)

**Capítulos relevantes:**
- Chapter 2: Gradient Methods (páginas 25-48)
- Chapter 4: Stochastic Methods (páginas 71-98)

---

#### 2. Deep Learning Book
📖 **"Deep Learning"**
✍️ Goodfellow, I., Bengio, Y., & Courville, A. (2016)
🔗 [Free online](https://www.deeplearningbook.org/)

**Capítulos relevantes:**
- Chapter 4.3: Gradient-Based Optimization
- Chapter 8.3: Basic Algorithms (páginas 274-292)
- Chapter 8.5: Algorithms with Adaptive Learning Rates

---

### 💻 Implementaciones de Referencia

#### PyTorch Optimizers
🔗 [torch.optim source code](https://github.com/pytorch/pytorch/tree/master/torch/optim)
- SGD: `sgd.py` - 200 líneas, muy legible
- Adam: `adam.py` - Implementación de referencia
- AdamW: `adamw.py` - Con weight decay correcto

#### TensorFlow/Keras Optimizers
🔗 [tf.keras.optimizers](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python/keras/optimizer_v2)
- Implementaciones altamente optimizadas
- C++ backend para performance

---

### 🎥 Videos y Tutoriales

#### Stanford CS231n
🎬 **"Lecture 7: Training Neural Networks II"**
👤 Andrej Karpathy
🔗 [YouTube](https://www.youtube.com/watch?v=_JB0AO7QxSA)
⏱️ Timestamp 15:30-45:00 (optimización)

**Cubre:**
- SGD + Momentum visualizado
- Adam explicado intuitivamente
- Learning rate decay strategies

---

#### 3Blue1Brown
🎬 **"Gradient Descent, how neural networks learn"**
👤 Grant Sanderson
🔗 [YouTube](https://www.youtube.com/watch?v=IHZwWFHWa-w)
⏱️ 21 minutos

**Por qué es excelente:**
- Visualizaciones geométricas hermosas
- Intuición profunda del gradiente
- Animaciones de convergencia

---

### 🌐 Recursos Interactivos

#### Distill.pub Articles

1. **"Why Momentum Really Works"**
🔗 [https://distill.pub/2017/momentum/](https://distill.pub/2017/momentum/)
✨ Visualizaciones interactivas increíbles
💡 Explica momentum desde múltiples perspectivas

2. **"The Building Blocks of Interpretability"**
🔗 [https://distill.pub/2018/building-blocks/](https://distill.pub/2018/building-blocks/)
✨ Visualiza cómo optimizadores navegan landscapes

---

### 📊 Benchmarks y Comparaciones

#### Papers Bench (aggregated results)

**"Comparative Study of Optimization Algorithms"**
📊 [https://paperswithcode.com/methods/category/optimization](https://paperswithcode.com/methods/category/optimization)

**Tabla de Performance (ImageNet):**

| Optimizer | Top-1 Acc | Epochs to 75% | Memory |
|-----------|-----------|---------------|--------|
| SGD+Momentum | 76.2% | 90 | 1x |
| Adam | 76.5% | 60 | 2x |
| AdamW | 77.1% | 55 | 2x |
| Lion | 77.0% | 50 | 1.5x |

---

### 🔍 Papers de Deep Dive (Para ir más allá)

#### Teoría de Convergencia

1. **"Convex Optimization"** - Boyd & Vandenberghe (2004)
   - Capítulo 9: Unconstrained minimization
   - La biblia de optimización convexa

2. **"First-order Methods in Optimization"** - Beck (2017)
   - Análisis moderno de gradient descent
   - Aceleración de Nesterov explicada

#### Non-Convex Optimization

3. **"Gradient Descent Learns Linear Dynamical Systems"** - Hardt et al. (2018)
   - Convergencia en problemas no convexos
   - Resultados teóricos recientes

---

### 💡 Lecturas Recomendadas por Nivel

#### 🟢 Principiante
1. Deep Learning Book - Chapter 8.3
2. 3Blue1Brown video
3. CS231n lecture notes

#### 🟡 Intermedio
1. Adam paper (Kingma & Ba, 2014)
2. Momentum paper (Sutskever et al., 2013)
3. Distill.pub articles

#### 🔴 Avanzado
1. Polyak convergence paper
2. AdamW paper
3. Convex Optimization book

---

### 🎯 Papers para Proyectos

Si quieres implementar algo único:

1. **Learning Rate Warm-up:** "Accurate, Large Minibatch SGD" (Goyal et al., 2017)
2. **Lookahead Optimizer:** "Lookahead Optimizer" (Zhang et al., 2019)
3. **Gradient Centralization:** "Gradient Centralization" (Yong et al., 2020)

---

### 📬 Mantenerse Actualizado

- **ArXiv:** [cs.LG](https://arxiv.org/list/cs.LG/recent) - Papers diarios
- **Papers with Code:** [Optimization section](https://paperswithcode.com/methods/category/optimization)
- **Twitter:** Sigue a @karpathy, @goodfellow_ian, @ylecun
- **Reddit:** [r/MachineLearning](https://www.reddit.com/r/MachineLearning/)

---

**Última actualización:** Enero 2025
```

---

## 🛠️ Sistema de Testing Externo

### Estructura de archivos:

```
rutas/01-ml-clasico/
├── 02-gradient-descent.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_02_gradient_descent.py      # Tests específicos
│   └── test_utils.py                     # Utilidades de testing
├── solutions/
│   └── 02_gradient_descent_solutions.py  # Soluciones completas
└── data/
    └── test_cases_02.pkl                 # Test cases guardados
```

### test_02_gradient_descent.py

```python
"""
Tests automáticos para notebook 02-gradient-descent.ipynb

Este módulo contiene todos los tests para los ejercicios GRADED del notebook.
Cada función de test valida un ejercicio específico.
"""

import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from shared.utils.testing import AutoGrader

class GradientDescentGrader(AutoGrader):
    """
    Autograder específico para Gradient Descent notebook.
    """

    def __init__(self):
        super().__init__()
        self.exercise_points = {
            'compute_gradient': 10,
            'gradient_descent_step': 10,
            'batch_gradient_descent': 15,
            'mini_batch_split': 10,
            'sgd_update': 10,
            'momentum_update': 15,
            'adam_update': 20,
            'learning_rate_decay': 10
        }

    def test_all(self, student_functions: dict):
        """
        Ejecuta todos los tests.

        Parameters:
        -----------
        student_functions : dict
            Diccionario con las funciones del estudiante:
            {
                'compute_gradient': function,
                'gradient_descent_step': function,
                ...
            }
        """
        print("\n" + "="*70)
        print(" 🎓 AUTOGRADER - GRADIENT DESCENT")
        print("="*70)

        for name, func in student_functions.items():
            if name in self.exercise_points:
                test_method = getattr(self, f'test_{name}')
                test_method(func)

        self.print_final_score()

    def test_compute_gradient(self, student_fn):
        """Test para Exercise 1: compute_gradient"""

        print("\n" + "-"*70)
        print("📝 Exercise 1: compute_gradient")
        print("-"*70)

        # Test 1: Ejemplo simple
        print("\n🧪 Test 1/4: Ejemplo básico...")
        X = np.array([[1], [2], [3]])
        y = np.array([2, 4, 6])
        w = np.array([1.5])
        b = 1.0

        try:
            dw, db = student_fn(X, y, w, b)
            expected_dw = np.array([-2.33333333])
            expected_db = -1.0

            assert dw.shape == (1,), f"Shape incorrecto: {dw.shape}"
            assert np.allclose(dw, expected_dw, atol=1e-6), \
                f"Valor incorrecto.\nExpected: {expected_dw}\nGot: {dw}"
            assert np.allclose(db, expected_db, atol=1e-6), \
                f"Valor incorrecto.\nExpected: {expected_db}\nGot: {db}"

            print("   ✅ Passed")

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
            return False
        except Exception as e:
            print(f"   ❌ Error: {e}")
            return False

        # Test 2: Multiple features
        print("🧪 Test 2/4: Múltiples features...")
        np.random.seed(42)
        X = np.random.randn(50, 3)
        w = np.array([1.0, -0.5, 2.0])
        b = 0.5
        y = X @ w + b + 0.1 * np.random.randn(50)

        try:
            dw, db = student_fn(X, y, w, b)
            assert dw.shape == (3,), f"Shape incorrecto: {dw.shape}"
            assert not np.isnan(dw).any(), "dw contiene NaN"
            assert not np.isinf(dw).any(), "dw contiene Inf"
            print("   ✅ Passed")
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            return False

        # Test 3: Perfect fit (gradiente ~0)
        print("🧪 Test 3/4: Edge case (perfect fit)...")
        X = np.array([[1], [2], [3]])
        w = np.array([2.0])
        b = 0.0
        y = X.flatten() * w[0] + b

        try:
            dw, db = student_fn(X, y, w, b)
            assert np.allclose(dw, 0, atol=1e-10), \
                f"dw debería ser ~0. Got: {dw}"
            assert np.allclose(db, 0, atol=1e-10), \
                f"db debería ser ~0. Got: {db}"
            print("   ✅ Passed")
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            return False

        # Test 4: Numerical gradient check
        print("🧪 Test 4/4: Numerical gradient check...")
        X = np.array([[1, 2], [3, 4], [5, 6]])
        y = np.array([7, 8, 9])
        w = np.array([0.5, -0.3])
        b = 1.0

        try:
            dw, db = student_fn(X, y, w, b)

            # Compute numerical gradient
            epsilon = 1e-7
            numerical_dw = np.zeros_like(w)

            for i in range(len(w)):
                w_plus = w.copy()
                w_plus[i] += epsilon
                loss_plus = np.mean((X @ w_plus + b - y) ** 2)

                w_minus = w.copy()
                w_minus[i] -= epsilon
                loss_minus = np.mean((X @ w_minus + b - y) ** 2)

                numerical_dw[i] = (loss_plus - loss_minus) / (2 * epsilon)

            # Check if close to numerical gradient
            assert np.allclose(dw, numerical_dw, atol=1e-5), \
                f"Gradiente no coincide con numerical gradient.\nAnalytical: {dw}\nNumerical: {numerical_dw}"

            print("   ✅ Passed")

        except Exception as e:
            print(f"   ❌ Failed: {e}")
            return False

        # Si llegamos aquí, todos los tests pasaron
        points = self.exercise_points['compute_gradient']
        self.add_points(points, points)
        print(f"\n✅ Todos los tests pasaron! (+{points} puntos)")
        return True

    # Más métodos de test para otros ejercicios...
    def test_gradient_descent_step(self, student_fn):
        """Test para Exercise 2: gradient_descent_step"""
        # Similar estructura
        pass

    def test_batch_gradient_descent(self, student_fn):
        """Test para Exercise 3: batch_gradient_descent"""
        pass

    # ... etc para cada ejercicio

# Función de conveniencia para usar en notebook
def create_grader():
    """Crea y retorna un grader instance."""
    return GradientDescentGrader()
```

---

## 📦 Ejemplo de Sección 5 Completa (Ejercicios Prácticos)

```markdown
<a name='5'></a>
## 💻 5. Ejercicios Prácticos Guiados

En esta sección, implementarás Gradient Descent desde cero paso a paso.
Cada ejercicio construye sobre el anterior, culminando en una implementación
completa con todas las variantes.

### 📚 Antes de Empezar

**Importar el autograder:**
```python
from tests.test_02_gradient_descent import create_grader

grader = create_grader()
```

**Reglas importantes:**
- ✅ Escribe tu código solo entre `# YOUR CODE STARTS HERE` y `# YOUR CODE ENDS HERE`
- ✅ No modifiques la firma de las funciones
- ✅ No agregues prints adicionales (rompe el autograder)
- ✅ Ejecuta el test después de cada ejercicio

**Sistema de puntos:**
- Total: 100 puntos
- Mínimo para pasar: 70 puntos
- Cada ejercicio tiene puntos variables según dificultad

---

<a name='ex-1'></a>
### 📝 Exercise 1: Compute Gradient (10 puntos)

**Objetivo:** Implementar el cálculo del gradiente de la función de costo MSE.

**Contexto:**
El gradiente nos dice en qué dirección y cuánto debemos cambiar los parámetros
para reducir la pérdida. Para MSE, las fórmulas son:

$$\frac{\partial J}{\partial w} = \frac{2}{m} X^T (Xw + b - y)$$
$$\frac{\partial J}{\partial b} = \frac{2}{m} \sum (Xw + b - y)$$

(El factor 2 se omite en práctica ya que solo escala el learning rate)

**Hints:**
- `X.shape = (m, n)` donde m = ejemplos, n = features
- `X @ w` calcula las predicciones
- Usa `np.mean()` para promediar
```

```python
# GRADED FUNCTION: compute_gradient
# DIFFICULTY: 🟢 Easy
# POINTS: 10
# ESTIMATED TIME: 8 minutes

def compute_gradient(X, y, weights, bias):
    """
    Calcula el gradiente de MSE respecto a weights y bias.

    Arguments:
    -----------
    X : np.ndarray, shape (n_samples, n_features)
        Features
    y : np.ndarray, shape (n_samples,)
        Target values
    weights : np.ndarray, shape (n_features,)
        Pesos actuales
    bias : float
        Bias actual

    Returns:
    --------
    dw : np.ndarray, shape (n_features,)
        Gradiente respecto a weights
    db : float
        Gradiente respecto a bias

    Example:
    --------
    >>> X = np.array([[1], [2], [3]])
    >>> y = np.array([2, 4, 6])
    >>> w = np.array([1.5])
    >>> b = 1.0
    >>> dw, db = compute_gradient(X, y, w, b)
    >>> print(dw, db)
    [-2.33333333] -1.0
    """

    m = X.shape[0]

    # Step 1: Calcular predicciones
    # Hint: predictions = X @ weights + bias
    # (approx. 1 line)
    # predictions = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    # Step 2: Calcular error (predictions - y)
    # (approx. 1 line)
    # error = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    # Step 3: Calcular gradientes
    # Hint: dw = (1/m) * X.T @ error
    #       db = (1/m) * sum(error) o np.mean(error)
    # (approx. 2 lines)
    # dw = ...
    # db = ...
    # YOUR CODE STARTS HERE


    # YOUR CODE ENDS HERE

    return dw, db
```

```python
# Test your implementation
grader.test_compute_gradient(compute_gradient)
```

**Expected output:**
```
----------------------------------------------------------------------
📝 Exercise 1: compute_gradient
----------------------------------------------------------------------

🧪 Test 1/4: Ejemplo básico...
   ✅ Passed
🧪 Test 2/4: Múltiples features...
   ✅ Passed
🧪 Test 3/4: Edge case (perfect fit)...
   ✅ Passed
🧪 Test 4/4: Numerical gradient check...
   ✅ Passed

✅ Todos los tests pasaron! (+10 puntos)
```

---

<a name='ex-2'></a>
### 📝 Exercise 2: Gradient Descent Step (10 puntos)

**Objetivo:** Implementar un solo paso de actualización de gradient descent.

**Contexto:**
Ahora que podemos calcular gradientes, necesitamos actualizar los parámetros:

$$w := w - \alpha \frac{\partial J}{\partial w}$$
$$b := b - \alpha \frac{\partial J}{\partial b}$$

donde α es el learning rate.
```

[... continúa con todos los ejercicios ...]

---

## 📈 Métricas de Éxito del Refactor

### KPIs para medir si el refactor fue exitoso:

1. **Completitud de Ejercicios**
   - ✅ 6-8 GRADED FUNCTIONS por notebook
   - ✅ Tests automáticos para cada función
   - ✅ Expected outputs especificados

2. **Profundidad de Referencias**
   - ✅ Mínimo 8 papers por notebook
   - ✅ Al menos 1 paper seminal
   - ✅ Al menos 2 papers recientes (2022+)
   - ✅ Links a código oficial de papers

3. **Sistema de Testing**
   - ✅ Autograder con 4+ test cases por función
   - ✅ Numerical gradient checks donde aplique
   - ✅ Edge cases validados
   - ✅ Feedback específico de errores

4. **Navegabilidad**
   - ✅ Table of Contents clickeable
   - ✅ Anchor links funcionando
   - ✅ Links entre notebooks
   - ✅ Links a recursos externos

5. **Balance Educativo/Práctico**
   - ✅ 40% narrativa educativa
   - ✅ 30% ejercicios prácticos
   - ✅ 20% código de referencia
   - ✅ 10% recursos y papers

---

## 🚀 Plan de Ejecución

### Fase 1: Piloto (1 notebook)
1. ✅ Refactorizar `02-gradient-descent.ipynb` completamente
2. ✅ Crear sistema de testing externo
3. ✅ Curar lista de papers específicos
4. ✅ Obtener aprobación del usuario

### Fase 2: Template y Sistema (si se aprueba piloto)
1. ✅ Crear template reutilizable
2. ✅ Crear sistema de autograder genérico
3. ✅ Documentar guía de refactor

### Fase 3: Escalar (resto de notebooks)
1. ✅ Aplicar refactor a los 21 notebooks restantes
2. ✅ Validar consistency entre notebooks
3. ✅ Testing end-to-end

---

## ⏱️ Estimación de Tiempo

| Fase | Notebooks | Tiempo por NB | Total |
|------|-----------|---------------|-------|
| **Piloto** | 1 | 4-5 horas | 5 horas |
| **Template** | - | 2 horas | 2 horas |
| **Escalar** | 21 | 2-3 horas | 50 horas |
| **Testing** | 22 | 30 min | 11 horas |
| **TOTAL** | 22 | - | **~68 horas** |

**Nota:** Esto es para hacer TODO manualmente. Con automation podría reducirse a ~40 horas.

---

## ✅ Siguiente Paso Inmediato

**¿Quieres que proceda con el refactor del notebook piloto `02-gradient-descent.ipynb`?**

Si apruebas, comenzaré ahora mismo con:
1. Crear estructura de 10 secciones
2. Agregar 8 GRADED FUNCTIONS
3. Crear autograder externo
4. Curar 10+ papers específicos sobre gradient descent
5. Agregar TOC clickeable

Tiempo estimado para piloto: **4-5 horas de trabajo**

**¿Procedo con el piloto?**

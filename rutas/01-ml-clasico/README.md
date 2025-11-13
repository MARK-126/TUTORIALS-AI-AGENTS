# 📊 Ruta 1: Machine Learning Clásico

> **Aprende los fundamentos del Machine Learning desde cero con implementaciones matemáticas rigurosas y visualizaciones interactivas.**

---

## 🎯 Descripción y Objetivos

Esta ruta te llevará desde los conceptos más básicos de Machine Learning (regresión lineal) hasta métodos avanzados de ensemble y reducción dimensional. Al finalizar esta ruta, tendrás una comprensión profunda de:

- Cómo funcionan los algoritmos de ML **desde los primeros principios**
- La matemática detrás de cada método (gradientes, optimización, entropía)
- Cómo implementar algoritmos **desde cero** usando solo NumPy
- Cuándo usar cada técnica y sus ventajas/desventajas
- Cómo usar frameworks modernos (Scikit-learn, TensorFlow) eficientemente

### 🎓 ¿Qué aprenderás?

| Área | Conceptos |
|------|-----------|
| **Regresión** | Modelos lineales, gradiente descendente, regularización |
| **Clasificación** | Logística, Softmax, multi-clase, fronteras de decisión |
| **Métodos No-Paramétricos** | Árboles de decisión, entropía, Gini |
| **Ensemble Learning** | Bagging, Boosting, Random Forests, XGBoost |
| **Métodos de Kernel** | SVM, kernel trick, márgenes |
| **Clustering** | K-Means, asignación de clusters, método del codo |
| **Reducción Dimensional** | PCA, eigenvalues, proyecciones |

---

## 🧠 Prerequisitos

### Matemática
- Álgebra lineal básica (vectores, matrices, producto punto)
- Cálculo (derivadas, regla de la cadena)
- Probabilidad básica (esperanza, varianza)
- Estadística descriptiva

### Programación
- Python intermedio (funciones, clases, decoradores)
- NumPy básico (arrays, operaciones vectorizadas)
- Familiaridad con Jupyter Notebooks

### Opcional pero recomendado
- Experiencia con Pandas para manipulación de datos
- Conocimientos básicos de visualización (Matplotlib)

Si alguno de estos prerequisitos te parece nuevo, ¡no te preocupes! Los notebooks incluyen recordatorios y explicaciones cuando sea necesario.

---

## 🗺️ Roadmap Visual

```
01. Regresión Lineal (🟢 60min)
         ↓
         ↓ [Optimización]
         ↓
02. Gradient Descent (🟡 75min)
         ↓
         ↓ [Clasificación Binaria]
         ↓
03. Regresión Logística (🟡 60min)
         ↓
         ↓ [Multi-clase]
         ↓
04. Regresión Softmax (🟡 60min)
         ↓
         ├─────────────────────┐
         ↓                     ↓
         ↓              [No-Paramétrico]
         ↓                     ↓
         ↓            05. Árboles de Decisión (🟢 60min)
         ↓                     ↓
         ↓                     ↓ [Ensemble: Bagging]
         ↓                     ↓
         ↓            06. Random Forests (🟡 75min)
         ↓                     ↓
         ↓                     ↓ [Ensemble: Boosting]
         ↓                     ↓
         ↓            07. Boosting (🔴 90min)
         ↓                     │
         └─────────────────────┘
                    ↓
            [Métodos de Kernel]
                    ↓
         08. SVM (🔴 90min)
                    ↓
         ┌──────────┴──────────┐
         ↓                     ↓
   [Clustering]      [Reducción Dimensional]
         ↓                     ↓
09. K-Means (🟢 60min)  10. PCA (🟡 75min)
```

---

## 📚 Tabla de Contenidos

| # | Notebook | Nivel | Tiempo | Conceptos Clave | Datasets |
|---|----------|-------|--------|-----------------|----------|
| 01 | [Regresión Lineal](01-regresion-lineal.ipynb) | 🟢 | 60 min | MSE, ajuste de parámetros, predicción continua | California Housing |
| 02 | [Gradient Descent](02-gradient-descent.ipynb) | 🟡 | 75 min | Optimización, learning rate, momentum, convergencia | Sintético |
| 03 | [Regresión Logística](03-regresion-logistica.ipynb) | 🟡 | 60 min | Sigmoide, cross-entropy, clasificación binaria | Breast Cancer |
| 04 | [Regresión Softmax](04-regresion-softmax.ipynb) | 🟡 | 60 min | Multi-clase, one-hot encoding, softmax | Iris, Wine |
| 05 | [Árboles de Decisión](05-arboles-decision.ipynb) | 🟢 | 60 min | Entropía, Gini, splitting, poda | Iris |
| 06 | [Random Forests](06-random-forests.ipynb) | 🟡 | 75 min | Bagging, OOB error, feature importance | Wine |
| 07 | [Boosting](07-boosting.ipynb) | 🔴 | 90 min | AdaBoost, XGBoost, LightGBM, regularización | Breast Cancer |
| 08 | [SVM](08-svm.ipynb) | 🔴 | 90 min | Márgenes, kernel trick, C parameter | Moons, Circles |
| 09 | [K-Means](09-kmeans.ipynb) | 🟢 | 60 min | Clustering, centroides, método del codo | Blobs, Iris |
| 10 | [PCA](10-pca.ipynb) | 🟡 | 75 min | Eigenvalues, varianza explicada, proyección | MNIST, Iris |

**Leyenda de niveles:**
- 🟢 **Principiante**: Conceptos fundamentales, matemática básica
- 🟡 **Intermedio**: Requiere comprensión de notebooks anteriores
- 🔴 **Avanzado**: Matemática más compleja, implementaciones sofisticadas

---

## 🚀 Guías de Uso

### Modo 1: Aprendizaje Lineal (Recomendado)

**Para quién:** Principiantes o cualquiera que quiera una base sólida

**Cómo:**
1. Sigue los notebooks en orden (01 → 10)
2. Completa TODOS los ejercicios antes de avanzar
3. Experimenta modificando hiperparámetros
4. Dedica tiempo a entender las visualizaciones

**Tiempo estimado:** 12-15 horas

**Beneficio:** Comprensión profunda y progresiva

---

### Modo 2: Exploración Selectiva

**Para quién:** Personas con experiencia que buscan refrescar conceptos específicos

**Cómo:**
1. Revisa la tabla de contenidos y elige temas de interés
2. Lee la sección de "Prerequisitos" en cada notebook
3. Si algo no es claro, vuelve a notebooks anteriores referenciados

**Tiempo estimado:** Variable

**Beneficio:** Eficiencia para llenar gaps específicos

---

### Modo 3: Orientado a Proyectos

**Para quién:** Personas que aprenden mejor con aplicaciones prácticas

**Cómo:**
1. Identifica tu proyecto (ver sugerencias abajo)
2. Estudia solo los notebooks relevantes
3. Aplica inmediatamente lo aprendido
4. Vuelve para profundizar si encuentras problemas

**Tiempo estimado:** 8-10 horas + tiempo de proyecto

**Beneficio:** Motivación por aplicación inmediata

---

## 🛠️ Proyectos Sugeridos

Después de completar esta ruta, estarás listo para:

### 🟢 Proyectos Principiantes

1. **Predictor de Precios de Viviendas**
   - Notebooks: 01, 02
   - Dataset: California Housing o Boston Housing
   - Objetivo: Predecir precios usando regresión lineal

2. **Clasificador de Flores Iris**
   - Notebooks: 03, 04
   - Dataset: Iris
   - Objetivo: Clasificar especies con regresión logística/softmax

3. **Segmentación de Clientes**
   - Notebook: 09
   - Dataset: Datos de e-commerce
   - Objetivo: Agrupar clientes con K-Means

### 🟡 Proyectos Intermedios

4. **Detector de Cáncer de Mama**
   - Notebooks: 03, 05, 06
   - Dataset: Breast Cancer Wisconsin
   - Objetivo: Clasificador médico con Random Forest

5. **Sistema de Recomendación Simple**
   - Notebooks: 09, 10
   - Dataset: MovieLens (pequeño)
   - Objetivo: Clustering + PCA para recomendaciones

6. **Análisis de Sentimientos (Features TF-IDF)**
   - Notebooks: 03, 07
   - Dataset: IMDB Reviews
   - Objetivo: Clasificar reviews con Boosting

### 🔴 Proyectos Avanzados

7. **Competición Kaggle: Titanic**
   - Notebooks: 03, 06, 07
   - Dataset: Titanic (Kaggle)
   - Objetivo: Ensemble de múltiples modelos

8. **Reconocimiento de Dígitos**
   - Notebooks: 04, 08, 10
   - Dataset: MNIST
   - Objetivo: PCA + SVM para clasificación

9. **Predictor de Churn de Clientes**
   - Notebooks: 03, 06, 07
   - Dataset: Telco Customer Churn
   - Objetivo: Pipeline completo con feature engineering

---

## 📖 Recursos Complementarios

### Libros Recomendados

1. **"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"** - Aurélien Géron
   - Excelente para aplicaciones prácticas
   - Cubre exactamente los mismos temas con más profundidad

2. **"Pattern Recognition and Machine Learning"** - Christopher Bishop
   - Más teórico, perfecto para profundizar en matemática
   - Referencia estándar académica

3. **"The Elements of Statistical Learning"** - Hastie, Tibshirani, Friedman
   - Gratuito online
   - Muy completo en teoría estadística

### Cursos Online

- **Andrew Ng - Machine Learning (Coursera)**
  - Clásico, cubre fundamentos similares
  - Más enfocado en aplicaciones

- **Fast.ai - Practical Deep Learning**
  - Top-down approach
  - Complementa bien con nuestro bottom-up

### Papers Fundamentales

Cada notebook incluye referencias a papers clave, pero algunos esenciales:

- **Regresión/Clasificación:**
  - "Logistic Regression" - Cox, 1958
  - "Ridge Regression" - Hoerl & Kennard, 1970

- **Ensemble Methods:**
  - "Random Forests" - Breiman, 2001
  - "XGBoost: A Scalable Tree Boosting System" - Chen & Guestrin, 2016

- **SVM:**
  - "Support-Vector Networks" - Cortes & Vapnik, 1995

---

## 🎯 Checklist de Progreso

Marca cada notebook cuando lo completes:

- [ ] 01. Regresión Lineal
- [ ] 02. Gradient Descent
- [ ] 03. Regresión Logística
- [ ] 04. Regresión Softmax
- [ ] 05. Árboles de Decisión
- [ ] 06. Random Forests
- [ ] 07. Boosting
- [ ] 08. SVM
- [ ] 09. K-Means
- [ ] 10. PCA

**Milestone 1:** Notebooks 01-04 → **Dominas regresión y clasificación básica**
**Milestone 2:** Notebooks 05-08 → **Comprendes métodos avanzados de clasificación**
**Milestone 3:** Notebooks 09-10 → **Sabes usar métodos no supervisados**

---

## ❓ Preguntas Frecuentes

**P: ¿Necesito conocer Deep Learning antes de esta ruta?**
R: No, esta ruta es completamente independiente y de hecho es prerequisito ideal para Deep Learning.

**P: ¿Por qué implementar desde cero si existen librerías?**
R: Implementar desde cero te da comprensión profunda de cómo funcionan los algoritmos, facilitando debugging y optimización en proyectos reales.

**P: ¿Cuánto tiempo me tomará completar esta ruta?**
R: Aproximadamente 12-15 horas si sigues linealmente, más tiempo si experimentas (recomendado).

**P: ¿Puedo saltarme notebooks?**
R: Puedes, pero los conceptos se construyen uno sobre otro. Lee los "Prerequisitos" en cada notebook para verificar.

**P: ¿Los ejercicios tienen soluciones?**
R: Los tests automáticos te indican si tu solución es correcta. Si te atascas, revisa las secciones de implementación.

---

## 🤝 Contribuir

¿Encontraste un error o quieres mejorar un notebook?

1. Abre un [Issue](../../issues) describiendo el problema
2. O envía un Pull Request con tu mejora
3. Asegúrate de seguir el formato estándar de notebooks

---

## ➡️ Próximos Pasos

Una vez completes esta ruta, puedes continuar con:

- **[Ruta 2: RL Clásico](../02-rl-clasico/)** - Si te interesan agentes y toma de decisiones secuenciales
- **[Ruta 3: LLM Agents](../03-llm-agents/)** - Si quieres aprender sobre Agentic AI moderna
- **Proyectos Integradores** - Aplica lo aprendido en problemas complejos

---

<div align="center">

**🎉 ¡Empieza tu viaje de ML ahora con el [Notebook 01: Regresión Lineal](01-regresion-lineal.ipynb)! 🎉**

[← Volver al README principal](../../README.md)

</div>

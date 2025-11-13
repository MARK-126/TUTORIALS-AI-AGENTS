# 🤝 Guía de Contribución

¡Gracias por tu interés en contribuir a este proyecto! Este es un proyecto educativo de código abierto y damos la bienvenida a contribuciones de todo tipo.

## 📋 Tabla de Contenidos

- [Código de Conducta](#código-de-conducta)
- [¿Cómo puedo contribuir?](#cómo-puedo-contribuir)
- [Guías de Estilo](#guías-de-estilo)
- [Proceso de Pull Request](#proceso-de-pull-request)
- [Desarrollo Local](#desarrollo-local)

---

## 📜 Código de Conducta

Este proyecto adhiere al código de conducta de Contributor Covenant. Al participar, se espera que mantengas este código. Por favor reporta comportamiento inaceptable abriendo un issue.

### Nuestros Estándares

**Comportamientos que contribuyen a crear un ambiente positivo:**
- Usar lenguaje acogedor e inclusivo
- Ser respetuoso de diferentes puntos de vista y experiencias
- Aceptar críticas constructivas con gracia
- Enfocarse en lo que es mejor para la comunidad
- Mostrar empatía hacia otros miembros de la comunidad

**Comportamientos inaceptables:**
- Uso de lenguaje o imágenes sexualizadas
- Trolling, comentarios insultantes/despectivos, y ataques personales o políticos
- Acoso público o privado
- Publicar información privada de otros sin permiso explícito
- Otra conducta que razonablemente podría considerarse inapropiada en un entorno profesional

---

## 🎯 ¿Cómo puedo contribuir?

Hay muchas formas de contribuir a este proyecto:

### 1. 🐛 Reportar Bugs

Si encuentras un error en un notebook o en el código:

1. **Verifica** que el bug no haya sido reportado ya en [Issues](../../issues)
2. **Abre un nuevo issue** con el template de bug report
3. **Incluye**:
   - Descripción clara del problema
   - Pasos para reproducirlo
   - Comportamiento esperado vs observado
   - Versiones de Python, librerías relevantes
   - Screenshots si aplica

### 2. 💡 Sugerir Mejoras

¿Tienes una idea para mejorar el proyecto?

1. **Abre un issue** con el template de feature request
2. **Describe**:
   - El problema que resolverías
   - Tu solución propuesta
   - Alternativas consideradas
   - Ejemplos de uso

### 3. 📝 Mejorar Documentación

La documentación siempre puede mejorar:

- Corregir typos o errores gramaticales
- Clarificar explicaciones confusas
- Agregar ejemplos adicionales
- Mejorar visualizaciones
- Traducir a otros idiomas

### 4. 🔧 Contribuir Código

#### Áreas donde contribuir:

**Notebooks:**
- Corregir errores en implementaciones
- Mejorar comentarios y explicaciones
- Agregar visualizaciones adicionales
- Crear ejercicios nuevos
- Optimizar código existente

**Utilidades:**
- Agregar funciones de visualización nuevas
- Mejorar tests automáticos
- Crear nuevos dataset loaders
- Optimizar rendimiento

**Nuevos Notebooks:**
- Crear notebooks para temas no cubiertos
- Expandir rutas existentes
- Crear rutas nuevas (Deep Learning, NLP, CV, etc.)

**Proyectos Integradores:**
- Crear proyectos que combinen múltiples notebooks
- Aplicaciones end-to-end
- Casos de estudio del mundo real

---

## 📐 Guías de Estilo

Para mantener consistencia en el proyecto, sigue estas guías:

### Notebooks

#### Estructura (8 secciones obligatorias):

1. **Header**: Nivel, tiempo, prerequisitos, objetivos
2. **Motivación**: Problema real, por qué importa
3. **Intuición Visual**: Visualizaciones interactivas
4. **Fundamentos Matemáticos**: Derivaciones paso a paso
5. **Implementación Desde Cero**: NumPy comentado
6. **Versión con Framework**: Scikit-learn/TensorFlow/etc.
7. **Ejercicios**: 3 niveles (🟢🟡🔴)
8. **Resumen y Recursos**: Papers, videos, próximos pasos

#### Código Python:

```python
# ✅ HACER:
def calculate_loss(predictions: np.ndarray, targets: np.ndarray) -> float:
    """
    Calcula el Mean Squared Error entre predicciones y targets.

    Parameters:
    -----------
    predictions : np.ndarray
        Predicciones del modelo
    targets : np.ndarray
        Valores reales

    Returns:
    --------
    float
        MSE calculado
    """
    return np.mean((predictions - targets) ** 2)

# ❌ EVITAR:
def calc_loss(p, t):  # Sin type hints, sin docstring
    return np.mean((p - t) ** 2)
```

#### Estilo de Escritura:

- **Tono**: Conversacional pero preciso, tutear al lector
- **Claridad**: Explicar el "por qué", no solo el "qué"
- **Ejemplos**: Incluir ejemplos numéricos concretos
- **Visualizaciones**: Preferir Plotly para interactividad

### Código Python

Seguimos **PEP 8** con algunas adaptaciones:

```python
# Imports organizados
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Nombres descriptivos
learning_rate = 0.01  # ✅
lr = 0.01            # ❌ (solo en contextos muy claros)

# Type hints cuando mejore claridad
def train_model(X: np.ndarray, y: np.ndarray, epochs: int = 100) -> dict:
    pass

# Comentarios que explican el por qué
# Normalizamos para que gradient descent converja más rápido
X_scaled = (X - X.mean()) / X.std()

# Docstrings para funciones y clases importantes
def important_function():
    """
    Descripción breve.

    Explicación más detallada si es necesario.

    Parameters:
    -----------
    param1 : type
        Descripción

    Returns:
    --------
    type
        Descripción
    """
    pass
```

### Matemática (LaTeX)

```latex
# ✅ Formato claro con numeración
$$
\begin{align}
J(w, b) &= \frac{1}{m} \sum_{i=1}^{m} (h(x^{(i)}) - y^{(i)})^2 \tag{1} \\
\text{donde: } & \\
m &: \text{número de ejemplos} \\
h(x) &: \text{hipótesis (predicción)}
\end{align}
$$

# ❌ Sin contexto
$$J = \frac{1}{m}\sum(h - y)^2$$
```

### Visualizaciones

```python
# ✅ Plotly con configuración completa
fig = go.Figure()
fig.add_trace(go.Scatter(x=X, y=y, mode='markers', name='Datos'))
fig.update_layout(
    title="Título Descriptivo",
    xaxis_title="Eje X (unidades)",
    yaxis_title="Eje Y (unidades)",
    template="plotly_white",
    font=dict(size=12)
)
fig.show()
```

### Tests para Ejercicios

```python
# ✅ Tests con mensajes claros
def test_ejercicio():
    resultado = ejercicio_funcion()
    assert resultado > 0.9, f"❌ R² muy bajo: {resultado:.3f}. Revisa la implementación."
    print(f"✅ ¡Correcto! R² = {resultado:.3f}")
    return True
```

---

## 🔄 Proceso de Pull Request

### 1. Fork y Clone

```bash
# Fork el repo en GitHub, luego:
git clone https://github.com/TU-USUARIO/TUTORIALS-AI-AGENTS.git
cd TUTORIALS-AI-AGENTS
git remote add upstream https://github.com/MARK-126/TUTORIALS-AI-AGENTS.git
```

### 2. Crear Branch

```bash
# Crear branch descriptivo
git checkout -b feature/agregar-notebook-transformers
# o
git checkout -b fix/corregir-error-gradient-descent
```

### 3. Hacer Cambios

- Sigue las guías de estilo
- Asegúrate que el código sea ejecutable
- Agrega tests si aplica
- Actualiza documentación relacionada

### 4. Commit

```bash
# Commits atómicos y descriptivos
git add .
git commit -m "Agregar notebook sobre Transformers

- Implementación de self-attention desde cero
- Comparación con HuggingFace
- 3 ejercicios con tests automáticos
- Visualizaciones de attention weights"
```

### 5. Sincronizar con Upstream

```bash
git fetch upstream
git rebase upstream/main
```

### 6. Push y PR

```bash
git push origin feature/agregar-notebook-transformers
```

Luego abre un Pull Request en GitHub con:

**Título claro**: `[Notebook] Agregar notebook sobre Transformers`

**Descripción**:
```markdown
## Descripción
Agrega un nuevo notebook sobre Transformers a la ruta de Deep Learning.

## Cambios
- ✅ Implementación de self-attention desde cero
- ✅ Multi-head attention
- ✅ Visualizaciones interactivas
- ✅ 3 ejercicios con tests
- ✅ Comparación con HuggingFace

## Checklist
- [x] El notebook sigue la estructura de 8 secciones
- [x] El código es ejecutable sin errores
- [x] Incluye docstrings y comentarios
- [x] Las visualizaciones funcionan
- [x] Los tests pasan
- [x] La documentación está actualizada

## Screenshots
[Opcional: capturas de visualizaciones]
```

### 7. Code Review

- Responde a comentarios constructivamente
- Haz cambios solicitados en nuevos commits
- Una vez aprobado, tu PR será mergeado

---

## 💻 Desarrollo Local

### Setup Inicial

```bash
# Clonar repo
git clone https://github.com/MARK-126/TUTORIALS-AI-AGENTS.git
cd TUTORIALS-AI-AGENTS

# Crear ambiente
conda env create -f environment.yml
conda activate ml-ai-tutorials

# O con pip
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Lanzar Jupyter
jupyter lab
```

### Ejecutar Tests

```bash
# Verificar que notebooks se ejecutan sin errores
pytest --nbmake rutas/**/*.ipynb

# O ejecutar notebook específico
jupyter nbconvert --to notebook --execute rutas/01-ml-clasico/01-regresion-lineal.ipynb
```

### Estructura del Proyecto

```
TUTORIALS-AI-AGENTS/
├── shared/              # Utilidades compartidas
│   └── utils/          # Funciones reutilizables
├── rutas/              # Rutas de aprendizaje
│   ├── 01-ml-clasico/
│   ├── 02-rl-clasico/
│   └── 03-llm-agents/
└── proyectos/          # Proyectos integradores
```

---

## 🎯 Prioridades Actuales

Áreas donde especialmente necesitamos ayuda:

1. **Traducciones** (inglés, portugués, etc.)
2. **Notebooks adicionales** (Deep Learning, NLP, CV)
3. **Proyectos integradores** end-to-end
4. **Mejoras en visualizaciones** (animaciones, interactividad)
5. **Tests automatizados** (CI/CD)
6. **Datasets de ejemplo** para quick start

---

## 📞 ¿Preguntas?

Si tienes preguntas sobre cómo contribuir:

1. Revisa [Issues existentes](../../issues)
2. Abre una [Discusión](../../discussions)
3. Contacta a los mantenedores

---

## 🙏 Reconocimientos

Todos los contribuidores serán reconocidos en:
- README principal
- CONTRIBUTORS.md
- Release notes

¡Gracias por hacer este proyecto mejor! 🎉

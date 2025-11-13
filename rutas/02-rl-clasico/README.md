# 🤖 Ruta 2: Reinforcement Learning Clásico

> **Domina el aprendizaje por refuerzo desde sus fundamentos matemáticos hasta métodos deep RL modernos con implementaciones desde cero.**

---

## 🎯 Descripción y Objetivos

Esta ruta te llevará desde los conceptos fundamentales de agentes inteligentes hasta algoritmos avanzados de Deep Reinforcement Learning. Al finalizar esta ruta, tendrás una comprensión profunda de:

- Cómo funcionan los **agentes autónomos** que aprenden de la experiencia
- La matemática detrás de **Procesos de Decisión de Markov** y ecuaciones de Bellman
- Cómo implementar algoritmos de RL **desde cero** usando NumPy
- La transición de métodos tabulares (Q-Learning) a **Deep RL** (DQN, Policy Gradients)
- Cuándo usar métodos basados en valor vs métodos basados en política
- Cómo entrenar agentes en ambientes complejos con frameworks modernos

### 🎓 ¿Qué aprenderás?

| Área | Conceptos |
|------|-----------|
| **Fundamentos** | Agentes, ambientes, ciclo percepción-acción, recompensas |
| **Teoría de Decisiones** | MDPs, estados, acciones, políticas, funciones de valor |
| **Métodos Tabulares** | Q-Learning, exploración vs explotación, convergencia |
| **Deep RL (Valor)** | DQN, experience replay, target networks, aproximación neuronal |
| **Deep RL (Política)** | REINFORCE, gradientes de política, baselines, ventajas |
| **Métodos Híbridos** | Actor-Critic, A2C, A3C, combinación valor-política |

---

## 🧠 Prerequisitos

### Matemática
- Probabilidad y estadística (distribuciones, esperanza)
- Álgebra lineal (vectores, matrices)
- Cálculo (derivadas, gradientes, regla de la cadena)
- Nociones de procesos estocásticos (útil pero no esencial)

### Programación
- Python intermedio/avanzado (clases, decoradores)
- NumPy (operaciones vectorizadas, broadcasting)
- Familiaridad con redes neuronales básicas
- Experiencia con Jupyter Notebooks

### Machine Learning
- **Recomendado:** Haber completado [Ruta 1: ML Clásico](../01-ml-clasico/)
- Comprensión de gradient descent y backpropagation
- Conceptos básicos de redes neuronales (al menos para notebooks 04-06)

Si algunos prerequisitos son nuevos, los notebooks incluyen recordatorios contextuales cuando sea necesario.

---

## 🗺️ Roadmap Visual

```
01. Fundamentos de Agentes (🟢 60min)
         ↓
         ↓ [Formalización: MDP]
         ↓
02. MDP y Ecuaciones de Bellman (🟡 75min)
         ↓
         ↓ [Métodos Tabulares]
         ↓
03. Q-Learning (🟡 90min)
         ↓
         ↓ [Aproximación con Redes Neuronales]
         ↓
04. Deep Q-Networks (DQN) (🔴 90min)
         ↓
         ├─────────────────────┐
         ↓                     ↓
   [Métodos Basados          [Métodos Basados
    en Valor]                 en Política]
         ↓                     ↓
         ↓            05. Policy Gradients (🔴 90min)
         ↓                     ↓
         └─────────────────────┘
                    ↓
            [Combinando Ambos]
                    ↓
         06. Actor-Critic (🔴 90min)
                    ↓
                [A2C/A3C]
```

---

## 📚 Tabla de Contenidos

| # | Notebook | Nivel | Tiempo | Conceptos Clave | Ambientes |
|---|----------|-------|--------|-----------------|-----------|
| 01 | [Fundamentos de Agentes](01-fundamentos-agentes.ipynb) | 🟢 | 60 min | Agentes, percepción-acción, ambientes, recompensas | GridWorld |
| 02 | [MDP y Bellman](02-mdp-bellman.ipynb) | 🟡 | 75 min | Estados, acciones, transiciones, políticas, value functions | GridWorld, FrozenLake |
| 03 | [Q-Learning](03-q-learning.ipynb) | 🟡 | 90 min | Tabla Q, ε-greedy, convergencia, TD learning | FrozenLake, Taxi |
| 04 | [Deep Q-Networks](04-deep-q-networks.ipynb) | 🔴 | 90 min | DQN, experience replay, target network, aproximación neuronal | CartPole, LunarLander |
| 05 | [Policy Gradients](05-policy-gradients.ipynb) | 🔴 | 90 min | REINFORCE, gradientes de política, baselines, ventajas | CartPole, LunarLander |
| 06 | [Actor-Critic](06-actor-critic.ipynb) | 🔴 | 90 min | A2C, A3C, combinación valor-política, paralelización | CartPole, LunarLander |

**Leyenda de niveles:**
- 🟢 **Principiante**: Conceptos fundamentales, implementaciones simples
- 🟡 **Intermedio**: Requiere comprensión de notebooks anteriores, matemática moderada
- 🔴 **Avanzado**: Deep RL, implementaciones complejas, matemática sofisticada

---

## 🚀 Guías de Uso

### Modo 1: Aprendizaje Lineal (Recomendado)

**Para quién:** Cualquiera nuevo en Reinforcement Learning

**Cómo:**
1. Sigue los notebooks en orden estricto (01 → 06)
2. Completa TODOS los ejercicios antes de avanzar
3. Experimenta entrenando agentes con diferentes hiperparámetros
4. Observa las visualizaciones de políticas aprendidas
5. Compara métodos: tabular vs deep RL, valor vs política

**Tiempo estimado:** 14-18 horas (incluyendo experimentación)

**Beneficio:** Comprensión profunda desde primeros principios hasta state-of-the-art

---

### Modo 2: Exploración Selectiva

**Para quién:** Personas con conocimientos de RL que buscan profundizar temas específicos

**Cómo:**
1. Revisa la tabla de contenidos
2. Si te interesan métodos tabulares: Notebooks 01-03
3. Si te interesa Deep RL: Notebooks 04-06 (pero revisa 02-03 para fundamentos)
4. Lee la sección de "Prerequisitos" en cada notebook

**Tiempo estimado:** Variable (3-6 horas por notebook)

**Beneficio:** Enfoque eficiente en áreas de interés

---

### Modo 3: Orientado a Proyectos

**Para quién:** Personas que aprenden mejor construyendo aplicaciones

**Cómo:**
1. Identifica tu proyecto (ver sugerencias abajo)
2. Estudia los notebooks relevantes para tu objetivo
3. Aplica inmediatamente lo aprendido
4. Profundiza en teoría cuando encuentres problemas
5. Compara diferentes algoritmos en tu ambiente

**Tiempo estimado:** 10-12 horas + tiempo de proyecto

**Beneficio:** Motivación práctica y aprendizaje por aplicación

---

## 🛠️ Proyectos Sugeridos

Después de completar esta ruta, estarás listo para:

### 🟢 Proyectos Principiantes

1. **Agente Navegador de Laberinto**
   - Notebooks: 01, 02, 03
   - Ambiente: GridWorld custom o FrozenLake
   - Objetivo: Agente que aprende a navegar evitando obstáculos

2. **Balanceador de CartPole**
   - Notebooks: 01, 02, 03, 04
   - Ambiente: CartPole (Gymnasium)
   - Objetivo: Entrenar agente para balancear polo vertical

3. **Taxi Autónomo Simple**
   - Notebooks: 02, 03
   - Ambiente: Taxi (Gymnasium)
   - Objetivo: Agente que recoge y entrega pasajeros eficientemente

### 🟡 Proyectos Intermedios

4. **Lunar Lander con DQN**
   - Notebooks: 04
   - Ambiente: LunarLander (Gymnasium)
   - Objetivo: Aterrizar nave espacial suavemente

5. **Comparación Q-Learning vs DQN**
   - Notebooks: 03, 04
   - Ambientes: CartPole, Acrobot
   - Objetivo: Análisis comparativo de métodos tabulares vs deep

6. **Agente con Policy Gradient**
   - Notebooks: 05
   - Ambiente: MountainCar, Pendulum
   - Objetivo: Resolver ambientes continuos con REINFORCE

### 🔴 Proyectos Avanzados

7. **Actor-Critic Multi-Ambiente**
   - Notebooks: 06
   - Ambientes: Suite completa de Gymnasium
   - Objetivo: Implementar A2C que generalice a múltiples tareas

8. **Agente Atari con DQN**
   - Notebooks: 04
   - Ambiente: Atari Games (Pong, Breakout)
   - Objetivo: Reproducir resultados del paper original de DQN

9. **Comparación Sistemática de Algoritmos RL**
   - Notebooks: 03-06
   - Ambientes: Suite estandarizada
   - Objetivo: Benchmark completo de Q-Learning, DQN, REINFORCE, A2C

10. **Agente Robótico Simulado**
    - Notebooks: 05, 06
    - Ambiente: PyBullet o MuJoCo
    - Objetivo: Control de robot con continuous actions

---

## 📖 Recursos Complementarios

### Libros Recomendados

1. **"Reinforcement Learning: An Introduction"** - Sutton & Barto (2nd Edition)
   - LA biblia del RL, disponible gratis online
   - Cubre desde fundamentos hasta métodos modernos
   - **Altamente recomendado** como lectura paralela

2. **"Deep Reinforcement Learning Hands-On"** - Maxim Lapan
   - Orientado a implementaciones prácticas
   - Excelente para Deep RL (notebooks 04-06)
   - Código en PyTorch

3. **"Algorithms for Reinforcement Learning"** - Csaba Szepesvári
   - Más teórico y conciso
   - Excelente para fundamentos matemáticos
   - Disponible gratis

### Cursos Online

- **David Silver - RL Course (DeepMind/UCL)**
  - Videos en YouTube
  - Sigue estructura similar a estos notebooks
  - Excelentes explicaciones conceptuales

- **Sergey Levine - Deep RL (UC Berkeley CS285)**
  - Más avanzado, enfocado en Deep RL
  - Cubre últimos avances en el campo
  - Lectures y slides disponibles gratis

- **Spinning Up in Deep RL (OpenAI)**
  - Tutorial práctico de OpenAI
  - Implementaciones de referencia
  - Excelente documentación

### Papers Fundamentales

Cada notebook incluye referencias específicas, pero algunos esenciales:

- **Q-Learning:**
  - "Q-Learning" - Watkins, 1989
  - Fundacional para RL moderno

- **DQN:**
  - "Playing Atari with Deep Reinforcement Learning" - Mnih et al., 2013
  - "Human-level control through deep RL" - Mnih et al., 2015 (Nature)

- **Policy Gradients:**
  - "Simple Statistical Gradient-Following Algorithms" - Williams, 1992 (REINFORCE)
  - "Policy Gradient Methods" - Sutton et al., 1999

- **Actor-Critic:**
  - "Asynchronous Methods for Deep RL" - Mnih et al., 2016 (A3C)
  - "Actor-Critic Algorithms" - Konda & Tsitsiklis, 1999

### Frameworks y Herramientas

- **Gymnasium (OpenAI Gym)**: Suite de ambientes estándar
- **Stable-Baselines3**: Implementaciones robustas de algoritmos RL
- **RLlib (Ray)**: RL distribuido y escalable
- **TF-Agents**: Framework de Google para RL
- **CleanRL**: Implementaciones simples y pedagógicas

---

## 🎯 Checklist de Progreso

Marca cada notebook cuando lo completes:

- [ ] 01. Fundamentos de Agentes
- [ ] 02. MDP y Ecuaciones de Bellman
- [ ] 03. Q-Learning
- [ ] 04. Deep Q-Networks (DQN)
- [ ] 05. Policy Gradients (REINFORCE)
- [ ] 06. Actor-Critic (A2C/A3C)

**Milestone 1:** Notebooks 01-02 → **Comprendes la teoría fundamental de RL**
**Milestone 2:** Notebook 03 → **Puedes implementar métodos tabulares de RL**
**Milestone 3:** Notebooks 04-06 → **Dominas Deep Reinforcement Learning**

---

## ❓ Preguntas Frecuentes

**P: ¿Necesito saber Deep Learning antes de esta ruta?**
R: Para notebooks 01-03, no es necesario. Para 04-06, necesitas conocimientos básicos de redes neuronales (feedforward, backpropagation).

**P: ¿Por qué implementar desde cero si existen Stable-Baselines3 y RLlib?**
R: Implementar desde cero te da comprensión profunda del funcionamiento interno, facilitando debugging y adaptación de algoritmos a problemas específicos.

**P: ¿Cuánto tiempo toma entrenar estos agentes?**
R: Métodos tabulares (notebook 03): segundos a minutos. Deep RL (04-06): minutos a horas dependiendo del ambiente y hardware.

**P: ¿Necesito GPU para estos notebooks?**
R: No es estrictamente necesario para los ambientes simples usados. GPU acelera notebooks 04-06, pero CPU es suficiente para aprender.

**P: ¿Qué diferencia hay entre RL y supervised learning?**
R: En supervised learning tienes etiquetas directas. En RL, el agente aprende de recompensas retrasadas y debe explorar para descubrir buenas acciones.

**P: ¿Cuál es la diferencia entre value-based y policy-based methods?**
R: Value-based (Q-Learning, DQN) aprende qué tan bueno es cada estado/acción. Policy-based (REINFORCE) aprende directamente la política. Actor-Critic combina ambos.

---

## 🤝 Contribuir

¿Encontraste un error o quieres mejorar un notebook?

1. Abre un [Issue](../../issues) describiendo el problema
2. O envía un Pull Request con tu mejora
3. Asegúrate de seguir el formato estándar de notebooks
4. Verifica que los agentes converjan correctamente

---

## ➡️ Próximos Pasos

Una vez completes esta ruta, puedes continuar con:

- **[Ruta 3: LLM Agents](../03-llm-agents/)** - RL aplicado a agentes basados en LLMs
- **[Ruta 1: ML Clásico](../01-ml-clasico/)** - Si necesitas reforzar fundamentos de ML
- **Proyectos Integradores** - Aplica RL a problemas complejos del mundo real
- **Papers Recientes** - Explora PPO, SAC, TD3, DDPG y otros algoritmos avanzados

---

## 🌟 Ventajas de esta Ruta

Esta ruta es única porque:

1. **Balance teoría-práctica**: Matemática rigurosa + código desde cero
2. **Progresión gradual**: De tabular a deep RL sin saltos bruscos
3. **Ambientes variados**: De GridWorld simple a LunarLander complejo
4. **Comparaciones directas**: Ver evolución de Q-Learning → DQN → Actor-Critic
5. **Ejercicios con tests**: Validación automática de tu comprensión
6. **Visualizaciones interactivas**: Ver políticas y funciones de valor en tiempo real

---

<div align="center">

**🚀 ¡Comienza tu viaje en RL ahora con el [Notebook 01: Fundamentos de Agentes](01-fundamentos-agentes.ipynb)! 🚀**

[← Volver al README principal](../../README.md)

</div>

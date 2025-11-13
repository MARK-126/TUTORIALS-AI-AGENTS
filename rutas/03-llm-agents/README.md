# 🧠 Ruta 3: LLM Agents (Agentic AI)

> **Domina el diseño e implementación de agentes inteligentes basados en LLMs, desde prompting agéntico hasta sistemas multi-agente complejos.**

---

## 🎯 Descripción y Objetivos

Esta ruta te llevará desde los fundamentos de agentes basados en LLMs hasta sistemas multi-agente sofisticados. Al finalizar esta ruta, tendrás una comprensión profunda de:

- La diferencia fundamental entre un **LLM** y un **Agente basado en LLM**
- Cómo diseñar **prompts agénticos** efectivos (Chain-of-Thought, Tree-of-Thought)
- El patrón **ReAct** (Reasoning + Acting) para alternancia pensamiento-acción
- Cómo integrar **herramientas externas** mediante function calling
- Sistemas de **memoria** para agentes (short-term, long-term, RAG)
- Arquitecturas **multi-agente** y patrones de colaboración
- Cómo construir agentes autónomos desde cero y con frameworks (LangChain, AutoGPT)

### 🎓 ¿Qué aprenderás?

| Área | Conceptos |
|------|-----------|
| **Fundamentos** | Arquitectura agente vs LLM, ciclo observación-pensamiento-acción |
| **Prompting Avanzado** | Chain-of-Thought, Tree-of-Thought, Self-Consistency, Few-shot |
| **ReAct Pattern** | Alternancia reasoning/acting, trazabilidad, ejemplos prácticos |
| **Tool Integration** | Function calling, tool selection, APIs externas, ejecución segura |
| **Memory Systems** | Buffer memory, summary memory, vector stores, RAG agéntico |
| **Multi-Agent** | Colaboración, comunicación, roles, AutoGPT, BabyAGI patterns |

---

## 🧠 Prerequisitos

### Conocimientos de IA/ML
- Comprensión básica de cómo funcionan los LLMs (transformers, tokens)
- Familiaridad con APIs de OpenAI/Anthropic (útil pero no esencial)
- Nociones de embeddings y similitud vectorial
- **Recomendado:** [Ruta 2: RL Clásico](../02-rl-clasico/) para contexto de agentes

### Programación
- Python avanzado (async/await, decoradores, context managers)
- Manejo de APIs REST
- JSON y estructuras de datos complejas
- Familiaridad con manejo de strings y templates

### Herramientas
- Jupyter Notebooks
- Gestión de API keys y variables de entorno
- Conceptos básicos de bases de datos vectoriales

### Opcional pero recomendado
- Experiencia con frameworks (LangChain, LlamaIndex)
- Conocimientos de NLP básico
- Familiaridad con cost management de APIs de LLMs

Si algunos prerequisitos son nuevos, los notebooks incluyen explicaciones contextuales.

---

## 🗺️ Roadmap Visual

```
01. Introducción a LLM Agents (🟢 60min)
         ↓
         ↓ [Prompting Efectivo]
         ↓
02. Prompting Agéntico (🟡 75min)
         ↓
         ↓ [Razonamiento + Acción]
         ↓
03. ReAct Pattern (🟡 75min)
         ↓
         ↓ [Capacidades Extendidas]
         ↓
04. Tool Use & Function Calling (🟡 90min)
         ↓
         ↓ [Persistencia]
         ↓
05. Memory Systems (🔴 90min)
         ↓
         ↓ [Colaboración]
         ↓
06. Sistemas Multi-Agente (🔴 90min)
         ↓
    [Autonomous Agents]
```

---

## 📚 Tabla de Contenidos

| # | Notebook | Nivel | Tiempo | Conceptos Clave | Ejemplos |
|---|----------|-------|--------|-----------------|----------|
| 01 | [Intro a LLM Agents](01-intro-llm-agents.ipynb) | 🟢 | 60 min | LLM vs Agent, arquitectura, componentes, loop básico | Simple Agent Loop |
| 02 | [Prompting Agéntico](02-prompting-agentico.ipynb) | 🟡 | 75 min | Chain-of-Thought, Tree-of-Thought, Self-Consistency, Few-shot | Math Reasoning |
| 03 | [ReAct Pattern](03-react-reasoning-acting.ipynb) | 🟡 | 75 min | Reasoning + Acting, trazabilidad, Wikipedia search | Question Answering |
| 04 | [Tool Use](04-tool-use-function-calling.ipynb) | 🟡 | 90 min | Function calling, tool definition, selection, execution | Calculator, Weather |
| 05 | [Memory Systems](05-memory-systems.ipynb) | 🔴 | 90 min | Short-term, long-term, RAG, vector databases, retrieval | Conversational Agent |
| 06 | [Multi-Agentes](06-multi-agentes.ipynb) | 🔴 | 90 min | Colaboración, comunicación, AutoGPT, BabyAGI, roles | Research Assistant |

**Leyenda de niveles:**
- 🟢 **Principiante**: Conceptos fundamentales de agentes LLM
- 🟡 **Intermedio**: Requiere comprensión de notebooks anteriores
- 🔴 **Avanzado**: Arquitecturas complejas, sistemas multi-componente

---

## 🚀 Guías de Uso

### Modo 1: Aprendizaje Lineal (Recomendado)

**Para quién:** Cualquiera nuevo en Agentic AI o LLM Agents

**Cómo:**
1. Sigue los notebooks en orden estricto (01 → 06)
2. Completa TODOS los ejercicios antes de avanzar
3. Experimenta con diferentes LLMs (GPT-4, Claude, modelos locales)
4. Monitorea costos de API durante experimentación
5. Construye sobre ejemplos anteriores

**Tiempo estimado:** 14-18 horas (incluyendo experimentación)

**Beneficio:** Comprensión profunda desde prompting básico hasta multi-agente

---

### Modo 2: Exploración Selectiva

**Para quién:** Desarrolladores con experiencia en LLMs que buscan aprender patterns agénticos

**Cómo:**
1. Revisa la tabla de contenidos
2. Si conoces prompting básico: Empieza desde notebook 03 (ReAct)
3. Si te interesan herramientas: Notebooks 04-05
4. Si te interesa multi-agente: Notebook 06 (pero revisa 03-05 para contexto)

**Tiempo estimado:** Variable (2-4 horas por notebook)

**Beneficio:** Enfoque eficiente en técnicas avanzadas

---

### Modo 3: Orientado a Proyectos

**Para quién:** Personas que aprenden mejor construyendo aplicaciones

**Cómo:**
1. Identifica tu proyecto (ver sugerencias abajo)
2. Estudia los notebooks relevantes para tu objetivo
3. Implementa un MVP rápidamente
4. Itera mejorando con técnicas de otros notebooks
5. Monitorea performance y costos

**Tiempo estimado:** 10-12 horas + tiempo de proyecto

**Beneficio:** Motivación práctica y portfolio de proyectos

---

## 🛠️ Proyectos Sugeridos

Después de completar esta ruta, estarás listo para:

### 🟢 Proyectos Principiantes

1. **Asistente de Q&A con Búsqueda Web**
   - Notebooks: 01, 03, 04
   - Herramientas: Wikipedia API, Google Search
   - Objetivo: Agente que responde preguntas con búsquedas web

2. **Calculadora Inteligente con Razonamiento**
   - Notebooks: 02, 04
   - Herramientas: Calculator, Math libraries
   - Objetivo: Resolver problemas matemáticos con CoT

3. **Chatbot con Memoria de Conversación**
   - Notebooks: 01, 05
   - Herramientas: Buffer memory
   - Objetivo: Mantener contexto en conversaciones largas

### 🟡 Proyectos Intermedios

4. **Agente de Análisis de Código**
   - Notebooks: 03, 04, 05
   - Herramientas: File system, code parsers
   - Objetivo: Analizar repositorios y responder preguntas

5. **Research Assistant con RAG**
   - Notebooks: 03, 05
   - Herramientas: Vector DB, web scraping
   - Objetivo: Asistente que investiga temas y sintetiza información

6. **Customer Support Agent**
   - Notebooks: 04, 05
   - Herramientas: Knowledge base, ticketing system
   - Objetivo: Agente autónomo de soporte al cliente

### 🔴 Proyectos Avanzados

7. **Sistema Multi-Agente de Desarrollo de Software**
   - Notebooks: 06
   - Componentes: Planner, Coder, Reviewer, Tester
   - Objetivo: Sistema que genera código con revisión automática

8. **Autonomous Research Agent (AutoGPT-style)**
   - Notebooks: 03, 04, 05, 06
   - Herramientas: Web, file system, APIs diversas
   - Objetivo: Agente completamente autónomo con objetivos de alto nivel

9. **Multi-Agent Debate System**
   - Notebooks: 06
   - Componentes: Múltiples agentes con perspectivas diferentes
   - Objetivo: Sistema de debate para mejorar respuestas

10. **Enterprise Knowledge Assistant**
    - Notebooks: 04, 05, 06
    - Componentes: RAG, multi-source data, access control
    - Objetivo: Sistema completo de Q&A empresarial

---

## 📖 Recursos Complementarios

### Libros y Papers Fundamentales

1. **"Prompt Engineering Guide"** - DAIR.AI
   - Guía completa de prompting
   - Cubre técnicas usadas en notebooks 02-03
   - Disponible gratis online

2. **Papers clave:**
   - **ReAct**: "ReAct: Synergizing Reasoning and Acting in Language Models" (Yao et al., 2022)
   - **Chain-of-Thought**: "Chain-of-Thought Prompting Elicits Reasoning in LLMs" (Wei et al., 2022)
   - **Tree-of-Thought**: "Tree of Thoughts: Deliberate Problem Solving with LLMs" (Yao et al., 2023)
   - **Toolformer**: "Toolformer: Language Models Can Teach Themselves to Use Tools" (Schick et al., 2023)
   - **AutoGPT**: Conceptos de autonomous agents

### Frameworks y Herramientas

- **LangChain**: Framework completo para LLM applications
- **LlamaIndex**: Especializado en RAG y data connectors
- **AutoGPT**: Autonomous agent framework
- **BabyAGI**: Task-driven autonomous agent
- **Semantic Kernel**: Framework de Microsoft
- **Haystack**: NLP framework con LLM support

### Cursos y Tutoriales

- **DeepLearning.AI - LangChain Courses**
  - Múltiples cursos especializados
  - Desde basics hasta multi-agent systems

- **OpenAI Cookbook**
  - Ejemplos prácticos de function calling
  - Best practices para prompting

- **Anthropic Claude Docs**
  - Técnicas avanzadas de prompting
  - Tool use con Claude

### APIs y Servicios

- **LLM Providers**: OpenAI, Anthropic, Google (Gemini), Cohere
- **Vector Databases**: Pinecone, Weaviate, Chroma, FAISS
- **Embedding Models**: OpenAI Ada, Cohere, Sentence Transformers
- **Local Models**: Ollama, LM Studio, HuggingFace Transformers

---

## 🎯 Checklist de Progreso

Marca cada notebook cuando lo completes:

- [ ] 01. Introducción a LLM Agents
- [ ] 02. Prompting Agéntico
- [ ] 03. ReAct (Reasoning + Acting)
- [ ] 04. Tool Use y Function Calling
- [ ] 05. Memory Systems
- [ ] 06. Sistemas Multi-Agente

**Milestone 1:** Notebooks 01-02 → **Comprendes la diferencia entre LLM y Agent**
**Milestone 2:** Notebooks 03-04 → **Puedes construir agentes con herramientas**
**Milestone 3:** Notebooks 05-06 → **Dominas sistemas agénticos complejos**

---

## ❓ Preguntas Frecuentes

**P: ¿Necesito pagar por APIs de OpenAI/Anthropic?**
R: Los notebooks incluyen opciones con modelos locales (Ollama, HuggingFace), pero APIs comerciales ofrecen mejor experiencia. Costos son típicamente <$5 para completar todos los notebooks.

**P: ¿Qué diferencia hay entre un LLM y un Agente?**
R: Un LLM solo genera texto. Un Agente usa LLMs para razonar + actuar: puede usar herramientas, mantener memoria, tomar decisiones y ejecutar acciones en el mundo.

**P: ¿Es mejor usar frameworks (LangChain) o construir desde cero?**
R: Ambos. Los notebooks implementan desde cero para comprensión profunda, luego muestran versiones con frameworks para productividad.

**P: ¿Cómo manejo los costos de las APIs?**
R: Los notebooks incluyen ejemplos de tracking de tokens, uso de modelos más pequeños para testing, y caching de resultados.

**P: ¿Qué es RAG y por qué es importante para agentes?**
R: Retrieval-Augmented Generation permite a agentes acceder a conocimiento actualizado y específico más allá de su training data. Es fundamental para aplicaciones prácticas.

**P: ¿Los agentes pueden ejecutar código arbitrario?**
R: Sí, pero con riesgos. Los notebooks cubren sandboxing y ejecución segura de código generado por agentes.

**P: ¿Cuál es la diferencia entre AutoGPT y BabyAGI?**
R: Ambos son patrones de agentes autónomos. AutoGPT enfatiza loops autónomos con memoria y herramientas. BabyAGI usa task management con priorización. El notebook 06 los compara en detalle.

---

## 💰 Gestión de Costos

### Estimación de Costos por Notebook

| Notebook | Modelo Sugerido | Tokens Estimados | Costo Aprox. |
|----------|----------------|------------------|--------------|
| 01 | GPT-3.5-turbo | ~10K | $0.02 |
| 02 | GPT-4-turbo | ~15K | $0.30 |
| 03 | GPT-4-turbo | ~20K | $0.40 |
| 04 | GPT-4-turbo | ~25K | $0.50 |
| 05 | GPT-4-turbo | ~30K | $0.60 |
| 06 | GPT-4-turbo | ~40K | $0.80 |
| **TOTAL** | | **~140K** | **~$2.50** |

**Alternativas gratuitas:**
- Modelos locales vía Ollama (Llama 3, Mistral)
- HuggingFace Inference API (rate-limited gratis)
- Google Colab con modelos open-source

---

## 🤝 Contribuir

¿Encontraste un error o quieres mejorar un notebook?

1. Abre un [Issue](../../issues) describiendo el problema
2. O envía un Pull Request con tu mejora
3. Asegúrate de seguir el formato estándar de notebooks
4. Verifica que el agente funcione correctamente
5. Documenta cualquier cambio en APIs o dependencias

---

## ⚠️ Consideraciones Éticas y de Seguridad

Al trabajar con agentes autónomos:

- ⚠️ **Nunca ejecutes agentes con acceso sin restricciones a sistemas críticos**
- 🔒 Usa sandboxing para ejecución de código generado
- 💰 Establece límites de gasto en APIs
- 🔍 Monitorea acciones del agente en producción
- 📝 Mantén logs detallados de decisiones del agente
- 🛡️ Valida outputs antes de ejecutar acciones irreversibles
- 🔑 Protege API keys y credenciales (usa .env, nunca hardcodees)

---

## ➡️ Próximos Pasos

Una vez completes esta ruta, puedes continuar con:

- **Proyectos Integradores** - Aplica agentes a problemas del mundo real
- **Papers Recientes** - Explora Agents 2.0, Constitutional AI, RLHF para agentes
- **Ruta Deep Learning** (futura) - Fundamenta el funcionamiento interno de LLMs
- **Contribuir al ecosistema** - Open-source agents y herramientas

### Lectura Avanzada

- Multi-modal agents (visión + lenguaje)
- Reinforcement Learning from Human Feedback (RLHF) para agentes
- Constitutional AI para agentes más seguros
- Agentic Workflows en producción
- Evaluation frameworks para agentes (AgentBench, etc.)

---

## 🌟 Ventajas de esta Ruta

Esta ruta es única porque:

1. **Implementaciones desde cero**: Entiendes cada componente internamente
2. **Multi-framework**: Aprende patterns, no solo una herramienta
3. **Costos controlados**: Alternativas locales + tracking de gastos
4. **Seguridad primero**: Cobertura de sandboxing y mejores prácticas
5. **Ejercicios prácticos**: Construye agentes reales, no solo teoría
6. **Actualizado**: Cubre técnicas de 2023-2024 (ReAct, Tree-of-Thought, etc.)
7. **Comparativas**: LangChain vs from-scratch en cada notebook

---

<div align="center">

**🧠 ¡Comienza tu viaje en Agentic AI ahora con el [Notebook 01: Introducción a LLM Agents](01-intro-llm-agents.ipynb)! 🧠**

[← Volver al README principal](../../README.md)

</div>

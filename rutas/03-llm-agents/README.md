# 🤖 Ruta 3: LLM Agents (Agentes basados en Modelos de Lenguaje)

## 📋 Descripción

Esta ruta te llevará desde los fundamentos de los agentes basados en LLMs hasta sistemas multi-agente complejos. Aprenderás cómo los modelos de lenguaje pueden actuar como "cerebros" para agentes autónomos capaces de razonar, usar herramientas y colaborar.

### ¿Por qué esta ruta es importante?

Los LLM Agents representan la frontera actual de la IA aplicada:
- **Flexibilidad**: Pueden adaptarse a nuevas tareas sin reentrenamiento
- **Razonamiento**: Capacidad de descomponer problemas complejos
- **Interacción natural**: Comunicación en lenguaje humano
- **Integración**: Conexión con APIs, bases de datos y herramientas externas

### Diferencia con RL Clásico

Mientras que los agentes de RL clásico aprenden mediante prueba y error en ambientes específicos, los LLM Agents:
- Usan conocimiento previo (preentrenamiento)
- Razonan explícitamente sobre acciones
- Se adaptan mediante prompting, no reentrenamiento
- Operan en dominios abiertos (no solo ambientes cerrados)

---

## 🎯 Objetivos de la Ruta

Al completar esta ruta, serás capaz de:

1. **Diseñar** agentes LLM para tareas autónomas complejas
2. **Implementar** patrones de razonamiento avanzados (ReAct, Chain-of-Thought)
3. **Integrar** herramientas y APIs con function calling
4. **Construir** sistemas de memoria para agentes conversacionales
5. **Orquestar** múltiples agentes colaborativos
6. **Evaluar** el desempeño y limitaciones de agentes LLM

---

## 📚 Prerequisitos

### Conocimientos de Programación
- ✅ Python intermedio (clases, decoradores, async/await)
- ✅ Manejo de APIs REST
- ✅ Familiaridad con JSON
- ✅ Comprensión de callbacks y promesas

### Conocimientos de IA/ML
- ⚠️ **Recomendado**: Completar Ruta 1 (ML Clásico) para entender conceptos base
- ⚠️ **Opcional**: Ruta 2 (RL Clásico) ayuda a contrastar paradigmas
- ✅ Nociones básicas de redes neuronales (no es obligatorio)
- ✅ Entender qué es un modelo de lenguaje

### Matemáticas
- ✅ Probabilidad básica (distribuciones, muestreo)
- ✅ Álgebra lineal básica (vectores, similitud coseno)
- ℹ️ **No requiere**: Cálculo avanzado ni teoría de grafos

### Configuración Técnica
- API key de OpenAI, Anthropic, o modelo local (LLaMA, Mistral)
- Python 3.10+
- Librerías: `openai`, `anthropic`, `langchain`, `chromadb`

---

## 🗺️ Roadmap de Notebooks

```
┌─────────────────────────────────────────────────────────────┐
│  01. Introducción a LLM Agents                              │
│  ¿Qué es un agente? LLM vs Agent                            │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  02. Prompting Agéntico                                     │
│  Chain-of-Thought, Tree-of-Thought, Self-Consistency        │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  03. ReAct (Reasoning + Acting)                             │
│  Loop: Thought → Action → Observation                       │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  04. Tool Use & Function Calling                            │
│  Integración con APIs, tool selection, error handling       │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  05. Memory Systems                                         │
│  Short-term, Long-term, RAG para agentes                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────────────────────────────────┐
│  06. Sistemas Multi-Agente                                  │
│  Colaboración, debate, especialización                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Tabla de Contenidos

| # | Notebook | Nivel | Tiempo | Conceptos Clave |
|---|----------|-------|--------|-----------------|
| 01 | **Introducción a LLM Agents** | 🟢 Principiante | 45 min | Arquitectura de agentes, ciclo percepción-acción, limitaciones |
| 02 | **Prompting Agéntico** | 🟢 Principiante | 60 min | Chain-of-Thought, Tree-of-Thought, Self-Consistency, prompting strategies |
| 03 | **ReAct (Reasoning + Acting)** | 🟡 Intermedio | 75 min | Loop ReAct, interleaving thought-action, ejemplos Wikipedia/Calculator |
| 04 | **Tool Use & Function Calling** | 🟡 Intermedio | 90 min | Function schemas, tool selection, parallel tool use, error recovery |
| 05 | **Memory Systems** | 🔴 Avanzado | 90 min | Conversation buffer, summarization, vector stores, RAG integration |
| 06 | **Sistemas Multi-Agente** | 🔴 Avanzado | 120 min | Debate, colaboración, CAMEL, AutoGPT patterns |

**Tiempo total estimado**: ~8 horas

---

## 🚀 Guías de Uso

### Modo 1: Lineal (Recomendado para principiantes)

Completa los notebooks en orden 01 → 06. Cada notebook asume que completaste los anteriores.

**Ventajas**:
- Construcción gradual de conocimiento
- Sin saltos conceptuales
- Todos los ejercicios son solucionables con lo visto

### Modo 2: Selectivo (Para quienes tienen experiencia)

Si ya conoces algunos temas, puedes saltar notebooks:

- **Solo quiero ReAct**: 01 → 03
- **Solo quiero tool use**: 01 → 04
- **Solo quiero RAG para agentes**: 01 → 05
- **Solo quiero multi-agente**: 01 → 02 → 06

### Modo 3: Por Proyecto

Comienza con un proyecto en mente y estudia los notebooks relevantes:

| Proyecto Objetivo | Notebooks Necesarios |
|-------------------|----------------------|
| **Chatbot con memoria** | 01 → 05 |
| **Agente que usa APIs** | 01 → 02 → 04 |
| **Asistente de investigación** | 01 → 03 → 05 |
| **Sistema de agentes colaborativos** | 01 → 02 → 06 |

---

## 💡 Proyectos Sugeridos

Al finalizar la ruta, podrás construir proyectos como:

### Proyecto Principiante: Asistente Personal
- Usa calendario, email, recordatorios
- Implementa memoria de conversaciones
- Maneja errores gracefully

### Proyecto Intermedio: Agente de Investigación
- Busca en web, lee papers, resume contenido
- Usa RAG para mantener contexto
- Genera reportes estructurados

### Proyecto Avanzado: Sistema Multi-Agente Colaborativo
- Agente investigador + escritor + crítico
- Debate entre agentes para refinar resultados
- Coordinación mediante protocolo de comunicación

---

## 📖 Recursos Complementarios

### Papers Fundamentales

1. **Chain-of-Thought Prompting** (Wei et al., 2022)
   - [Paper](https://arxiv.org/abs/2201.11903)
   - Introduce el concepto de razonamiento paso a paso

2. **ReAct: Synergizing Reasoning and Acting** (Yao et al., 2023)
   - [Paper](https://arxiv.org/abs/2210.03629)
   - Base del notebook 03

3. **Toolformer** (Schick et al., 2023)
   - [Paper](https://arxiv.org/abs/2302.04761)
   - LLMs que aprenden a usar herramientas

4. **Generative Agents** (Park et al., 2023)
   - [Paper](https://arxiv.org/abs/2304.03442)
   - Agentes con memoria y planificación

5. **AutoGPT y AgentGPT**
   - Arquitecturas de agentes autónomos

### Libros Recomendados

- **"Building LLM Apps"** - Valentina Alto (O'Reilly, 2024)
- **"Prompt Engineering for LLMs"** - James Phoenix & Mike Taylor

### Cursos Online

- **DeepLearning.AI**: "LangChain for LLM Application Development"
- **Andrew Ng**: "Building Systems with ChatGPT API"

### Frameworks y Herramientas

- **LangChain** ([docs](https://python.langchain.com/)): Framework completo para LLM apps
- **LlamaIndex** ([docs](https://docs.llamaindex.ai/)): RAG y data connectors
- **Semantic Kernel** (Microsoft): Orquestación de agentes
- **AutoGPT** ([GitHub](https://github.com/Significant-Gravitas/AutoGPT)): Agente autónomo

### Blogs y Comunidades

- [Lil'Log](https://lilianweng.github.io/): Blog de Lilian Weng (OpenAI)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA): Comunidad de LLMs locales
- [LangChain Blog](https://blog.langchain.dev/): Patrones y best practices

---

## ⚙️ Configuración del Entorno

### Opción 1: OpenAI API (Recomendado para empezar)

```bash
pip install openai langchain chromadb tiktoken
export OPENAI_API_KEY="tu-api-key"
```

**Costo estimado**: ~$2-5 para completar todos los notebooks

### Opción 2: Anthropic Claude

```bash
pip install anthropic langchain
export ANTHROPIC_API_KEY="tu-api-key"
```

### Opción 3: Modelos Locales (Gratuito, requiere GPU)

```bash
pip install langchain transformers accelerate
# Usar LLaMA 3, Mistral, o similar via HuggingFace
```

**Requiere**: GPU con 8GB+ VRAM (para modelos 7B) o 16GB+ (para 13B)

---

## 🧪 Validación de Conocimientos

Después de cada notebook, deberías poder:

- ✅ **Notebook 01**: Explicar la diferencia entre LLM y Agent, implementar un agente básico
- ✅ **Notebook 02**: Aplicar Chain-of-Thought a un problema nuevo
- ✅ **Notebook 03**: Implementar el loop ReAct desde cero
- ✅ **Notebook 04**: Crear un agente que use 3+ herramientas
- ✅ **Notebook 05**: Diseñar un sistema de memoria para conversaciones largas
- ✅ **Notebook 06**: Orquestar un debate entre 2+ agentes

---

## 🤝 Contribuciones

Si encuentras errores, tienes sugerencias de mejora, o quieres agregar ejemplos:
1. Abre un issue describiendo el problema/sugerencia
2. Si es código, incluye un ejemplo mínimo reproducible
3. Para nuevos notebooks, consulta las guías de estilo del proyecto

---

## 📜 Licencia

[Especificar licencia del proyecto]

---

## 🚦 Estado de Desarrollo

| Notebook | Estado | Última actualización |
|----------|--------|----------------------|
| 01-intro-llm-agents | ✅ Completo | 2025-11-15 |
| 02-prompting-agentico | ✅ Completo | 2025-11-15 |
| 03-react | ✅ Completo | 2025-11-15 |
| 04-tool-use | ✅ Completo | 2025-11-15 |
| 05-memory-systems | ✅ Completo | 2025-11-15 |
| 06-multi-agentes | ✅ Completo | 2025-11-15 |

---

**¡Comienza tu viaje en LLM Agents! 🚀**

_Siguiente paso: Abre `01-intro-llm-agents.ipynb` y descubre qué hace a un LLM ser un "agente"._

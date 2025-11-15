#!/usr/bin/env python3
"""Script para refactorizar notebook 05-memory-systems.ipynb"""

import json

def md(lines):
    """Crea celda markdown"""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

def code(lines):
    """Crea celda de código"""
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines
    }

# Cargar original
with open('05-memory-systems-ORIGINAL-BACKUP.ipynb', 'r') as f:
    original = json.load(f)

orig_cells = original['cells']

# Construir notebook refactorizado
cells = []

# ========== HEADER CON TOC ==========
cells.append(md([
    "# 05. Memory Systems para Agentes\n",
    "\n",
    "**Nivel:** 🔴 Avanzado  \n",
    "**Tiempo estimado:** 120 minutos  \n",
    "**Prerequisitos:** [01-04: Intro, Prompting, ReAct, Tool Use](01-intro-llm-agents.ipynb)\n",
    "\n",
    "## 📋 Tabla de Contenidos\n",
    "\n",
    "1. [Motivación: Agentes Que Recuerdan](#1-motivacion)\n",
    "2. [Arquitectura de Memory Systems](#2-arquitectura)\n",
    "3. [Implementación: Memory Types](#3-implementacion)\n",
    "4. [Agente con Memory System Completo](#4-agente-completo)\n",
    "5. [**🎯 Ejercicios GRADED**](#5-ejercicios-graded) ⭐\n",
    "6. [Papers Fundamentales](#6-papers)\n",
    "7. [Best Practices](#7-best-practices)\n",
    "8. [Conclusiones](#8-conclusiones)\n",
    "9. [Referencias](#9-referencias)\n",
    "10. [Navegación](#10-navegacion)\n",
    "\n",
    "---\n",
    "\n",
    "## 🎯 Objetivos de Aprendizaje\n",
    "\n",
    "Al finalizar este notebook, podrás:\n",
    "- Implementar diferentes tipos de memoria (short-term, long-term)\n",
    "- Usar vectores embeddings para retrieval semántico\n",
    "- Construir sistemas RAG (Retrieval-Augmented Generation) para agentes\n",
    "- Integrar bases de datos vectoriales (FAISS, Chroma)\n",
    "- Manejar contextos largos con windowing y summarization\n",
    "- Diseñar estrategias de memoria para conversaciones multi-turno\n"
]))

# ========== SECCIONES 1-4: CONTENIDO ORIGINAL ==========
# Copiar celdas 1-13 del original (motivación, arquitectura, implementación, agente completo, RAG)
cells.extend(orig_cells[1:14])

# ========== SECCIÓN 5: EJERCICIOS GRADED ==========
cells.append(md([
    "## 5. 🎯 Ejercicios GRADED\n",
    "\n",
    "**IMPORTANTE:** Esta sección contiene los ejercicios evaluados del notebook.\n",
    "\n",
    "- **Total de puntos:** 100\n",
    "- **Puntos para aprobar:** 70\n",
    "- **Ejercicios:** 5\n",
    "\n",
    "### 📝 Instrucciones\n",
    "\n",
    "1. Completa cada función marcada con `# TODO`\n",
    "2. Ejecuta las pruebas con: `pytest tests/test_05_memory.py -v`\n",
    "3. Verifica tu puntuación total\n",
    "\n",
    "---\n"
]))

# Ejercicio 1: implement_short_term_memory (20 pts)
cells.append(md([
    "### Ejercicio 1: Implementar Short-Term Memory (20 puntos)\n",
    "\n",
    "**Objetivo:** Crear sistema de memoria a corto plazo que mantenga los últimos N mensajes.\n",
    "\n",
    "**Requisitos:**\n",
    "- Implementar buffer con tamaño máximo configurable\n",
    "- Mantener orden cronológico\n",
    "- Descartar mensajes antiguos cuando se excede límite\n",
    "- Retornar mensajes en formato compatible con LLM APIs\n",
    "\n",
    "**Tests validarán:**\n",
    "- Buffer respeta límite max_messages\n",
    "- Mensajes más antiguos se descartan correctamente\n",
    "- Formato de salida correcto para LLM\n",
    "- Método clear() funciona\n"
]))

cells.append(code([
    "def implement_short_term_memory(max_messages: int = 10):\n",
    "    \"\"\"\n",
    "    Implementa memoria a corto plazo con buffer limitado.\n",
    "    \n",
    "    Args:\n",
    "        max_messages: Número máximo de mensajes a mantener\n",
    "    \n",
    "    Returns:\n",
    "        Objeto con métodos:\n",
    "        - add(role, content): Agregar mensaje\n",
    "        - get_messages(): Retornar lista de mensajes\n",
    "        - clear(): Limpiar buffer\n",
    "    \n",
    "    Ejemplo:\n",
    "        >>> memory = implement_short_term_memory(max_messages=3)\n",
    "        >>> memory.add(\"user\", \"Hola\")\n",
    "        >>> memory.add(\"assistant\", \"Hola, ¿cómo estás?\")\n",
    "        >>> memory.get_messages()\n",
    "        [{\"role\": \"user\", \"content\": \"Hola\"}, \n",
    "         {\"role\": \"assistant\", \"content\": \"Hola, ¿cómo estás?\"}]\n",
    "    \"\"\"\n",
    "    # TODO: Implementar aquí\n",
    "    # Pista: Usa collections.deque con maxlen\n",
    "    pass\n"
]))

# Ejercicio 2: compute_similarity (20 pts)
cells.append(md([
    "### Ejercicio 2: Calcular Similitud entre Textos (20 puntos)\n",
    "\n",
    "**Objetivo:** Implementar función de similitud semántica para retrieval de memorias.\n",
    "\n",
    "**Requisitos:**\n",
    "- Usar embeddings para representar textos\n",
    "- Calcular similitud coseno entre vectores\n",
    "- Normalizar resultados entre 0 y 1\n",
    "- Manejar casos edge (textos vacíos, etc.)\n",
    "\n",
    "**Tests validarán:**\n",
    "- Textos idénticos tienen similitud ≈ 1.0\n",
    "- Textos diferentes tienen similitud < 1.0\n",
    "- Similitud es simétrica\n",
    "- Manejo correcto de edge cases\n"
]))

cells.append(code([
    "def compute_similarity(text1: str, text2: str, encoder=None) -> float:\n",
    "    \"\"\"\n",
    "    Calcula similitud semántica entre dos textos.\n",
    "    \n",
    "    Args:\n",
    "        text1: Primer texto\n",
    "        text2: Segundo texto\n",
    "        encoder: Modelo de embeddings (opcional)\n",
    "    \n",
    "    Returns:\n",
    "        Similitud coseno entre 0.0 y 1.0\n",
    "    \n",
    "    Ejemplo:\n",
    "        >>> compute_similarity(\"me gusta Python\", \"me encanta Python\")\n",
    "        0.92\n",
    "        >>> compute_similarity(\"Python\", \"JavaScript\")\n",
    "        0.45\n",
    "    \"\"\"\n",
    "    # TODO: Implementar aquí\n",
    "    # Pista 1: Usa sentence_transformers o sklearn TfidfVectorizer\n",
    "    # Pista 2: Similitud coseno = dot(v1, v2) / (norm(v1) * norm(v2))\n",
    "    pass\n"
]))

# Ejercicio 3: retrieve_relevant_memories (25 pts)
cells.append(md([
    "### Ejercicio 3: Retrieval de Memorias Relevantes (25 puntos)\n",
    "\n",
    "**Objetivo:** Implementar sistema de retrieval semántico tipo RAG.\n",
    "\n",
    "**Requisitos:**\n",
    "- Almacenar memorias con embeddings\n",
    "- Buscar top-k memorias más relevantes dado query\n",
    "- Usar búsqueda por similitud vectorial\n",
    "- Retornar resultados ordenados por relevancia\n",
    "\n",
    "**Tests validarán:**\n",
    "- Retrieval retorna top-k correcto\n",
    "- Resultados ordenados por similitud\n",
    "- Query relevante recupera memorias correctas\n",
    "- Manejo cuando memoria vacía\n"
]))

cells.append(code([
    "def retrieve_relevant_memories(memories: List[str], query: str, top_k: int = 3) -> List[Dict]:\n",
    "    \"\"\"\n",
    "    Recupera las memorias más relevantes para un query.\n",
    "    \n",
    "    Args:\n",
    "        memories: Lista de textos en memoria\n",
    "        query: Consulta del usuario\n",
    "        top_k: Número de memorias a retornar\n",
    "    \n",
    "    Returns:\n",
    "        Lista de dicts con keys: 'text', 'similarity'\n",
    "        Ordenados de mayor a menor similitud\n",
    "    \n",
    "    Ejemplo:\n",
    "        >>> memories = [\n",
    "        ...     \"Python es un lenguaje de programación\",\n",
    "        ...     \"Me gusta el café por la mañana\",\n",
    "        ...     \"Python fue creado por Guido van Rossum\"\n",
    "        ... ]\n",
    "        >>> retrieve_relevant_memories(memories, \"¿Qué es Python?\", top_k=2)\n",
    "        [{\"text\": \"Python es un lenguaje de programación\", \"similarity\": 0.85},\n",
    "         {\"text\": \"Python fue creado por Guido van Rossum\", \"similarity\": 0.72}]\n",
    "    \"\"\"\n",
    "    # TODO: Implementar aquí\n",
    "    # Pista: Usa compute_similarity() del ejercicio anterior\n",
    "    pass\n"
]))

# Ejercicio 4: update_long_term_memory (20 pts)
cells.append(md([
    "### Ejercicio 4: Actualizar Long-Term Memory (20 puntos)\n",
    "\n",
    "**Objetivo:** Implementar persistencia de memorias importantes.\n",
    "\n",
    "**Requisitos:**\n",
    "- Detectar información importante para guardar\n",
    "- Persistir en storage (JSON, DB, etc.)\n",
    "- Recuperar memorias entre sesiones\n",
    "- Actualizar memorias existentes\n",
    "\n",
    "**Tests validarán:**\n",
    "- Memorias se guardan correctamente\n",
    "- Memorias se recuperan entre sesiones\n",
    "- Actualización de memorias existentes funciona\n",
    "- Filtrado por metadatos (timestamps, tipos)\n"
]))

cells.append(code([
    "def update_long_term_memory(memory_store: Dict, key: str, value: str, metadata: Dict = None) -> Dict:\n",
    "    \"\"\"\n",
    "    Actualiza memoria a largo plazo con persistencia.\n",
    "    \n",
    "    Args:\n",
    "        memory_store: Diccionario de memorias persistentes\n",
    "        key: Identificador de la memoria\n",
    "        value: Contenido de la memoria\n",
    "        metadata: Información adicional (timestamp, tipo, etc.)\n",
    "    \n",
    "    Returns:\n",
    "        memory_store actualizado\n",
    "    \n",
    "    Ejemplo:\n",
    "        >>> store = {}\n",
    "        >>> store = update_long_term_memory(\n",
    "        ...     store, \n",
    "        ...     \"user_name\", \n",
    "        ...     \"Alice\",\n",
    "        ...     {\"type\": \"personal_info\", \"timestamp\": \"2024-01-15\"}\n",
    "        ... )\n",
    "        >>> store[\"user_name\"]\n",
    "        {\"value\": \"Alice\", \"metadata\": {\"type\": \"personal_info\", ...}}\n",
    "    \"\"\"\n",
    "    # TODO: Implementar aquí\n",
    "    # Pista: Estructura {key: {\"value\": ..., \"metadata\": {...}}}\n",
    "    pass\n"
]))

# Ejercicio 5: memory_compression (15 pts)
cells.append(md([
    "### Ejercicio 5: Compresión de Memoria (15 puntos)\n",
    "\n",
    "**Objetivo:** Implementar compresión de memorias largas para optimizar tokens.\n",
    "\n",
    "**Requisitos:**\n",
    "- Resumir conversaciones largas preservando información clave\n",
    "- Reducir tokens sin perder contexto importante\n",
    "- Combinar múltiples mensajes en resúmenes\n",
    "\n",
    "**Tests validarán:**\n",
    "- Compresión reduce tamaño significativamente\n",
    "- Información clave se preserva\n",
    "- Resumen es coherente\n",
    "- Ratio de compresión aceptable (>50%)\n"
]))

cells.append(code([
    "def memory_compression(messages: List[Dict], max_tokens: int = 500) -> str:\n",
    "    \"\"\"\n",
    "    Comprime lista de mensajes en resumen conciso.\n",
    "    \n",
    "    Args:\n",
    "        messages: Lista de mensajes {\"role\": ..., \"content\": ...}\n",
    "        max_tokens: Máximo de tokens permitidos\n",
    "    \n",
    "    Returns:\n",
    "        Resumen comprimido de la conversación\n",
    "    \n",
    "    Ejemplo:\n",
    "        >>> messages = [\n",
    "        ...     {\"role\": \"user\", \"content\": \"Hola, mi nombre es Alice\"},\n",
    "        ...     {\"role\": \"assistant\", \"content\": \"Mucho gusto Alice\"},\n",
    "        ...     {\"role\": \"user\", \"content\": \"Me gusta Python\"},\n",
    "        ...     # ... 20 mensajes más ...\n",
    "        ... ]\n",
    "        >>> memory_compression(messages, max_tokens=100)\n",
    "        \"Alice se presentó. Expresa interés en Python...\"\n",
    "    \"\"\"\n",
    "    # TODO: Implementar aquí\n",
    "    # Pista 1: Extraer puntos clave de cada mensaje\n",
    "    # Pista 2: Simplificar sin usar LLM (para ejercicio)\n",
    "    pass\n"
]))

# ========== SECCIÓN 6: PAPERS ==========
cells.append(md([
    "## 6. 📄 Papers Fundamentales\n",
    "\n",
    "### Paper 1: Retrieval-Augmented Generation (RAG)\n",
    "\n",
    "**\"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks\"**  \n",
    "*Lewis et al., Meta AI, 2020*  \n",
    "[arXiv:2005.11401](https://arxiv.org/abs/2005.11401)\n",
    "\n",
    "**Contribución clave:**\n",
    "- Combina retrieval denso + generación seq2seq\n",
    "- Permite a LLMs acceder conocimiento externo dinámicamente\n",
    "- Supera modelos puramente paramétricos en Q&A\n",
    "\n",
    "**Arquitectura:**\n",
    "```\n",
    "Query → Dense Retriever → Top-k Docs → LLM Generator → Answer\n",
    "         (DPR)              (FAISS)       (BART)\n",
    "```\n",
    "\n",
    "**Impacto:** Base de sistemas RAG modernos (ChatGPT with browsing, Perplexity, etc.)\n",
    "\n",
    "---\n",
    "\n",
    "### Paper 2: MemGPT - LLMs as Operating Systems\n",
    "\n",
    "**\"MemGPT: Towards LLMs as Operating Systems\"**  \n",
    "*Packer et al., UC Berkeley, 2023*  \n",
    "[arXiv:2310.08560](https://arxiv.org/abs/2310.08560)\n",
    "\n",
    "**Contribución clave:**\n",
    "- Trata LLM como CPU y memoria como jerarquía (similar a OS)\n",
    "- Implementa virtual context con paging entre memoria rápida/lenta\n",
    "- Agentes manejan contextos ilimitados\n",
    "\n",
    "**Jerarquía de memoria:**\n",
    "```\n",
    "Main Context (Limited)  ←→  External Storage (Unlimited)\n",
    "     ↓                            ↓\n",
    "  Recent msgs              Vector DB / Disk\n",
    "  Active facts             Archived convos\n",
    "```\n",
    "\n",
    "**Impacto:** Inspiró sistemas de memoria en LangChain, AutoGPT, etc.\n",
    "\n",
    "---\n",
    "\n",
    "### Paper 3: Dense Passage Retrieval (DPR)\n",
    "\n",
    "**\"Dense Passage Retrieval for Open-Domain Question Answering\"**  \n",
    "*Karpukhin et al., Meta AI, 2020*  \n",
    "[arXiv:2004.04906](https://arxiv.org/abs/2004.04906)\n",
    "\n",
    "**Contribución clave:**\n",
    "- Retrieval denso supera BM25 en Q&A abierta\n",
    "- Dual-encoder: BERT para query + BERT para pasajes\n",
    "- FAISS para búsqueda eficiente en millones de docs\n",
    "\n",
    "**Método:**\n",
    "```python\n",
    "# Similarity = dot product en espacio denso\n",
    "sim(q, p) = E_Q(q)^T · E_P(p)\n",
    "```\n",
    "\n",
    "**Impacto:** Base de retrieval en RAG, embeddings en OpenAI, Pinecone, etc.\n"
]))

# ========== SECCIÓN 7: BEST PRACTICES ==========
cells.append(md([
    "## 7. ✅ Best Practices\n",
    "\n",
    "### 1. Diseño de Memory Systems\n",
    "\n",
    "**✅ DO:**\n",
    "- Usar jerarquía de memoria (buffer → resumen → vector → persistente)\n",
    "- Implementar límites de tokens claros para cada nivel\n",
    "- Combinar búsqueda semántica + keyword search (hybrid)\n",
    "- Persistir memorias críticas en storage duradero\n",
    "\n",
    "**❌ DON'T:**\n",
    "- Pasar conversación completa al LLM sin límite\n",
    "- Usar solo keyword search (pierde semántica)\n",
    "- Olvidar limpiar memorias obsoletas\n",
    "\n",
    "---\n",
    "\n",
    "### 2. RAG Optimization\n",
    "\n",
    "**✅ DO:**\n",
    "- Chunking inteligente: 256-512 tokens por chunk\n",
    "- Overlapping entre chunks (20-50 tokens)\n",
    "- Metadata filtering antes de similarity search\n",
    "- Re-ranking de resultados con cross-encoder\n",
    "\n",
    "**❌ DON'T:**\n",
    "- Chunks muy grandes (>1000 tokens) → diluye relevancia\n",
    "- Chunks muy pequeños (<100 tokens) → pierde contexto\n",
    "- Ignorar calidad de embeddings (usar modelos buenos)\n",
    "\n",
    "---\n",
    "\n",
    "### 3. Vector Databases\n",
    "\n",
    "**Selección por caso de uso:**\n",
    "\n",
    "| DB | Caso de uso | Pros | Contras |\n",
    "|---|---|---|---|\n",
    "| **FAISS** | Prototyping local | Rápido, gratis | No persistente |\n",
    "| **ChromaDB** | Apps pequeñas | Simple, embeddable | Escalabilidad limitada |\n",
    "| **Pinecone** | Producción | Managed, escalable | Costo |\n",
    "| **Weaviate** | Hybrid search | GraphQL, flexible | Complejidad |\n",
    "\n",
    "---\n",
    "\n",
    "### 4. Context Window Management\n",
    "\n",
    "**Estrategias efectivas:**\n",
    "\n",
    "```python\n",
    "# 1. Sliding Window\n",
    "def get_context(messages, window_size=10):\n",
    "    return messages[-window_size:]\n",
    "\n",
    "# 2. Summarization\n",
    "def compress_old_messages(messages, threshold=20):\n",
    "    if len(messages) > threshold:\n",
    "        old = messages[:-10]\n",
    "        summary = summarize(old)  # LLM call\n",
    "        recent = messages[-10:]\n",
    "        return [summary] + recent\n",
    "    return messages\n",
    "\n",
    "# 3. Importance Scoring\n",
    "def filter_by_importance(messages, max_tokens=4000):\n",
    "    scored = [(msg, importance_score(msg)) for msg in messages]\n",
    "    sorted_msgs = sorted(scored, key=lambda x: x[1], reverse=True)\n",
    "    # Tomar hasta max_tokens\n",
    "    return select_top_by_tokens(sorted_msgs, max_tokens)\n",
    "```\n",
    "\n",
    "---\n",
    "\n",
    "### 5. Memory Privacy & Security\n",
    "\n",
    "**✅ DO:**\n",
    "- Encriptar memorias sensibles at-rest\n",
    "- Implementar TTL (time-to-live) para datos temporales\n",
    "- User consent para persistencia de datos\n",
    "- Anonymización de PII antes de almacenar\n",
    "\n",
    "**❌ DON'T:**\n",
    "- Guardar passwords, tokens, PII sin protección\n",
    "- Compartir memorias entre usuarios sin aislamiento\n",
    "- Persistir indefinidamente sin política de retención\n"
]))

# ========== SECCIÓN 8: CONCLUSIONES ==========
cells.append(md([
    "## 8. 🎓 Conclusiones\n",
    "\n",
    "### Conceptos Clave\n",
    "\n",
    "1. **Memory Hierarchy**: Buffer → Summarization → Vector → Persistent\n",
    "2. **RAG = Retrieval + Augmented + Generation**: Permite conocimiento externo dinámico\n",
    "3. **Vector Search**: Embeddings + similarity search para retrieval semántico\n",
    "4. **Context Management**: Crítico para conversaciones largas y multi-sesión\n",
    "\n",
    "### Pregunta Inicial: ¿RESPONDIDA?\n",
    "\n",
    "**Pregunta:** *¿Cómo diseñar sistemas de memoria que permitan a agentes mantener contexto coherente en conversaciones largas y entre sesiones?*\n",
    "\n",
    "**Respuesta:**\n",
    "- Combinar múltiples niveles de memoria (corto/largo plazo)\n",
    "- Usar RAG para retrieval semántico eficiente\n",
    "- Implementar compresión/summarization para optimizar tokens\n",
    "- Persistir información crítica en storage duradero\n",
    "\n",
    "### Lo Aprendido\n",
    "\n",
    "- ✅ Implementación de diferentes tipos de memoria\n",
    "- ✅ Vector databases y semantic search\n",
    "- ✅ RAG para agentes\n",
    "- ✅ Estrategias de context window management\n",
    "- ✅ Best practices de memory systems\n",
    "\n",
    "### Próximos Pasos\n",
    "\n",
    "1. **Sistemas Multi-Agente**: Coordinación y comunicación entre agentes\n",
    "2. **Evaluación de Agentes**: Métricas, benchmarks, testing\n",
    "3. **Deployment**: Producción, escalabilidad, monitoring\n"
]))

# ========== SECCIÓN 9: REFERENCIAS ==========
cells.append(md([
    "## 9. 📚 Referencias\n",
    "\n",
    "### Papers\n",
    "\n",
    "1. Lewis et al. (2020) - [RAG for Knowledge-Intensive NLP](https://arxiv.org/abs/2005.11401)\n",
    "2. Packer et al. (2023) - [MemGPT: LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)\n",
    "3. Karpukhin et al. (2020) - [Dense Passage Retrieval](https://arxiv.org/abs/2004.04906)\n",
    "\n",
    "### Herramientas\n",
    "\n",
    "- [LangChain Memory](https://python.langchain.com/docs/modules/memory/)\n",
    "- [FAISS](https://github.com/facebookresearch/faiss)\n",
    "- [ChromaDB](https://www.trychroma.com/)\n",
    "- [Pinecone](https://www.pinecone.io/)\n",
    "- [Sentence Transformers](https://www.sbert.net/)\n",
    "\n",
    "### Documentación\n",
    "\n",
    "- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)\n",
    "- [Vector Database Comparison](https://github.com/erikbern/ann-benchmarks)\n"
]))

# ========== SECCIÓN 10: NAVEGACIÓN ==========
cells.append(md([
    "## 10. 🧭 Navegación\n",
    "\n",
    "### Notebooks de la Ruta LLM Agents\n",
    "\n",
    "1. [01 - Introducción a LLM Agents](01-intro-llm-agents.ipynb)\n",
    "2. [02 - Prompting Agéntico](02-prompting-agentico.ipynb)\n",
    "3. [03 - ReAct (Reasoning + Acting)](03-react-reasoning-acting.ipynb)\n",
    "4. [04 - Tool Use & Function Calling](04-tool-use-function-calling.ipynb)\n",
    "5. **[05 - Memory Systems](05-memory-systems.ipynb)** ⭐ Estás aquí\n",
    "6. [06 - Sistemas Multi-Agente](06-multi-agentes.ipynb)\n",
    "\n",
    "---\n",
    "\n",
    "### ⬅️ Anterior | Siguiente ➡️\n",
    "\n",
    "**[⬅️ 04 - Tool Use](04-tool-use-function-calling.ipynb)** | **[06 - Multi-Agentes ➡️](06-multi-agentes.ipynb)**\n",
    "\n",
    "---\n",
    "\n",
    "**[🏠 Volver al índice principal](../../README.md)**\n"
]))

# ========== CONSTRUIR NOTEBOOK FINAL ==========
refactored = {
    "cells": cells,
    "metadata": original["metadata"],
    "nbformat": original["nbformat"],
    "nbformat_minor": original["nbformat_minor"]
}

# Guardar
with open('05-memory-systems.ipynb', 'w', encoding='utf-8') as f:
    json.dump(refactored, f, ensure_ascii=False, indent=1)

print(f"✅ Notebook refactorizado: {len(cells)} celdas")
print("📊 Estructura:")
print("  - Header con TOC")
print("  - Secciones 1-4: Contenido original")
print("  - Sección 5: 5 ejercicios GRADED (100 pts)")
print("  - Sección 6: 3 papers fundamentales")
print("  - Sección 7: Best practices")
print("  - Secciones 8-10: Conclusiones, referencias, navegación")

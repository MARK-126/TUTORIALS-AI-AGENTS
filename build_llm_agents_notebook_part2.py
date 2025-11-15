#!/usr/bin/env python3
"""
Script para completar el notebook 01-intro-llm-agents.ipynb con secciones 7-10.
"""

import json

def markdown_cell(content):
    """Crea una celda markdown."""
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": content if isinstance(content, list) else [content]
    }

def code_cell(content):
    """Crea una celda de código."""
    return {
        "cell_type": "code",
        "metadata": {},
        "source": content if isinstance(content, list) else [content],
        "execution_count": None,
        "outputs": []
    }

# Cargar notebook parcial
with open('/home/user/TUTORIALS-AI-AGENTS/rutas/03-llm-agents/01-intro-llm-agents-PARTIAL.json', 'r') as f:
    notebook = json.load(f)

cells = notebook['cells']
print(f"📖 Cargadas {len(cells)} celdas existentes")

# ========================================
# SECCIÓN 7: EJERCICIOS AVANZADOS
# ========================================
print("Construyendo sección 7: Ejercicios Avanzados...")

cells.append(markdown_cell([
    '<a id="7-ejercicios-avanzados"></a>\n',
    "## 7. Ejercicios Avanzados (Opcionales)\n",
    "\n",
    "Estos ejercicios son para profundizar tu comprensión. No son calificados, pero te ayudarán a desarrollar habilidades avanzadas.\n"
]))

cells.append(markdown_cell([
    "### 🟡 Ejercicio Avanzado 1: Multi-Step Tool Use\n",
    "\n",
    "**Desafío**: Implementa un agente que pueda usar múltiples herramientas en secuencia.\n",
    "\n",
    "**Ejemplo**:\n",
    "- Query: \"Calcula cuántos días faltan para el 31 de diciembre y multiplica por 24\"\n",
    "- Paso 1: Usar `get_time` para obtener fecha actual\n",
    "- Paso 2: Usar `calculator` para calcular días restantes\n",
    "- Paso 3: Usar `calculator` para multiplicar por 24\n",
    "- Paso 4: Responder\n",
    "\n",
    "**Pistas**:\n",
    "- Necesitarás un loop en `SimpleAgent.run()`\n",
    "- Después de cada tool use, actualiza la query con la observación\n",
    "- Limita el número de iteraciones para evitar loops infinitos\n"
]))

cells.append(code_cell([
    "# Tu código aquí\n",
    "# Modifica SimpleAgent o crea MultiStepAgent\n",
    "\n",
    "pass\n"
]))

cells.append(markdown_cell([
    "### 🟡 Ejercicio Avanzado 2: Error Recovery\n",
    "\n",
    "**Desafío**: Implementa un agente que pueda recuperarse de errores.\n",
    "\n",
    "**Escenarios**:\n",
    "1. Tool falla → Agente intenta con otra herramienta\n",
    "2. Input inválido → Agente reformula el input\n",
    "3. Resultado inesperado → Agente razona y reintenta\n",
    "\n",
    "**Ejemplo**:\n",
    "```\n",
    "User: \"Divide 100 entre 0\"\n",
    "Agent: *intenta calculator(100/0)*\n",
    "Tool: \"Error: division by zero\"\n",
    "Agent: \"Lo siento, no puedo dividir entre cero. El resultado no está definido.\"\n",
    "```\n"
]))

cells.append(code_cell([
    "# Tu código aquí\n",
    "# Agrega lógica de retry y error handling\n",
    "\n",
    "pass\n"
]))

cells.append(markdown_cell([
    "### 🔴 Ejercicio Avanzado 3: Planning Agent\n",
    "\n",
    "**Desafío**: Implementa un agente que planifique antes de actuar.\n",
    "\n",
    "**Arquitectura**:\n",
    "1. **Planner**: Descompone tarea compleja en subtareas\n",
    "2. **Executor**: Ejecuta cada subtarea\n",
    "3. **Validator**: Verifica que el plan funcionó\n",
    "\n",
    "**Ejemplo**:\n",
    "```\n",
    "Task: \"Investiga qué lenguaje de programación es más popular y calcula su crecimiento\"\n",
    "\n",
    "Plan:\n",
    "1. Search(\"most popular programming language 2024\")\n",
    "2. Extract(language_name from results)\n",
    "3. Search(f\"{language_name} popularity growth rate\")\n",
    "4. Calculate(growth_percentage)\n",
    "5. Summarize(findings)\n",
    "```\n",
    "\n",
    "**Recursos**:\n",
    "- Paper: \"ReAct: Synergizing Reasoning and Acting in Language Models\"\n",
    "- Paper: \"Plan-and-Solve Prompting\"\n"
]))

cells.append(code_cell([
    "# Tu código aquí\n",
    "# Implementa PlanningAgent con fases separadas\n",
    "\n",
    "class PlanningAgent:\n",
    "    def __init__(self, tools, llm):\n",
    "        pass\n",
    "    \n",
    "    def plan(self, task: str) -> List[str]:\n",
    "        \"\"\"Genera un plan de pasos a seguir\"\"\"\n",
    "        pass\n",
    "    \n",
    "    def execute_plan(self, plan: List[str]):\n",
    "        \"\"\"Ejecuta el plan paso a paso\"\"\"\n",
    "        pass\n"
]))

cells.append(markdown_cell([
    "### 🔴 Ejercicio Avanzado 4: Multi-Agent System\n",
    "\n",
    "**Desafío**: Crea un sistema con múltiples agentes especializados.\n",
    "\n",
    "**Agentes**:\n",
    "1. **Researcher**: Busca información\n",
    "2. **Analyzer**: Analiza datos\n",
    "3. **Writer**: Redacta respuestas\n",
    "4. **Coordinator**: Orquesta a los demás\n",
    "\n",
    "**Ejemplo de flujo**:\n",
    "```\n",
    "User: \"Escribe un resumen sobre el cambio climático con datos actuales\"\n",
    "\n",
    "Coordinator → Researcher: \"Busca datos sobre cambio climático 2024\"\n",
    "Researcher → Analyzer: [datos encontrados]\n",
    "Analyzer → Writer: [análisis estadístico]\n",
    "Writer → User: [resumen bien escrito]\n",
    "```\n",
    "\n",
    "**Recursos**:\n",
    "- Paper: \"MetaGPT: Meta Programming for Multi-Agent Collaborative Framework\"\n",
    "- Framework: AutoGen (Microsoft Research)\n"
]))

cells.append(code_cell([
    "# Tu código aquí\n",
    "# Implementa sistema multi-agente\n",
    "\n",
    "pass\n"
]))

print("Sección 7: Ejercicios Avanzados... OK")

# ========================================
# SECCIÓN 8: PAPERS
# ========================================
print("Construyendo sección 8: Papers...")

cells.append(markdown_cell([
    '<a id="8-papers"></a>\n',
    "## 8. 📄 Papers y Referencias\n",
    "\n",
    "Los LLM Agents son un campo muy reciente (2022-2024). Aquí tienes los papers más importantes organizados por tema.\n",
    "\n",
    "### 📖 Guía de Lectura\n",
    "\n",
    "**Para Principiantes** (empieza aquí):\n",
    "1. ReAct paper (Yao et al., 2023)\n",
    "2. Lilian Weng's blog post\n",
    "3. Chain-of-Thought paper (Wei et al., 2022)\n",
    "\n",
    "**Para Implementadores**:\n",
    "1. Toolformer (Schick et al., 2023)\n",
    "2. ToolLLM (Qin et al., 2023)\n",
    "3. Gorilla (Patil et al., 2023)\n",
    "\n",
    "**Para Investigadores**:\n",
    "1. Surveys (Wang et al., Xi et al.)\n",
    "2. Evaluation papers (AgentBench, WebArena)\n",
    "3. Multi-agent systems (MetaGPT, AutoGen)\n",
    "\n",
    "---\n"
]))

cells.append(markdown_cell([
    "### 🏛️ Papers Fundacionales\n",
    "\n",
    "1. **ReAct: Synergizing Reasoning and Acting in Language Models**\n",
    "   - Autores: Yao et al., ICLR 2023\n",
    "   - Link: https://arxiv.org/abs/2210.03629\n",
    "   - Citas: 3,500+\n",
    "   - **Por qué leerlo**: Introduce el patrón ReAct (Reasoning + Acting) que usamos en este notebook. Es THE foundational paper para agentes.\n",
    "   - **Key insight**: Alternar entre razonamiento (thinking) y acción (tool use) mejora significativamente el desempeño.\n",
    "\n",
    "2. **Toolformer: Language Models Can Teach Themselves to Use Tools**\n",
    "   - Autores: Schick et al., Meta AI, 2023\n",
    "   - Link: https://arxiv.org/abs/2302.04761\n",
    "   - Citas: 2,800+\n",
    "   - **Por qué leerlo**: Muestra cómo LLMs pueden aprender a usar herramientas mediante self-supervised learning.\n",
    "   - **Key insight**: Los LLMs pueden autodescubrir cuándo necesitan herramientas externas.\n",
    "\n",
    "3. **Language Models as Agent Models**\n",
    "   - Autores: Andreas, MIT, 2022\n",
    "   - Link: https://arxiv.org/abs/2212.01681\n",
    "   - **Por qué leerlo**: Análisis teórico profundo sobre LLMs como agentes.\n",
    "   - **Key insight**: Formaliza la conexión entre LLMs y teoría de agentes en RL.\n"
]))

cells.append(markdown_cell([
    "### 🎯 Prompting y Razonamiento\n",
    "\n",
    "4. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**\n",
    "   - Autores: Wei et al., Google Research, 2022\n",
    "   - Link: https://arxiv.org/abs/2201.11903\n",
    "   - Citas: 8,000+ (MEGA influential)\n",
    "   - **Por qué leerlo**: Revolucionó cómo hacemos prompting. Base de todo razonamiento agéntico.\n",
    "   - **Key insight**: \"Let's think step by step\" mejora dramáticamente el razonamiento.\n",
    "\n",
    "5. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**\n",
    "   - Autores: Yao et al., Princeton, 2023\n",
    "   - Link: https://arxiv.org/abs/2305.10601\n",
    "   - Citas: 1,200+\n",
    "   - **Por qué leerlo**: Extiende CoT a exploración tipo árbol.\n",
    "   - **Key insight**: Explorar múltiples caminos de razonamiento en paralelo.\n",
    "\n",
    "6. **Self-Consistency Improves Chain of Thought Reasoning**\n",
    "   - Autores: Wang et al., Google Research, 2022\n",
    "   - Link: https://arxiv.org/abs/2203.11171\n",
    "   - Citas: 2,500+\n",
    "   - **Por qué leerlo**: Técnica simple pero poderosa para mejorar precisión.\n",
    "   - **Key insight**: Generar múltiples respuestas y votar por mayoría.\n"
]))

cells.append(markdown_cell([
    "### 🔧 Tool Use y Function Calling\n",
    "\n",
    "7. **Gorilla: Large Language Model Connected with Massive APIs**\n",
    "   - Autores: Patil et al., UC Berkeley, 2023\n",
    "   - Link: https://arxiv.org/abs/2305.15334\n",
    "   - **Por qué leerlo**: LLM especializado en llamar APIs correctamente.\n",
    "   - **Key insight**: Fine-tuning específico para tool use mejora mucho la precisión.\n",
    "\n",
    "8. **ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs**\n",
    "   - Autores: Qin et al., Tsinghua University, 2023\n",
    "   - Link: https://arxiv.org/abs/2307.16789\n",
    "   - **Por qué leerlo**: Dataset masivo de APIs reales + framework de evaluación.\n",
    "   - **Key insight**: Necesitamos datasets especializados para entrenar agentes efectivos.\n",
    "\n",
    "9. **OpenAI Function Calling**\n",
    "   - Documentación: https://platform.openai.com/docs/guides/function-calling\n",
    "   - **Por qué leerlo**: Estándar de facto en la industria.\n",
    "   - **Key insight**: Structured outputs hacen tool use más confiable.\n"
]))

cells.append(markdown_cell([
    "### 👥 Multi-Agent Systems\n",
    "\n",
    "10. **MetaGPT: Meta Programming for Multi-Agent Collaborative Framework**\n",
    "    - Autores: Hong et al., 2023\n",
    "    - Link: https://arxiv.org/abs/2308.00352\n",
    "    - Citas: 800+\n",
    "    - **Por qué leerlo**: Framework para múltiples agentes colaborando en desarrollo de software.\n",
    "    - **Key insight**: Asignar roles (Product Manager, Engineer, QA) mejora colaboración.\n",
    "\n",
    "11. **AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**\n",
    "    - Autores: Wu et al., Microsoft Research, 2023\n",
    "    - Link: https://arxiv.org/abs/2308.08155\n",
    "    - **Por qué leerlo**: Framework práctico de Microsoft para multi-agentes.\n",
    "    - **Key insight**: Conversaciones entre agentes pueden resolver tareas complejas.\n",
    "\n",
    "12. **AgentVerse: Facilitating Multi-Agent Collaboration**\n",
    "    - Autores: Chen et al., Tsinghua, 2023\n",
    "    - Link: https://arxiv.org/abs/2308.10848\n",
    "    - **Por qué leerlo**: Estudia dinámicas de grupos de agentes.\n",
    "    - **Key insight**: Diferentes topologías de comunicación afectan el desempeño.\n"
]))

cells.append(markdown_cell([
    "### 🧠 Memory y RAG\n",
    "\n",
    "13. **MemGPT: Towards LLMs as Operating Systems**\n",
    "    - Autores: Packer et al., UC Berkeley, 2023\n",
    "    - Link: https://arxiv.org/abs/2310.08560\n",
    "    - **Por qué leerlo**: Innovadora arquitectura de memoria inspirada en OS.\n",
    "    - **Key insight**: Separar memoria en main context + external storage como un OS.\n",
    "\n",
    "14. **Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks**\n",
    "    - Autores: Lewis et al., Meta AI, 2020\n",
    "    - Link: https://arxiv.org/abs/2005.11401\n",
    "    - Citas: 5,000+\n",
    "    - **Por qué leerlo**: Fundación de RAG, critical para agentes con conocimiento externo.\n",
    "    - **Key insight**: Combinar retrieval + generation supera modelos puramente paramétricos.\n",
    "\n",
    "15. **Reflexion: Language Agents with Verbal Reinforcement Learning**\n",
    "    - Autores: Shinn et al., Northeastern, 2023\n",
    "    - Link: https://arxiv.org/abs/2303.11366\n",
    "    - Citas: 900+\n",
    "    - **Por qué leerlo**: Agentes que aprenden de sus errores mediante auto-reflexión.\n",
    "    - **Key insight**: Feedback textual permite \"reinforcement learning\" sin gradientes.\n"
]))

cells.append(markdown_cell([
    "### 📋 Planning\n",
    "\n",
    "16. **HuggingGPT: Solving AI Tasks with ChatGPT and Friends in Hugging Face**\n",
    "    - Autores: Shen et al., Microsoft, 2023\n",
    "    - Link: https://arxiv.org/abs/2303.17580\n",
    "    - Citas: 1,500+\n",
    "    - **Por qué leerlo**: LLM como controlador de otros modelos especializados.\n",
    "    - **Key insight**: Un LLM puede orquestar cientos de modelos especializados.\n",
    "\n",
    "17. **Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning**\n",
    "    - Autores: Wang et al., 2023\n",
    "    - Link: https://arxiv.org/abs/2305.04091\n",
    "    - Citas: 600+\n",
    "    - **Por qué leerlo**: Mejora CoT al separar planning y execution.\n",
    "    - **Key insight**: \"Let's first understand the problem and devise a plan\" funciona mejor que CoT vanilla.\n"
]))

cells.append(markdown_cell([
    "### 🧪 Evaluation y Benchmarks\n",
    "\n",
    "18. **AgentBench: Evaluating LLMs as Agents**\n",
    "    - Autores: Liu et al., Tsinghua, 2023\n",
    "    - Link: https://arxiv.org/abs/2308.03688\n",
    "    - **Por qué leerlo**: Benchmark comprehensive para evaluar agentes.\n",
    "    - **Key insight**: Performance en benchmarks tradicionales != performance como agente.\n",
    "\n",
    "19. **WebArena: A Realistic Web Environment for Building Autonomous Agents**\n",
    "    - Autores: Zhou et al., CMU, 2023\n",
    "    - Link: https://arxiv.org/abs/2307.13854\n",
    "    - **Por qué leerlo**: Environment realista para evaluar web agents.\n",
    "    - **Key insight**: Agents actuales aún luchan con tareas web complejas.\n"
]))

cells.append(markdown_cell([
    "### 🛡️ Safety y Alignment\n",
    "\n",
    "20. **Jailbroken: How Does LLM Safety Training Fail?**\n",
    "    - Autores: Wei et al., Anthropic + OpenAI, 2023\n",
    "    - Link: https://arxiv.org/abs/2307.02483\n",
    "    - **Por qué leerlo**: Critical para entender vulnerabilidades de agentes.\n",
    "    - **Key insight**: Safety training puede fallar de maneras sorprendentes.\n",
    "\n",
    "21. **Constitutional AI: Harmlessness from AI Feedback**\n",
    "    - Autores: Bai et al., Anthropic, 2022\n",
    "    - Link: https://arxiv.org/abs/2212.08073\n",
    "    - Citas: 1,200+\n",
    "    - **Por qué leerlo**: Método de Anthropic para alinear agentes.\n",
    "    - **Key insight**: LLMs pueden auto-mejorarse usando principios constitucionales.\n"
]))

cells.append(markdown_cell([
    "### 📚 Surveys y Reviews\n",
    "\n",
    "22. **A Survey on Large Language Model based Autonomous Agents**\n",
    "    - Autores: Wang et al., 2023\n",
    "    - Link: https://arxiv.org/abs/2308.11432\n",
    "    - Citas: 800+\n",
    "    - **Por qué leerlo**: Comprehensive survey de ~50 páginas. Excelente overview.\n",
    "    - **Scope**: Cubre construcción, aplicaciones, y evaluación de agentes.\n",
    "\n",
    "23. **The Rise and Potential of Large Language Model Based Agents**\n",
    "    - Autores: Xi et al., 2023\n",
    "    - Link: https://arxiv.org/abs/2309.07864\n",
    "    - Citas: 500+\n",
    "    - **Por qué leerlo**: Survey reciente con foco en aplicaciones prácticas.\n",
    "    - **Scope**: Desde fundamentos hasta aplicaciones en robótica, gaming, etc.\n"
]))

cells.append(markdown_cell([
    "### 🏗️ Frameworks y Documentación\n",
    "\n",
    "24. **LangChain Documentation**\n",
    "    - Link: https://python.langchain.com/docs/modules/agents/\n",
    "    - **Por qué leerlo**: Framework más popular para agentes.\n",
    "    - **Scope**: Tutoriales, ejemplos, best practices.\n",
    "\n",
    "25. **LlamaIndex Documentation**\n",
    "    - Link: https://docs.llamaindex.ai/en/stable/\n",
    "    - **Por qué leerlo**: Mejor framework para RAG + agentes.\n",
    "    - **Scope**: Especialmente fuerte en data connectors.\n"
]))

cells.append(markdown_cell([
    "### 📝 Blogs y Recursos Educativos\n",
    "\n",
    "26. **LLM Powered Autonomous Agents** (Lilian Weng)\n",
    "    - Link: https://lilianweng.github.io/posts/2023-06-23-agent/\n",
    "    - **Por qué leerlo**: Excelente overview técnico por investigadora de OpenAI.\n",
    "    - **Scope**: Cubre planning, memory, tool use con diagramas claros.\n",
    "\n",
    "27. **Building LLM applications for production** (Chip Huyen)\n",
    "    - Link: https://huyenchip.com/2023/04/11/llm-engineering.html\n",
    "    - **Por qué leerlo**: Perspectiva práctica de ingeniera en Snorkel AI.\n",
    "    - **Scope**: Costos, latencia, evaluación, prompt engineering.\n"
]))

cells.append(markdown_cell([
    "### 🗺️ Roadmap de Lectura por Caso de Uso\n",
    "\n",
    "**Si quieres construir un asistente personal**:\n",
    "- ReAct → MemGPT → Reflexion → ToolLLM\n",
    "\n",
    "**Si quieres construir agentes para desarrollo de software**:\n",
    "- MetaGPT → HuggingGPT → AutoGen → AgentBench\n",
    "\n",
    "**Si quieres construir agentes con bases de datos/documentos**:\n",
    "- RAG → LlamaIndex docs → MemGPT → ToolLLM\n",
    "\n",
    "**Si estás investigando agentes en general**:\n",
    "- Wang et al. survey → Xi et al. survey → Papers por tema de interés\n",
    "\n",
    "**Si te preocupa safety**:\n",
    "- Constitutional AI → Jailbroken → AgentBench (eval section)\n"
]))

print("Sección 8: Papers... OK")

# ========================================
# SECCIÓN 9: BEST PRACTICES
# ========================================
print("Construyendo sección 9: Best Practices...")

cells.append(markdown_cell([
    '<a id="9-best-practices"></a>\n',
    "## 9. 💡 Best Practices y Producción\n",
    "\n",
    "Implementar agentes en producción requiere consideraciones especiales que van más allá de prototipos.\n"
]))

cells.append(markdown_cell([
    "### 🏗️ Arquitectura para Producción\n",
    "\n",
    "**Principios clave**:\n",
    "\n",
    "1. **Separation of Concerns**\n",
    "   - LLM brain: Solo razonamiento\n",
    "   - Tools: Lógica de negocio aislada\n",
    "   - Orchestrator: Control de flujo\n",
    "   - State management: Separado del resto\n",
    "\n",
    "2. **Observability**\n",
    "   ```python\n",
    "   # Logging exhaustivo\n",
    "   logger.info(f\"Agent step {i}: Tool={action.tool}, Input={action.input}\")\n",
    "   logger.info(f\"Tool output: {observation}\")\n",
    "   logger.info(f\"LLM tokens: {response.usage}\")\n",
    "   ```\n",
    "\n",
    "3. **Error Handling**\n",
    "   ```python\n",
    "   try:\n",
    "       result = tool.run(input)\n",
    "   except ToolExecutionError as e:\n",
    "       # Log error\n",
    "       # Retry con exponential backoff\n",
    "       # O skip y continuar\n",
    "   except Exception as e:\n",
    "       # Log unexpected error\n",
    "       # Graceful degradation\n",
    "   ```\n",
    "\n",
    "4. **Rate Limiting y Costos**\n",
    "   ```python\n",
    "   # Limitar llamadas a LLM\n",
    "   @rate_limit(calls_per_minute=60)\n",
    "   def call_llm(prompt):\n",
    "       ...\n",
    "   \n",
    "   # Monitorear costos\n",
    "   cost_tracker.add(tokens_used * price_per_token)\n",
    "   if cost_tracker.total > budget:\n",
    "       raise BudgetExceededError()\n",
    "   ```\n"
]))

cells.append(markdown_cell([
    "### 🐛 Common Pitfalls y Soluciones\n",
    "\n",
    "#### Pitfall 1: Infinite Loops\n",
    "\n",
    "**Problema**: Agente entra en loop infinito.\n",
    "\n",
    "```python\n",
    "# ❌ MAL\n",
    "while True:\n",
    "    action = agent.step()\n",
    "    if action.is_final:\n",
    "        break\n",
    "```\n",
    "\n",
    "**Solución**:\n",
    "```python\n",
    "# ✅ BIEN\n",
    "max_iterations = 10\n",
    "for i in range(max_iterations):\n",
    "    action = agent.step()\n",
    "    if action.is_final:\n",
    "        break\n",
    "else:\n",
    "    logger.warning(f\"Agent hit max iterations ({max_iterations})\")\n",
    "    return fallback_response()\n",
    "```\n",
    "\n",
    "#### Pitfall 2: Prompt Injection\n",
    "\n",
    "**Problema**: Usuario manipula el agente via prompts maliciosos.\n",
    "\n",
    "```python\n",
    "# ❌ VULNERABLE\n",
    "prompt = f\"User query: {user_input}\"  # user_input podría contener \"Ignore previous instructions...\"\n",
    "```\n",
    "\n",
    "**Solución**:\n",
    "```python\n",
    "# ✅ MEJOR\n",
    "# 1. Sanitizar input\n",
    "user_input = sanitize(user_input)\n",
    "\n",
    "# 2. Usar structured prompts\n",
    "messages = [\n",
    "    {\"role\": \"system\", \"content\": \"You are a helpful assistant...\"},\n",
    "    {\"role\": \"user\", \"content\": user_input}  # Claramente separado\n",
    "]\n",
    "\n",
    "# 3. Validar outputs\n",
    "if not is_safe_action(action):\n",
    "    raise SecurityError()\n",
    "```\n",
    "\n",
    "#### Pitfall 3: Tool Hallucination\n",
    "\n",
    "**Problema**: LLM inventa herramientas que no existen.\n",
    "\n",
    "**Solución**:\n",
    "```python\n",
    "# Validar tool calls\n",
    "if action.tool not in available_tools:\n",
    "    # Re-prompt con lista de herramientas válidas\n",
    "    error_prompt = f\"\"\"Error: '{action.tool}' no existe.\n",
    "    Herramientas disponibles: {list(available_tools.keys())}\n",
    "    Por favor, elige una herramienta válida.\"\"\"\n",
    "    return agent.step(error_prompt)\n",
    "```\n",
    "\n",
    "#### Pitfall 4: Context Window Overflow\n",
    "\n",
    "**Problema**: Historial crece hasta exceder context window.\n",
    "\n",
    "**Solución**:\n",
    "```python\n",
    "# Summarization strategy\n",
    "if len(history) > max_history:\n",
    "    # Resumir historia antigua\n",
    "    summary = llm.summarize(history[:10])\n",
    "    history = [{\"role\": \"system\", \"content\": f\"Summary: {summary}\"}] + history[10:]\n",
    "```\n"
]))

cells.append(markdown_cell([
    "### 💰 Cost Optimization\n",
    "\n",
    "**Estrategias**:\n",
    "\n",
    "1. **Use cheaper models where possible**\n",
    "   ```python\n",
    "   # GPT-4 para razonamiento crítico\n",
    "   # GPT-3.5 para tareas simples\n",
    "   if complexity_score(task) > threshold:\n",
    "       model = \"gpt-4\"\n",
    "   else:\n",
    "       model = \"gpt-3.5-turbo\"\n",
    "   ```\n",
    "\n",
    "2. **Cache responses**\n",
    "   ```python\n",
    "   @cache(ttl=3600)  # Cache por 1 hora\n",
    "   def call_llm(prompt):\n",
    "       # Queries idénticas no gastan API calls\n",
    "   ```\n",
    "\n",
    "3. **Batch operations**\n",
    "   ```python\n",
    "   # En vez de 10 llamadas\n",
    "   results = [llm.call(q) for q in queries]  # ❌ 10x costo\n",
    "   \n",
    "   # Batch\n",
    "   batch_prompt = \"\\n\".join(f\"{i}. {q}\" for i, q in enumerate(queries))\n",
    "   batch_result = llm.call(batch_prompt)  # ✅ 1x costo (tal vez)\n",
    "   ```\n",
    "\n",
    "4. **Monitoreo de costos**\n",
    "   ```python\n",
    "   class CostTracker:\n",
    "       def __init__(self, budget: float):\n",
    "           self.budget = budget\n",
    "           self.spent = 0.0\n",
    "       \n",
    "       def add_call(self, tokens: int, model: str):\n",
    "           cost = tokens * PRICE_PER_1K_TOKENS[model] / 1000\n",
    "           self.spent += cost\n",
    "           if self.spent > self.budget:\n",
    "               raise BudgetExceededError(f\"Spent ${self.spent:.2f} > ${self.budget:.2f}\")\n",
    "   ```\n"
]))

cells.append(markdown_cell([
    "### 🔒 Security Best Practices\n",
    "\n",
    "1. **Sandboxing de tool execution**\n",
    "   ```python\n",
    "   # ❌ PELIGROSO: eval directo\n",
    "   result = eval(user_code)\n",
    "   \n",
    "   # ✅ SEGURO: sandbox\n",
    "   import docker\n",
    "   container = docker.from_image(\"python:3.9-alpine\")\n",
    "   result = container.exec(user_code, timeout=5, network=False)\n",
    "   ```\n",
    "\n",
    "2. **Principle of Least Privilege**\n",
    "   - Tools solo tienen permisos mínimos necesarios\n",
    "   - Database tools → read-only cuando sea posible\n",
    "   - File system tools → limitados a directorio específico\n",
    "\n",
    "3. **Input Validation**\n",
    "   ```python\n",
    "   def validate_tool_input(tool_name: str, input_str: str):\n",
    "       if tool_name == \"database_query\":\n",
    "           # No permitir DROP, DELETE, etc.\n",
    "           forbidden = [\"DROP\", \"DELETE\", \"UPDATE\", \"INSERT\"]\n",
    "           if any(kw in input_str.upper() for kw in forbidden):\n",
    "               raise SecurityError(\"Forbidden SQL operation\")\n",
    "   ```\n",
    "\n",
    "4. **Audit Logging**\n",
    "   ```python\n",
    "   # Log TODAS las acciones para auditoria\n",
    "   audit_log.record({\n",
    "       \"timestamp\": datetime.now(),\n",
    "       \"user_id\": user.id,\n",
    "       \"agent_id\": agent.id,\n",
    "       \"action\": action.tool,\n",
    "       \"input\": action.input,\n",
    "       \"output\": result,\n",
    "       \"cost\": cost\n",
    "   })\n",
    "   ```\n"
]))

cells.append(markdown_cell([
    "### 📊 Monitoring y Metrics\n",
    "\n",
    "**Métricas críticas a trackear**:\n",
    "\n",
    "1. **Performance Metrics**\n",
    "   - Latency promedio por query\n",
    "   - Latency p95, p99\n",
    "   - Success rate\n",
    "   - Tool usage distribution\n",
    "\n",
    "2. **Cost Metrics**\n",
    "   - Costo por query\n",
    "   - Tokens promedio por query\n",
    "   - Costo total diario/mensual\n",
    "\n",
    "3. **Quality Metrics**\n",
    "   - User satisfaction (thumbs up/down)\n",
    "   - Task completion rate\n",
    "   - Retry rate\n",
    "   - Error rate por tipo de error\n",
    "\n",
    "4. **Agent Behavior Metrics**\n",
    "   - Promedio de pasos por query\n",
    "   - Tool call accuracy\n",
    "   - Hallucination rate\n",
    "   - Loop frequency\n",
    "\n",
    "**Ejemplo de dashboard**:\n",
    "```python\n",
    "# Prometheus + Grafana\n",
    "from prometheus_client import Counter, Histogram\n",
    "\n",
    "queries_total = Counter('agent_queries_total', 'Total queries')\n",
    "query_duration = Histogram('agent_query_duration_seconds', 'Query duration')\n",
    "query_cost = Histogram('agent_query_cost_dollars', 'Query cost')\n",
    "\n",
    "with query_duration.time():\n",
    "    result = agent.run(query)\n",
    "    queries_total.inc()\n",
    "    query_cost.observe(calculate_cost(result))\n",
    "```\n"
]))

cells.append(markdown_cell([
    "### 🎯 Use Cases Reales y Patrones\n",
    "\n",
    "#### Use Case 1: Customer Support Agent\n",
    "\n",
    "**Arquitectura**:\n",
    "- **Tools**: FAQ search, ticket creation, knowledge base RAG\n",
    "- **Memory**: Conversation history + user profile\n",
    "- **Fallback**: Escalate to human si confidence < threshold\n",
    "\n",
    "**Patrón**:\n",
    "```python\n",
    "if agent.confidence < 0.7:\n",
    "    return escalate_to_human(query, context)\n",
    "```\n",
    "\n",
    "#### Use Case 2: Code Review Agent\n",
    "\n",
    "**Arquitectura**:\n",
    "- **Tools**: Static analysis, test runner, git diff\n",
    "- **Memory**: Code style guide, previous reviews\n",
    "- **Output**: Structured comments in GitHub\n",
    "\n",
    "**Patrón**:\n",
    "```python\n",
    "# Multi-pass review\n",
    "pass1 = agent.review(code, focus=\"bugs\")\n",
    "pass2 = agent.review(code, focus=\"style\")\n",
    "pass3 = agent.review(code, focus=\"performance\")\n",
    "```\n",
    "\n",
    "#### Use Case 3: Data Analysis Agent\n",
    "\n",
    "**Arquitectura**:\n",
    "- **Tools**: SQL query, Python exec (sandboxed), plotting\n",
    "- **Memory**: Dataset schema, previous queries\n",
    "- **Output**: Visualizations + narrative insights\n",
    "\n",
    "**Patrón**:\n",
    "```python\n",
    "# Iterative refinement\n",
    "query = agent.generate_sql(user_question)\n",
    "results = db.execute(query)\n",
    "if results.empty:\n",
    "    query = agent.refine_sql(query, \"No results, try different approach\")\n",
    "```\n"
]))

cells.append(markdown_cell([
    "### ✅ Production Checklist\n",
    "\n",
    "Antes de deployar a producción:\n",
    "\n",
    "**Funcionalidad**:\n",
    "- [ ] Manejo de errores en todos los tool calls\n",
    "- [ ] Límites de iteraciones del agent loop\n",
    "- [ ] Fallback responses para casos sin respuesta\n",
    "- [ ] Validación de todos los inputs y outputs\n",
    "\n",
    "**Performance**:\n",
    "- [ ] Latency p95 < SLA target\n",
    "- [ ] Caching implementado donde sea posible\n",
    "- [ ] Rate limiting configurado\n",
    "- [ ] Timeouts en todos los IO operations\n",
    "\n",
    "**Security**:\n",
    "- [ ] Tool execution sandboxed\n",
    "- [ ] Input sanitization implementada\n",
    "- [ ] Secrets management (no hardcoded API keys)\n",
    "- [ ] Audit logging habilitado\n",
    "\n",
    "**Observability**:\n",
    "- [ ] Logging estructurado\n",
    "- [ ] Metrics dashboard configurado\n",
    "- [ ] Alertas para errores críticos\n",
    "- [ ] Tracing de requests end-to-end\n",
    "\n",
    "**Cost Management**:\n",
    "- [ ] Budget limits configurados\n",
    "- [ ] Cost tracking por usuario/query\n",
    "- [ ] Alertas de costo anormal\n",
    "- [ ] Modelo selection logic (cheap vs expensive)\n",
    "\n",
    "**Testing**:\n",
    "- [ ] Unit tests para cada tool\n",
    "- [ ] Integration tests para agent loop\n",
    "- [ ] Adversarial tests (prompt injection, etc.)\n",
    "- [ ] Load testing completado\n"
]))

print("Sección 9: Best Practices... OK")

# ========================================
# SECCIÓN 10: NAVEGACIÓN
# ========================================
print("Construyendo sección 10: Navegación...")

cells.append(markdown_cell([
    '<a id="10-navegacion"></a>\n',
    "## 10. 📍 Navegación y Próximos Pasos\n",
    "\n",
    "### 🎉 ¡Felicitaciones!\n",
    "\n",
    "Has completado el notebook de Introducción a LLM Agents. Ahora puedes:\n",
    "\n",
    "✅ Explicar la diferencia entre un LLM y un Agente  \n",
    "✅ Implementar un agente básico desde cero  \n",
    "✅ Entender el loop observación → razonamiento → acción  \n",
    "✅ Usar frameworks como LangChain  \n",
    "✅ Conocer los papers fundamentales del campo  \n",
    "✅ Aplicar best practices para producción  \n"
]))

cells.append(markdown_cell([
    "### 📚 Ruta de Aprendizaje Sugerida\n",
    "\n",
    "```\n",
    "Tú estás aquí ──┐\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 01. Intro a LLM Agents ✅                                   │\n",
    "│ • Fundamentos de agentes                                    │\n",
    "│ • Agent loop básico                                         │\n",
    "│ • Tool use simple                                           │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 02. Prompting Agéntico 🎯                                   │\n",
    "│ • Chain-of-Thought (CoT)                                    │\n",
    "│ • Tree-of-Thought (ToT)                                     │\n",
    "│ • ReAct pattern en detalle                                  │\n",
    "│ • Self-consistency                                          │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 03. Memory y RAG para Agentes 🧠                            │\n",
    "│ • Short-term vs long-term memory                            │\n",
    "│ • Vector stores y retrieval                                 │\n",
    "│ • MemGPT architecture                                       │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 04. Planning y Reasoning Avanzado 🎲                        │\n",
    "│ • Hierarchical planning                                     │\n",
    "│ • Task decomposition                                        │\n",
    "│ • Search algorithms (BFS, A*)                               │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 05. Multi-Agent Systems 👥                                  │\n",
    "│ • Agent communication protocols                             │\n",
    "│ • Coordination strategies                                   │\n",
    "│ • Conflict resolution                                       │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "                │\n",
    "                ▼\n",
    "┌─────────────────────────────────────────────────────────────┐\n",
    "│ 06. Proyecto Final: Production Agent 🚀                     │\n",
    "│ • Design + implementation                                   │\n",
    "│ • Deployment                                                │\n",
    "│ • Monitoring y optimization                                 │\n",
    "└─────────────────────────────────────────────────────────────┘\n",
    "```\n"
]))

cells.append(markdown_cell([
    "### 🎯 Próximo Notebook Recomendado\n",
    "\n",
    "**[➡️ 02. Prompting Agéntico](02-prompting-agentico.ipynb)**\n",
    "\n",
    "En el siguiente notebook aprenderás:\n",
    "- **Chain-of-Thought (CoT)**: Cómo hacer que agentes razonen paso a paso\n",
    "- **Tree-of-Thought (ToT)**: Exploración de múltiples caminos de razonamiento\n",
    "- **ReAct Pattern**: Implementación completa del patrón Reasoning + Acting\n",
    "- **Self-Consistency**: Mejorar precisión con múltiples muestreos\n",
    "- **Few-shot Prompting**: Aprendizaje desde ejemplos\n",
    "\n",
    "Estas técnicas son CRÍTICAS para construir agentes efectivos en producción.\n"
]))

cells.append(markdown_cell([
    "### 📊 Tu Progreso\n",
    "\n",
    "Marca lo que has completado:\n",
    "\n",
    "**Conceptos Fundamentales**:\n",
    "- [ ] Entiendo la diferencia entre LLM y Agente\n",
    "- [ ] Puedo explicar el agent loop\n",
    "- [ ] Conozco los componentes principales (cerebro, memoria, tools, loop)\n",
    "\n",
    "**Implementación**:\n",
    "- [ ] He implementado un agente básico desde cero\n",
    "- [ ] Completé los 5 ejercicios GRADED (≥70 pts)\n",
    "- [ ] Probé LangChain u otro framework\n",
    "\n",
    "**Conocimiento Teórico**:\n",
    "- [ ] Leí al menos 3 papers de la lista\n",
    "- [ ] Entiendo ReAct pattern\n",
    "- [ ] Conozco tradeoffs de frameworks vs desde cero\n",
    "\n",
    "**Best Practices**:\n",
    "- [ ] Sé cómo manejar errores en agentes\n",
    "- [ ] Conozco consideraciones de seguridad\n",
    "- [ ] Entiendo cost optimization strategies\n",
    "\n",
    "**Si marcaste ≥10 items**: ¡Excelente! Estás listo para el siguiente notebook.  \n",
    "**Si marcaste <10 items**: Considera revisar secciones que te faltaron.\n"
]))

cells.append(markdown_cell([
    "### 🌟 Recursos Adicionales\n",
    "\n",
    "**Comunidades**:\n",
    "- **LangChain Discord**: https://discord.gg/langchain\n",
    "- **r/LangChain**: https://reddit.com/r/LangChain\n",
    "- **HuggingFace Discord**: Canal #agents\n",
    "\n",
    "**Newsletters**:\n",
    "- **The Batch** (Andrew Ng): Actualizaciones semanales en AI\n",
    "- **LangChain Blog**: Nuevas features y tutoriales\n",
    "\n",
    "**Cursos**:\n",
    "- **DeepLearning.AI**: \"LangChain for LLM Application Development\"\n",
    "- **DeepLearning.AI**: \"Functions, Tools and Agents with LangChain\"\n",
    "\n",
    "**GitHub Repos para estudiar**:\n",
    "- **AutoGPT**: Agente completamente autónomo\n",
    "- **BabyAGI**: Implementación simple y educativa\n",
    "- **LangChain examples**: Cientos de ejemplos prácticos\n"
]))

cells.append(markdown_cell([
    "### 💬 Feedback\n",
    "\n",
    "¿Cómo fue tu experiencia con este notebook?\n",
    "\n",
    "- ¿Qué secciones fueron más útiles?\n",
    "- ¿Qué temas necesitan más profundidad?\n",
    "- ¿Los ejercicios fueron del nivel adecuado?\n",
    "- ¿Qué agregarías?\n",
    "\n",
    "Tu feedback ayuda a mejorar estos materiales. Gracias por aprender con nosotros!\n"
]))

cells.append(markdown_cell([
    "---\n",
    "\n",
    "<div align=\"center\">\n",
    "\n",
    "## 🎓 ¡Has Completado la Introducción a LLM Agents!\n",
    "\n",
    "### Respuesta a la Pregunta Guía\n",
    "\n",
    "*¿Cómo transformamos un LLM pasivo en un agente activo?*\n",
    "\n",
    "**Respuesta**: Envolvemos el LLM en un **control loop** que:\n",
    "1. 🧠 Construye prompts con contexto sobre herramientas disponibles\n",
    "2. 📝 Parsea respuestas del LLM para identificar acciones\n",
    "3. 🔧 Ejecuta acciones en el entorno (usando herramientas)\n",
    "4. 👀 Retroalimenta observaciones al LLM\n",
    "5. 🔄 Itera hasta completar la tarea\n",
    "\n",
    "La \"agenticidad\" emerge de este loop, no del LLM en sí.\n",
    "\n",
    "### Continúa tu viaje\n",
    "\n",
    "**[➡️ Siguiente: 02. Prompting Agéntico](02-prompting-agentico.ipynb)**\n",
    "\n",
    "---\n",
    "\n",
    "*Built with ❤️ for AI learners everywhere*\n",
    "\n",
    "</div>\n"
]))

print("Sección 10: Navegación... OK")

# Guardar notebook completo
notebook['cells'] = cells

output_path = "/home/user/TUTORIALS-AI-AGENTS/rutas/03-llm-agents/01-intro-llm-agents.ipynb"
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print(f"\n{'='*60}")
print(f"✅ NOTEBOOK COMPLETO GENERADO")
print(f"{'='*60}")
print(f"📍 Ubicación: {output_path}")
print(f"📊 Total de celdas: {len(cells)}")
print(f"\nDesglose por tipo:")
markdown_count = sum(1 for c in cells if c['cell_type'] == 'markdown')
code_count = sum(1 for c in cells if c['cell_type'] == 'code')
print(f"  - Markdown: {markdown_count}")
print(f"  - Code: {code_count}")
print(f"\n🎉 Notebook listo para usar!")

# 🚀 Instrucciones Rápidas: Completar Notebooks 03-06

## ⚡ Quick Start (5 minutos)

### 1. Ver qué se completó
```bash
cd /home/user/TUTORIALS-AI-AGENTS/rutas/03-llm-agents
cat REPORTE_COMPLETACION_NOTEBOOKS.md
```

### 2. Ejecutar generador automático
```bash
python3 AUTO_COMPLETE_NOTEBOOKS.py
```

### 3. Ver notebooks actuales
```bash
jupyter notebook
# Abrir: 03-react-reasoning-acting.ipynb
```

---

## 📋 Lo Que Está Listo

### Notebook 03: ReAct
- ✅ Ejercicios 1-3: **COMPLETOS** (hints, solución, tests insertados)
- ⏳ Ejercicios 4-5: Contenido generado en `temp_nb03_exercises_4_5.py`

### Notebooks 04-06
- ⏳ 15 ejercicios: Templates generados por `AUTO_COMPLETE_NOTEBOOKS.py`

---

## 🔥 Completar en 30 Minutos (Modo Rápido)

### Paso 1: Notebook 03 - Ejercicios 4 y 5 (10 min)

```python
# En Python o Jupyter
exec(open('temp_nb03_exercises_4_5.py').read())

# Copiar-pegar en notebook:
# - EX4_DESCRIPTION → Celda markdown antes de ejercicio 4
# - EX4_HINTS → Celda markdown después de función
# - EX4_TESTS → Celda code después de hints
# - EX5_DESCRIPTION → Celda markdown antes de ejercicio 5
# - EX5_HINTS → Celda markdown después de función
# - EX5_TESTS → Celda code después de hints
```

### Paso 2: Notebooks 04-06 - Insertar Templates (20 min)

```bash
# Opción A: Script automático (crear)
cat > insert_templates.py << 'EOF'
import json
from AUTO_COMPLETE_NOTEBOOKS import *

def insert_to_notebook(nb_path, exercises_dict, nb_num):
    """Inserta templates en notebook"""
    with open(nb_path, 'r') as f:
        nb = json.load(f)

    # TODO: Identificar celdas y actualizar
    # Ver notebooks 01-02 como referencia

    with open(nb_path, 'w') as f:
        json.dump(nb, f, indent=1)

# Ejecutar para cada notebook
insert_to_notebook('04-tool-use-function-calling.ipynb', NB04_EXERCISES, 4)
insert_to_notebook('05-memory-systems.ipynb', NB05_EXERCISES, 5)
insert_to_notebook('06-multi-agentes.ipynb', NB06_EXERCISES, 6)
EOF

python3 insert_templates.py
```

---

## 🎯 Completar con Calidad (4-6 horas)

### Fase 1: Finalizar NB03 (1 hora)

1. **Abrir notebook 03**
2. **Insertar ejercicios 4-5** usando contenido de `temp_nb03_exercises_4_5.py`
3. **Ejecutar tests** para validar
4. **Guardar notebook**

### Fase 2: Implementar NB04 (1.5 horas)

Para cada ejercicio:
1. Copiar template de `AUTO_COMPLETE_NOTEBOOKS.py`
2. Implementar solución real:
   ```python
   # Ejemplo: define_tool_schema
   def define_tool_schema(name, description, parameters):
       return {
           "type": "function",
           "function": {
               "name": name,
               "description": description,
               "parameters": {
                   "type": "object",
                   "properties": parameters.get("properties", {}),
                   "required": parameters.get("required", [])
               }
           }
       }
   ```
3. Implementar tests reales
4. Insertar en notebook

### Fase 3: Implementar NB05 (1.5 horas)

Similar a Fase 2, personalizar para memory systems:
```python
# Ejemplo: implement_short_term_memory
from collections import deque

class ShortTermMemory:
    def __init__(self, capacity=10):
        self.memory = deque(maxlen=capacity)

    def add(self, item):
        self.memory.append(item)

    def get_recent(self, n=5):
        return list(self.memory)[-n:]
```

### Fase 4: Implementar NB06 (1.5 horas)

Personalizar para multi-agentes:
```python
# Ejemplo: implement_sequential_pipeline
def implement_sequential_pipeline(agents, task):
    result = task
    for agent in agents:
        result = agent.run(result)
    return result
```

### Fase 5: Validación Final (30 min)

1. Ejecutar todos los notebooks
2. Verificar que tests pasen
3. Revisar formato consistente
4. Commit cambios

---

## 🛠️ Herramientas Disponibles

### 1. NotebookEdit (para insertar programáticamente)
```python
from claude_tools import NotebookEdit

NotebookEdit(
    notebook_path="/path/to/notebook.ipynb",
    cell_id="cell-X",
    new_source="contenido"
)
```

### 2. Templates Pre-generados

**NB03 ejercicios 4-5:**
- Archivo: `temp_nb03_exercises_4_5.py`
- Variables: `EX4_*`, `EX5_*`

**NB04-06:**
- Archivo: `AUTO_COMPLETE_NOTEBOOKS.py`
- Diccionarios: `NB04_EXERCISES`, `NB05_EXERCISES`, `NB06_EXERCISES`
- Función: `generate_exercise_content()`

---

## 📚 Referencias

### Patrón a Seguir
Ver notebooks 01-02 (ya completados) para:
- Formato de hints
- Estructura de soluciones
- Estilo de tests

### Notebooks con Ejercicios Completos
- `01-intro-llm-agents.ipynb` - Referencia perfecta
- `02-prompting-agentico.ipynb` - Referencia perfecta
- `03-react-reasoning-acting.ipynb` - Ejercicios 1-3 completos

---

## ❓ Troubleshooting

### Error: Celda no encontrada
```python
# Listar IDs de celdas
import json
nb = json.load(open('notebook.ipynb'))
for i, cell in enumerate(nb['cells']):
    print(f"{i}: {cell.get('id', 'no-id')}")
```

### Error: Formato incorrecto
- Copiar formato exacto de notebooks 01-02
- Usar `<details><summary>` para hints
- Mantener indentación en código Python

### Tests no pasan
- Verificar que función esté implementada (no solo `pass`)
- Revisar que imports estén presentes
- Validar edge cases

---

## 🎓 Niveles de Completación

### Nivel 1: Estructura (✅ YA HECHO)
- [x] Todos los ejercicios tienen descripción
- [x] Todas las funciones definidas con docstrings
- [x] Templates de hints generados

### Nivel 2: Implementación (⏳ 60% HECHO)
- [x] NB03 ejercicios 1-3 implementados
- [ ] NB03 ejercicios 4-5 implementados
- [ ] NB04-06 implementados

### Nivel 3: Validación (⏳ PENDIENTE)
- [ ] Todos los tests pasan
- [ ] Notebooks ejecutan sin errores
- [ ] Código bien documentado

---

## 🚀 Comando Único para Ver Todo

```bash
cd /home/user/TUTORIALS-AI-AGENTS

echo "=== ARCHIVOS GENERADOS ==="
ls -lh *.md *.py 2>/dev/null

echo -e "\n=== NOTEBOOKS ==="
ls -lh rutas/03-llm-agents/*.ipynb

echo -e "\n=== ESTADO NOTEBOOKS ==="
cat REPORTE_COMPLETACION_NOTEBOOKS.md | grep -A 5 "Estado Final"

echo -e "\n=== PRÓXIMOS PASOS ==="
cat REPORTE_COMPLETACION_NOTEBOOKS.md | grep -A 10 "Próximos Pasos"
```

---

## ✅ Checklist Final

Antes de considerar completo:

- [ ] NB03: 5/5 ejercicios con hints, solución, tests
- [ ] NB04: 5/5 ejercicios con hints, solución, tests
- [ ] NB05: 5/5 ejercicios con hints, solución, tests
- [ ] NB06: 5/5 ejercicios con hints, solución, tests
- [ ] Todos los tests ejecutan sin errores
- [ ] Formato consistente con NB01-02
- [ ] Documentación completa en cada ejercicio

---

*Usa este archivo como guía rápida. Para detalles completos, ver REPORTE_COMPLETACION_NOTEBOOKS.md*

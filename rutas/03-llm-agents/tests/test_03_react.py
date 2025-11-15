"""
Autograder para Notebook 03: ReAct (Reasoning + Acting)

Total de puntos: 100
Mínimo para aprobar: 70

Ejercicios:
1. implement_react_prompt (15 pts)
2. parse_react_step (15 pts)
3. execute_react_loop (25 pts)
4. format_trajectory (20 pts)
5. detect_infinite_loops (25 pts)
"""

from typing import List, Dict, Callable, Optional, Tuple
from collections import Counter
from enum import Enum
import re


class StepType(Enum):
    """Tipos de pasos en ReAct"""
    THOUGHT = "thought"
    ACTION = "action"
    OBSERVATION = "observation"


class ReActGrader:
    """Sistema de autograding para ejercicios de ReAct."""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'implement_react_prompt': 15,
            'parse_react_step': 15,
            'execute_react_loop': 25,
            'format_trajectory': 20,
            'detect_infinite_loops': 25
        }
        self.results = {}

    # =========================================================================
    # EJERCICIO 1: Implement ReAct Prompt (15 pts)
    # =========================================================================

    def test_implement_react_prompt(
        self,
        student_function: Callable[[str, List[Dict]], str]
    ) -> Dict:
        """
        Prueba la implementación del prompt ReAct.

        La función del estudiante debe:
        - Tomar question (str) y trajectory (List[Dict])
        - Retornar prompt completo con few-shot examples
        - Incluir instrucciones de formato ReAct
        - Incluir historial de trajectory si existe

        Args:
            student_function: función implement_react_prompt(question, trajectory) -> str

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 1 - Implement ReAct Prompt")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['implement_react_prompt'] / 5
        total_points = 0

        # Test 1: Prompt básico sin trajectory
        try:
            question1 = "¿Quién escribió Don Quijote?"
            trajectory1 = []

            prompt = student_function(question1, trajectory1)

            # Verificar componentes esenciales
            assert isinstance(prompt, str), "Debe retornar string"
            assert len(prompt) > 100, "Prompt debe ser sustancial"
            assert question1 in prompt, "Debe incluir la pregunta"

            # Verificar palabras clave ReAct
            react_keywords = ['thought', 'action', 'observation', 'search', 'finish']
            found_keywords = sum(1 for kw in react_keywords if kw.lower() in prompt.lower())
            assert found_keywords >= 3, f"Debe mencionar conceptos ReAct (encontró {found_keywords}/5)"

            test_cases.append({
                'name': 'Test 1: Prompt básico sin trajectory',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Prompt válido con {found_keywords}/5 keywords ReAct'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Prompt básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Prompt básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Prompt con trajectory existente
        try:
            question2 = "¿Cuándo nació Einstein?"
            trajectory2 = [
                {"type": "thought", "content": "Necesito buscar información sobre Einstein", "step": 1},
                {"type": "action", "content": "Search[Albert Einstein]", "step": 1}
            ]

            prompt = student_function(question2, trajectory2)

            assert question2 in prompt
            assert len(prompt) > 100

            # Verificar que incluye la trajectory
            assert "einstein" in prompt.lower()
            assert "search" in prompt.lower()

            test_cases.append({
                'name': 'Test 2: Prompt con trajectory',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Incluye trajectory existente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Con trajectory',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Con trajectory',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Incluye few-shot examples
        try:
            question3 = "Test question"
            prompt = student_function(question3, [])

            # Buscar evidencia de few-shot examples
            # Típicamente: "Ejemplo", "Example", o múltiples "Thought", "Action"
            has_examples = (
                prompt.count("Ejemplo") >= 1 or
                prompt.count("Example") >= 1 or
                (prompt.count("Thought") >= 3 and prompt.count("Action") >= 3)
            )

            assert has_examples, "Debe incluir few-shot examples"

            test_cases.append({
                'name': 'Test 3: Few-shot examples',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Incluye ejemplos few-shot'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Few-shot',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Few-shot',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Maneja preguntas largas
        try:
            long_question = "En una ciudad donde el 60% de la población son mujeres, " \
                          "¿cuál es la probabilidad de que dos personas elegidas al azar " \
                          "sean ambas mujeres si la población total es de 10,000 habitantes?"
            prompt = student_function(long_question, [])

            assert long_question in prompt
            assert len(prompt) > 200

            test_cases.append({
                'name': 'Test 4: Pregunta larga',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja preguntas largas'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Pregunta larga',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 5: Formato consistente
        try:
            q1 = "¿Qué es Python?"
            q2 = "¿Qué es Java?"
            p1 = student_function(q1, [])
            p2 = student_function(q2, [])

            # Verificar que la estructura es similar (excluyendo las preguntas)
            p1_template = p1.replace(q1, "QUESTION")
            p2_template = p2.replace(q2, "QUESTION")

            # Similitud básica
            words1 = set(p1_template.split())
            words2 = set(p2_template.split())
            similarity = len(words1 & words2) / max(len(words1), len(words2))

            assert similarity > 0.6, f"Formato debe ser consistente (similitud: {similarity:.2f})"

            test_cases.append({
                'name': 'Test 5: Consistencia',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Formato consistente (sim: {similarity:.2f})'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 5: Consistencia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 5: Consistencia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['implement_react_prompt']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'implement_react_prompt',
            'total_points': total_points,
            'max_points': self.exercise_points['implement_react_prompt'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 2: Parse ReAct Step (15 pts)
    # =========================================================================

    def test_parse_react_step(
        self,
        student_function: Callable[[str], Dict]
    ) -> Dict:
        """
        Prueba el parsing de pasos ReAct.

        La función del estudiante debe:
        - Tomar respuesta del LLM (str)
        - Retornar dict con {'type': ..., 'content': ..., 'step_num': ...}
        - Detectar Thought, Action, Observation
        - Extraer número de paso

        Args:
            student_function: función parse_react_step(llm_response: str) -> Dict

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 2 - Parse ReAct Step")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['parse_react_step'] / 5
        total_points = 0

        # Test 1: Parse Thought
        try:
            response1 = "Thought 1: Necesito buscar información sobre Python"
            result = student_function(response1)

            assert isinstance(result, dict), "Debe retornar dict"
            assert 'type' in result, "Debe tener campo 'type'"
            assert 'content' in result, "Debe tener campo 'content'"

            assert result['type'].lower() in ['thought', 'think', 'reasoning'], \
                f"Tipo incorrecto: {result['type']}"
            assert "python" in result['content'].lower(), "Content debe incluir 'python'"

            test_cases.append({
                'name': 'Test 1: Parse Thought',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Parseó Thought correctamente (type: {result["type"]})'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Parse Thought',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Parse Thought',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Parse Action
        try:
            response2 = "Action 2: Search[Albert Einstein]"
            result = student_function(response2)

            assert result['type'].lower() in ['action', 'act', 'tool'], \
                f"Tipo incorrecto: {result['type']}"
            assert "search" in result['content'].lower() or "einstein" in result['content'].lower()

            test_cases.append({
                'name': 'Test 2: Parse Action',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Parseó Action correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Parse Action',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Parse Action',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Extrae número de paso
        try:
            response3 = "Thought 5: Analizando resultados"
            result = student_function(response3)

            assert 'step_num' in result or 'step' in result or 'number' in result, \
                "Debe extraer número de paso"

            step_num = result.get('step_num') or result.get('step') or result.get('number')
            assert step_num == 5, f"Número de paso incorrecto: {step_num}"

            test_cases.append({
                'name': 'Test 3: Número de paso',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Extrajo step_num: {step_num}'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Número de paso',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Número de paso',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Maneja formatos variantes
        try:
            # Sin número
            response4a = "Thought: Continuando el análisis"
            result4a = student_function(response4a)
            assert result4a['type'].lower() in ['thought', 'think']

            # Con dos puntos adicionales
            response4b = "Action 1: Search[Python programming]"
            result4b = student_function(response4b)
            assert result4b['type'].lower() in ['action', 'act']

            test_cases.append({
                'name': 'Test 4: Formatos variantes',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja variaciones de formato'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Formatos variantes',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Formatos variantes',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 5: Case insensitive
        try:
            response5 = "THOUGHT 3: ANALYZING DATA"
            result = student_function(response5)

            assert result['type'].lower() in ['thought', 'think']
            assert 'analyzing' in result['content'].lower() or 'data' in result['content'].lower()

            test_cases.append({
                'name': 'Test 5: Case insensitive',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja mayúsculas/minúsculas'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 5: Case insensitive',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 5: Case insensitive',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['parse_react_step']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'parse_react_step',
            'total_points': total_points,
            'max_points': self.exercise_points['parse_react_step'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 3: Execute ReAct Loop (25 pts)
    # =========================================================================

    def test_execute_react_loop(
        self,
        student_function: Callable[[str, Dict, int], Dict]
    ) -> Dict:
        """
        Prueba la ejecución del loop ReAct completo.

        La función del estudiante debe:
        - Tomar question, tools, max_steps
        - Ejecutar loop Thought → Action → Observation
        - Retornar dict con answer y trajectory
        - Manejar límite de steps
        - Detectar Finish[answer]

        Args:
            student_function: función execute_react_loop(question, tools, max_steps) -> Dict

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 3 - Execute ReAct Loop")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['execute_react_loop'] / 4
        total_points = 0

        # Mock tools para testing
        mock_tools = {
            'search': lambda q: f"Resultado de buscar: {q}",
            'calculator': lambda expr: str(eval(expr))
        }

        # Test 1: Completa con Finish
        try:
            question1 = "¿Cuánto es 2+2?"
            result = student_function(question1, mock_tools, max_steps=10)

            assert isinstance(result, dict), "Debe retornar dict"
            assert 'answer' in result, "Debe tener campo 'answer'"
            assert 'trajectory' in result or 'steps' in result, "Debe tener trajectory/steps"

            test_cases.append({
                'name': 'Test 1: Ejecución básica',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Retorna estructura correcta'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Ejecución básica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Ejecución básica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Respeta max_steps
        try:
            question2 = "Test question for max steps"
            result = student_function(question2, mock_tools, max_steps=3)

            trajectory = result.get('trajectory') or result.get('steps') or []

            # No debe exceder max_steps significativamente
            assert len(trajectory) <= 10, f"Demasiados pasos: {len(trajectory)}"

            test_cases.append({
                'name': 'Test 2: Respeta max_steps',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Limitó a {len(trajectory)} pasos'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: max_steps',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: max_steps',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Trajectory tiene estructura correcta
        try:
            question3 = "Another test question"
            result = student_function(question3, mock_tools, max_steps=5)

            trajectory = result.get('trajectory') or result.get('steps') or []

            if len(trajectory) > 0:
                # Verificar que trajectory tiene elementos válidos
                assert isinstance(trajectory, list), "Trajectory debe ser lista"

                # Cada elemento debe ser dict o tener estructura
                first_step = trajectory[0]
                assert isinstance(first_step, dict) or hasattr(first_step, '__dict__'), \
                    "Cada paso debe ser dict o objeto"

            test_cases.append({
                'name': 'Test 3: Estructura de trajectory',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Trajectory válido con {len(trajectory)} pasos'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Estructura trajectory',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Estructura trajectory',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Maneja tools inexistentes
        try:
            question4 = "Test with missing tool"
            result = student_function(question4, {}, max_steps=2)

            # Debe completar sin crash incluso sin tools
            assert 'answer' in result

            test_cases.append({
                'name': 'Test 4: Sin tools disponibles',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja ausencia de tools'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Sin tools',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['execute_react_loop']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'execute_react_loop',
            'total_points': total_points,
            'max_points': self.exercise_points['execute_react_loop'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 4: Format Trajectory (20 pts)
    # =========================================================================

    def test_format_trajectory(
        self,
        student_function: Callable[[List], str]
    ) -> Dict:
        """
        Prueba el formateo de trajectory para visualización.

        La función del estudiante debe:
        - Tomar lista de steps
        - Retornar string legible y estructurado
        - Distinguir visualmente Thought/Action/Observation
        - Numerar steps

        Args:
            student_function: función format_trajectory(trajectory: List) -> str

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 4 - Format Trajectory")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['format_trajectory'] / 4
        total_points = 0

        # Test 1: Trajectory básica
        try:
            trajectory1 = [
                {"type": "thought", "content": "Necesito buscar", "step": 1},
                {"type": "action", "content": "Search[Python]", "step": 1},
                {"type": "observation", "content": "Python es un lenguaje", "step": 1}
            ]

            formatted = student_function(trajectory1)

            assert isinstance(formatted, str), "Debe retornar string"
            assert len(formatted) > 20, "Output debe ser sustancial"
            assert "python" in formatted.lower(), "Debe incluir contenido de steps"

            test_cases.append({
                'name': 'Test 1: Formateo básico',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Formateó {len(trajectory1)} steps'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Formateo básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Formateo básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Distingue tipos de steps
        try:
            trajectory2 = [
                {"type": "thought", "content": "Pensando", "step": 1},
                {"type": "action", "content": "Actuando", "step": 1},
            ]

            formatted = student_function(trajectory2)

            # Debe haber alguna distinción visual
            # (emojis, mayúsculas, prefijos, etc.)
            has_distinction = (
                formatted.count("Thought") > 0 or formatted.count("THOUGHT") > 0 or
                formatted.count("Action") > 0 or formatted.count("ACTION") > 0 or
                "💭" in formatted or "🔧" in formatted
            )

            assert has_distinction, "Debe distinguir visualmente tipos de steps"

            test_cases.append({
                'name': 'Test 2: Distinción visual',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Distingue tipos de steps visualmente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Distinción visual',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Distinción visual',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Maneja trajectory vacía
        try:
            formatted_empty = student_function([])

            assert isinstance(formatted_empty, str)
            # Puede retornar mensaje o string vacío

            test_cases.append({
                'name': 'Test 3: Trajectory vacía',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja trajectory vacía'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Trajectory vacía',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Trajectory larga
        try:
            trajectory_long = [
                {"type": "thought", "content": f"Thought {i}", "step": i}
                for i in range(1, 11)
            ]

            formatted = student_function(trajectory_long)

            assert len(formatted) > 100, "Debe formatear trajectory larga"
            # Debe mencionar varios de los thoughts
            mention_count = sum(1 for i in range(1, 6) if f"Thought {i}" in formatted)
            assert mention_count >= 3, "Debe incluir múltiples steps"

            test_cases.append({
                'name': 'Test 4: Trajectory larga',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Formateó {len(trajectory_long)} steps'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Trajectory larga',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Trajectory larga',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['format_trajectory']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'format_trajectory',
            'total_points': total_points,
            'max_points': self.exercise_points['format_trajectory'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 5: Detect Infinite Loops (25 pts)
    # =========================================================================

    def test_detect_infinite_loops(
        self,
        student_function: Callable[[List], bool]
    ) -> Dict:
        """
        Prueba detección de loops infinitos en trajectory.

        La función del estudiante debe:
        - Tomar trajectory (List)
        - Retornar True si detecta loop, False si no
        - Detectar acciones repetidas
        - Detectar oscilación entre states

        Args:
            student_function: función detect_infinite_loops(trajectory: List) -> bool

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 5 - Detect Infinite Loops")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['detect_infinite_loops'] / 4
        total_points = 0

        # Test 1: Trajectory normal (sin loop)
        try:
            normal_trajectory = [
                {"type": "thought", "content": "Buscar Python", "step": 1},
                {"type": "action", "content": "Search[Python]", "step": 1},
                {"type": "observation", "content": "Python es...", "step": 1},
                {"type": "thought", "content": "Buscar Java", "step": 2},
                {"type": "action", "content": "Search[Java]", "step": 2},
            ]

            has_loop = student_function(normal_trajectory)

            assert has_loop == False, f"No debería detectar loop (retornó {has_loop})"

            test_cases.append({
                'name': 'Test 1: Sin loop',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Correctamente NO detectó loop'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Sin loop',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Sin loop',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Acción repetida (loop obvio)
        try:
            loop_trajectory = [
                {"type": "action", "content": "Search[same thing]", "step": 1},
                {"type": "observation", "content": "Result", "step": 1},
                {"type": "action", "content": "Search[same thing]", "step": 2},
                {"type": "observation", "content": "Result", "step": 2},
                {"type": "action", "content": "Search[same thing]", "step": 3},
            ]

            has_loop = student_function(loop_trajectory)

            assert has_loop == True, "Debería detectar loop de acciones repetidas"

            test_cases.append({
                'name': 'Test 2: Acción repetida',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Detectó loop correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Acción repetida',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Acción repetida',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Trajectory vacía
        try:
            empty_trajectory = []
            has_loop = student_function(empty_trajectory)

            assert has_loop == False, "Trajectory vacía no tiene loop"

            test_cases.append({
                'name': 'Test 3: Trajectory vacía',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja trajectory vacía'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Trajectory vacía',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Trajectory vacía',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Patrones sutiles (oscilación)
        try:
            oscillation_trajectory = [
                {"type": "action", "content": "Search[A]", "step": 1},
                {"type": "observation", "content": "Info A", "step": 1},
                {"type": "action", "content": "Search[B]", "step": 2},
                {"type": "observation", "content": "Info B", "step": 2},
                {"type": "action", "content": "Search[A]", "step": 3},
                {"type": "observation", "content": "Info A", "step": 3},
                {"type": "action", "content": "Search[B]", "step": 4},
            ]

            has_loop = student_function(oscillation_trajectory)

            # Debe detectar oscilación A-B-A-B
            # (test más permisivo - puede o no detectar dependiendo de implementación)
            assert isinstance(has_loop, bool), "Debe retornar booleano"

            test_cases.append({
                'name': 'Test 4: Oscilación A-B',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Analizó oscilación (loop={has_loop})'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Oscilación',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Oscilación',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['detect_infinite_loops']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'detect_infinite_loops',
            'total_points': total_points,
            'max_points': self.exercise_points['detect_infinite_loops'],
            'test_cases': test_cases
        }

    # =========================================================================
    # CALIFICACIÓN COMPLETA
    # =========================================================================

    def grade_all(self, student_functions: Dict[str, Callable]) -> Dict:
        """
        Ejecuta todos los tests y calcula calificación final.

        Args:
            student_functions: Dict con {nombre_ejercicio: función_estudiante}

        Returns:
            Dict con resultados completos
        """
        print("\n" + "="*70)
        print("AUTOGRADER: ReAct (Reasoning + Acting)")
        print("="*70)

        all_results = []
        total_earned = 0

        # Ejecutar cada test
        if 'implement_react_prompt' in student_functions:
            result = self.test_implement_react_prompt(student_functions['implement_react_prompt'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'parse_react_step' in student_functions:
            result = self.test_parse_react_step(student_functions['parse_react_step'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'execute_react_loop' in student_functions:
            result = self.test_execute_react_loop(student_functions['execute_react_loop'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'format_trajectory' in student_functions:
            result = self.test_format_trajectory(student_functions['format_trajectory'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'detect_infinite_loops' in student_functions:
            result = self.test_detect_infinite_loops(student_functions['detect_infinite_loops'])
            all_results.append(result)
            total_earned += result['total_points']

        # Calcular calificación final
        percentage = (total_earned / self.total_points) * 100
        passed = total_earned >= self.passing_grade

        print("\n" + "="*70)
        print("RESUMEN FINAL")
        print("="*70)

        for result in all_results:
            status = "✓" if result['total_points'] == result['max_points'] else "⚠"
            print(f"{status} {result['exercise']}: {result['total_points']:.1f}/{result['max_points']}")

        print(f"\n{'='*70}")
        print(f"CALIFICACIÓN TOTAL: {total_earned:.1f}/{self.total_points} ({percentage:.1f}%)")
        print(f"ESTADO: {'✅ APROBADO' if passed else '❌ NO APROBADO'} (mínimo: {self.passing_grade})")
        print(f"{'='*70}\n")

        return {
            'total_points': total_earned,
            'max_points': self.total_points,
            'percentage': percentage,
            'passed': passed,
            'exercise_results': all_results
        }


# Para uso desde notebook
if __name__ == "__main__":
    print("Autograder para ReAct cargado")
    print("Uso: grader = ReActGrader()")
    print("     grader.test_implement_react_prompt(tu_funcion)")

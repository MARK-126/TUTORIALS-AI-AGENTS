"""
Autograder para Notebook 02: Prompting Agéntico

Total de puntos: 100
Mínimo para aprobar: 70

Ejercicios:
1. implement_zero_shot_cot (15 pts)
2. parse_cot_steps (15 pts)
3. implement_majority_vote (20 pts)
4. evaluate_reasoning_path (25 pts)
5. select_best_examples (25 pts)
"""

from typing import List, Dict, Callable, Optional, Tuple
from collections import Counter
import re


class PromptingAgenticoGrader:
    """Sistema de autograding para ejercicios de Prompting Agéntico."""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'implement_zero_shot_cot': 15,
            'parse_cot_steps': 15,
            'implement_majority_vote': 20,
            'evaluate_reasoning_path': 25,
            'select_best_examples': 25
        }
        self.results = {}

    # =========================================================================
    # EJERCICIO 1: Implement Zero-Shot CoT (15 pts)
    # =========================================================================

    def test_zero_shot_cot(self, student_function: Callable[[str], str]) -> Dict:
        """
        Prueba la implementación de Zero-Shot Chain-of-Thought.

        La función del estudiante debe:
        - Tomar una pregunta (str)
        - Retornar la pregunta con el prompt CoT agregado
        - Debe incluir frases como "step by step", "razona", "piensa", etc.

        Args:
            student_function: función implement_zero_shot_cot(question: str) -> str

        Returns:
            Dict con puntos ganados y feedback
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 1 - Zero-Shot CoT")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['implement_zero_shot_cot'] / 5
        total_points = 0

        # Test 1: Pregunta matemática básica
        try:
            question1 = "¿Cuánto es 15 + 27?"
            result1 = student_function(question1)

            # Verificar que la pregunta está incluida
            assert question1 in result1, "La pregunta original debe estar incluida"

            # Verificar que tiene prompt CoT
            cot_keywords = ['paso a paso', 'step by step', 'piensa', 'think',
                          'razona', 'reason']
            has_cot = any(keyword in result1.lower() for keyword in cot_keywords)
            assert has_cot, "Debe incluir palabras clave de CoT"

            # Verificar que es más largo que la pregunta original
            assert len(result1) > len(question1), "El prompt debe ser más largo que la pregunta sola"

            test_cases.append({
                'name': 'Test 1: Pregunta matemática básica',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Correctamente formateado con prompt CoT'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Pregunta matemática básica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Pregunta matemática básica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error inesperado: {str(e)}'
            })

        # Test 2: Pregunta lógica
        try:
            question2 = "Si todos los gatos son animales y algunos animales vuelan, ¿pueden volar los gatos?"
            result2 = student_function(question2)

            assert question2 in result2
            cot_keywords = ['paso', 'step', 'analiza', 'analyze', 'razona']
            has_cot = any(keyword in result2.lower() for keyword in cot_keywords)
            assert has_cot, "Debe tener prompt CoT"

            test_cases.append({
                'name': 'Test 2: Pregunta lógica',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja preguntas lógicas correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Pregunta lógica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Pregunta lógica',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: String vacío
        try:
            result3 = student_function("")
            assert len(result3) > 0, "Debe manejar strings vacíos"

            test_cases.append({
                'name': 'Test 3: String vacío',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja casos edge correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: String vacío',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: String vacío',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Pregunta larga
        try:
            question4 = "En una tienda, el precio de un libro es $15, una pluma $2, y un cuaderno $5. " \
                       "Si compro 3 libros, 5 plumas y 2 cuadernos, ¿cuánto pago en total?"
            result4 = student_function(question4)

            assert question4 in result4
            assert len(result4) > len(question4)

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
            q1 = "¿Qué es 2+2?"
            q2 = "¿Qué es 3+3?"
            r1 = student_function(q1)
            r2 = student_function(q2)

            # El formato debe ser consistente (misma estructura excepto la pregunta)
            # Reemplazamos las preguntas para verificar
            r1_template = r1.replace(q1, "QUESTION")
            r2_template = r2.replace(q2, "QUESTION")

            # Deben ser similares (no exactamente iguales está ok, pero la estructura sí)
            similarity = len(set(r1_template.split()) & set(r2_template.split())) / \
                        max(len(r1_template.split()), len(r2_template.split()))

            assert similarity > 0.5, "El formato debe ser consistente entre llamadas"

            test_cases.append({
                'name': 'Test 5: Consistencia de formato',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Formato consistente (similitud: {similarity:.2f})'
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
        print(f"Total: {total_points:.1f}/{self.exercise_points['implement_zero_shot_cot']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'implement_zero_shot_cot',
            'total_points': total_points,
            'max_points': self.exercise_points['implement_zero_shot_cot'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 2: Parse CoT Steps (15 pts)
    # =========================================================================

    def test_parse_cot_steps(self, student_function: Callable[[str], List[str]]) -> Dict:
        """
        Prueba el parsing de pasos de razonamiento CoT.

        La función del estudiante debe:
        - Tomar una respuesta CoT (str) con pasos numerados o marcados
        - Retornar lista de pasos (List[str])
        - Manejar diferentes formatos (1., -, Paso 1:, etc.)

        Args:
            student_function: función parse_cot_steps(cot_response: str) -> List[str]

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 2 - Parse CoT Steps")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['parse_cot_steps'] / 5
        total_points = 0

        # Test 1: Formato numerado estándar
        try:
            response1 = """Pensemos paso a paso:
1. Roger empieza con 5 pelotas
2. Compra 2 latas de pelotas
3. Cada lata tiene 3 pelotas
4. Total de pelotas nuevas: 2 × 3 = 6
5. Total final: 5 + 6 = 11 pelotas"""

            steps = student_function(response1)

            assert isinstance(steps, list), "Debe retornar una lista"
            assert len(steps) == 5, f"Debe encontrar 5 pasos, encontró {len(steps)}"
            assert "Roger empieza con 5 pelotas" in steps[0], "Primer paso incorrecto"
            assert "11 pelotas" in steps[4], "Último paso incorrecto"

            test_cases.append({
                'name': 'Test 1: Formato numerado (1. 2. 3.)',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Parseó {len(steps)} pasos correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Formato numerado',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Formato numerado',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Formato con guiones
        try:
            response2 = """Analicemos:
- Primer paso: identificar variables
- Segundo paso: establecer ecuaciones
- Tercer paso: resolver
- Cuarto paso: verificar resultado"""

            steps = student_function(response2)

            assert isinstance(steps, list)
            assert len(steps) == 4, f"Debe encontrar 4 pasos, encontró {len(steps)}"

            test_cases.append({
                'name': 'Test 2: Formato con guiones (-)',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja formato con guiones'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Formato con guiones',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Formato con guiones',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Formato "Paso N:"
        try:
            response3 = """Paso 1: Analizar el problema
Paso 2: Identificar datos conocidos
Paso 3: Aplicar fórmula
Paso 4: Calcular resultado"""

            steps = student_function(response3)

            assert isinstance(steps, list)
            assert len(steps) >= 4, f"Debe encontrar al menos 4 pasos"

            test_cases.append({
                'name': 'Test 3: Formato "Paso N:"',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja formato "Paso N:"'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Formato Paso N',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Formato Paso N',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Sin formato claro (debe retornar vacío o [])
        try:
            response4 = "Esta es una respuesta sin pasos claros, solo texto continuo."
            steps = student_function(response4)

            assert isinstance(steps, list), "Debe retornar lista (puede estar vacía)"
            # Acepto que retorne vacío o que intente parsear algo

            test_cases.append({
                'name': 'Test 4: Sin formato de pasos',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Maneja texto sin pasos (retornó {len(steps)} items)'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Sin formato',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 5: Formato mixto
        try:
            response5 = """Razonamiento:
1. Primer análisis
- Sub-punto A
- Sub-punto B
2. Segundo análisis
Paso 3: Conclusión"""

            steps = student_function(response5)

            assert isinstance(steps, list)
            assert len(steps) >= 3, "Debe encontrar al menos los pasos principales"

            test_cases.append({
                'name': 'Test 5: Formato mixto',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Maneja formatos mixtos ({len(steps)} pasos)'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 5: Formato mixto',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 5: Formato mixto',
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
        print(f"Total: {total_points:.1f}/{self.exercise_points['parse_cot_steps']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'parse_cot_steps',
            'total_points': total_points,
            'max_points': self.exercise_points['parse_cot_steps'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 3: Implement Majority Vote (20 pts)
    # =========================================================================

    def test_majority_vote(self, student_function: Callable[[List[str]], str]) -> Dict:
        """
        Prueba la implementación de votación por mayoría.

        La función del estudiante debe:
        - Tomar lista de respuestas (List[str])
        - Retornar la respuesta más común (str)
        - Manejar empates (cualquier estrategia razonable)

        Args:
            student_function: función implement_majority_vote(responses: List[str]) -> str

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 3 - Majority Vote")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['implement_majority_vote'] / 4
        total_points = 0

        # Test 1: Mayoría clara
        try:
            responses1 = ["11", "11", "11", "10", "12"]
            result = student_function(responses1)

            assert result == "11", f"Mayoría clara es '11', obtuvo '{result}'"

            test_cases.append({
                'name': 'Test 1: Mayoría clara',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Identificó correctamente la mayoría'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Mayoría clara',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Mayoría clara',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Empate (debe retornar uno de los empatados)
        try:
            responses2 = ["A", "A", "B", "B"]
            result = student_function(responses2)

            assert result in ["A", "B"], f"Debe retornar 'A' o 'B' en empate, obtuvo '{result}'"

            test_cases.append({
                'name': 'Test 2: Empate',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Maneja empates (retornó "{result}")'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Empate',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Empate',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Lista con un solo elemento
        try:
            responses3 = ["única"]
            result = student_function(responses3)

            assert result == "única", "Con un solo elemento debe retornar ese elemento"

            test_cases.append({
                'name': 'Test 3: Un solo elemento',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja lista con un elemento'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Un solo elemento',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Un solo elemento',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Todos diferentes
        try:
            responses4 = ["1", "2", "3", "4", "5"]
            result = student_function(responses4)

            # Debe retornar alguno de los valores
            assert result in responses4, "Debe retornar uno de los valores de entrada"

            test_cases.append({
                'name': 'Test 4: Todos diferentes',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Maneja caso todos diferentes (retornó "{result}")'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Todos diferentes',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Todos diferentes',
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
        print(f"Total: {total_points:.1f}/{self.exercise_points['implement_majority_vote']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'implement_majority_vote',
            'total_points': total_points,
            'max_points': self.exercise_points['implement_majority_vote'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 4: Evaluate Reasoning Path (25 pts)
    # =========================================================================

    def test_evaluate_reasoning_path(
        self,
        student_function: Callable[[str, str], float]
    ) -> Dict:
        """
        Prueba la función de evaluación de caminos de razonamiento.

        La función del estudiante debe:
        - Tomar problema (str) y pensamiento/camino (str)
        - Retornar score 0.0-1.0 (float)
        - Dar scores más altos a pensamientos prometedores

        Args:
            student_function: función evaluate_reasoning_path(problem: str, thought: str) -> float

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 4 - Evaluate Reasoning Path")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['evaluate_reasoning_path'] / 4
        total_points = 0

        # Test 1: Score en rango correcto
        try:
            problem1 = "¿Cuál es la raíz cuadrada de 144?"
            thought1 = "Buscar un número que multiplicado por sí mismo dé 144"

            score = student_function(problem1, thought1)

            assert isinstance(score, (float, int)), "Score debe ser numérico"
            assert 0.0 <= score <= 1.0, f"Score debe estar en [0,1], obtuvo {score}"

            test_cases.append({
                'name': 'Test 1: Score en rango válido',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Score en rango correcto: {score:.2f}'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Rango válido',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Rango válido',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Diferencia entre buen y mal pensamiento
        try:
            problem2 = "Resolver 2x + 5 = 13"
            good_thought = "Aislar x restando 5 de ambos lados, luego dividir por 2"
            bad_thought = "Adivinar valores aleatorios hasta encontrar el correcto"

            score_good = student_function(problem2, good_thought)
            score_bad = student_function(problem2, bad_thought)

            assert 0.0 <= score_good <= 1.0
            assert 0.0 <= score_bad <= 1.0

            # El pensamiento bueno debe tener score mayor o igual
            # (con cierta tolerancia para diferentes implementaciones)
            assert score_good >= score_bad - 0.1, \
                f"Pensamiento sistemático debería tener score ≥ que adivinanzas (good:{score_good:.2f}, bad:{score_bad:.2f})"

            test_cases.append({
                'name': 'Test 2: Discrimina calidad',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Bueno: {score_good:.2f}, Malo: {score_bad:.2f}'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Discrimina calidad',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Discrimina calidad',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Consistencia
        try:
            problem3 = "Calcular el área de un círculo de radio 5"
            thought3 = "Usar la fórmula A = πr²"

            score1 = student_function(problem3, thought3)
            score2 = student_function(problem3, thought3)

            assert abs(score1 - score2) < 0.01, "Debe ser determinístico (mismo input → mismo output)"

            test_cases.append({
                'name': 'Test 3: Consistencia',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Evaluación consistente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Consistencia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Consistencia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Maneja inputs vacíos o extraños
        try:
            score_empty = student_function("", "")
            score_weird = student_function("???", "!!!")

            assert 0.0 <= score_empty <= 1.0
            assert 0.0 <= score_weird <= 1.0

            test_cases.append({
                'name': 'Test 4: Casos edge',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja inputs extraños sin fallar'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Casos edge',
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
        print(f"Total: {total_points:.1f}/{self.exercise_points['evaluate_reasoning_path']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'evaluate_reasoning_path',
            'total_points': total_points,
            'max_points': self.exercise_points['evaluate_reasoning_path'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 5: Select Best Examples (25 pts)
    # =========================================================================

    def test_select_best_examples(
        self,
        student_function: Callable[[str, List[Dict], int], List[Dict]]
    ) -> Dict:
        """
        Prueba la selección de mejores ejemplos para few-shot prompting.

        La función del estudiante debe:
        - Tomar query (str), ejemplos disponibles (List[Dict]), k (int)
        - Retornar los k ejemplos más relevantes (List[Dict])
        - Usar alguna métrica de similitud/relevancia

        Args:
            student_function: función select_best_examples(query, examples, k) -> List[Dict]

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 5 - Select Best Examples")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['select_best_examples'] / 4
        total_points = 0

        # Ejemplos de prueba
        example_pool = [
            {"question": "¿Cuánto es 2+2?", "answer": "4"},
            {"question": "¿Cuál es la capital de Francia?", "answer": "París"},
            {"question": "¿Cuánto es 5*5?", "answer": "25"},
            {"question": "¿Cuál es la capital de España?", "answer": "Madrid"},
            {"question": "Si tengo 3 manzanas y compro 2 más, ¿cuántas tengo?", "answer": "5"},
        ]

        # Test 1: Retorna k ejemplos
        try:
            query1 = "¿Cuánto es 10+15?"
            k = 2
            selected = student_function(query1, example_pool, k)

            assert isinstance(selected, list), "Debe retornar una lista"
            assert len(selected) == k, f"Debe retornar {k} ejemplos, retornó {len(selected)}"
            assert all(isinstance(ex, dict) for ex in selected), "Cada ejemplo debe ser un diccionario"

            test_cases.append({
                'name': f'Test 1: Retorna {k} ejemplos',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Retornó {len(selected)} ejemplos correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Cantidad correcta',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Cantidad correcta',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Selecciona ejemplos relevantes
        try:
            query2 = "¿Cuánto es 100 - 50?"
            k = 3
            selected = student_function(query2, example_pool, k)

            # Contar cuántos son matemáticos (debería priorizar)
            math_questions = ["2+2", "5*5", "3 manzanas"]
            math_count = sum(
                1 for ex in selected
                if any(math in ex['question'] for math in math_questions)
            )

            # Al menos 2 de los 3 deberían ser matemáticos
            assert math_count >= 2, \
                f"Debería priorizar ejemplos matemáticos (encontró {math_count}/3)"

            test_cases.append({
                'name': 'Test 2: Relevancia temática',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Seleccionó {math_count} ejemplos matemáticos de {k}'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Relevancia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Relevancia',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: k > len(examples)
        try:
            query3 = "Test query"
            k_large = 10
            selected = student_function(query3, example_pool, k_large)

            # Debe retornar todos los disponibles (5) o manejar correctamente
            assert len(selected) <= len(example_pool), \
                "No puede retornar más ejemplos de los disponibles"

            test_cases.append({
                'name': 'Test 3: k mayor que pool',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Manejó k>{len(example_pool)} (retornó {len(selected)})'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: k grande',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: k grande',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Sin duplicados
        try:
            query4 = "¿Qué es la capital?"
            k = 2
            selected = student_function(query4, example_pool, k)

            # Verificar que no hay duplicados
            selected_questions = [ex['question'] for ex in selected]
            assert len(selected_questions) == len(set(selected_questions)), \
                "No debe haber ejemplos duplicados"

            test_cases.append({
                'name': 'Test 4: Sin duplicados',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ No hay duplicados'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Sin duplicados',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Sin duplicados',
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
        print(f"Total: {total_points:.1f}/{self.exercise_points['select_best_examples']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'select_best_examples',
            'total_points': total_points,
            'max_points': self.exercise_points['select_best_examples'],
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
        print("AUTOGRADER: PROMPTING AGÉNTICO")
        print("="*70)

        all_results = []
        total_earned = 0

        # Ejecutar cada test
        if 'implement_zero_shot_cot' in student_functions:
            result = self.test_zero_shot_cot(student_functions['implement_zero_shot_cot'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'parse_cot_steps' in student_functions:
            result = self.test_parse_cot_steps(student_functions['parse_cot_steps'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'implement_majority_vote' in student_functions:
            result = self.test_majority_vote(student_functions['implement_majority_vote'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'evaluate_reasoning_path' in student_functions:
            result = self.test_evaluate_reasoning_path(student_functions['evaluate_reasoning_path'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'select_best_examples' in student_functions:
            result = self.test_select_best_examples(student_functions['select_best_examples'])
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
    print("Autograder para Prompting Agéntico cargado")
    print("Uso: grader = PromptingAgenticoGrader()")
    print("     grader.test_zero_shot_cot(tu_funcion)")

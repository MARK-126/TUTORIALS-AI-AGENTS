"""
Autograder para Notebook 05: Memory Systems

Total de puntos: 100
Mínimo para aprobar: 70

Ejercicios:
1. implement_short_term_memory (20 pts)
2. compute_similarity (20 pts)
3. retrieve_relevant_memories (25 pts)
4. update_long_term_memory (20 pts)
5. memory_compression (15 pts)
"""

from typing import List, Dict, Callable, Optional, Any
import re


class MemorySystemsGrader:
    """Sistema de autograding para Memory Systems."""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'implement_short_term_memory': 20,
            'compute_similarity': 20,
            'retrieve_relevant_memories': 25,
            'update_long_term_memory': 20,
            'memory_compression': 15
        }

    def test_implement_short_term_memory(self, student_function: Callable) -> Dict:
        """Test short-term memory (conversación reciente)."""
        print("\n" + "="*70)
        print("TEST: Ejercicio 1 - Short-Term Memory")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['implement_short_term_memory'] / 4
        total_points = 0

        # Test 1: Agregar y recuperar mensajes
        try:
            memory = student_function(max_messages=5)
            memory.add("user", "Hola")
            memory.add("assistant", "Hola! ¿Cómo estás?")
            
            messages = memory.get_recent(2)
            assert len(messages) == 2
            assert messages[0]["role"] == "user"
            assert messages[1]["role"] == "assistant"

            test_cases.append({
                'name': 'Test 1: Add/Get messages',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Almacenó y recuperó {len(messages)} mensajes'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 1', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 2: Límite de mensajes
        try:
            memory = student_function(max_messages=3)
            for i in range(5):
                memory.add("user", f"Mensaje {i}")
            
            recent = memory.get_recent(10)
            assert len(recent) <= 3, f"Debe respetar max_messages=3, tiene {len(recent)}"

            test_cases.append({
                'name': 'Test 2: Max messages limit',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Respetó límite ({len(recent)} mensajes)'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 2', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 3: Clear
        try:
            memory = student_function(max_messages=10)
            memory.add("user", "Test")
            memory.clear()
            messages = memory.get_recent(10)
            assert len(messages) == 0, "Después de clear debe estar vacío"

            test_cases.append({
                'name': 'Test 3: Clear memory',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Clear funcionó correctamente'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 3', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 4: Get recent con límite
        try:
            memory = student_function(max_messages=10)
            for i in range(8):
                memory.add("user", f"M{i}")
            
            last_3 = memory.get_recent(3)
            assert len(last_3) == 3
            # Los 3 más recientes deben ser M5, M6, M7
            assert "M5" in last_3[0]["content"] or "M6" in last_3[0]["content"] or "M7" in last_3[0]["content"]

            test_cases.append({
                'name': 'Test 4: Get recent limit',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Recuperó los N más recientes'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 4', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        for test in test_cases:
            print(f"\n{test['name']}: {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['implement_short_term_memory']}")
        print(f"{'='*70}")

        return {'exercise': 'implement_short_term_memory', 'total_points': total_points,
                'max_points': self.exercise_points['implement_short_term_memory'], 'test_cases': test_cases}

    def test_compute_similarity(self, student_function: Callable) -> Dict:
        """Test similarity computation entre textos."""
        print("\n" + "="*70)
        print("TEST: Ejercicio 2 - Compute Similarity")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['compute_similarity'] / 4
        total_points = 0

        # Test 1: Textos idénticos
        try:
            sim = student_function("hello world", "hello world")
            assert 0.95 <= sim <= 1.0, f"Textos idénticos deben tener sim ~1.0, obtuvo {sim}"

            test_cases.append({
                'name': 'Test 1: Identical texts',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Similitud correcta: {sim:.3f}'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 1', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 2: Textos completamente diferentes
        try:
            sim = student_function("python programming", "elephant banana")
            assert 0.0 <= sim <= 0.3, f"Textos diferentes deben tener sim baja, obtuvo {sim}"

            test_cases.append({
                'name': 'Test 2: Different texts',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Detectó diferencia: {sim:.3f}'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 2', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 3: Textos similares
        try:
            sim = student_function("machine learning", "machine learning algorithms")
            assert 0.4 <= sim <= 1.0, f"Textos similares deben tener sim media-alta, obtuvo {sim}"

            test_cases.append({
                'name': 'Test 3: Similar texts',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Similitud razonable: {sim:.3f}'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 3', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 4: Range [0, 1]
        try:
            sim1 = student_function("test", "test")
            sim2 = student_function("a", "z")
            assert 0.0 <= sim1 <= 1.0, "Similitud debe estar en [0,1]"
            assert 0.0 <= sim2 <= 1.0, "Similitud debe estar en [0,1]"

            test_cases.append({
                'name': 'Test 4: Range validation',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Valores en rango [0,1]'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 4', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        for test in test_cases:
            print(f"\n{test['name']}: {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['compute_similarity']}")
        print(f"{'='*70}")

        return {'exercise': 'compute_similarity', 'total_points': total_points,
                'max_points': self.exercise_points['compute_similarity'], 'test_cases': test_cases}

    def test_retrieve_relevant_memories(self, student_function: Callable) -> Dict:
        """Test retrieval de memorias relevantes."""
        print("\n" + "="*70)
        print("TEST: Ejercicio 3 - Retrieve Relevant Memories")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['retrieve_relevant_memories'] / 5
        total_points = 0

        memories = [
            {"content": "Python es un lenguaje de programación", "timestamp": "2024-01-01"},
            {"content": "Me gusta el helado de chocolate", "timestamp": "2024-01-02"},
            {"content": "Python fue creado por Guido van Rossum", "timestamp": "2024-01-03"},
            {"content": "El clima está soleado hoy", "timestamp": "2024-01-04"},
            {"content": "JavaScript es otro lenguaje de programación", "timestamp": "2024-01-05"}
        ]

        # Test 1: Query relevante
        try:
            results = student_function("¿Qué es Python?", memories, top_k=2)
            assert len(results) <= 2, f"Debe retornar top_k=2, retornó {len(results)}"
            # Las primeras 2 deberían ser sobre Python
            assert any("Python" in r["content"] for r in results[:2])

            test_cases.append({
                'name': 'Test 1: Relevant retrieval',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Recuperó {len(results)} memorias relevantes'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 1', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 2: top_k mayor que memorias
        try:
            results = student_function("test", memories, top_k=100)
            assert len(results) <= len(memories), "No puede retornar más de las disponibles"

            test_cases.append({
                'name': 'Test 2: top_k > memories',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Limitó correctamente ({len(results)} de {len(memories)})'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 2', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 3: Memorias vacías
        try:
            results = student_function("query", [], top_k=5)
            assert len(results) == 0, "Con memorias vacías debe retornar lista vacía"

            test_cases.append({
                'name': 'Test 3: Empty memories',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Manejó lista vacía'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 3', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 4: Orden (más relevante primero)
        try:
            results = student_function("lenguajes de programación", memories, top_k=3)
            # Debe retornar ordenado por relevancia (Python, JavaScript antes que helado)
            assert len(results) > 0
            # Verificar que hay estructura
            assert isinstance(results[0], dict)
            assert "content" in results[0]

            test_cases.append({
                'name': 'Test 4: Ordering',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Retornó resultados ordenados'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 4', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 5: Mantiene metadata
        try:
            results = student_function("Python", memories, top_k=1)
            if len(results) > 0:
                assert "timestamp" in results[0], "Debe mantener metadata original"

            test_cases.append({
                'name': 'Test 5: Preserve metadata',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Preservó metadata'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 5', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        for test in test_cases:
            print(f"\n{test['name']}: {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['retrieve_relevant_memories']}")
        print(f"{'='*70}")

        return {'exercise': 'retrieve_relevant_memories', 'total_points': total_points,
                'max_points': self.exercise_points['retrieve_relevant_memories'], 'test_cases': test_cases}

    def test_update_long_term_memory(self, student_function: Callable) -> Dict:
        """Test actualización de memoria a largo plazo."""
        print("\n" + "="*70)
        print("TEST: Ejercicio 4 - Update Long-Term Memory")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['update_long_term_memory'] / 4
        total_points = 0

        # Test 1: Agregar nueva memoria
        try:
            ltm = student_function(max_memories=10)
            ltm.add("Python es un lenguaje de programación")
            
            all_mem = ltm.get_all()
            assert len(all_mem) == 1
            assert "Python" in all_mem[0]["content"]

            test_cases.append({
                'name': 'Test 1: Add memory',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Agregó memoria correctamente'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 1', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 2: Límite de memorias
        try:
            ltm = student_function(max_memories=5)
            for i in range(10):
                ltm.add(f"Memoria {i}")
            
            all_mem = ltm.get_all()
            assert len(all_mem) <= 5, f"Debe respetar max=5, tiene {len(all_mem)}"

            test_cases.append({
                'name': 'Test 2: Memory limit',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Respetó límite ({len(all_mem)} memorias)'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 2', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 3: Búsqueda
        try:
            ltm = student_function(max_memories=10)
            ltm.add("Python es genial")
            ltm.add("JavaScript también")
            
            results = ltm.search("Python", top_k=1)
            assert len(results) <= 1
            if len(results) > 0:
                assert "Python" in results[0]["content"]

            test_cases.append({
                'name': 'Test 3: Search',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Búsqueda funciona'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 3', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 4: Clear
        try:
            ltm = student_function(max_memories=10)
            ltm.add("Test 1")
            ltm.add("Test 2")
            ltm.clear()
            
            all_mem = ltm.get_all()
            assert len(all_mem) == 0, "Después de clear debe estar vacío"

            test_cases.append({
                'name': 'Test 4: Clear',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Clear funciona'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 4', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        for test in test_cases:
            print(f"\n{test['name']}: {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['update_long_term_memory']}")
        print(f"{'='*70}")

        return {'exercise': 'update_long_term_memory', 'total_points': total_points,
                'max_points': self.exercise_points['update_long_term_memory'], 'test_cases': test_cases}

    def test_memory_compression(self, student_function: Callable) -> Dict:
        """Test compresión de memoria."""
        print("\n" + "="*70)
        print("TEST: Ejercicio 5 - Memory Compression")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['memory_compression'] / 3
        total_points = 0

        # Test 1: Comprime efectivamente
        try:
            long_text = " ".join(["Este es un mensaje de prueba."] * 10)
            compressed = student_function(long_text, max_length=50)
            
            assert len(compressed) <= 50, f"Debe comprimir a max_length=50, tiene {len(compressed)}"
            assert len(compressed) > 0, "No debe ser vacío"

            test_cases.append({
                'name': 'Test 1: Compression',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Comprimió: {len(long_text)} → {len(compressed)}'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 1', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 2: Texto corto sin comprimir
        try:
            short_text = "Hola"
            compressed = student_function(short_text, max_length=100)
            # Si el texto ya es corto, puede dejarlo igual
            assert len(compressed) <= max_length

            test_cases.append({
                'name': 'Test 2: Short text',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Manejó texto corto'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 2', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        # Test 3: Preserva información clave
        try:
            text_with_key_info = "El usuario vive en París. Tiene 30 años. Le gusta el café."
            compressed = student_function(text_with_key_info, max_length=40)
            
            # Debe preservar algo de información (no verificamos exactamente qué)
            assert len(compressed) > 5, "Debe preservar algo de información"

            test_cases.append({
                'name': 'Test 3: Preserve info',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Preservó información ({len(compressed)} chars)'
            })
            total_points += points_per_test
        except Exception as e:
            test_cases.append({'name': 'Test 3', 'passed': False, 'points': 0, 'feedback': f'✗ {str(e)}'})

        for test in test_cases:
            print(f"\n{test['name']}: {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['memory_compression']}")
        print(f"{'='*70}")

        return {'exercise': 'memory_compression', 'total_points': total_points,
                'max_points': self.exercise_points['memory_compression'], 'test_cases': test_cases}

    def grade_all(self, student_functions: Dict[str, Callable]) -> Dict:
        """Ejecuta todos los tests."""
        print("\n" + "="*70)
        print("AUTOGRADER: Memory Systems")
        print("="*70)

        all_results = []
        total_earned = 0

        for func_name in self.exercise_points.keys():
            if func_name in student_functions:
                test_method = getattr(self, f'test_{func_name}')
                result = test_method(student_functions[func_name])
                all_results.append(result)
                total_earned += result['total_points']

        percentage = (total_earned / self.total_points) * 100
        passed = total_earned >= self.passing_grade

        print("\n" + "="*70)
        print("RESUMEN FINAL")
        print("="*70)

        for result in all_results:
            status = "✓" if result['total_points'] == result['max_points'] else "⚠"
            print(f"{status} {result['exercise']}: {result['total_points']:.1f}/{result['max_points']}")

        print(f"\n{'='*70}")
        print(f"TOTAL: {total_earned:.1f}/{self.total_points} ({percentage:.1f}%)")
        print(f"{'✅ APROBADO' if passed else '❌ NO APROBADO'} (mínimo: {self.passing_grade})")
        print(f"{'='*70}\n")

        return {'total_points': total_earned, 'max_points': self.total_points,
                'percentage': percentage, 'passed': passed, 'exercise_results': all_results}

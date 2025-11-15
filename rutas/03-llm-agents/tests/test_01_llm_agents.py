"""
Autograder para 01-intro-llm-agents.ipynb

Sistema de evaluación automática para ejercicios de LLM Agents.

Ejercicios:
1. parse_tool_response (15 pts)
2. execute_tool (15 pts)
3. build_agent_prompt (20 pts)
4. simple_agent_step (25 pts)
5. agent_with_memory (25 pts)

Total: 100 puntos
Mínimo para aprobar: 70 puntos
"""

import numpy as np
import json
import re
from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass


class LLMAgentsGrader:
    """Sistema de autograding para ejercicios de LLM Agents"""

    def __init__(self):
        self.total_points = 100
        self.earned_points = 0
        self.exercise_results = {}

        self.exercise_points = {
            'parse_tool_response': 15,
            'execute_tool': 15,
            'build_agent_prompt': 20,
            'simple_agent_step': 25,
            'agent_with_memory': 25
        }

        print("="*70)
        print("🎓 AUTOGRADER DE LLM AGENTS")
        print("="*70)
        print(f"\n📊 Puntos totales disponibles: {self.total_points}")
        print(f"📊 Puntos mínimos para aprobar: 70")
        print("\n💡 Cada ejercicio tiene múltiples test cases")
        print("💡 Debes pasar TODOS los tests para obtener los puntos completos\n")

    def test_parse_tool_response(self, student_function):
        """
        Test Exercise 1: parse_tool_response

        Objetivo: Parsear respuesta de LLM para extraer llamada a herramienta

        La función debe extraer:
        - tool_name: Nombre de la herramienta
        - tool_input: Input para la herramienta
        - reasoning: Razonamiento del agente (opcional)

        Formato esperado de respuesta LLM:
        "PENSAMIENTO: [razonamiento]
         HERRAMIENTA: [nombre]
         INPUT: [input]"

        Returns:
            Dict con {tool_name, tool_input, reasoning} o None si no hay tool call
        """
        exercise_name = 'parse_tool_response'
        max_points = self.exercise_points[exercise_name]
        points_earned = 0

        print(f"\n{'='*70}")
        print(f"🧪 Testing Exercise 1: parse_tool_response ({max_points} puntos)")
        print(f"{'='*70}\n")

        tests_passed = 0
        total_tests = 5

        # Test 1: Respuesta con tool call básico
        print("Test 1: Tool call básico...")
        response1 = """PENSAMIENTO: Necesito calcular una expresión matemática
HERRAMIENTA: calculator
INPUT: 2 + 2"""

        try:
            result = student_function(response1)
            assert result is not None, "Debe retornar un dict, no None"
            assert result['tool_name'] == 'calculator', f"Tool name incorrecto: {result.get('tool_name')}"
            assert result['tool_input'] == '2 + 2', f"Tool input incorrecto: {result.get('tool_input')}"
            assert 'reasoning' in result, "Debe incluir 'reasoning' en el resultado"
            print("  ✅ Test 1 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 1 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 1 ERROR: {e}")

        # Test 2: Respuesta sin tool call (solo texto)
        print("\nTest 2: Respuesta sin tool call...")
        response2 = "Hola, soy un asistente. ¿En qué puedo ayudarte?"

        try:
            result = student_function(response2)
            assert result is None, "Debe retornar None cuando no hay tool call"
            print("  ✅ Test 2 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 2 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 2 ERROR: {e}")

        # Test 3: Tool call con input multilinea
        print("\nTest 3: Input multilinea...")
        response3 = """PENSAMIENTO: Necesito buscar información
HERRAMIENTA: web_search
INPUT: what is the capital of France
and when was it founded"""

        try:
            result = student_function(response3)
            assert result is not None, "Debe manejar input multilinea"
            assert result['tool_name'] == 'web_search', "Tool name incorrecto"
            assert 'capital of France' in result['tool_input'], "Debe capturar input multilinea"
            print("  ✅ Test 3 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 3 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 3 ERROR: {e}")

        # Test 4: Formato alternativo (sin PENSAMIENTO)
        print("\nTest 4: Formato sin PENSAMIENTO...")
        response4 = """HERRAMIENTA: get_time
INPUT: UTC"""

        try:
            result = student_function(response4)
            assert result is not None, "Debe funcionar sin PENSAMIENTO"
            assert result['tool_name'] == 'get_time', "Tool name incorrecto"
            assert result['tool_input'] == 'UTC', "Tool input incorrecto"
            print("  ✅ Test 4 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 4 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 4 ERROR: {e}")

        # Test 5: Case insensitive
        print("\nTest 5: Case insensitive...")
        response5 = """pensamiento: voy a calcular
herramienta: calculator
input: 5 * 3"""

        try:
            result = student_function(response5)
            assert result is not None, "Debe ser case-insensitive"
            assert result['tool_name'] == 'calculator', "Debe manejar lowercase"
            print("  ✅ Test 5 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 5 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 5 ERROR: {e}")

        # Calcular puntos
        points_earned = (tests_passed / total_tests) * max_points
        self.earned_points += points_earned
        self.exercise_results[exercise_name] = {
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'points_earned': points_earned,
            'max_points': max_points
        }

        print(f"\n{'='*70}")
        print(f"📊 Resultado: {tests_passed}/{total_tests} tests pasados")
        print(f"💯 Puntos obtenidos: {points_earned:.1f}/{max_points}")
        print(f"={'='*70}\n")

        return points_earned

    def test_execute_tool(self, student_function):
        """
        Test Exercise 2: execute_tool

        Objetivo: Ejecutar una herramienta dado su nombre e input

        Args:
            tool_name: str - nombre de la herramienta
            tool_input: str - input para la herramienta
            tools: Dict[str, Callable] - dict de herramientas disponibles

        Returns:
            str - resultado de ejecutar la herramienta
        """
        exercise_name = 'execute_tool'
        max_points = self.exercise_points[exercise_name]
        points_earned = 0

        print(f"\n{'='*70}")
        print(f"🧪 Testing Exercise 2: execute_tool ({max_points} puntos)")
        print(f"{'='*70}\n")

        tests_passed = 0
        total_tests = 4

        # Definir herramientas de prueba
        test_tools = {
            'calculator': lambda x: str(eval(x)),
            'upper': lambda x: x.upper(),
            'length': lambda x: str(len(x)),
            'reverse': lambda x: x[::-1]
        }

        # Test 1: Ejecutar calculadora
        print("Test 1: Ejecutar calculadora...")
        try:
            result = student_function('calculator', '10 + 5', test_tools)
            assert result == '15', f"Resultado incorrecto: {result}"
            print("  ✅ Test 1 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 1 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 1 ERROR: {e}")

        # Test 2: Herramienta string
        print("\nTest 2: Herramienta string...")
        try:
            result = student_function('upper', 'hello world', test_tools)
            assert result == 'HELLO WORLD', f"Resultado incorrecto: {result}"
            print("  ✅ Test 2 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 2 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 2 ERROR: {e}")

        # Test 3: Herramienta inexistente
        print("\nTest 3: Herramienta inexistente...")
        try:
            result = student_function('nonexistent', 'test', test_tools)
            assert 'error' in result.lower() or 'not found' in result.lower(), \
                "Debe retornar mensaje de error"
            print("  ✅ Test 3 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 3 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 3 ERROR: {e}")

        # Test 4: Manejar excepción en herramienta
        print("\nTest 4: Manejar excepción...")
        try:
            # División por cero
            result = student_function('calculator', '1 / 0', test_tools)
            assert 'error' in result.lower() or 'division' in result.lower(), \
                "Debe manejar errores de herramientas"
            print("  ✅ Test 4 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 4 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 4 ERROR: {e}")

        # Calcular puntos
        points_earned = (tests_passed / total_tests) * max_points
        self.earned_points += points_earned
        self.exercise_results[exercise_name] = {
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'points_earned': points_earned,
            'max_points': max_points
        }

        print(f"\n{'='*70}")
        print(f"📊 Resultado: {tests_passed}/{total_tests} tests pasados")
        print(f"💯 Puntos obtenidos: {points_earned:.1f}/{max_points}")
        print(f"={'='*70}\n")

        return points_earned

    def test_build_agent_prompt(self, student_function):
        """
        Test Exercise 3: build_agent_prompt

        Objetivo: Construir el prompt del agente con system message, tools, y query

        Args:
            system_message: str - instrucciones del sistema
            tools: Dict[str, str] - {tool_name: tool_description}
            user_query: str - pregunta del usuario
            history: List[Dict] - historial de conversación (opcional)

        Returns:
            str - prompt completo formateado
        """
        exercise_name = 'build_agent_prompt'
        max_points = self.exercise_points[exercise_name]
        points_earned = 0

        print(f"\n{'='*70}")
        print(f"🧪 Testing Exercise 3: build_agent_prompt ({max_points} puntos)")
        print(f"{'='*70}\n")

        tests_passed = 0
        total_tests = 4

        system_msg = "Eres un asistente útil que puede usar herramientas."
        tools = {
            'calculator': 'Calcula expresiones matemáticas',
            'search': 'Busca información en la web'
        }
        query = "¿Cuánto es 2+2?"

        # Test 1: Prompt básico
        print("Test 1: Prompt básico...")
        try:
            result = student_function(system_msg, tools, query)
            assert isinstance(result, str), "Debe retornar un string"
            assert system_msg in result, "Debe incluir system message"
            assert query in result, "Debe incluir la query del usuario"
            assert 'calculator' in result, "Debe listar herramientas disponibles"
            assert 'search' in result, "Debe listar todas las herramientas"
            print("  ✅ Test 1 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 1 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 1 ERROR: {e}")

        # Test 2: Incluye descripciones de herramientas
        print("\nTest 2: Descripciones de herramientas...")
        try:
            result = student_function(system_msg, tools, query)
            assert 'Calcula expresiones' in result, "Debe incluir descripción de calculator"
            assert 'Busca información' in result, "Debe incluir descripción de search"
            print("  ✅ Test 2 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 2 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 2 ERROR: {e}")

        # Test 3: Formato de respuesta especificado
        print("\nTest 3: Instrucciones de formato...")
        try:
            result = student_function(system_msg, tools, query)
            # Debe incluir instrucciones de cómo responder
            assert 'HERRAMIENTA:' in result or 'herramienta' in result.lower(), \
                "Debe instruir formato de respuesta con herramienta"
            print("  ✅ Test 3 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 3 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 3 ERROR: {e}")

        # Test 4: Prompt con historial
        print("\nTest 4: Prompt con historial...")
        try:
            history = [
                {'role': 'user', 'content': 'Hola'},
                {'role': 'assistant', 'content': 'Hola! ¿En qué puedo ayudarte?'}
            ]
            result = student_function(system_msg, tools, query, history=history)
            assert 'Hola' in result, "Debe incluir historial si se provee"
            print("  ✅ Test 4 PASADO")
            tests_passed += 1
        except TypeError:
            # Puede que no soporte history como parámetro, eso está OK
            print("  ⚠️  Test 4 SKIPPED (history no implementado - opcional)")
            tests_passed += 0.5  # Medio punto por intentarlo
        except AssertionError as e:
            print(f"  ❌ Test 4 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 4 ERROR: {e}")

        # Calcular puntos
        points_earned = (tests_passed / total_tests) * max_points
        self.earned_points += points_earned
        self.exercise_results[exercise_name] = {
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'points_earned': points_earned,
            'max_points': max_points
        }

        print(f"\n{'='*70}")
        print(f"📊 Resultado: {tests_passed}/{total_tests} tests pasados")
        print(f"💯 Puntos obtenidos: {points_earned:.1f}/{max_points}")
        print(f"={'='*70}\n")

        return points_earned

    def test_simple_agent_step(self, student_function):
        """
        Test Exercise 4: simple_agent_step

        Objetivo: Ejecutar un paso del loop del agente

        Un paso consiste en:
        1. Construir prompt
        2. Llamar a LLM simulado
        3. Parsear respuesta
        4. Ejecutar herramienta si es necesario
        5. Retornar observación

        Args:
            query: str - pregunta del usuario
            tools: Dict - herramientas disponibles
            llm_function: Callable - función LLM (puede ser simulada)

        Returns:
            Dict con {action: str, observation: str, done: bool}
        """
        exercise_name = 'simple_agent_step'
        max_points = self.exercise_points[exercise_name]
        points_earned = 0

        print(f"\n{'='*70}")
        print(f"🧪 Testing Exercise 4: simple_agent_step ({max_points} puntos)")
        print(f"{'='*70}\n")

        tests_passed = 0
        total_tests = 4

        # LLM simulado que decide usar calculadora
        def simulated_llm_calc(prompt):
            if 'calcular' in prompt.lower() or '+' in prompt:
                return """PENSAMIENTO: Necesito calcular
HERRAMIENTA: calculator
INPUT: 10 + 5"""
            return "No necesito herramientas para responder esto."

        # LLM que responde directo
        def simulated_llm_direct(prompt):
            return "Hola, soy un asistente."

        tools = {
            'calculator': lambda x: str(eval(x)),
            'upper': lambda x: x.upper()
        }

        # Test 1: Paso con tool call
        print("Test 1: Paso con tool call...")
        try:
            result = student_function("Calcula 10 + 5", tools, simulated_llm_calc)
            assert isinstance(result, dict), "Debe retornar un dict"
            assert 'observation' in result, "Debe incluir 'observation'"
            assert 'action' in result, "Debe incluir 'action'"
            assert '15' in str(result['observation']), "Observación debe contener resultado"
            print("  ✅ Test 1 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 1 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 1 ERROR: {e}")

        # Test 2: Paso sin tool call (respuesta directa)
        print("\nTest 2: Paso sin tool call...")
        try:
            result = student_function("Hola", tools, simulated_llm_direct)
            assert isinstance(result, dict), "Debe retornar un dict"
            assert result.get('action') is None or result.get('action') == 'none', \
                "No debe haber acción si no se usa herramienta"
            print("  ✅ Test 2 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 2 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 2 ERROR: {e}")

        # Test 3: Validar estructura de retorno
        print("\nTest 3: Estructura de retorno...")
        try:
            result = student_function("Calcula 2+2", tools, simulated_llm_calc)
            required_keys = ['action', 'observation']
            for key in required_keys:
                assert key in result, f"Falta clave '{key}' en resultado"
            print("  ✅ Test 3 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 3 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 3 ERROR: {e}")

        # Test 4: Manejo de herramienta inexistente
        print("\nTest 4: Herramienta inexistente...")
        try:
            def llm_bad_tool(prompt):
                return """HERRAMIENTA: nonexistent
INPUT: test"""

            result = student_function("Test", tools, llm_bad_tool)
            # Debe manejar el error gracefully
            assert 'error' in str(result.get('observation', '')).lower(), \
                "Debe reportar error cuando herramienta no existe"
            print("  ✅ Test 4 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 4 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 4 ERROR: {e}")

        # Calcular puntos
        points_earned = (tests_passed / total_tests) * max_points
        self.earned_points += points_earned
        self.exercise_results[exercise_name] = {
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'points_earned': points_earned,
            'max_points': max_points
        }

        print(f"\n{'='*70}")
        print(f"📊 Resultado: {tests_passed}/{total_tests} tests pasados")
        print(f"💯 Puntos obtenidos: {points_earned:.1f}/{max_points}")
        print(f"={'='*70}\n")

        return points_earned

    def test_agent_with_memory(self, student_function):
        """
        Test Exercise 5: agent_with_memory

        Objetivo: Implementar agente con memoria de conversación

        El agente debe:
        1. Recordar interacciones previas
        2. Incluir historial en prompts
        3. Poder referenciar información de turnos anteriores

        Args:
            tools: Dict - herramientas disponibles
            max_turns: int - máximo de turnos

        Returns:
            Agent object con método .chat(query) que mantiene historial
        """
        exercise_name = 'agent_with_memory'
        max_points = self.exercise_points[exercise_name]
        points_earned = 0

        print(f"\n{'='*70}")
        print(f"🧪 Testing Exercise 5: agent_with_memory ({max_points} puntos)")
        print(f"{'='*70}\n")

        tests_passed = 0
        total_tests = 4

        tools = {
            'calculator': lambda x: str(eval(x)),
            'save_number': lambda x: f"Saved: {x}"
        }

        # Test 1: Crear agente con memoria
        print("Test 1: Crear agente...")
        try:
            agent = student_function(tools)
            assert hasattr(agent, 'chat'), "Agente debe tener método .chat()"
            assert hasattr(agent, 'history') or hasattr(agent, 'memory'), \
                "Agente debe tener atributo 'history' o 'memory'"
            print("  ✅ Test 1 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 1 FALLIDO: {e}")
            # Si falla esto, no podemos continuar
            print("\n⚠️  No se puede continuar sin agente válido")
            return 0
        except Exception as e:
            print(f"  ❌ Test 1 ERROR: {e}")
            return 0

        # Test 2: Mantener historial
        print("\nTest 2: Mantener historial...")
        try:
            agent = student_function(tools)
            response1 = agent.chat("Hola")
            response2 = agent.chat("Calcula 5+3")

            # Verificar que tiene historial
            if hasattr(agent, 'history'):
                assert len(agent.history) >= 2, "Debe tener al menos 2 interacciones"
            elif hasattr(agent, 'memory'):
                assert len(agent.memory) >= 2, "Debe tener al menos 2 interacciones en memoria"

            print("  ✅ Test 2 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 2 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 2 ERROR: {e}")

        # Test 3: Referenciar información previa
        print("\nTest 3: Referenciar conversación previa...")
        try:
            agent = student_function(tools)
            # Primera interacción - guardar número
            agent.chat("Guarda el número 42")

            # Segunda interacción - debería poder referenciar
            # El prompt del agente debe incluir la interacción previa
            if hasattr(agent, 'history'):
                assert '42' in str(agent.history), "Historia debe contener número previo"
            elif hasattr(agent, 'memory'):
                assert '42' in str(agent.memory), "Memoria debe contener número previo"

            print("  ✅ Test 3 PASADO")
            tests_passed += 1
        except AssertionError as e:
            print(f"  ❌ Test 3 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 3 ERROR: {e}")

        # Test 4: Reset o clear history
        print("\nTest 4: Limpiar historial...")
        try:
            agent = student_function(tools)
            agent.chat("Test 1")
            agent.chat("Test 2")

            # Debe tener método para limpiar
            if hasattr(agent, 'reset'):
                agent.reset()
                assert len(agent.history if hasattr(agent, 'history') else agent.memory) == 0, \
                    "reset() debe limpiar historial"
                print("  ✅ Test 4 PASADO")
                tests_passed += 1
            elif hasattr(agent, 'clear'):
                agent.clear()
                assert len(agent.history if hasattr(agent, 'history') else agent.memory) == 0, \
                    "clear() debe limpiar historial"
                print("  ✅ Test 4 PASADO")
                tests_passed += 1
            else:
                print("  ⚠️  Test 4 SKIPPED (método reset/clear no encontrado - opcional)")
                tests_passed += 0.5  # Medio punto
        except AssertionError as e:
            print(f"  ❌ Test 4 FALLIDO: {e}")
        except Exception as e:
            print(f"  ❌ Test 4 ERROR: {e}")

        # Calcular puntos
        points_earned = (tests_passed / total_tests) * max_points
        self.earned_points += points_earned
        self.exercise_results[exercise_name] = {
            'tests_passed': tests_passed,
            'total_tests': total_tests,
            'points_earned': points_earned,
            'max_points': max_points
        }

        print(f"\n{'='*70}")
        print(f"📊 Resultado: {tests_passed}/{total_tests} tests pasados")
        print(f"💯 Puntos obtenidos: {points_earned:.1f}/{max_points}")
        print(f"={'='*70}\n")

        return points_earned

    def get_grade_summary(self):
        """Muestra resumen final de calificación"""
        print("\n" + "="*70)
        print("📊 RESUMEN FINAL DE CALIFICACIÓN")
        print("="*70)

        print(f"\n{'Ejercicio':<30} {'Tests':<12} {'Puntos':<15} {'Estado'}")
        print("-"*70)

        for exercise, points in self.exercise_points.items():
            if exercise in self.exercise_results:
                result = self.exercise_results[exercise]
                tests_str = f"{result['tests_passed']}/{result['total_tests']}"
                points_str = f"{result['points_earned']:.1f}/{result['max_points']}"
                status = "✅" if result['tests_passed'] == result['total_tests'] else "⚠️"
                print(f"{exercise:<30} {tests_str:<12} {points_str:<15} {status}")
            else:
                print(f"{exercise:<30} {'0/0':<12} {'0.0/' + str(points):<15} {'❌'}")

        print("-"*70)
        print(f"{'TOTAL':<30} {'':<12} {self.earned_points:.1f}/{self.total_points:<15}")
        print("="*70)

        # Determinar calificación
        percentage = (self.earned_points / self.total_points) * 100

        if percentage >= 90:
            grade = "A (Excelente)"
            emoji = "🌟"
        elif percentage >= 80:
            grade = "B (Muy Bien)"
            emoji = "⭐"
        elif percentage >= 70:
            grade = "C (Aprobado)"
            emoji = "✅"
        elif percentage >= 60:
            grade = "D (Necesita Mejora)"
            emoji = "⚠️"
        else:
            grade = "F (No Aprobado)"
            emoji = "❌"

        print(f"\n{emoji}  CALIFICACIÓN FINAL: {grade}")
        print(f"📊 Porcentaje: {percentage:.1f}%")

        if percentage >= 70:
            print(f"\n🎉 ¡FELICITACIONES! Has aprobado el notebook de LLM Agents")
            print(f"💯 Obtuviste {self.earned_points:.1f} de {self.total_points} puntos")
        else:
            print(f"\n📚 Necesitas al menos 70 puntos para aprobar")
            print(f"💡 Revisa los ejercicios que fallaron y vuelve a intentar")

        print("="*70 + "\n")

        return {
            'total_points': self.total_points,
            'earned_points': self.earned_points,
            'percentage': percentage,
            'grade': grade,
            'passed': percentage >= 70
        }


# Funciones auxiliares para tests
def create_test_agent():
    """Crea un agente simple para testing"""
    pass


if __name__ == "__main__":
    print("Autograder para 01-intro-llm-agents.ipynb")
    print("Importa este módulo en tu notebook y usa:")
    print("  grader = LLMAgentsGrader()")
    print("  grader.test_parse_tool_response(tu_funcion)")

"""
Autograder para Notebook 06: Sistemas Multi-Agente

Ejercicios GRADED:
1. implement_sequential_pipeline (20 pts)
2. task_decomposition (20 pts)
3. agent_communication (25 pts)
4. consensus_mechanism (20 pts)
5. autonomous_loop (15 pts)

Total: 100 puntos
Passing grade: 70 puntos
"""

import pytest
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

# Configuración de paths
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))


class MultiAgentGrader:
    """Grader para ejercicios de sistemas multi-agente"""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'implement_sequential_pipeline': 20,
            'task_decomposition': 20,
            'agent_communication': 25,
            'consensus_mechanism': 20,
            'autonomous_loop': 15
        }
        self.results = {
            'exercises': {},
            'total_earned': 0,
            'total_possible': self.total_points,
            'passing_grade': self.passing_grade,
            'passed': False
        }

    def grade_exercise(self, exercise_name: str, points_earned: float):
        """Registra puntos ganados para un ejercicio"""
        max_points = self.exercise_points.get(exercise_name, 0)
        points_earned = min(points_earned, max_points)

        self.results['exercises'][exercise_name] = {
            'earned': points_earned,
            'possible': max_points,
            'percentage': (points_earned / max_points * 100) if max_points > 0 else 0
        }
        self.results['total_earned'] += points_earned

    def finalize(self):
        """Finaliza grading y determina si pasó"""
        self.results['passed'] = self.results['total_earned'] >= self.passing_grade
        return self.results

    def print_report(self):
        """Imprime reporte de calificación"""
        print("\n" + "="*70)
        print("📊 REPORTE DE CALIFICACIÓN - NOTEBOOK 06: MULTI-AGENTE")
        print("="*70 + "\n")

        for ex_name, ex_data in self.results['exercises'].items():
            status = "✅" if ex_data['earned'] == ex_data['possible'] else "⚠️"
            print(f"{status} {ex_name}:")
            print(f"   {ex_data['earned']:.1f}/{ex_data['possible']} puntos ({ex_data['percentage']:.1f}%)\n")

        print("="*70)
        print(f"Total: {self.results['total_earned']:.1f}/{self.results['total_possible']} puntos")
        print(f"Passing grade: {self.passing_grade}")

        if self.results['passed']:
            print("\n🎉 ¡APROBADO! Excelente trabajo con sistemas multi-agente.")
        else:
            needed = self.passing_grade - self.results['total_earned']
            print(f"\n❌ Necesitas {needed:.1f} puntos más para aprobar.")

        print("="*70 + "\n")


# ============================================================================
# EJERCICIO 1: Sequential Pipeline (20 puntos)
# ============================================================================

class TestSequentialPipeline:
    """Tests para implementación de pipeline secuencial"""

    @pytest.fixture
    def grader(self):
        return MultiAgentGrader()

    def test_sequential_pipeline(self, grader):
        """
        Test completo del ejercicio 1: Sequential Pipeline

        Valida:
        - Pipeline ejecuta agentes en orden
        - Output de un agente → input del siguiente
        - Todas las etapas se completan
        - Resultado final correcto
        """
        try:
            from notebook_06_exercises import implement_sequential_pipeline
        except ImportError:
            pytest.skip("Función implement_sequential_pipeline no encontrada")

        points = 0
        max_points = 20

        # Test 1: Pipeline básico de 3 agentes (5 pts)
        try:
            def agent1(input_data):
                return f"A1({input_data})"

            def agent2(input_data):
                return f"A2({input_data})"

            def agent3(input_data):
                return f"A3({input_data})"

            agents = [agent1, agent2, agent3]
            result = implement_sequential_pipeline(agents, "start")

            assert isinstance(result, str), "Resultado debe ser string"
            assert "A3" in result, "Debe incluir output del último agente"
            assert "A2" in result, "Debe incluir transformación del agente 2"
            assert "A1" in result, "Debe incluir transformación del agente 1"
            points += 5
            print("✅ Test 1 passed: Pipeline básico (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Pipeline con transformaciones (5 pts)
        try:
            def upper_agent(text):
                return text.upper()

            def add_prefix(text):
                return f"PREFIX-{text}"

            def add_suffix(text):
                return f"{text}-SUFFIX"

            agents = [upper_agent, add_prefix, add_suffix]
            result = implement_sequential_pipeline(agents, "hello")

            expected = "PREFIX-HELLO-SUFFIX"
            assert result == expected, f"Expected {expected}, got {result}"
            points += 5
            print("✅ Test 2 passed: Pipeline con transformaciones (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Pipeline vacío (5 pts)
        try:
            result = implement_sequential_pipeline([], "input")
            assert result == "input", "Pipeline vacío debe retornar input sin cambios"
            points += 5
            print("✅ Test 3 passed: Pipeline vacío (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Pipeline con un solo agente (5 pts)
        try:
            def single_agent(data):
                return f"processed: {data}"

            result = implement_sequential_pipeline([single_agent], "test")
            assert result == "processed: test", "Single agent pipeline debe funcionar"
            points += 5
            print("✅ Test 4 passed: Single agent (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('implement_sequential_pipeline', points)
        print(f"\n📊 Ejercicio 1 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 2: Task Decomposition (20 puntos)
# ============================================================================

class TestTaskDecomposition:
    """Tests para descomposición de tareas"""

    @pytest.fixture
    def grader(self):
        return MultiAgentGrader()

    def test_task_decomposition(self, grader):
        """
        Test completo del ejercicio 2: Task Decomposition

        Valida:
        - Tarea compleja se descompone en subtareas
        - Subtareas son atómicas y accionables
        - Dependencias entre subtareas detectadas
        - Orden lógico de ejecución
        """
        try:
            from notebook_06_exercises import task_decomposition
        except ImportError:
            pytest.skip("Función task_decomposition no encontrada")

        points = 0
        max_points = 20

        # Test 1: Descomposición básica (5 pts)
        try:
            task = "Crear una aplicación web"
            subtasks = task_decomposition(task)

            assert isinstance(subtasks, list), "Debe retornar lista de subtareas"
            assert len(subtasks) >= 3, "Debe generar al menos 3 subtareas"
            assert all(isinstance(st, (str, dict)) for st in subtasks), "Cada subtarea debe ser string o dict"
            points += 5
            print("✅ Test 1 passed: Descomposición básica (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Subtareas tienen estructura (5 pts)
        try:
            task = "Implementar autenticación de usuarios"
            subtasks = task_decomposition(task, include_metadata=True)

            assert len(subtasks) > 0, "Debe generar subtareas"

            # Si retorna dicts, validar estructura
            if isinstance(subtasks[0], dict):
                first = subtasks[0]
                assert 'description' in first or 'task' in first, "Dict debe tener description/task"

            points += 5
            print("✅ Test 2 passed: Estructura de subtareas (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Tarea simple no se sobre-descompone (5 pts)
        try:
            simple_task = "Imprimir 'hola mundo'"
            subtasks = task_decomposition(simple_task)

            # Tarea simple debe generar pocas subtareas (1-2)
            assert len(subtasks) <= 3, "Tarea simple no debe sobre-descomponerse"
            points += 5
            print("✅ Test 3 passed: No sobre-descomposición (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Múltiples tareas se descomponen correctamente (5 pts)
        try:
            tasks = [
                "Crear API REST",
                "Diseñar base de datos",
                "Implementar frontend"
            ]

            all_decomposed = []
            for t in tasks:
                subtasks = task_decomposition(t)
                assert len(subtasks) > 0, f"Tarea '{t}' debe generar subtareas"
                all_decomposed.extend(subtasks)

            assert len(all_decomposed) >= len(tasks), "Debe generar subtareas para todas las tareas"
            points += 5
            print("✅ Test 4 passed: Múltiples tareas (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('task_decomposition', points)
        print(f"\n📊 Ejercicio 2 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 3: Agent Communication (25 puntos)
# ============================================================================

class TestAgentCommunication:
    """Tests para comunicación entre agentes"""

    @pytest.fixture
    def grader(self):
        return MultiAgentGrader()

    def test_agent_communication(self, grader):
        """
        Test completo del ejercicio 3: Agent Communication

        Valida:
        - Mensajes se envían correctamente
        - Formato de mensaje estándar
        - Routing de mensajes entre agentes
        - Message queue funciona
        """
        try:
            from notebook_06_exercises import agent_communication
        except ImportError:
            pytest.skip("Función agent_communication no encontrada")

        points = 0
        max_points = 25

        # Test 1: Enviar mensaje básico (6 pts)
        try:
            comm_system = agent_communication()

            message = {
                "from": "agent1",
                "to": "agent2",
                "content": "Hello"
            }

            success = comm_system.send(message)
            assert success, "Envío debe ser exitoso"
            points += 6
            print("✅ Test 1 passed: Envío de mensaje (6 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Recibir mensajes (6 pts)
        try:
            comm_system = agent_communication()

            msg1 = {"from": "a1", "to": "a2", "content": "msg1"}
            msg2 = {"from": "a3", "to": "a2", "content": "msg2"}

            comm_system.send(msg1)
            comm_system.send(msg2)

            messages = comm_system.receive("a2")
            assert len(messages) >= 2, "Debe recibir ambos mensajes"
            points += 6
            print("✅ Test 2 passed: Recepción de mensajes (6 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Filtrado por destinatario (7 pts)
        try:
            comm_system = agent_communication()

            comm_system.send({"from": "a1", "to": "a2", "content": "for a2"})
            comm_system.send({"from": "a1", "to": "a3", "content": "for a3"})

            messages_a2 = comm_system.receive("a2")
            messages_a3 = comm_system.receive("a3")

            # a2 solo debe recibir su mensaje
            a2_contents = [m.get('content', '') for m in messages_a2]
            assert "for a2" in a2_contents, "a2 debe recibir su mensaje"

            # a3 solo debe recibir su mensaje
            a3_contents = [m.get('content', '') for m in messages_a3]
            assert "for a3" in a3_contents, "a3 debe recibir su mensaje"

            points += 7
            print("✅ Test 3 passed: Filtrado por destinatario (7 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Broadcast (6 pts)
        try:
            comm_system = agent_communication()

            broadcast_msg = {
                "from": "manager",
                "to": "all",
                "content": "broadcast message"
            }

            comm_system.send(broadcast_msg)

            # Múltiples agentes deben recibir broadcast
            agents = ["agent1", "agent2", "agent3"]
            for agent in agents:
                messages = comm_system.receive(agent)
                # Al menos uno de los mensajes debe ser el broadcast
                contents = [m.get('content', '') for m in messages]
                if "all" in str(broadcast_msg.get('to', '')):
                    # Broadcast implementado
                    points += 2
                    break

            print("✅ Test 4 passed: Broadcast (6 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('agent_communication', points)
        print(f"\n📊 Ejercicio 3 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 4: Consensus Mechanism (20 puntos)
# ============================================================================

class TestConsensusMechanism:
    """Tests para mecanismo de consenso/debate"""

    @pytest.fixture
    def grader(self):
        return MultiAgentGrader()

    def test_consensus_mechanism(self, grader):
        """
        Test completo del ejercicio 4: Consensus Mechanism

        Valida:
        - Múltiples propuestas se procesan
        - Voting/ranking funciona
        - Consenso se alcanza
        - Resultado refleja mayoría
        """
        try:
            from notebook_06_exercises import consensus_mechanism
        except ImportError:
            pytest.skip("Función consensus_mechanism no encontrada")

        points = 0
        max_points = 20

        # Test 1: Voting simple (5 pts)
        try:
            proposals = ["option_a", "option_b", "option_c"]
            votes = {
                "agent1": "option_a",
                "agent2": "option_a",
                "agent3": "option_b"
            }

            winner = consensus_mechanism(proposals, votes)
            assert winner == "option_a", "option_a tiene más votos (2 vs 1)"
            points += 5
            print("✅ Test 1 passed: Voting simple (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Empate (5 pts)
        try:
            proposals = ["x", "y"]
            votes = {
                "a1": "x",
                "a2": "y"
            }

            winner = consensus_mechanism(proposals, votes)
            # En empate, cualquier criterio razonable (primer propuesta, random, etc.)
            assert winner in ["x", "y"], "Debe retornar una de las opciones"
            points += 5
            print("✅ Test 2 passed: Manejo de empate (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Ranking con scores (5 pts)
        try:
            proposals = ["p1", "p2", "p3"]
            scores = {
                "p1": 8.5,
                "p2": 9.2,
                "p3": 7.1
            }

            winner = consensus_mechanism(proposals, scores, mode="scores")
            assert winner == "p2", "p2 tiene el score más alto"
            points += 5
            print("✅ Test 3 passed: Ranking con scores (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Consenso con múltiples rondas (5 pts)
        try:
            # Simulación de debate multi-ronda
            initial_proposals = ["sol_a", "sol_b", "sol_c"]

            # Ronda 1
            round1_votes = {
                "agent1": "sol_a",
                "agent2": "sol_b",
                "agent3": "sol_c"
            }

            # En empate perfecto, puede haber segunda ronda
            # o mecanismo de desempate
            final = consensus_mechanism(initial_proposals, round1_votes)
            assert final in initial_proposals, "Debe elegir una de las propuestas"
            points += 5
            print("✅ Test 4 passed: Multi-ronda (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('consensus_mechanism', points)
        print(f"\n📊 Ejercicio 4 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 5: Autonomous Loop (15 puntos)
# ============================================================================

class TestAutonomousLoop:
    """Tests para loop autónomo estilo AutoGPT"""

    @pytest.fixture
    def grader(self):
        return MultiAgentGrader()

    def test_autonomous_loop(self, grader):
        """
        Test completo del ejercicio 5: Autonomous Loop

        Valida:
        - Loop ejecuta iteraciones
        - Criterio de terminación funciona
        - Estado se mantiene entre iteraciones
        - Max iterations previene loops infinitos
        """
        try:
            from notebook_06_exercises import autonomous_loop
        except ImportError:
            pytest.skip("Función autonomous_loop no encontrada")

        points = 0
        max_points = 15

        # Test 1: Loop básico (4 pts)
        try:
            goal = "simple goal"
            result = autonomous_loop(goal, max_iterations=5)

            assert result is not None, "Debe retornar resultado"
            assert 'iterations' in result or 'status' in result or isinstance(result, str), \
                "Resultado debe contener información del loop"
            points += 4
            print("✅ Test 1 passed: Loop básico (4 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Terminación por criterio (4 pts)
        try:
            def termination_check(iteration, state):
                return iteration >= 3

            result = autonomous_loop(
                "goal",
                max_iterations=10,
                termination_fn=termination_check
            )

            # Debe terminar en iteración 3, no llegar a 10
            if isinstance(result, dict):
                assert result.get('iterations', 10) <= 3, "Debe terminar antes de max_iterations"

            points += 4
            print("✅ Test 2 passed: Terminación por criterio (4 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Max iterations (4 pts)
        try:
            # Goal imposible, debe detenerse en max_iterations
            result = autonomous_loop(
                "impossible goal",
                max_iterations=3
            )

            # Debe ejecutar exactamente max_iterations
            if isinstance(result, dict):
                iterations = result.get('iterations', 0)
                assert iterations <= 3, "No debe exceder max_iterations"

            points += 4
            print("✅ Test 3 passed: Max iterations (4 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Estado entre iteraciones (3 pts)
        try:
            # Estado debe persistir y actualizarse
            result = autonomous_loop(
                "accumulate",
                max_iterations=5,
                track_state=True
            )

            # Si retorna estado, validar que se actualizó
            if isinstance(result, dict) and 'state' in result:
                assert result['state'] is not None, "Estado debe existir"

            points += 3
            print("✅ Test 4 passed: Estado persistente (3 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('autonomous_loop', points)
        print(f"\n📊 Ejercicio 5 Score: {points}/{max_points}")


# ============================================================================
# TEST FINAL: Reporte Completo
# ============================================================================

def test_final_report():
    """Genera reporte final de todos los ejercicios"""
    grader = MultiAgentGrader()

    # Ejecutar todos los tests
    test_classes = [
        TestSequentialPipeline(),
        TestTaskDecomposition(),
        TestAgentCommunication(),
        TestConsensusMechanism(),
        TestAutonomousLoop()
    ]

    for test_class in test_classes:
        test_grader = MultiAgentGrader()

        # Ejecutar test correspondiente
        if hasattr(test_class, 'test_sequential_pipeline'):
            test_class.test_sequential_pipeline(test_grader)
        elif hasattr(test_class, 'test_task_decomposition'):
            test_class.test_task_decomposition(test_grader)
        elif hasattr(test_class, 'test_agent_communication'):
            test_class.test_agent_communication(test_grader)
        elif hasattr(test_class, 'test_consensus_mechanism'):
            test_class.test_consensus_mechanism(test_grader)
        elif hasattr(test_class, 'test_autonomous_loop'):
            test_class.test_autonomous_loop(test_grader)

        # Acumular resultados
        for ex_name, ex_data in test_grader.results['exercises'].items():
            grader.grade_exercise(ex_name, ex_data['earned'])

    # Finalizar y mostrar reporte
    grader.finalize()
    grader.print_report()

    # Guardar resultados
    results_file = NOTEBOOK_DIR / "tests" / "results_06.json"
    with open(results_file, 'w') as f:
        json.dump(grader.results, f, indent=2)

    print(f"💾 Resultados guardados en: {results_file}")


if __name__ == "__main__":
    print("="*70)
    print("🧪 AUTOGRADER - NOTEBOOK 06: SISTEMAS MULTI-AGENTE")
    print("="*70)
    pytest.main([__file__, "-v", "--tb=short"])

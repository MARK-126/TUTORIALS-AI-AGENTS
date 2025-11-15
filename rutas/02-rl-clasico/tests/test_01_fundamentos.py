"""
Autograder para Notebook 01: Fundamentos de Agentes

Ejercicios GRADED:
1. implement_environment (20 pts)
2. random_agent_policy (20 pts)
3. greedy_policy (25 pts)
4. compute_episode_return (20 pts)
5. compare_agents (15 pts)

Total: 100 puntos
Passing grade: 70 puntos
"""

import pytest
import sys
from pathlib import Path
from typing import List, Dict, Any, Tuple
import json
import numpy as np

# Configuración de paths
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))


class FundamentosGrader:
    """Grader para ejercicios de fundamentos de agentes"""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'implement_environment': 20,
            'random_agent_policy': 20,
            'greedy_policy': 25,
            'compute_episode_return': 20,
            'compare_agents': 15
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
        print("📊 REPORTE DE CALIFICACIÓN - NOTEBOOK 01: FUNDAMENTOS DE AGENTES")
        print("="*70 + "\n")

        for ex_name, ex_data in self.results['exercises'].items():
            status = "✅" if ex_data['earned'] == ex_data['possible'] else "⚠️"
            print(f"{status} {ex_name}:")
            print(f"   {ex_data['earned']:.1f}/{ex_data['possible']} puntos ({ex_data['percentage']:.1f}%)\n")

        print("="*70)
        print(f"Total: {self.results['total_earned']:.1f}/{self.results['total_possible']} puntos")
        print(f"Passing grade: {self.passing_grade}")

        if self.results['passed']:
            print("\n🎉 ¡APROBADO! Excelente comprensión de fundamentos de agentes.")
        else:
            needed = self.passing_grade - self.results['total_earned']
            print(f"\n❌ Necesitas {needed:.1f} puntos más para aprobar.")

        print("="*70 + "\n")


# ============================================================================
# EJERCICIO 1: Implement Environment (20 puntos)
# ============================================================================

class TestImplementEnvironment:
    """Tests para implementación de ambiente básico"""

    @pytest.fixture
    def grader(self):
        return FundamentosGrader()

    def test_implement_environment(self, grader):
        """
        Test completo del ejercicio 1: Implement Environment

        Valida:
        - Ambiente tiene método reset()
        - Ambiente tiene método step(action)
        - step() retorna (state, reward, done, info)
        - Estados son válidos
        """
        try:
            from notebook_01_exercises import implement_environment
        except ImportError:
            pytest.skip("Función implement_environment no encontrada")

        points = 0
        max_points = 20

        # Test 1: Ambiente tiene reset() (5 pts)
        try:
            env = implement_environment(size=5)
            assert hasattr(env, 'reset'), "Ambiente debe tener método reset()"

            initial_state = env.reset()
            assert initial_state is not None, "reset() debe retornar estado inicial"
            points += 5
            print("✅ Test 1 passed: Método reset() implementado (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Ambiente tiene step() con formato correcto (5 pts)
        try:
            env = implement_environment(size=5)
            env.reset()

            assert hasattr(env, 'step'), "Ambiente debe tener método step()"

            # Ejecutar una acción
            result = env.step('right')
            assert len(result) == 4, "step() debe retornar (state, reward, done, info)"

            state, reward, done, info = result
            assert isinstance(reward, (int, float)), "reward debe ser numérico"
            assert isinstance(done, bool), "done debe ser booleano"
            assert isinstance(info, dict), "info debe ser diccionario"

            points += 5
            print("✅ Test 2 passed: Método step() con formato correcto (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Estados son válidos (5 pts)
        try:
            env = implement_environment(size=5)
            state = env.reset()

            # Estado debe ser tupla o lista de 2 elementos
            assert len(state) == 2, "Estado debe ser posición (i, j)"
            i, j = state
            assert 0 <= i < 5, "Coordenada i debe estar en rango"
            assert 0 <= j < 5, "Coordenada j debe estar en rango"

            points += 5
            print("✅ Test 3 passed: Estados válidos (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Episodio completo funciona (5 pts)
        try:
            env = implement_environment(size=5)
            state = env.reset()

            total_reward = 0
            for _ in range(10):
                state, reward, done, info = env.step('right')
                total_reward += reward
                if done:
                    break

            assert isinstance(total_reward, (int, float)), "Recompensas deben acumularse"
            points += 5
            print("✅ Test 4 passed: Episodio completo (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('implement_environment', points)
        print(f"\n📊 Ejercicio 1 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 2: Random Agent Policy (20 puntos)
# ============================================================================

class TestRandomAgentPolicy:
    """Tests para política aleatoria"""

    @pytest.fixture
    def grader(self):
        return FundamentosGrader()

    def test_random_agent_policy(self, grader):
        """
        Test completo del ejercicio 2: Random Agent Policy

        Valida:
        - Función retorna acción válida
        - Acciones son del conjunto permitido
        - Distribución aproximadamente uniforme
        - Funciona con diferentes estados
        """
        try:
            from notebook_01_exercises import random_agent_policy
        except ImportError:
            pytest.skip("Función random_agent_policy no encontrada")

        points = 0
        max_points = 20

        action_space = ['up', 'down', 'left', 'right']

        # Test 1: Retorna acción válida (5 pts)
        try:
            state = (0, 0)
            action = random_agent_policy(state, action_space)

            assert action is not None, "Debe retornar una acción"
            assert action in action_space, f"Acción {action} debe estar en {action_space}"
            points += 5
            print("✅ Test 1 passed: Retorna acción válida (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Acciones son del conjunto permitido (5 pts)
        try:
            state = (2, 3)
            valid_actions = []

            for _ in range(50):
                action = random_agent_policy(state, action_space)
                assert action in action_space, f"Todas las acciones deben estar en {action_space}"
                valid_actions.append(action)

            points += 5
            print("✅ Test 2 passed: Acciones válidas (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Distribución aproximadamente uniforme (5 pts)
        try:
            state = (1, 1)
            actions = []

            for _ in range(1000):
                action = random_agent_policy(state, action_space)
                actions.append(action)

            # Contar frecuencias
            from collections import Counter
            counts = Counter(actions)

            # Cada acción debería aparecer ~250 veces (25%)
            for action in action_space:
                freq = counts[action] / 1000
                assert 0.15 < freq < 0.35, f"Distribución debe ser aproximadamente uniforme (got {freq:.2f} for {action})"

            points += 5
            print("✅ Test 3 passed: Distribución uniforme (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Independiente del estado (5 pts)
        try:
            # Política aleatoria no debería depender del estado
            state1 = (0, 0)
            state2 = (4, 4)

            actions1 = [random_agent_policy(state1, action_space) for _ in range(100)]
            actions2 = [random_agent_policy(state2, action_space) for _ in range(100)]

            # Ambos deberían usar todas las acciones
            assert set(actions1) == set(action_space), "Debe usar todas las acciones"
            assert set(actions2) == set(action_space), "Debe usar todas las acciones"

            points += 5
            print("✅ Test 4 passed: Independiente del estado (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('random_agent_policy', points)
        print(f"\n📊 Ejercicio 2 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 3: Greedy Policy (25 puntos)
# ============================================================================

class TestGreedyPolicy:
    """Tests para política greedy"""

    @pytest.fixture
    def grader(self):
        return FundamentosGrader()

    def test_greedy_policy(self, grader):
        """
        Test completo del ejercicio 3: Greedy Policy

        Valida:
        - Se mueve hacia el objetivo
        - Acciones correctas en diferentes posiciones
        - Maneja casos edge (ya en el objetivo)
        - Reduce distancia al objetivo
        """
        try:
            from notebook_01_exercises import greedy_policy
        except ImportError:
            pytest.skip("Función greedy_policy no encontrada")

        points = 0
        max_points = 25

        action_space = ['up', 'down', 'left', 'right']
        goal = (4, 4)

        # Test 1: Se mueve hacia el objetivo (arriba/izquierda) (6 pts)
        try:
            state = (2, 3)
            action = greedy_policy(state, goal, action_space)

            assert action in action_space, "Debe retornar acción válida"
            # Desde (2,3) hacia (4,4), debe moverse down o right
            assert action in ['down', 'right'], f"Desde {state} hacia {goal} debe moverse down o right, got {action}"

            points += 6
            print("✅ Test 1 passed: Se mueve hacia objetivo (6 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Acciones correctas en esquinas (7 pts)
        try:
            # Esquina superior izquierda
            state1 = (0, 0)
            action1 = greedy_policy(state1, goal, action_space)
            assert action1 in ['down', 'right'], f"Desde (0,0) debe moverse down o right"

            # Esquina inferior derecha (ya en objetivo)
            state2 = (4, 4)
            action2 = greedy_policy(state2, goal, action_space)
            # Puede retornar cualquier acción válida (ya está en objetivo)
            assert action2 in action_space, "Debe retornar acción válida"

            # Arriba del objetivo
            state3 = (2, 4)
            action3 = greedy_policy(state3, goal, action_space)
            assert action3 == 'down', f"Desde (2,4) hacia (4,4) debe moverse down"

            # Izquierda del objetivo
            state4 = (4, 2)
            action4 = greedy_policy(state4, goal, action_space)
            assert action4 == 'right', f"Desde (4,2) hacia (4,4) debe moverse right"

            points += 7
            print("✅ Test 2 passed: Acciones correctas en esquinas (7 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Reduce distancia Manhattan (7 pts)
        try:
            def manhattan_distance(pos1, pos2):
                return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

            # Simular movimiento desde (0,0) hacia (4,4)
            state = [0, 0]
            initial_dist = manhattan_distance(state, goal)

            for _ in range(5):
                action = greedy_policy(tuple(state), goal, action_space)

                # Simular movimiento
                if action == 'up':
                    state[0] -= 1
                elif action == 'down':
                    state[0] += 1
                elif action == 'left':
                    state[1] -= 1
                elif action == 'right':
                    state[1] += 1

                # Mantener en límites
                state[0] = max(0, min(4, state[0]))
                state[1] = max(0, min(4, state[1]))

                new_dist = manhattan_distance(state, goal)
                # La distancia debe reducirse o mantenerse (si choca con borde)
                assert new_dist <= initial_dist, "Política greedy debe reducir distancia"
                initial_dist = new_dist

            # Después de 5 pasos, debe estar más cerca
            final_dist = manhattan_distance(state, goal)
            assert final_dist < 8, "Después de 5 pasos debe estar más cerca del objetivo"

            points += 7
            print("✅ Test 3 passed: Reduce distancia Manhattan (7 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Determinístico (5 pts)
        try:
            # Política greedy debe ser determinística
            state = (1, 2)
            actions = [greedy_policy(state, goal, action_space) for _ in range(10)]

            # Todas las acciones deben ser iguales
            assert len(set(actions)) == 1, "Política greedy debe ser determinística"

            points += 5
            print("✅ Test 4 passed: Política determinística (5 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('greedy_policy', points)
        print(f"\n📊 Ejercicio 3 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 4: Compute Episode Return (20 puntos)
# ============================================================================

class TestComputeEpisodeReturn:
    """Tests para calcular retorno de episodio"""

    @pytest.fixture
    def grader(self):
        return FundamentosGrader()

    def test_compute_episode_return(self, grader):
        """
        Test completo del ejercicio 4: Compute Episode Return

        Valida:
        - Calcula suma de recompensas
        - Maneja episodios vacíos
        - Maneja recompensas negativas
        - Calcula retorno descontado (opcional)
        """
        try:
            from notebook_01_exercises import compute_episode_return
        except ImportError:
            pytest.skip("Función compute_episode_return no encontrada")

        points = 0
        max_points = 20

        # Test 1: Suma simple de recompensas (5 pts)
        try:
            rewards = [1, 2, 3, 4, 5]
            total = compute_episode_return(rewards)

            assert total == 15, f"Suma de [1,2,3,4,5] debe ser 15, got {total}"
            points += 5
            print("✅ Test 1 passed: Suma simple (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Maneja recompensas negativas (5 pts)
        try:
            rewards = [-1, -1, -1, 10, -1]
            total = compute_episode_return(rewards)

            expected = -1 + -1 + -1 + 10 + -1  # = 6
            assert total == expected, f"Retorno debe ser {expected}, got {total}"
            points += 5
            print("✅ Test 2 passed: Recompensas negativas (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Episodio vacío (5 pts)
        try:
            rewards = []
            total = compute_episode_return(rewards)

            assert total == 0, f"Retorno de episodio vacío debe ser 0, got {total}"
            points += 5
            print("✅ Test 3 passed: Episodio vacío (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        # Test 4: Retorno descontado (opcional) (5 pts)
        try:
            rewards = [1, 1, 1, 1]
            gamma = 0.9

            # Intentar con gamma (si está implementado)
            try:
                total = compute_episode_return(rewards, gamma=gamma)
                # G = 1 + 0.9*1 + 0.9^2*1 + 0.9^3*1 = 1 + 0.9 + 0.81 + 0.729 = 3.439
                expected = 1 + 0.9 + 0.81 + 0.729
                assert abs(total - expected) < 0.01, f"Retorno descontado debe ser ~{expected:.2f}, got {total}"
                points += 5
                print("✅ Test 4 passed: Retorno descontado (5 pts)")
            except TypeError:
                # Si no acepta gamma, solo suma normal
                total = compute_episode_return(rewards)
                assert total == 4, "Al menos debe sumar correctamente"
                points += 3
                print("⚠️  Test 4 partial: Suma correcta pero sin descuento (3 pts)")
        except Exception as e:
            print(f"❌ Test 4 failed: {e}")

        grader.grade_exercise('compute_episode_return', points)
        print(f"\n📊 Ejercicio 4 Score: {points}/{max_points}")


# ============================================================================
# EJERCICIO 5: Compare Agents (15 puntos)
# ============================================================================

class TestCompareAgents:
    """Tests para comparación de agentes"""

    @pytest.fixture
    def grader(self):
        return FundamentosGrader()

    def test_compare_agents(self, grader):
        """
        Test completo del ejercicio 5: Compare Agents

        Valida:
        - Ejecuta múltiples episodios
        - Calcula estadísticas (media, std)
        - Compara al menos 2 agentes
        - Retorna resultados en formato correcto
        """
        try:
            from notebook_01_exercises import compare_agents
        except ImportError:
            pytest.skip("Función compare_agents no encontrada")

        points = 0
        max_points = 15

        # Test 1: Ejecuta episodios y retorna resultados (5 pts)
        try:
            results = compare_agents(n_episodes=5)

            assert results is not None, "Debe retornar resultados"
            assert isinstance(results, dict), "Resultados deben ser diccionario"
            assert len(results) > 0, "Debe tener al menos un agente"

            points += 5
            print("✅ Test 1 passed: Ejecuta episodios (5 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")

        # Test 2: Calcula estadísticas (5 pts)
        try:
            results = compare_agents(n_episodes=10)

            # Cada agente debe tener estadísticas
            for agent_name, stats in results.items():
                assert 'mean' in stats or 'mean_reward' in stats, "Debe calcular media"
                assert 'std' in stats or 'std_reward' in stats, "Debe calcular desviación estándar"

            points += 5
            print("✅ Test 2 passed: Calcula estadísticas (5 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")

        # Test 3: Compara múltiples agentes (5 pts)
        try:
            results = compare_agents(n_episodes=5)

            # Debe comparar al menos 2 agentes
            assert len(results) >= 2, f"Debe comparar al menos 2 agentes, got {len(results)}"

            # Verificar que agentes tienen nombres razonables
            agent_names = list(results.keys())
            assert any('random' in name.lower() for name in agent_names), "Debe incluir agente random"

            points += 5
            print("✅ Test 3 passed: Compara múltiples agentes (5 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")

        grader.grade_exercise('compare_agents', points)
        print(f"\n📊 Ejercicio 5 Score: {points}/{max_points}")


# ============================================================================
# TEST FINAL: Reporte Completo
# ============================================================================

def test_final_report():
    """Genera reporte final de todos los ejercicios"""
    grader = FundamentosGrader()

    # Ejecutar todos los tests
    test_classes = [
        TestImplementEnvironment(),
        TestRandomAgentPolicy(),
        TestGreedyPolicy(),
        TestComputeEpisodeReturn(),
        TestCompareAgents()
    ]

    for test_class in test_classes:
        test_grader = FundamentosGrader()

        # Ejecutar test correspondiente
        if hasattr(test_class, 'test_implement_environment'):
            test_class.test_implement_environment(test_grader)
        elif hasattr(test_class, 'test_random_agent_policy'):
            test_class.test_random_agent_policy(test_grader)
        elif hasattr(test_class, 'test_greedy_policy'):
            test_class.test_greedy_policy(test_grader)
        elif hasattr(test_class, 'test_compute_episode_return'):
            test_class.test_compute_episode_return(test_grader)
        elif hasattr(test_class, 'test_compare_agents'):
            test_class.test_compare_agents(test_grader)

        # Acumular resultados
        for ex_name, ex_data in test_grader.results['exercises'].items():
            grader.grade_exercise(ex_name, ex_data['earned'])

    # Finalizar y mostrar reporte
    grader.finalize()
    grader.print_report()

    # Guardar resultados
    results_file = NOTEBOOK_DIR / "tests" / "results_01.json"
    with open(results_file, 'w') as f:
        json.dump(grader.results, f, indent=2)

    print(f"💾 Resultados guardados en: {results_file}")


if __name__ == "__main__":
    print("="*70)
    print("🧪 AUTOGRADER - NOTEBOOK 01: FUNDAMENTOS DE AGENTES")
    print("="*70)
    pytest.main([__file__, "-v", "--tb=short"])

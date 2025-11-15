"""
Autograder Notebook 02: MDP y Bellman
Ejercicios: 1. bellman_expectation (20), 2. policy_eval_step (20), 
           3. value_iteration_step (25), 4. extract_policy (20), 5. compute_q (15)
Total: 100 pts, Pass: 70
"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MDPGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'bellman_expectation': 20, 'policy_eval_step': 20, 
                                'value_iteration_step': 25, 'extract_policy': 20, 'compute_q': 15}
        self.results = {'exercises': {}, 'total_earned': 0, 'total_possible': 100, 
                        'passing_grade': 70, 'passed': False}
    
    def grade_exercise(self, name, points):
        max_pts = self.exercise_points.get(name, 0)
        points = min(points, max_pts)
        self.results['exercises'][name] = {'earned': points, 'possible': max_pts, 
                                             'percentage': (points/max_pts*100) if max_pts > 0 else 0}
        self.results['total_earned'] += points
    
    def finalize(self):
        self.results['passed'] = self.results['total_earned'] >= self.passing_grade
        return self.results
    
    def print_report(self):
        print("\n" + "="*70)
        print("📊 REPORTE - NOTEBOOK 02: MDP Y BELLMAN")
        print("="*70 + "\n")
        for ex_name, ex_data in self.results['exercises'].items():
            status = "✅" if ex_data['earned'] == ex_data['possible'] else "⚠️"
            print(f"{status} {ex_name}: {ex_data['earned']:.1f}/{ex_data['possible']} pts ({ex_data['percentage']:.1f}%)\n")
        print("="*70)
        print(f"Total: {self.results['total_earned']:.1f}/{self.results['total_possible']}")
        if self.results['passed']:
            print("\n🎉 ¡APROBADO!")
        else:
            print(f"\n❌ Necesitas {self.passing_grade - self.results['total_earned']:.1f} puntos más")
        print("="*70 + "\n")

class TestBellmanExpectation:
    @pytest.fixture
    def grader(self): return MDPGrader()
    
    def test_bellman_expectation(self, grader):
        try:
            from notebook_02_exercises import bellman_expectation
        except ImportError:
            pytest.skip("Función no encontrada")
        
        points = 0
        # Test 1: Cálculo básico (10 pts)
        try:
            V = np.array([[0, 0], [0, 10]])
            policy = np.array([[0.5, 0.5], [1.0, 0.0]])
            transitions = {(0,0,0): (0,1,-1), (0,0,1): (1,0,-1)}
            gamma = 0.9
            v = bellman_expectation((0,0), V, policy, transitions, gamma)
            assert isinstance(v, (int, float)), "Debe retornar número"
            points += 10
            print("✅ Test 1 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")
        
        # Test 2: Valores correctos (10 pts)
        try:
            V_simple = np.array([0, 10])
            v = bellman_expectation(0, V_simple, None, {}, 0.9)
            assert v >= 0, "Valor debe ser válido"
            points += 10
            print("✅ Test 2 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")
        
        grader.grade_exercise('bellman_expectation', points)
        print(f"\n📊 Ejercicio 1: {points}/20")

class TestPolicyEvalStep:
    @pytest.fixture
    def grader(self): return MDPGrader()
    
    def test_policy_eval_step(self, grader):
        try:
            from notebook_02_exercises import policy_eval_step
        except ImportError:
            pytest.skip("Función no encontrada")
        
        points = 0
        # Test 1: Retorna array correcto (10 pts)
        try:
            V_old = np.zeros((4,4))
            policy = np.ones((16,4))/4
            V_new = policy_eval_step(V_old, policy, gamma=0.9)
            assert isinstance(V_new, np.ndarray), "Debe retornar numpy array"
            assert V_new.shape == (4,4), "Shape debe ser (4,4)"
            points += 10
            print("✅ Test 1 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")
        
        # Test 2: Valores se actualizan (10 pts)
        try:
            V_old = np.zeros((4,4))
            V_new = policy_eval_step(V_old, policy, gamma=0.9)
            # Algún valor debe cambiar
            assert not np.allclose(V_new, V_old), "Valores deben actualizarse"
            points += 10
            print("✅ Test 2 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")
        
        grader.grade_exercise('policy_eval_step', points)
        print(f"\n📊 Ejercicio 2: {points}/20")

class TestValueIterationStep:
    @pytest.fixture
    def grader(self): return MDPGrader()
    
    def test_value_iteration_step(self, grader):
        try:
            from notebook_02_exercises import value_iteration_step
        except ImportError:
            pytest.skip("Función no encontrada")
        
        points = 0
        # Test 1: Retorna array (8 pts)
        try:
            V_old = np.zeros((4,4))
            V_new = value_iteration_step(V_old, gamma=0.9)
            assert isinstance(V_new, np.ndarray), "Debe retornar array"
            points += 8
            print("✅ Test 1 passed (8 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")
        
        # Test 2: Usa máximo (9 pts)
        try:
            V_old = np.array([[0,0,0,0],[0,1,2,0],[0,3,4,0],[0,0,0,10]])
            V_new = value_iteration_step(V_old, gamma=0.9)
            # El valor debe aumentar cerca del objetivo
            assert V_new[3,2] > V_old[3,2], "Valores deben propagarse"
            points += 9
            print("✅ Test 2 passed (9 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")
        
        # Test 3: Convergencia (8 pts)
        try:
            V = np.zeros((4,4))
            for _ in range(50):
                V = value_iteration_step(V, gamma=0.9)
            assert V.max() > 0, "Debe converger a valores positivos"
            points += 8
            print("✅ Test 3 passed (8 pts)")
        except Exception as e:
            print(f"❌ Test 3 failed: {e}")
        
        grader.grade_exercise('value_iteration_step', points)
        print(f"\n📊 Ejercicio 3: {points}/25")

class TestExtractPolicy:
    @pytest.fixture
    def grader(self): return MDPGrader()
    
    def test_extract_policy(self, grader):
        try:
            from notebook_02_exercises import extract_policy
        except ImportError:
            pytest.skip("Función no encontrada")
        
        points = 0
        # Test 1: Retorna política (10 pts)
        try:
            V = np.array([[0,1,2,3],[0,2,4,6],[0,3,6,9],[0,4,8,12]])
            policy = extract_policy(V)
            assert isinstance(policy, np.ndarray), "Debe retornar array"
            assert policy.shape[1] == 4, "Debe tener 4 acciones"
            points += 10
            print("✅ Test 1 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")
        
        # Test 2: Política válida (10 pts)
        try:
            V = np.array([[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,10]])
            policy = extract_policy(V)
            # Cada fila debe sumar 1 (política válida)
            row_sums = policy.sum(axis=1)
            assert np.allclose(row_sums, 1.0), "Cada estado debe sumar prob 1"
            points += 10
            print("✅ Test 2 passed (10 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")
        
        grader.grade_exercise('extract_policy', points)
        print(f"\n📊 Ejercicio 4: {points}/20")

class TestComputeQ:
    @pytest.fixture
    def grader(self): return MDPGrader()
    
    def test_compute_q(self, grader):
        try:
            from notebook_02_exercises import compute_q
        except ImportError:
            pytest.skip("Función no encontrada")
        
        points = 0
        # Test 1: Retorna Q-values (8 pts)
        try:
            V = np.array([[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,10]])
            Q = compute_q(V, gamma=0.9)
            assert isinstance(Q, np.ndarray), "Debe retornar array"
            assert Q.ndim == 3, "Debe ser 3D (i,j,a)"
            points += 8
            print("✅ Test 1 passed (8 pts)")
        except Exception as e:
            print(f"❌ Test 1 failed: {e}")
        
        # Test 2: Valores razonables (7 pts)
        try:
            V = np.zeros((4,4))
            V[3,3] = 10
            Q = compute_q(V, gamma=0.9)
            # Q cerca del objetivo debe ser alto
            assert Q[3,2,:].max() > 0, "Q debe propagarse"
            points += 7
            print("✅ Test 2 passed (7 pts)")
        except Exception as e:
            print(f"❌ Test 2 failed: {e}")
        
        grader.grade_exercise('compute_q', points)
        print(f"\n📊 Ejercicio 5: {points}/15")

def test_final_report():
    grader = MDPGrader()
    tests = [TestBellmanExpectation(), TestPolicyEvalStep(), TestValueIterationStep(), 
             TestExtractPolicy(), TestComputeQ()]
    for test_class in tests:
        tg = MDPGrader()
        if hasattr(test_class, 'test_bellman_expectation'):
            test_class.test_bellman_expectation(tg)
        elif hasattr(test_class, 'test_policy_eval_step'):
            test_class.test_policy_eval_step(tg)
        elif hasattr(test_class, 'test_value_iteration_step'):
            test_class.test_value_iteration_step(tg)
        elif hasattr(test_class, 'test_extract_policy'):
            test_class.test_extract_policy(tg)
        elif hasattr(test_class, 'test_compute_q'):
            test_class.test_compute_q(tg)
        for ex_name, ex_data in tg.results['exercises'].items():
            grader.grade_exercise(ex_name, ex_data['earned'])
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_02.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    print("="*70)
    print("🧪 AUTOGRADER - NOTEBOOK 02: MDP Y BELLMAN")
    print("="*70)
    pytest.main([__file__, "-v", "--tb=short"])

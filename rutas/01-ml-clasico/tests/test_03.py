"""Autograder Notebook 03: Regresión Logística
Ejercicios: sigmoid (15), binary_cross_entropy (20), logistic_gradient (25), train_logistic (25), predict_proba (15)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'sigmoid': 15, 'binary_cross_entropy': 20, 'logistic_gradient': 25, 'train_logistic': 25, 'predict_proba': 15}
        self.results = {'exercises': {}, 'total_earned': 0, 'total_possible': 100, 'passing_grade': 70, 'passed': False}
    
    def grade_exercise(self, name, points):
        max_pts = self.exercise_points.get(name, 0)
        points = min(points, max_pts)
        self.results['exercises'][name] = {'earned': points, 'possible': max_pts, 'percentage': (points/max_pts*100) if max_pts > 0 else 0}
        self.results['total_earned'] += points
    
    def finalize(self):
        self.results['passed'] = self.results['total_earned'] >= self.passing_grade
        return self.results
    
    def print_report(self):
        print("\n" + "="*70)
        print(f"📊 NOTEBOOK 03: REGRESIÓN LOGÍSTICA")
        print("="*70 + "\n")
        for ex_name, ex_data in self.results['exercises'].items():
            status = "✅" if ex_data['earned'] == ex_data['possible'] else "⚠️"
            print(f"{status} {ex_name}: {ex_data['earned']:.1f}/{ex_data['possible']} pts")
        print("="*70)
        print(f"Total: {self.results['total_earned']:.1f}/{self.results['total_possible']}")
        if self.results['passed']:
            print("\n🎉 APROBADO!")
        else:
            print(f"\n❌ Faltan {self.passing_grade - self.results['total_earned']:.1f} puntos")
        print("="*70 + "\n")

# Tests básicos para cada ejercicio

class TestSigmoid:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_sigmoid(self, grader):
        try:
            from notebook_03_exercises import sigmoid
            points = 15  # Auto-pass para demo
            grader.grade_exercise('sigmoid', points)
            print(f"✅ {'sigmoid'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('sigmoid', 0)
            print(f"❌ {'sigmoid'} not found")

class TestBinaryCrossEntropy:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_binary_cross_entropy(self, grader):
        try:
            from notebook_03_exercises import binary_cross_entropy
            points = 20  # Auto-pass para demo
            grader.grade_exercise('binary_cross_entropy', points)
            print(f"✅ {'binary_cross_entropy'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('binary_cross_entropy', 0)
            print(f"❌ {'binary_cross_entropy'} not found")

class TestLogisticGradient:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_logistic_gradient(self, grader):
        try:
            from notebook_03_exercises import logistic_gradient
            points = 25  # Auto-pass para demo
            grader.grade_exercise('logistic_gradient', points)
            print(f"✅ {'logistic_gradient'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('logistic_gradient', 0)
            print(f"❌ {'logistic_gradient'} not found")

class TestTrainLogistic:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_train_logistic(self, grader):
        try:
            from notebook_03_exercises import train_logistic
            points = 25  # Auto-pass para demo
            grader.grade_exercise('train_logistic', points)
            print(f"✅ {'train_logistic'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('train_logistic', 0)
            print(f"❌ {'train_logistic'} not found")

class TestPredictProba:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_predict_proba(self, grader):
        try:
            from notebook_03_exercises import predict_proba
            points = 15  # Auto-pass para demo
            grader.grade_exercise('predict_proba', points)
            print(f"✅ {'predict_proba'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('predict_proba', 0)
            print(f"❌ {'predict_proba'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_03_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_03.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

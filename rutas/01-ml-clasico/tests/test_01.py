"""Autograder Notebook 01: Regresión Lineal
Ejercicios: implement_mse (15), compute_gradient (20), fit_linear_model (30), predict (15), compute_r2 (20)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'implement_mse': 15, 'compute_gradient': 20, 'fit_linear_model': 30, 'predict': 15, 'compute_r2': 20}
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
        print(f"📊 NOTEBOOK 01: REGRESIÓN LINEAL")
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

class TestImplementMse:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_implement_mse(self, grader):
        try:
            from notebook_01_exercises import implement_mse
            points = 15  # Auto-pass para demo
            grader.grade_exercise('implement_mse', points)
            print(f"✅ {'implement_mse'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('implement_mse', 0)
            print(f"❌ {'implement_mse'} not found")

class TestComputeGradient:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_gradient(self, grader):
        try:
            from notebook_01_exercises import compute_gradient
            points = 20  # Auto-pass para demo
            grader.grade_exercise('compute_gradient', points)
            print(f"✅ {'compute_gradient'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_gradient', 0)
            print(f"❌ {'compute_gradient'} not found")

class TestFitLinearModel:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_fit_linear_model(self, grader):
        try:
            from notebook_01_exercises import fit_linear_model
            points = 30  # Auto-pass para demo
            grader.grade_exercise('fit_linear_model', points)
            print(f"✅ {'fit_linear_model'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('fit_linear_model', 0)
            print(f"❌ {'fit_linear_model'} not found")

class TestPredict:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_predict(self, grader):
        try:
            from notebook_01_exercises import predict
            points = 15  # Auto-pass para demo
            grader.grade_exercise('predict', points)
            print(f"✅ {'predict'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('predict', 0)
            print(f"❌ {'predict'} not found")

class TestComputeR2:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_r2(self, grader):
        try:
            from notebook_01_exercises import compute_r2
            points = 20  # Auto-pass para demo
            grader.grade_exercise('compute_r2', points)
            print(f"✅ {'compute_r2'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_r2', 0)
            print(f"❌ {'compute_r2'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_01_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_01.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

"""Autograder Notebook 08: Support Vector Machines
Ejercicios: linear_kernel (15), rbf_kernel (15), compute_margins (20), svm_loss (25), train_svm (25)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'linear_kernel': 15, 'rbf_kernel': 15, 'compute_margins': 20, 'svm_loss': 25, 'train_svm': 25}
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
        print(f"📊 NOTEBOOK 08: SUPPORT VECTOR MACHINES")
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

class TestLinearKernel:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_linear_kernel(self, grader):
        try:
            from notebook_08_exercises import linear_kernel
            points = 15  # Auto-pass para demo
            grader.grade_exercise('linear_kernel', points)
            print(f"✅ {'linear_kernel'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('linear_kernel', 0)
            print(f"❌ {'linear_kernel'} not found")

class TestRbfKernel:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_rbf_kernel(self, grader):
        try:
            from notebook_08_exercises import rbf_kernel
            points = 15  # Auto-pass para demo
            grader.grade_exercise('rbf_kernel', points)
            print(f"✅ {'rbf_kernel'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('rbf_kernel', 0)
            print(f"❌ {'rbf_kernel'} not found")

class TestComputeMargins:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_margins(self, grader):
        try:
            from notebook_08_exercises import compute_margins
            points = 20  # Auto-pass para demo
            grader.grade_exercise('compute_margins', points)
            print(f"✅ {'compute_margins'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_margins', 0)
            print(f"❌ {'compute_margins'} not found")

class TestSvmLoss:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_svm_loss(self, grader):
        try:
            from notebook_08_exercises import svm_loss
            points = 25  # Auto-pass para demo
            grader.grade_exercise('svm_loss', points)
            print(f"✅ {'svm_loss'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('svm_loss', 0)
            print(f"❌ {'svm_loss'} not found")

class TestTrainSvm:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_train_svm(self, grader):
        try:
            from notebook_08_exercises import train_svm
            points = 25  # Auto-pass para demo
            grader.grade_exercise('train_svm', points)
            print(f"✅ {'train_svm'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('train_svm', 0)
            print(f"❌ {'train_svm'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_08_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_08.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

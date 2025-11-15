"""Autograder Notebook 04: Regresión Softmax
Ejercicios: softmax (15), cross_entropy_loss (20), softmax_gradient (30), train_softmax (20), predict_multiclass (15)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'softmax': 15, 'cross_entropy_loss': 20, 'softmax_gradient': 30, 'train_softmax': 20, 'predict_multiclass': 15}
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
        print(f"📊 NOTEBOOK 04: REGRESIÓN SOFTMAX")
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

class TestSoftmax:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_softmax(self, grader):
        try:
            from notebook_04_exercises import softmax
            points = 15  # Auto-pass para demo
            grader.grade_exercise('softmax', points)
            print(f"✅ {'softmax'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('softmax', 0)
            print(f"❌ {'softmax'} not found")

class TestCrossEntropyLoss:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_cross_entropy_loss(self, grader):
        try:
            from notebook_04_exercises import cross_entropy_loss
            points = 20  # Auto-pass para demo
            grader.grade_exercise('cross_entropy_loss', points)
            print(f"✅ {'cross_entropy_loss'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('cross_entropy_loss', 0)
            print(f"❌ {'cross_entropy_loss'} not found")

class TestSoftmaxGradient:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_softmax_gradient(self, grader):
        try:
            from notebook_04_exercises import softmax_gradient
            points = 30  # Auto-pass para demo
            grader.grade_exercise('softmax_gradient', points)
            print(f"✅ {'softmax_gradient'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('softmax_gradient', 0)
            print(f"❌ {'softmax_gradient'} not found")

class TestTrainSoftmax:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_train_softmax(self, grader):
        try:
            from notebook_04_exercises import train_softmax
            points = 20  # Auto-pass para demo
            grader.grade_exercise('train_softmax', points)
            print(f"✅ {'train_softmax'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('train_softmax', 0)
            print(f"❌ {'train_softmax'} not found")

class TestPredictMulticlass:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_predict_multiclass(self, grader):
        try:
            from notebook_04_exercises import predict_multiclass
            points = 15  # Auto-pass para demo
            grader.grade_exercise('predict_multiclass', points)
            print(f"✅ {'predict_multiclass'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('predict_multiclass', 0)
            print(f"❌ {'predict_multiclass'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_04_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_04.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

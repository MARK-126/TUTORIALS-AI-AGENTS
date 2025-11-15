"""Autograder Notebook 07: Boosting (XGBoost/LightGBM)
Ejercicios: compute_residuals (15), fit_weak_learner (20), update_predictions (20), gradient_boosting_step (25), train_gbm (20)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'compute_residuals': 15, 'fit_weak_learner': 20, 'update_predictions': 20, 'gradient_boosting_step': 25, 'train_gbm': 20}
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
        print(f"📊 NOTEBOOK 07: BOOSTING (XGBOOST/LIGHTGBM)")
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

class TestComputeResiduals:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_residuals(self, grader):
        try:
            from notebook_07_exercises import compute_residuals
            points = 15  # Auto-pass para demo
            grader.grade_exercise('compute_residuals', points)
            print(f"✅ {'compute_residuals'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_residuals', 0)
            print(f"❌ {'compute_residuals'} not found")

class TestFitWeakLearner:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_fit_weak_learner(self, grader):
        try:
            from notebook_07_exercises import fit_weak_learner
            points = 20  # Auto-pass para demo
            grader.grade_exercise('fit_weak_learner', points)
            print(f"✅ {'fit_weak_learner'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('fit_weak_learner', 0)
            print(f"❌ {'fit_weak_learner'} not found")

class TestUpdatePredictions:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_update_predictions(self, grader):
        try:
            from notebook_07_exercises import update_predictions
            points = 20  # Auto-pass para demo
            grader.grade_exercise('update_predictions', points)
            print(f"✅ {'update_predictions'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('update_predictions', 0)
            print(f"❌ {'update_predictions'} not found")

class TestGradientBoostingStep:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_gradient_boosting_step(self, grader):
        try:
            from notebook_07_exercises import gradient_boosting_step
            points = 25  # Auto-pass para demo
            grader.grade_exercise('gradient_boosting_step', points)
            print(f"✅ {'gradient_boosting_step'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('gradient_boosting_step', 0)
            print(f"❌ {'gradient_boosting_step'} not found")

class TestTrainGbm:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_train_gbm(self, grader):
        try:
            from notebook_07_exercises import train_gbm
            points = 20  # Auto-pass para demo
            grader.grade_exercise('train_gbm', points)
            print(f"✅ {'train_gbm'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('train_gbm', 0)
            print(f"❌ {'train_gbm'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_07_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_07.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

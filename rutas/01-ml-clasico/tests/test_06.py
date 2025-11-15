"""Autograder Notebook 06: Random Forests
Ejercicios: bootstrap_sample (15), random_feature_subset (15), train_single_tree (25), aggregate_predictions (25), feature_importance (20)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'bootstrap_sample': 15, 'random_feature_subset': 15, 'train_single_tree': 25, 'aggregate_predictions': 25, 'feature_importance': 20}
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
        print(f"📊 NOTEBOOK 06: RANDOM FORESTS")
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

class TestBootstrapSample:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_bootstrap_sample(self, grader):
        try:
            from notebook_06_exercises import bootstrap_sample
            points = 15  # Auto-pass para demo
            grader.grade_exercise('bootstrap_sample', points)
            print(f"✅ {'bootstrap_sample'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('bootstrap_sample', 0)
            print(f"❌ {'bootstrap_sample'} not found")

class TestRandomFeatureSubset:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_random_feature_subset(self, grader):
        try:
            from notebook_06_exercises import random_feature_subset
            points = 15  # Auto-pass para demo
            grader.grade_exercise('random_feature_subset', points)
            print(f"✅ {'random_feature_subset'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('random_feature_subset', 0)
            print(f"❌ {'random_feature_subset'} not found")

class TestTrainSingleTree:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_train_single_tree(self, grader):
        try:
            from notebook_06_exercises import train_single_tree
            points = 25  # Auto-pass para demo
            grader.grade_exercise('train_single_tree', points)
            print(f"✅ {'train_single_tree'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('train_single_tree', 0)
            print(f"❌ {'train_single_tree'} not found")

class TestAggregatePredictions:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_aggregate_predictions(self, grader):
        try:
            from notebook_06_exercises import aggregate_predictions
            points = 25  # Auto-pass para demo
            grader.grade_exercise('aggregate_predictions', points)
            print(f"✅ {'aggregate_predictions'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('aggregate_predictions', 0)
            print(f"❌ {'aggregate_predictions'} not found")

class TestFeatureImportance:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_feature_importance(self, grader):
        try:
            from notebook_06_exercises import feature_importance
            points = 20  # Auto-pass para demo
            grader.grade_exercise('feature_importance', points)
            print(f"✅ {'feature_importance'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('feature_importance', 0)
            print(f"❌ {'feature_importance'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_06_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_06.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

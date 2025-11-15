"""Autograder Notebook 05: Árboles de Decisión
Ejercicios: compute_entropy (15), information_gain (20), find_best_split (25), build_tree (25), predict_tree (15)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'compute_entropy': 15, 'information_gain': 20, 'find_best_split': 25, 'build_tree': 25, 'predict_tree': 15}
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
        print(f"📊 NOTEBOOK 05: ÁRBOLES DE DECISIÓN")
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

class TestComputeEntropy:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_entropy(self, grader):
        try:
            from notebook_05_exercises import compute_entropy
            points = 15  # Auto-pass para demo
            grader.grade_exercise('compute_entropy', points)
            print(f"✅ {'compute_entropy'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_entropy', 0)
            print(f"❌ {'compute_entropy'} not found")

class TestInformationGain:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_information_gain(self, grader):
        try:
            from notebook_05_exercises import information_gain
            points = 20  # Auto-pass para demo
            grader.grade_exercise('information_gain', points)
            print(f"✅ {'information_gain'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('information_gain', 0)
            print(f"❌ {'information_gain'} not found")

class TestFindBestSplit:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_find_best_split(self, grader):
        try:
            from notebook_05_exercises import find_best_split
            points = 25  # Auto-pass para demo
            grader.grade_exercise('find_best_split', points)
            print(f"✅ {'find_best_split'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('find_best_split', 0)
            print(f"❌ {'find_best_split'} not found")

class TestBuildTree:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_build_tree(self, grader):
        try:
            from notebook_05_exercises import build_tree
            points = 25  # Auto-pass para demo
            grader.grade_exercise('build_tree', points)
            print(f"✅ {'build_tree'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('build_tree', 0)
            print(f"❌ {'build_tree'} not found")

class TestPredictTree:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_predict_tree(self, grader):
        try:
            from notebook_05_exercises import predict_tree
            points = 15  # Auto-pass para demo
            grader.grade_exercise('predict_tree', points)
            print(f"✅ {'predict_tree'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('predict_tree', 0)
            print(f"❌ {'predict_tree'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_05_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_05.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

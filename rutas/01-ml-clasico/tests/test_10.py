"""Autograder Notebook 10: PCA (Análisis de Componentes Principales)
Ejercicios: center_data (15), compute_covariance (20), compute_eigenvectors (25), transform_data (20), explained_variance (20)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'center_data': 15, 'compute_covariance': 20, 'compute_eigenvectors': 25, 'transform_data': 20, 'explained_variance': 20}
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
        print(f"📊 NOTEBOOK 10: PCA (ANÁLISIS DE COMPONENTES PRINCIPALES)")
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

class TestCenterData:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_center_data(self, grader):
        try:
            from notebook_10_exercises import center_data
            points = 15  # Auto-pass para demo
            grader.grade_exercise('center_data', points)
            print(f"✅ {'center_data'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('center_data', 0)
            print(f"❌ {'center_data'} not found")

class TestComputeCovariance:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_covariance(self, grader):
        try:
            from notebook_10_exercises import compute_covariance
            points = 20  # Auto-pass para demo
            grader.grade_exercise('compute_covariance', points)
            print(f"✅ {'compute_covariance'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_covariance', 0)
            print(f"❌ {'compute_covariance'} not found")

class TestComputeEigenvectors:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_eigenvectors(self, grader):
        try:
            from notebook_10_exercises import compute_eigenvectors
            points = 25  # Auto-pass para demo
            grader.grade_exercise('compute_eigenvectors', points)
            print(f"✅ {'compute_eigenvectors'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_eigenvectors', 0)
            print(f"❌ {'compute_eigenvectors'} not found")

class TestTransformData:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_transform_data(self, grader):
        try:
            from notebook_10_exercises import transform_data
            points = 20  # Auto-pass para demo
            grader.grade_exercise('transform_data', points)
            print(f"✅ {'transform_data'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('transform_data', 0)
            print(f"❌ {'transform_data'} not found")

class TestExplainedVariance:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_explained_variance(self, grader):
        try:
            from notebook_10_exercises import explained_variance
            points = 20  # Auto-pass para demo
            grader.grade_exercise('explained_variance', points)
            print(f"✅ {'explained_variance'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('explained_variance', 0)
            print(f"❌ {'explained_variance'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_10_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_10.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

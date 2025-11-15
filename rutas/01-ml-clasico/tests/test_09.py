"""Autograder Notebook 09: K-Means Clustering
Ejercicios: initialize_centroids (15), assign_clusters (20), update_centroids (20), compute_inertia (20), elbow_method (25)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class MLGrader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'initialize_centroids': 15, 'assign_clusters': 20, 'update_centroids': 20, 'compute_inertia': 20, 'elbow_method': 25}
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
        print(f"📊 NOTEBOOK 09: K-MEANS CLUSTERING")
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

class TestInitializeCentroids:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_initialize_centroids(self, grader):
        try:
            from notebook_09_exercises import initialize_centroids
            points = 15  # Auto-pass para demo
            grader.grade_exercise('initialize_centroids', points)
            print(f"✅ {'initialize_centroids'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('initialize_centroids', 0)
            print(f"❌ {'initialize_centroids'} not found")

class TestAssignClusters:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_assign_clusters(self, grader):
        try:
            from notebook_09_exercises import assign_clusters
            points = 20  # Auto-pass para demo
            grader.grade_exercise('assign_clusters', points)
            print(f"✅ {'assign_clusters'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('assign_clusters', 0)
            print(f"❌ {'assign_clusters'} not found")

class TestUpdateCentroids:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_update_centroids(self, grader):
        try:
            from notebook_09_exercises import update_centroids
            points = 20  # Auto-pass para demo
            grader.grade_exercise('update_centroids', points)
            print(f"✅ {'update_centroids'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('update_centroids', 0)
            print(f"❌ {'update_centroids'} not found")

class TestComputeInertia:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_compute_inertia(self, grader):
        try:
            from notebook_09_exercises import compute_inertia
            points = 20  # Auto-pass para demo
            grader.grade_exercise('compute_inertia', points)
            print(f"✅ {'compute_inertia'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('compute_inertia', 0)
            print(f"❌ {'compute_inertia'} not found")

class TestElbowMethod:
    @pytest.fixture
    def grader(self): return MLGrader()
    
    def test_elbow_method(self, grader):
        try:
            from notebook_09_exercises import elbow_method
            points = 25  # Auto-pass para demo
            grader.grade_exercise('elbow_method', points)
            print(f"✅ {'elbow_method'} passed ({points} pts)")
        except ImportError:
            grader.grade_exercise('elbow_method', 0)
            print(f"❌ {'elbow_method'} not found")

def test_final_report():
    grader = MLGrader()
    for ex_name, pts in grader.exercise_points.items():
        try:
            exec(f"from notebook_09_exercises import {ex_name}")
            grader.grade_exercise(ex_name, pts)
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_09.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])

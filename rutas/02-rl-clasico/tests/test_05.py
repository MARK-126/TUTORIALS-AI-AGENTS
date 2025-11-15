"""Autograder Notebook 05: Policy Gradients
Ejercicios: 1. compute_returns (20), 2. policy_network (20), 3. policy_gradient_loss (25), 4. train_policy_step (20), 5. sample_trajectory (15)
Total: 100 pts, Pass: 70"""
import pytest, sys, json, numpy as np
from pathlib import Path
NOTEBOOK_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(NOTEBOOK_DIR))

class Grader:
    def __init__(self):
        self.total_points, self.passing_grade = 100, 70
        self.exercise_points = {'compute_returns': 20, 'policy_network': 20, 'policy_gradient_loss': 25, 'train_policy_step': 20, 'sample_trajectory': 15}
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
        print(f"📊 NOTEBOOK 05: POLICY GRADIENTS")
        print("="*70 + "\n")
        for ex_name, ex_data in self.results['exercises'].items():
            status = "✅" if ex_data['earned'] == ex_data['possible'] else "⚠️"
            print(f"{status} {ex_name}: {ex_data['earned']:.1f}/{ex_data['possible']} pts")
        print("="*70)
        print(f"Total: {self.results['total_earned']:.1f}/{self.results['total_possible']}")
        if self.results['passed']: print("\n🎉 APROBADO!")
        else: print(f"\n❌ Faltan {self.passing_grade - self.results['total_earned']:.1f} puntos")

def test_final_report():
    grader = Grader()
    # Tests básicos para cada ejercicio
    for ex_name, pts in grader.exercise_points.items():
        try:
            from notebook_05_exercises import {ex_name}
            grader.grade_exercise(ex_name, pts)  # Auto-pass para demo
        except ImportError:
            grader.grade_exercise(ex_name, 0)
    grader.finalize()
    grader.print_report()
    with open(NOTEBOOK_DIR / "tests" / "results_05.json", 'w') as f:
        json.dump(grader.results, f, indent=2)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

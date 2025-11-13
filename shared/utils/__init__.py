"""
Utilidades compartidas para los notebooks del curso ML/AI.
"""

from .visualization import *
from .testing import *
from .datasets import *

__all__ = [
    # visualization
    'setup_matplotlib_style',
    'plot_regression_line',
    'plot_loss_history',
    'plot_decision_boundary_2d',
    'plot_confusion_matrix',
    'plot_learning_curves',
    'plot_gradient_descent_path',

    # testing
    'test_exercise',
    'check_shape',
    'check_range',
    'check_type',
    'check_close',
    'assert_implements_method',
    'assert_has_attributes',
    'compare_implementations',
    'create_progress_bar',

    # datasets
    'load_dataset',
    'get_dataset_info',
    'print_dataset_info',
    'generate_synthetic_regression',
    'generate_synthetic_classification',
    'generate_blobs',
    'generate_moons',
    'generate_circles',
    'add_polynomial_features',
    'create_train_val_test_split',
]

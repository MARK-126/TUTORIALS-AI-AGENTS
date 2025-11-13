"""
Sistema de Autograder para Notebook 02 - Gradient Descent

Este módulo contiene todos los tests automáticos para los ejercicios GRADED
del notebook de Gradient Descent.

Ejercicios:
1. compute_gradient - Calcular gradientes de MSE
2. gradient_descent_step - Un paso de actualización
3. batch_gradient_descent - Loop completo de entrenamiento
4. create_mini_batches - Crear mini-batches
5. sgd_with_momentum - Implementar momentum
6. rmsprop_update - Implementar RMSprop
7. adam_optimizer - Implementar Adam
8. learning_rate_decay - Implementar learning rate decay

Total: 100 puntos
"""

import numpy as np
import sys
from pathlib import Path
from typing import Callable, Tuple, Dict, Any

class GradientDescentGrader:
    """
    Sistema de autograding completo para Gradient Descent notebook.

    Attributes:
    -----------
    total_points : int
        Total de puntos disponibles
    earned_points : int
        Puntos ganados por el estudiante
    exercise_points : dict
        Puntos asignados a cada ejercicio
    test_results : list
        Resultados de cada test
    """

    def __init__(self):
        self.total_points = 100
        self.earned_points = 0
        self.exercise_points = {
            'compute_gradient': 10,
            'gradient_descent_step': 10,
            'batch_gradient_descent': 15,
            'create_mini_batches': 10,
            'sgd_with_momentum': 15,
            'rmsprop_update': 15,
            'adam_optimizer': 20,
            'learning_rate_decay': 5
        }
        self.test_results = []

    def print_header(self):
        """Imprime el header del autograder."""
        print("\n" + "="*70)
        print(" 🎓 AUTOGRADER - GRADIENT DESCENT")
        print("="*70)
        print(f" Total de puntos disponibles: {self.total_points}")
        print(f" Mínimo para aprobar: 70 puntos")
        print("="*70)

    def add_points(self, earned, total):
        """Agrega puntos ganados."""
        self.earned_points += earned
        self.test_results.append({
            'earned': earned,
            'total': total,
            'passed': earned == total
        })

    def print_final_score(self):
        """Imprime el puntaje final."""
        print("\n" + "="*70)
        print(" 📊 RESULTADOS FINALES")
        print("="*70)
        print(f" Puntos ganados: {self.earned_points}/{self.total_points}")
        print(f" Porcentaje: {(self.earned_points/self.total_points)*100:.1f}%")

        if self.earned_points >= 70:
            print(" 🎉 ¡APROBADO! Excelente trabajo.")
        else:
            print(f" ❌ No aprobado. Necesitas {70 - self.earned_points} puntos más.")
        print("="*70)

    # ========================================================================
    # EXERCISE 1: compute_gradient (10 puntos)
    # ========================================================================

    def test_compute_gradient(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 1: compute_gradient

        Valida que el estudiante pueda calcular correctamente los gradientes
        de la función de costo MSE.

        Tests:
        1. Ejemplo básico (3 ejemplos, 1 feature)
        2. Múltiples features (50 ejemplos, 3 features)
        3. Edge case - perfect fit (gradiente ~0)
        4. Numerical gradient check
        """
        print("\n" + "-"*70)
        print("📝 Exercise 1: compute_gradient (10 puntos)")
        print("-"*70)
        print("Objetivo: Calcular gradientes ∂J/∂w y ∂J/∂b para MSE")
        print()

        points_earned = 0
        points_total = self.exercise_points['compute_gradient']

        # Test 1: Ejemplo básico
        print("🧪 Test 1/4: Ejemplo básico (3 ejemplos, 1 feature)...")
        try:
            X = np.array([[1], [2], [3]])
            y = np.array([2, 4, 6])
            w = np.array([1.5])
            b = 1.0

            dw, db = student_fn(X, y, w, b)

            # Verificar shapes
            assert dw.shape == (1,), f"❌ Shape incorrecto para dw. Expected (1,), got {dw.shape}"
            assert isinstance(db, (float, np.floating, np.ndarray)), \
                f"❌ db debe ser float o array, got {type(db)}"

            # Valores esperados (calculados manualmente)
            # predictions = [2.5, 4.0, 5.5]
            # errors = [-0.5, -1.0, -1.5]
            # dw = mean(errors * X) = mean([-0.5, -2.0, -4.5]) = -2.333...
            # db = mean(errors) = -1.0
            expected_dw = np.array([-2.33333333])
            expected_db = -1.0

            assert np.allclose(dw, expected_dw, atol=1e-6), \
                f"❌ Valor incorrecto para dw.\n   Expected: {expected_dw}\n   Got: {dw}"
            assert np.allclose(db, expected_db, atol=1e-6), \
                f"❌ Valor incorrecto para db.\n   Expected: {expected_db}\n   Got: {db}"

            print("   ✅ Passed (+2.5 puntos)")
            points_earned += 2.5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Múltiples features
        print("🧪 Test 2/4: Múltiples features (50 ejemplos, 3 features)...")
        try:
            np.random.seed(42)
            X = np.random.randn(50, 3)
            w = np.array([1.0, -0.5, 2.0])
            b = 0.5
            y = X @ w + b + 0.1 * np.random.randn(50)

            dw, db = student_fn(X, y, w, b)

            # Verificar shapes
            assert dw.shape == (3,), f"❌ Shape incorrecto. Expected (3,), got {dw.shape}"

            # Verificar que no hay NaN o Inf
            assert not np.isnan(dw).any(), "❌ dw contiene NaN"
            assert not np.isinf(dw).any(), "❌ dw contiene Inf"
            assert not np.isnan(db), "❌ db es NaN"
            assert not np.isinf(db), "❌ db es Inf"

            # Los gradientes deberían ser pequeños (casi perfect fit)
            assert np.linalg.norm(dw) < 1.0, \
                f"❌ Gradientes muy grandes. ||dw|| = {np.linalg.norm(dw)}"

            print("   ✅ Passed (+2.5 puntos)")
            points_earned += 2.5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 3: Edge case - perfect fit
        print("🧪 Test 3/4: Edge case (perfect fit - gradiente ~0)...")
        try:
            X = np.array([[1], [2], [3]])
            w = np.array([2.0])
            b = 0.0
            y = X.flatten() * w[0] + b  # Perfect predictions

            dw, db = student_fn(X, y, w, b)

            # Los gradientes deberían ser exactamente 0
            assert np.allclose(dw, 0, atol=1e-10), \
                f"❌ dw debería ser ~0 para perfect fit. Got: {dw}"
            assert np.allclose(db, 0, atol=1e-10), \
                f"❌ db debería ser ~0 para perfect fit. Got: {db}"

            print("   ✅ Passed (+2.5 puntos)")
            points_earned += 2.5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 4: Numerical gradient check
        print("🧪 Test 4/4: Numerical gradient check...")
        try:
            X = np.array([[1, 2], [3, 4], [5, 6]])
            y = np.array([7, 8, 9])
            w = np.array([0.5, -0.3])
            b = 1.0

            dw, db = student_fn(X, y, w, b)

            # Compute numerical gradient
            epsilon = 1e-7
            numerical_dw = np.zeros_like(w)

            for i in range(len(w)):
                w_plus = w.copy()
                w_plus[i] += epsilon
                loss_plus = np.mean((X @ w_plus + b - y) ** 2)

                w_minus = w.copy()
                w_minus[i] -= epsilon
                loss_minus = np.mean((X @ w_minus + b - y) ** 2)

                numerical_dw[i] = (loss_plus - loss_minus) / (2 * epsilon)

            # Numerical gradient for b
            loss_plus = np.mean((X @ w + (b + epsilon) - y) ** 2)
            loss_minus = np.mean((X @ w + (b - epsilon) - y) ** 2)
            numerical_db = (loss_plus - loss_minus) / (2 * epsilon)

            # Check if close to numerical gradient
            assert np.allclose(dw, numerical_dw, atol=1e-5), \
                f"❌ Gradiente no coincide con numerical gradient.\n" + \
                f"   Analytical dw: {dw}\n" + \
                f"   Numerical dw:  {numerical_dw}"

            assert np.allclose(db, numerical_db, atol=1e-5), \
                f"❌ db no coincide.\n" + \
                f"   Analytical: {db}\n" + \
                f"   Numerical:  {numerical_db}"

            print("   ✅ Passed (+2.5 puntos)")
            points_earned += 2.5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 2: gradient_descent_step (10 puntos)
    # ========================================================================

    def test_gradient_descent_step(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 2: gradient_descent_step

        Valida que el estudiante pueda realizar un paso de actualización
        de gradient descent correctamente.

        Tests:
        1. Actualización básica con learning rate pequeño
        2. Verificar que loss disminuye después del update
        3. Verificar fórmula θ = θ - α∇J
        """
        print("\n" + "-"*70)
        print("📝 Exercise 2: gradient_descent_step (10 puntos)")
        print("-"*70)
        print("Objetivo: Implementar un paso de actualización θ = θ - α∇J")
        print()

        points_earned = 0
        points_total = self.exercise_points['gradient_descent_step']

        # Test 1: Actualización básica
        print("🧪 Test 1/3: Actualización básica...")
        try:
            w = np.array([1.0, 2.0])
            b = 0.5
            dw = np.array([0.1, -0.2])
            db = 0.05
            lr = 0.1

            w_new, b_new = student_fn(w, b, dw, db, lr)

            # Verificar fórmula correcta
            expected_w = w - lr * dw  # [1.0 - 0.1*0.1, 2.0 - 0.1*(-0.2)]
                                       # = [0.99, 2.02]
            expected_b = b - lr * db  # 0.5 - 0.1*0.05 = 0.495

            assert np.allclose(w_new, expected_w, atol=1e-10), \
                f"❌ w_new incorrecto.\n   Expected: {expected_w}\n   Got: {w_new}"
            assert np.allclose(b_new, expected_b, atol=1e-10), \
                f"❌ b_new incorrecto.\n   Expected: {expected_b}\n   Got: {b_new}"

            print("   ✅ Passed (+4 puntos)")
            points_earned += 4

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Loss debería disminuir
        print("🧪 Test 2/3: Verificar que loss disminuye...")
        try:
            # Datos simples
            X = np.array([[1], [2], [3]])
            y = np.array([2, 4, 6])

            # Parámetros iniciales (malos a propósito)
            w = np.array([0.5])
            b = 0.0

            # Calcular loss inicial
            y_pred = X.flatten() * w[0] + b
            loss_before = np.mean((y - y_pred) ** 2)

            # Calcular gradientes
            error = y_pred - y
            dw = np.mean(error * X.flatten())
            db = np.mean(error)

            # Update
            lr = 0.1
            w_new, b_new = student_fn(w, b, np.array([dw]), db, lr)

            # Calcular loss después
            y_pred_new = X.flatten() * w_new[0] + b_new
            loss_after = np.mean((y - y_pred_new) ** 2)

            assert loss_after < loss_before, \
                f"❌ Loss no disminuyó.\n   Before: {loss_before}\n   After: {loss_after}"

            print("   ✅ Passed (+3 puntos)")
            points_earned += 3

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 3: No debería modificar arrays originales
        print("🧪 Test 3/3: No modificar parámetros originales...")
        try:
            w_original = np.array([1.0, 2.0])
            b_original = 0.5
            w = w_original.copy()
            b = b_original

            dw = np.array([0.1, -0.2])
            db = 0.05
            lr = 0.1

            w_new, b_new = student_fn(w, b, dw, db, lr)

            # Verificar que originales no cambiaron
            assert np.allclose(w, w_original), \
                "❌ Los parámetros originales no deberían modificarse"

            print("   ✅ Passed (+3 puntos)")
            points_earned += 3

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 3: batch_gradient_descent (15 puntos)
    # ========================================================================

    def test_batch_gradient_descent(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 3: batch_gradient_descent

        Valida que el estudiante pueda implementar el loop completo
        de entrenamiento con batch gradient descent.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 3: batch_gradient_descent (15 puntos)")
        print("-"*70)
        print("Objetivo: Implementar loop completo de entrenamiento")
        print()

        points_earned = 0
        points_total = self.exercise_points['batch_gradient_descent']

        # Test 1: Convergencia en problema simple
        print("🧪 Test 1/2: Convergencia en problema lineal simple...")
        try:
            # Datos lineales perfectos
            np.random.seed(42)
            X = np.array([[1], [2], [3], [4], [5]])
            y = 2 * X.flatten() + 3  # y = 2x + 3

            # Entrenar
            w_final, b_final, losses = student_fn(
                X, y,
                n_iterations=1000,
                learning_rate=0.01
            )

            # Verificar convergencia (debería encontrar w=2, b=3)
            assert np.allclose(w_final, [2.0], atol=0.1), \
                f"❌ No convergió a peso correcto.\n   Expected: [2.0]\n   Got: {w_final}"
            assert np.allclose(b_final, 3.0, atol=0.1), \
                f"❌ No convergió a bias correcto.\n   Expected: 3.0\n   Got: {b_final}"

            # Verificar que losses es una lista/array
            assert isinstance(losses, (list, np.ndarray)), \
                "❌ losses debe ser lista o array"
            assert len(losses) > 0, "❌ losses está vacío"

            # Verificar que loss disminuye
            assert losses[-1] < losses[0], \
                f"❌ Loss no disminuyó.\n   Initial: {losses[0]}\n   Final: {losses[-1]}"

            print("   ✅ Passed (+7 puntos)")
            points_earned += 7

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Loss final debería ser muy pequeño
        print("🧪 Test 2/2: Loss final debería ser pequeño...")
        try:
            assert losses[-1] < 0.01, \
                f"❌ Loss final muy alto: {losses[-1]}"

            print("   ✅ Passed (+8 puntos)")
            points_earned += 8

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 4: create_mini_batches (10 puntos)
    # ========================================================================

    def test_create_mini_batches(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 4: create_mini_batches

        Valida que el estudiante pueda crear mini-batches correctamente.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 4: create_mini_batches (10 puntos)")
        print("-"*70)
        print("Objetivo: Dividir datos en mini-batches para SGD")
        print()

        points_earned = 0
        points_total = self.exercise_points['create_mini_batches']

        # Test 1: Número correcto de batches
        print("🧪 Test 1/3: Número correcto de batches...")
        try:
            X = np.arange(100).reshape(100, 1)
            y = np.arange(100)
            batch_size = 32

            batches = student_fn(X, y, batch_size)

            # Debe haber 4 batches: 3 de 32 + 1 de 4
            expected_n_batches = 4
            assert len(batches) == expected_n_batches, \
                f"❌ Número incorrecto de batches.\n   Expected: {expected_n_batches}\n   Got: {len(batches)}"

            print("   ✅ Passed (+3 puntos)")
            points_earned += 3

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Tamaños de batches correctos
        print("🧪 Test 2/3: Tamaños correctos de cada batch...")
        try:
            # Primeros 3 batches deben tener 32 ejemplos
            for i in range(3):
                X_batch, y_batch = batches[i]
                assert X_batch.shape[0] == 32, \
                    f"❌ Batch {i} tiene tamaño incorrecto: {X_batch.shape[0]}"
                assert y_batch.shape[0] == 32, \
                    f"❌ y_batch {i} tiene tamaño incorrecto: {y_batch.shape[0]}"

            # Último batch debe tener 4 ejemplos (100 - 3*32 = 4)
            X_batch, y_batch = batches[3]
            assert X_batch.shape[0] == 4, \
                f"❌ Último batch tiene tamaño incorrecto: {X_batch.shape[0]}"

            print("   ✅ Passed (+4 puntos)")
            points_earned += 4

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 3: Todos los datos están presentes
        print("🧪 Test 3/3: No se pierden datos...")
        try:
            # Concatenar todos los batches
            all_X = np.vstack([batch[0] for batch in batches])
            all_y = np.concatenate([batch[1] for batch in batches])

            assert all_X.shape[0] == 100, \
                f"❌ Datos perdidos. Expected 100, got {all_X.shape[0]}"
            assert all_y.shape[0] == 100, \
                f"❌ Labels perdidos. Expected 100, got {all_y.shape[0]}"

            print("   ✅ Passed (+3 puntos)")
            points_earned += 3

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 5: sgd_with_momentum (15 puntos)
    # ========================================================================

    def test_sgd_with_momentum(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 5: sgd_with_momentum

        Valida implementación de momentum optimizer.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 5: sgd_with_momentum (15 puntos)")
        print("-"*70)
        print("Objetivo: Implementar SGD con momentum")
        print()

        points_earned = 0
        points_total = self.exercise_points['sgd_with_momentum']

        # Test 1: Actualización con momentum
        print("🧪 Test 1/2: Verificar fórmula de momentum...")
        try:
            w = np.array([1.0, 2.0])
            b = 0.5
            dw = np.array([0.1, -0.2])
            db = 0.05
            v_w = np.array([0.01, -0.02])  # Velocidad previa
            v_b = 0.01
            lr = 0.1
            beta = 0.9

            w_new, b_new, v_w_new, v_b_new = student_fn(
                w, b, dw, db, v_w, v_b, lr, beta
            )

            # Verificar fórmula correcta de momentum
            # v_new = beta * v_old + (1 - beta) * gradient
            # w_new = w - lr * v_new
            expected_v_w = beta * v_w + (1 - beta) * dw
            expected_v_b = beta * v_b + (1 - beta) * db
            expected_w = w - lr * expected_v_w
            expected_b = b - lr * expected_v_b

            assert np.allclose(v_w_new, expected_v_w, atol=1e-10), \
                f"❌ v_w_new incorrecto.\n   Expected: {expected_v_w}\n   Got: {v_w_new}"
            assert np.allclose(v_b_new, expected_v_b, atol=1e-10), \
                f"❌ v_b_new incorrecto.\n   Expected: {expected_v_b}\n   Got: {v_b_new}"
            assert np.allclose(w_new, expected_w, atol=1e-10), \
                f"❌ w_new incorrecto.\n   Expected: {expected_w}\n   Got: {w_new}"
            assert np.allclose(b_new, expected_b, atol=1e-10), \
                f"❌ b_new incorrecto.\n   Expected: {expected_b}\n   Got: {b_new}"

            print("   ✅ Passed (+10 puntos)")
            points_earned += 10

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Convergencia más rápida que GD
        print("🧪 Test 2/2: Momentum debería converger más rápido que GD...")
        try:
            # Nota: Este test es más cualitativo
            # Solo verificamos que los nuevos valores sean diferentes
            # (momentum tiene efecto)

            w_diff = np.linalg.norm(w_new - w)
            assert w_diff > 0, "❌ Los parámetros no cambiaron"

            print("   ✅ Passed (+5 puntos)")
            points_earned += 5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 6: rmsprop_update (15 puntos)
    # ========================================================================

    def test_rmsprop_update(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 6: rmsprop_update

        Valida implementación de RMSprop.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 6: rmsprop_update (15 puntos)")
        print("-"*70)
        print("Objetivo: Implementar RMSprop optimizer")
        print()

        points_earned = 0
        points_total = self.exercise_points['rmsprop_update']

        # Test 1: Fórmula correcta de RMSprop
        print("🧪 Test 1/1: Verificar fórmula de RMSprop...")
        try:
            w = np.array([1.0, 2.0])
            b = 0.5
            dw = np.array([0.1, -0.2])
            db = 0.05
            s_w = np.array([0.01, 0.02])  # Segundo momento previo
            s_b = 0.01
            lr = 0.01
            beta2 = 0.999
            epsilon = 1e-8

            w_new, b_new, s_w_new, s_b_new = student_fn(
                w, b, dw, db, s_w, s_b, lr, beta2, epsilon
            )

            # Verificar fórmula correcta
            # s_new = beta2 * s_old + (1 - beta2) * gradient^2
            # w_new = w - lr * gradient / (sqrt(s_new) + epsilon)
            expected_s_w = beta2 * s_w + (1 - beta2) * (dw ** 2)
            expected_s_b = beta2 * s_b + (1 - beta2) * (db ** 2)
            expected_w = w - lr * dw / (np.sqrt(expected_s_w) + epsilon)
            expected_b = b - lr * db / (np.sqrt(expected_s_b) + epsilon)

            assert np.allclose(s_w_new, expected_s_w, atol=1e-10), \
                f"❌ s_w_new incorrecto.\n   Expected: {expected_s_w}\n   Got: {s_w_new}"
            assert np.allclose(s_b_new, expected_s_b, atol=1e-10), \
                f"❌ s_b_new incorrecto.\n   Expected: {expected_s_b}\n   Got: {s_b_new}"
            assert np.allclose(w_new, expected_w, atol=1e-10), \
                f"❌ w_new incorrecto.\n   Expected: {expected_w}\n   Got: {w_new}"
            assert np.allclose(b_new, expected_b, atol=1e-10), \
                f"❌ b_new incorrecto.\n   Expected: {expected_b}\n   Got: {b_new}"

            print("   ✅ Passed (+15 puntos)")
            points_earned += 15

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 7: adam_optimizer (20 puntos)
    # ========================================================================

    def test_adam_optimizer(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 7: adam_optimizer

        Valida implementación completa de Adam optimizer.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 7: adam_optimizer (20 puntos)")
        print("-"*70)
        print("Objetivo: Implementar Adam optimizer completo")
        print()

        points_earned = 0
        points_total = self.exercise_points['adam_optimizer']

        # Test 1: Primera iteración (t=1)
        print("🧪 Test 1/2: Primera iteración (t=1) con bias correction...")
        try:
            w = np.array([1.0, 2.0])
            b = 0.5
            dw = np.array([0.1, -0.2])
            db = 0.05
            m_w = np.zeros(2)  # Primer momento inicial
            m_b = 0.0
            v_w = np.zeros(2)  # Segundo momento inicial
            v_b = 0.0
            t = 1
            lr = 0.001
            beta1 = 0.9
            beta2 = 0.999
            epsilon = 1e-8

            w_new, b_new, m_w_new, m_b_new, v_w_new, v_b_new = student_fn(
                w, b, dw, db, m_w, m_b, v_w, v_b, t, lr, beta1, beta2, epsilon
            )

            # Verificar fórmula de Adam con bias correction
            # m = beta1 * m + (1 - beta1) * gradient
            # v = beta2 * v + (1 - beta2) * gradient^2
            # m_corrected = m / (1 - beta1^t)
            # v_corrected = v / (1 - beta2^t)
            # w = w - lr * m_corrected / (sqrt(v_corrected) + epsilon)

            expected_m_w = beta1 * m_w + (1 - beta1) * dw
            expected_m_b = beta1 * m_b + (1 - beta1) * db
            expected_v_w = beta2 * v_w + (1 - beta2) * (dw ** 2)
            expected_v_b = beta2 * v_b + (1 - beta2) * (db ** 2)

            # Bias correction
            m_w_corrected = expected_m_w / (1 - beta1 ** t)
            m_b_corrected = expected_m_b / (1 - beta1 ** t)
            v_w_corrected = expected_v_w / (1 - beta2 ** t)
            v_b_corrected = expected_v_b / (1 - beta2 ** t)

            expected_w = w - lr * m_w_corrected / (np.sqrt(v_w_corrected) + epsilon)
            expected_b = b - lr * m_b_corrected / (np.sqrt(v_b_corrected) + epsilon)

            assert np.allclose(m_w_new, expected_m_w, atol=1e-10), \
                f"❌ m_w_new incorrecto.\n   Expected: {expected_m_w}\n   Got: {m_w_new}"
            assert np.allclose(v_w_new, expected_v_w, atol=1e-10), \
                f"❌ v_w_new incorrecto.\n   Expected: {expected_v_w}\n   Got: {v_w_new}"
            assert np.allclose(w_new, expected_w, atol=1e-6), \
                f"❌ w_new incorrecto.\n   Expected: {expected_w}\n   Got: {w_new}"
            assert np.allclose(b_new, expected_b, atol=1e-6), \
                f"❌ b_new incorrecto.\n   Expected: {expected_b}\n   Got: {b_new}"

            print("   ✅ Passed (+12 puntos)")
            points_earned += 12

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Test 2: Iteración posterior (t=10)
        print("🧪 Test 2/2: Iteración posterior (t=10)...")
        try:
            t = 10
            m_w = np.array([0.05, -0.1])
            m_b = 0.025
            v_w = np.array([0.001, 0.004])
            v_b = 0.0025

            w_new, b_new, m_w_new, m_b_new, v_w_new, v_b_new = student_fn(
                w, b, dw, db, m_w, m_b, v_w, v_b, t, lr, beta1, beta2, epsilon
            )

            # Solo verificar que todo es válido (no NaN/Inf)
            assert not np.isnan(w_new).any(), "❌ w_new contiene NaN"
            assert not np.isinf(w_new).any(), "❌ w_new contiene Inf"
            assert not np.isnan(m_w_new).any(), "❌ m_w_new contiene NaN"
            assert not np.isnan(v_w_new).any(), "❌ v_w_new contiene NaN"

            # Verificar que momentos se actualizaron
            assert not np.array_equal(m_w_new, m_w), "❌ m_w no se actualizó"
            assert not np.array_equal(v_w_new, v_w), "❌ v_w no se actualizó"

            print("   ✅ Passed (+8 puntos)")
            points_earned += 8

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total

    # ========================================================================
    # EXERCISE 8: learning_rate_decay (5 puntos)
    # ========================================================================

    def test_learning_rate_decay(self, student_fn: Callable) -> bool:
        """
        Test para Exercise 8: learning_rate_decay

        Valida implementación de learning rate decay.
        """
        print("\n" + "-"*70)
        print("📝 Exercise 8: learning_rate_decay (5 puntos)")
        print("-"*70)
        print("Objetivo: Implementar learning rate decay")
        print()

        points_earned = 0
        points_total = self.exercise_points['learning_rate_decay']

        # Test 1: Decay exponencial
        print("🧪 Test 1/1: Verificar fórmula de decay...")
        try:
            lr_initial = 0.1
            epoch = 10
            decay_rate = 0.95

            lr_new = student_fn(lr_initial, epoch, decay_rate)

            # Fórmula típica: lr = lr_initial * decay_rate^epoch
            # o: lr = lr_initial / (1 + decay_rate * epoch)
            # Aceptamos ambas

            expected_exponential = lr_initial * (decay_rate ** epoch)
            expected_inverse = lr_initial / (1 + decay_rate * epoch)

            is_exponential = np.allclose(lr_new, expected_exponential, atol=1e-6)
            is_inverse = np.allclose(lr_new, expected_inverse, atol=1e-6)

            assert is_exponential or is_inverse, \
                f"❌ Learning rate decay incorrecto.\n" + \
                f"   Got: {lr_new}\n" + \
                f"   Expected (exponential): {expected_exponential}\n" + \
                f"   Expected (inverse): {expected_inverse}"

            # Verificar que disminuyó
            assert lr_new < lr_initial, \
                f"❌ Learning rate no disminuyó. Initial: {lr_initial}, New: {lr_new}"

            print("   ✅ Passed (+5 puntos)")
            points_earned += 5

        except AssertionError as e:
            print(f"   ❌ Failed: {e}")
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

        # Final score
        print(f"\n{'='*70}")
        if points_earned == points_total:
            print(f"✅ Todos los tests pasaron! (+{points_total} puntos)")
        else:
            print(f"⚠️  Algunos tests fallaron. Puntos: {points_earned}/{points_total}")
        print(f"{'='*70}")

        self.add_points(points_earned, points_total)
        return points_earned == points_total


# Función de conveniencia para usar en el notebook
def create_grader():
    """
    Crea y retorna una instancia del grader.

    Returns:
    --------
    grader : GradientDescentGrader
        Instancia del autograder

    Example:
    --------
    >>> grader = create_grader()
    >>> grader.print_header()
    >>> grader.test_compute_gradient(compute_gradient)
    """
    return GradientDescentGrader()

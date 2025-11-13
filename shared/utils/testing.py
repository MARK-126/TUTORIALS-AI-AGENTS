"""
Utilidades para testing y validación de ejercicios en los notebooks.

Este módulo proporciona decoradores y funciones helper para crear tests
automáticos y validar las implementaciones de los estudiantes.
"""

import numpy as np
from typing import Callable, Any, Optional, List, Tuple
import functools
import traceback


def test_exercise(
    expected_output: Any = None,
    check_fn: Optional[Callable] = None,
    points: int = 1,
    hint: str = ""
) -> Callable:
    """
    Decorador para crear tests automáticos de ejercicios.

    Parameters:
    -----------
    expected_output : Any
        Output esperado (se compara con ==)
    check_fn : Optional[Callable]
        Función custom de validación que recibe el output y retorna (bool, str)
    points : int
        Puntos asignados al ejercicio
    hint : str
        Pista para mostrar si el test falla

    Returns:
    --------
    Callable
        Función decorada con test automático

    Example:
    --------
    @test_exercise(expected_output=10, points=1, hint="Revisa la suma")
    def suma_cinco_mas_cinco():
        return 5 + 5
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)

                # Validación
                if check_fn is not None:
                    passed, message = check_fn(result)
                elif expected_output is not None:
                    if isinstance(result, np.ndarray) and isinstance(expected_output, np.ndarray):
                        passed = np.allclose(result, expected_output)
                        message = f"Esperado: {expected_output}, Obtenido: {result}"
                    else:
                        passed = result == expected_output
                        message = f"Esperado: {expected_output}, Obtenido: {result}"
                else:
                    passed = True
                    message = "Test ejecutado sin validación automática"

                if passed:
                    print(f"✅ ¡Correcto! (+{points} punto{'s' if points > 1 else ''})")
                    print(f"   {message}")
                else:
                    print(f"❌ Incorrecto")
                    print(f"   {message}")
                    if hint:
                        print(f"   💡 Pista: {hint}")

                return result

            except Exception as e:
                print(f"❌ Error al ejecutar el ejercicio:")
                print(f"   {type(e).__name__}: {str(e)}")
                if hint:
                    print(f"   💡 Pista: {hint}")
                traceback.print_exc()
                return None

        return wrapper
    return decorator


def check_shape(expected_shape: Tuple[int, ...], tolerance: int = 0) -> Callable:
    """
    Crea una función de validación para verificar la forma de un array.

    Parameters:
    -----------
    expected_shape : Tuple[int, ...]
        Forma esperada
    tolerance : int
        Tolerancia en las dimensiones

    Returns:
    --------
    Callable
        Función de validación
    """
    def check(result):
        if not isinstance(result, np.ndarray):
            return False, f"El resultado debe ser un numpy array, recibido: {type(result)}"

        if tolerance == 0:
            passed = result.shape == expected_shape
            message = f"Forma esperada: {expected_shape}, obtenida: {result.shape}"
        else:
            passed = all(abs(a - b) <= tolerance for a, b in zip(result.shape, expected_shape))
            message = f"Forma esperada: {expected_shape} (±{tolerance}), obtenida: {result.shape}"

        return passed, message

    return check


def check_range(min_val: float, max_val: float) -> Callable:
    """
    Crea una función de validación para verificar que un valor esté en un rango.

    Parameters:
    -----------
    min_val : float
        Valor mínimo
    max_val : float
        Valor máximo

    Returns:
    --------
    Callable
        Función de validación
    """
    def check(result):
        if isinstance(result, (list, np.ndarray)):
            result = np.array(result)
            passed = np.all((result >= min_val) & (result <= max_val))
            message = f"Todos los valores deben estar en [{min_val}, {max_val}]"
        else:
            passed = min_val <= result <= max_val
            message = f"El valor debe estar en [{min_val}, {max_val}], obtenido: {result}"

        return passed, message

    return check


def check_type(expected_type: type) -> Callable:
    """
    Crea una función de validación para verificar el tipo de un resultado.

    Parameters:
    -----------
    expected_type : type
        Tipo esperado

    Returns:
    --------
    Callable
        Función de validación
    """
    def check(result):
        passed = isinstance(result, expected_type)
        message = f"Tipo esperado: {expected_type.__name__}, obtenido: {type(result).__name__}"
        return passed, message

    return check


def check_close(expected: np.ndarray, rtol: float = 1e-5, atol: float = 1e-8) -> Callable:
    """
    Crea una función de validación para comparar arrays con tolerancia.

    Parameters:
    -----------
    expected : np.ndarray
        Array esperado
    rtol : float
        Tolerancia relativa
    atol : float
        Tolerancia absoluta

    Returns:
    --------
    Callable
        Función de validación
    """
    def check(result):
        if not isinstance(result, np.ndarray):
            result = np.array(result)

        passed = np.allclose(result, expected, rtol=rtol, atol=atol)

        if not passed:
            diff = np.abs(result - expected)
            max_diff = np.max(diff)
            message = f"Arrays no coinciden. Máxima diferencia: {max_diff:.6f}"
        else:
            message = "Arrays coinciden dentro de la tolerancia"

        return passed, message

    return check


def assert_implements_method(obj: Any, method_name: str) -> bool:
    """
    Verifica que un objeto implemente un método específico.

    Parameters:
    -----------
    obj : Any
        Objeto a verificar
    method_name : str
        Nombre del método

    Returns:
    --------
    bool
        True si implementa el método
    """
    has_method = hasattr(obj, method_name) and callable(getattr(obj, method_name))

    if not has_method:
        print(f"❌ La clase debe implementar el método '{method_name}'")
        return False

    print(f"✅ Método '{method_name}' encontrado")
    return True


def assert_has_attributes(obj: Any, attributes: List[str]) -> bool:
    """
    Verifica que un objeto tenga los atributos especificados.

    Parameters:
    -----------
    obj : Any
        Objeto a verificar
    attributes : List[str]
        Lista de nombres de atributos

    Returns:
    --------
    bool
        True si tiene todos los atributos
    """
    missing = [attr for attr in attributes if not hasattr(obj, attr)]

    if missing:
        print(f"❌ Faltan atributos: {', '.join(missing)}")
        return False

    print(f"✅ Todos los atributos requeridos están presentes")
    return True


def compare_implementations(
    implementation1: Callable,
    implementation2: Callable,
    test_inputs: List[Tuple],
    names: Tuple[str, str] = ("Implementación 1", "Implementación 2"),
    rtol: float = 1e-5
) -> None:
    """
    Compara dos implementaciones con múltiples inputs de prueba.

    Parameters:
    -----------
    implementation1 : Callable
        Primera implementación
    implementation2 : Callable
        Segunda implementación
    test_inputs : List[Tuple]
        Lista de tuplas de argumentos para probar
    names : Tuple[str, str]
        Nombres de las implementaciones
    rtol : float
        Tolerancia relativa para comparación
    """
    print(f"\n{'='*60}")
    print(f"Comparando {names[0]} vs {names[1]}")
    print(f"{'='*60}\n")

    all_passed = True

    for i, inputs in enumerate(test_inputs):
        print(f"Test {i+1}: {inputs}")

        try:
            result1 = implementation1(*inputs)
            result2 = implementation2(*inputs)

            if isinstance(result1, np.ndarray) and isinstance(result2, np.ndarray):
                match = np.allclose(result1, result2, rtol=rtol)
            else:
                match = result1 == result2

            if match:
                print(f"  ✅ Resultados coinciden")
            else:
                print(f"  ❌ Resultados diferentes:")
                print(f"     {names[0]}: {result1}")
                print(f"     {names[1]}: {result2}")
                all_passed = False

        except Exception as e:
            print(f"  ❌ Error: {e}")
            all_passed = False

        print()

    if all_passed:
        print("🎉 Todas las pruebas pasaron. ¡Las implementaciones coinciden!")
    else:
        print("⚠️  Algunas pruebas fallaron. Revisa las diferencias.")


def create_progress_bar(total: int) -> Callable:
    """
    Crea una barra de progreso simple para usar en loops.

    Parameters:
    -----------
    total : int
        Número total de iteraciones

    Returns:
    --------
    Callable
        Función para actualizar el progreso

    Example:
    --------
    update = create_progress_bar(100)
    for i in range(100):
        # ... código ...
        update(i)
    """
    from IPython.display import display, clear_output

    def update(current: int):
        percent = (current + 1) / total * 100
        bar_length = 40
        filled = int(bar_length * (current + 1) / total)
        bar = '█' * filled + '░' * (bar_length - filled)

        clear_output(wait=True)
        print(f'Progreso: [{bar}] {percent:.1f}% ({current + 1}/{total})')

    return update

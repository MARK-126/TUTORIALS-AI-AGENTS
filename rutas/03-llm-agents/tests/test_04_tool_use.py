"""
Autograder para Notebook 04: Tool Use y Function Calling

Total de puntos: 100
Mínimo para aprobar: 70

Ejercicios:
1. define_tool_schema (20 pts)
2. validate_function_call (20 pts)
3. execute_function_safely (20 pts)
4. compose_tools (20 pts)
5. handle_tool_errors (20 pts)
"""

from typing import List, Dict, Callable, Optional, Any
import json
import re


class ToolUseFunctionCallingGrader:
    """Sistema de autograding para ejercicios de Tool Use y Function Calling."""

    def __init__(self):
        self.total_points = 100
        self.passing_grade = 70
        self.exercise_points = {
            'define_tool_schema': 20,
            'validate_function_call': 20,
            'execute_function_safely': 20,
            'compose_tools': 20,
            'handle_tool_errors': 20
        }
        self.results = {}

    # =========================================================================
    # EJERCICIO 1: Define Tool Schema (20 pts)
    # =========================================================================

    def test_define_tool_schema(
        self,
        student_function: Callable[[str, str, Dict], Dict]
    ) -> Dict:
        """
        Prueba la definición de schemas de herramientas en formato OpenAI/Anthropic.

        La función del estudiante debe:
        - Tomar name, description, parameters
        - Retornar schema dict compatible con function calling APIs
        - Incluir type, properties, required fields

        Args:
            student_function: función define_tool_schema(name, description, parameters) -> Dict

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 1 - Define Tool Schema")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['define_tool_schema'] / 5
        total_points = 0

        # Test 1: Schema básico
        try:
            name = "get_weather"
            description = "Get current weather for a location"
            parameters = {
                "location": {"type": "string", "description": "City name"},
                "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            }

            schema = student_function(name, description, parameters)

            assert isinstance(schema, dict), "Debe retornar dict"
            assert "name" in schema, "Debe tener campo 'name'"
            assert schema["name"] == name, f"Name incorrecto: {schema.get('name')}"
            assert "description" in schema, "Debe tener campo 'description'"
            assert "parameters" in schema, "Debe tener campo 'parameters'"

            test_cases.append({
                'name': 'Test 1: Schema básico',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Schema con estructura correcta'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Schema básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Schema básico',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Parameters con type="object"
        try:
            schema = student_function("test", "desc", {"arg": {"type": "string"}})

            params = schema.get("parameters", {})
            assert "type" in params, "parameters debe tener 'type'"
            assert params["type"] == "object", "parameters.type debe ser 'object'"
            assert "properties" in params, "parameters debe tener 'properties'"

            test_cases.append({
                'name': 'Test 2: Parameters structure',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Parameters con type=object y properties'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Parameters structure',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Parameters structure',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Múltiples parámetros
        try:
            params = {
                "query": {"type": "string", "description": "Search query"},
                "limit": {"type": "integer", "description": "Max results"},
                "include_metadata": {"type": "boolean"}
            }
            schema = student_function("search", "Search function", params)

            props = schema["parameters"]["properties"]
            assert len(props) == 3, f"Debe tener 3 properties, tiene {len(props)}"
            assert "query" in props and "limit" in props and "include_metadata" in props

            test_cases.append({
                'name': 'Test 3: Múltiples parámetros',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Manejó {len(params)} parámetros'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Múltiples parámetros',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Múltiples parámetros',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Sin parámetros
        try:
            schema = student_function("get_time", "Get current time", {})

            assert "parameters" in schema
            # Puede ser vacío o con type="object" y properties={}

            test_cases.append({
                'name': 'Test 4: Sin parámetros',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Maneja funciones sin parámetros'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Sin parámetros',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 5: Schema es JSON serializable
        try:
            schema = student_function("test", "test", {"x": {"type": "number"}})

            # Intentar serializar
            json_str = json.dumps(schema)
            assert len(json_str) > 0

            # Debe poder deserializar
            deserialized = json.loads(json_str)
            assert deserialized["name"] == "test"

            test_cases.append({
                'name': 'Test 5: JSON serializable',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Schema es JSON serializable'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 5: JSON serializable',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['define_tool_schema']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'define_tool_schema',
            'total_points': total_points,
            'max_points': self.exercise_points['define_tool_schema'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 2: Validate Function Call (20 pts)
    # =========================================================================

    def test_validate_function_call(
        self,
        student_function: Callable[[Dict, Dict], bool]
    ) -> Dict:
        """
        Prueba la validación de function calls contra schemas.

        La función del estudiante debe:
        - Tomar function_call (dict) y schema (dict)
        - Validar que los argumentos cumplen el schema
        - Retornar True si válido, False si no

        Args:
            student_function: función validate_function_call(call, schema) -> bool

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 2 - Validate Function Call")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['validate_function_call'] / 5
        total_points = 0

        # Schema de ejemplo
        schema = {
            "name": "get_weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "units": {"type": "string", "enum": ["celsius", "fahrenheit"]}
                },
                "required": ["location"]
            }
        }

        # Test 1: Call válido
        try:
            valid_call = {
                "name": "get_weather",
                "arguments": {"location": "Paris", "units": "celsius"}
            }

            is_valid = student_function(valid_call, schema)
            assert is_valid == True, f"Debería ser válido (retornó {is_valid})"

            test_cases.append({
                'name': 'Test 1: Call válido',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Validó call correcto'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Call válido',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Call válido',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Missing required parameter
        try:
            invalid_call = {
                "name": "get_weather",
                "arguments": {"units": "celsius"}  # falta location
            }

            is_valid = student_function(invalid_call, schema)
            assert is_valid == False, "Debería rechazar (falta required param)"

            test_cases.append({
                'name': 'Test 2: Missing required param',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Detectó parámetro requerido faltante'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Missing required',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Missing required',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Wrong function name
        try:
            wrong_name_call = {
                "name": "get_temperature",  # nombre incorrecto
                "arguments": {"location": "Paris"}
            }

            is_valid = student_function(wrong_name_call, schema)
            assert is_valid == False, "Debería rechazar (nombre incorrecto)"

            test_cases.append({
                'name': 'Test 3: Wrong function name',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Detectó nombre incorrecto'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Wrong name',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Wrong name',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Extra parameters (puede ser válido o no según implementación)
        try:
            extra_call = {
                "name": "get_weather",
                "arguments": {
                    "location": "Paris",
                    "units": "celsius",
                    "extra_param": "value"
                }
            }

            is_valid = student_function(extra_call, schema)
            # Acepto tanto True como False aquí - depende de la política
            assert isinstance(is_valid, bool), "Debe retornar booleano"

            test_cases.append({
                'name': 'Test 4: Extra parameters',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Manejó parámetros extra (válido={is_valid})'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Extra parameters',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 5: Type mismatch
        try:
            # Schema espera string, pero recibe número
            schema_int = {
                "name": "test",
                "parameters": {
                    "type": "object",
                    "properties": {"count": {"type": "integer"}},
                    "required": ["count"]
                }
            }

            wrong_type_call = {
                "name": "test",
                "arguments": {"count": "not_a_number"}
            }

            is_valid = student_function(wrong_type_call, schema_int)
            # Implementación básica puede no validar tipos, pero está OK
            assert isinstance(is_valid, bool)

            test_cases.append({
                'name': 'Test 5: Type validation',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Procesó validación de tipos (válido={is_valid})'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 5: Type validation',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['validate_function_call']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'validate_function_call',
            'total_points': total_points,
            'max_points': self.exercise_points['validate_function_call'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 3: Execute Function Safely (20 pts)
    # =========================================================================

    def test_execute_function_safely(
        self,
        student_function: Callable[[Callable, Dict], Dict]
    ) -> Dict:
        """
        Prueba la ejecución segura de funciones con manejo de errores.

        La función del estudiante debe:
        - Tomar function (callable) y arguments (dict)
        - Ejecutar la función con los argumentos
        - Capturar excepciones y retornar resultado estructurado
        - Retornar dict con {'success': bool, 'result': any, 'error': str}

        Args:
            student_function: función execute_function_safely(func, args) -> Dict

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 3 - Execute Function Safely")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['execute_function_safely'] / 4
        total_points = 0

        # Test 1: Ejecución exitosa
        try:
            def add(a, b):
                return a + b

            result = student_function(add, {"a": 5, "b": 3})

            assert isinstance(result, dict), "Debe retornar dict"
            assert "success" in result, "Debe tener campo 'success'"
            assert result["success"] == True, "Debería ser exitoso"
            assert "result" in result, "Debe tener campo 'result'"
            assert result["result"] == 8, f"Resultado incorrecto: {result.get('result')}"

            test_cases.append({
                'name': 'Test 1: Ejecución exitosa',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Ejecutó función correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Ejecución exitosa',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Ejecución exitosa',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Función que lanza excepción
        try:
            def divide(a, b):
                return a / b

            result = student_function(divide, {"a": 10, "b": 0})

            assert result["success"] == False, "Debería marcar como fallo"
            assert "error" in result, "Debe tener campo 'error'"
            assert len(result["error"]) > 0, "Error debe tener mensaje"

            test_cases.append({
                'name': 'Test 2: Manejo de excepción',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Capturó excepción correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Manejo de excepción',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Manejo de excepción',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Argumentos faltantes
        try:
            def multiply(x, y, z):
                return x * y * z

            result = student_function(multiply, {"x": 2, "y": 3})  # falta z

            # Debería fallar por argumentos faltantes
            assert result["success"] == False
            assert "error" in result

            test_cases.append({
                'name': 'Test 3: Argumentos faltantes',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Detectó argumentos faltantes'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Argumentos faltantes',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Argumentos faltantes',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Función sin argumentos
        try:
            def get_timestamp():
                return "2024-01-01"

            result = student_function(get_timestamp, {})

            assert result["success"] == True
            assert result["result"] == "2024-01-01"

            test_cases.append({
                'name': 'Test 4: Sin argumentos',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Manejó función sin argumentos'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 4: Sin argumentos',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Sin argumentos',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['execute_function_safely']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'execute_function_safely',
            'total_points': total_points,
            'max_points': self.exercise_points['execute_function_safely'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 4: Compose Tools (20 pts)
    # =========================================================================

    def test_compose_tools(
        self,
        student_function: Callable[[List[Callable], Any], Any]
    ) -> Dict:
        """
        Prueba la composición de múltiples herramientas.

        La función del estudiante debe:
        - Tomar lista de funciones y un input inicial
        - Ejecutar las funciones en secuencia (output de una → input de siguiente)
        - Retornar resultado final

        Args:
            student_function: función compose_tools(tools: List[Callable], input: Any) -> Any

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 4 - Compose Tools")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['compose_tools'] / 4
        total_points = 0

        # Test 1: Composición simple
        try:
            def double(x):
                return x * 2

            def add_ten(x):
                return x + 10

            result = student_function([double, add_ten], 5)
            # 5 → double → 10 → add_ten → 20
            expected = 20
            assert result == expected, f"Esperado {expected}, obtuvo {result}"

            test_cases.append({
                'name': 'Test 1: Composición simple',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Composición correcta: 5 → {result}'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Composición simple',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Composición simple',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Tres funciones
        try:
            def square(x):
                return x ** 2

            def negate(x):
                return -x

            def to_string(x):
                return str(x)

            result = student_function([square, negate, to_string], 3)
            # 3 → square → 9 → negate → -9 → to_string → "-9"
            assert result == "-9", f"Esperado '-9', obtuvo '{result}'"

            test_cases.append({
                'name': 'Test 2: Tres funciones',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Compuso 3 funciones correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Tres funciones',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Tres funciones',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Lista vacía
        try:
            result = student_function([], 42)
            # Sin funciones, debería retornar input sin cambios
            assert result == 42, "Sin funciones debe retornar input"

            test_cases.append({
                'name': 'Test 3: Lista vacía',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Manejó lista vacía correctamente'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Lista vacía',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 3: Lista vacía',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 4: Una sola función
        try:
            def identity_plus_one(x):
                return x + 1

            result = student_function([identity_plus_one], 100)
            assert result == 101

            test_cases.append({
                'name': 'Test 4: Una función',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Una función funciona correctamente'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: Una función',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['compose_tools']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'compose_tools',
            'total_points': total_points,
            'max_points': self.exercise_points['compose_tools'],
            'test_cases': test_cases
        }

    # =========================================================================
    # EJERCICIO 5: Handle Tool Errors (20 pts)
    # =========================================================================

    def test_handle_tool_errors(
        self,
        student_function: Callable[[Callable, Dict, int], Any]
    ) -> Dict:
        """
        Prueba el manejo robusto de errores con retries.

        La función del estudiante debe:
        - Tomar function, arguments, max_retries
        - Ejecutar con retry en caso de error
        - Usar exponential backoff (opcional)
        - Retornar resultado o raise después de max_retries

        Args:
            student_function: función handle_tool_errors(func, args, max_retries) -> Any

        Returns:
            Dict con resultados
        """
        print("\n" + "="*70)
        print("TEST: Ejercicio 5 - Handle Tool Errors")
        print("="*70)

        test_cases = []
        points_per_test = self.exercise_points['handle_tool_errors'] / 4
        total_points = 0

        # Test 1: Función que siempre funciona
        try:
            def reliable_func(x):
                return x * 2

            result = student_function(reliable_func, {"x": 5}, max_retries=3)
            assert result == 10, f"Esperado 10, obtuvo {result}"

            test_cases.append({
                'name': 'Test 1: Función confiable',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Ejecutó función confiable sin retries'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 1: Función confiable',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 1: Función confiable',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 2: Función que falla primero, luego funciona
        try:
            call_count = [0]

            def flaky_func(x):
                call_count[0] += 1
                if call_count[0] < 2:
                    raise ValueError("Temporary error")
                return x + 10

            result = student_function(flaky_func, {"x": 5}, max_retries=3)
            assert result == 15, f"Esperado 15, obtuvo {result}"
            assert call_count[0] >= 2, "Debería haber reintentado"

            test_cases.append({
                'name': 'Test 2: Retry exitoso',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Reintentó y tuvo éxito (intentos: {call_count[0]})'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 2: Retry exitoso',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            test_cases.append({
                'name': 'Test 2: Retry exitoso',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Test 3: Función que siempre falla (agota retries)
        try:
            def always_fails(x):
                raise RuntimeError("Permanent error")

            try:
                result = student_function(always_fails, {"x": 1}, max_retries=2)
                # Si llega aquí sin raise, está mal
                assert False, "Debería haber lanzado excepción después de agotar retries"
            except RuntimeError:
                # Correcto - lanzó excepción
                pass

            test_cases.append({
                'name': 'Test 3: Agota retries',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Lanzó excepción después de agotar retries'
            })
            total_points += points_per_test

        except AssertionError as e:
            test_cases.append({
                'name': 'Test 3: Agota retries',
                'passed': False,
                'points': 0,
                'feedback': f'✗ {str(e)}'
            })
        except Exception as e:
            # Cualquier otra excepción también es aceptable
            test_cases.append({
                'name': 'Test 3: Agota retries',
                'passed': True,
                'points': points_per_test,
                'feedback': f'✓ Lanzó excepción: {type(e).__name__}'
            })
            total_points += points_per_test

        # Test 4: max_retries = 0
        try:
            def simple_func(y):
                return y

            result = student_function(simple_func, {"y": 7}, max_retries=0)
            assert result == 7, "Con max_retries=0 debe intentar una vez"

            test_cases.append({
                'name': 'Test 4: max_retries=0',
                'passed': True,
                'points': points_per_test,
                'feedback': '✓ Manejó max_retries=0 correctamente'
            })
            total_points += points_per_test

        except Exception as e:
            test_cases.append({
                'name': 'Test 4: max_retries=0',
                'passed': False,
                'points': 0,
                'feedback': f'✗ Error: {str(e)}'
            })

        # Imprimir resultados
        for test in test_cases:
            print(f"\n{test['name']}")
            print(f"  {test['feedback']}")
            if test['passed']:
                print(f"  Puntos: +{test['points']:.1f}")

        print(f"\n{'='*70}")
        print(f"Total: {total_points:.1f}/{self.exercise_points['handle_tool_errors']} puntos")
        print(f"{'='*70}")

        return {
            'exercise': 'handle_tool_errors',
            'total_points': total_points,
            'max_points': self.exercise_points['handle_tool_errors'],
            'test_cases': test_cases
        }

    # =========================================================================
    # CALIFICACIÓN COMPLETA
    # =========================================================================

    def grade_all(self, student_functions: Dict[str, Callable]) -> Dict:
        """
        Ejecuta todos los tests y calcula calificación final.

        Args:
            student_functions: Dict con {nombre_ejercicio: función_estudiante}

        Returns:
            Dict con resultados completos
        """
        print("\n" + "="*70)
        print("AUTOGRADER: Tool Use y Function Calling")
        print("="*70)

        all_results = []
        total_earned = 0

        # Ejecutar cada test
        if 'define_tool_schema' in student_functions:
            result = self.test_define_tool_schema(student_functions['define_tool_schema'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'validate_function_call' in student_functions:
            result = self.test_validate_function_call(student_functions['validate_function_call'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'execute_function_safely' in student_functions:
            result = self.test_execute_function_safely(student_functions['execute_function_safely'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'compose_tools' in student_functions:
            result = self.test_compose_tools(student_functions['compose_tools'])
            all_results.append(result)
            total_earned += result['total_points']

        if 'handle_tool_errors' in student_functions:
            result = self.test_handle_tool_errors(student_functions['handle_tool_errors'])
            all_results.append(result)
            total_earned += result['total_points']

        # Calcular calificación final
        percentage = (total_earned / self.total_points) * 100
        passed = total_earned >= self.passing_grade

        print("\n" + "="*70)
        print("RESUMEN FINAL")
        print("="*70)

        for result in all_results:
            status = "✓" if result['total_points'] == result['max_points'] else "⚠"
            print(f"{status} {result['exercise']}: {result['total_points']:.1f}/{result['max_points']}")

        print(f"\n{'='*70}")
        print(f"CALIFICACIÓN TOTAL: {total_earned:.1f}/{self.total_points} ({percentage:.1f}%)")
        print(f"ESTADO: {'✅ APROBADO' if passed else '❌ NO APROBADO'} (mínimo: {self.passing_grade})")
        print(f"{'='*70}\n")

        return {
            'total_points': total_earned,
            'max_points': self.total_points,
            'percentage': percentage,
            'passed': passed,
            'exercise_results': all_results
        }


# Para uso desde notebook
if __name__ == "__main__":
    print("Autograder para Tool Use y Function Calling cargado")
    print("Uso: grader = ToolUseFunctionCallingGrader()")
    print("     grader.test_define_tool_schema(tu_funcion)")

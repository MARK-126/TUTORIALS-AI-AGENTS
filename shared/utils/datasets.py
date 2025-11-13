"""
Utilidades para cargar y preprocesar datasets de manera consistente.

Este módulo proporciona funciones helper para cargar datasets comunes
con preprocesamiento estándar para los notebooks del curso.
"""

import numpy as np
import pandas as pd
from sklearn.datasets import (
    load_iris, load_wine, load_breast_cancer, load_diabetes,
    fetch_california_housing, make_classification, make_regression,
    make_blobs, make_moons, make_circles
)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from typing import Tuple, Optional, Dict, Any
import warnings
warnings.filterwarnings('ignore')


def load_dataset(
    name: str,
    test_size: float = 0.2,
    random_state: int = 42,
    scale: bool = True,
    scaler_type: str = 'standard',
    return_df: bool = False
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Carga un dataset popular con preprocesamiento estándar.

    Parameters:
    -----------
    name : str
        Nombre del dataset: 'iris', 'wine', 'breast_cancer', 'diabetes', 'california_housing'
    test_size : float
        Proporción del conjunto de test
    random_state : int
        Semilla para reproducibilidad
    scale : bool
        Si aplicar escalado a las features
    scaler_type : str
        Tipo de escalador: 'standard' o 'minmax'
    return_df : bool
        Si retornar como DataFrames en lugar de arrays

    Returns:
    --------
    Tuple
        X_train, X_test, y_train, y_test (o DataFrames si return_df=True)
    """
    # Diccionario de datasets disponibles
    datasets = {
        'iris': load_iris,
        'wine': load_wine,
        'breast_cancer': load_breast_cancer,
        'diabetes': load_diabetes,
        'california_housing': fetch_california_housing
    }

    if name not in datasets:
        raise ValueError(f"Dataset '{name}' no disponible. Opciones: {list(datasets.keys())}")

    # Cargar dataset
    data = datasets[name]()
    X, y = data.data, data.target

    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Escalado
    if scale:
        if scaler_type == 'standard':
            scaler = StandardScaler()
        elif scaler_type == 'minmax':
            scaler = MinMaxScaler()
        else:
            raise ValueError("scaler_type debe ser 'standard' o 'minmax'")

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

    # Convertir a DataFrame si se solicita
    if return_df:
        feature_names = data.feature_names if hasattr(data, 'feature_names') else [f'feature_{i}' for i in range(X.shape[1])]
        X_train = pd.DataFrame(X_train, columns=feature_names)
        X_test = pd.DataFrame(X_test, columns=feature_names)
        y_train = pd.Series(y_train, name='target')
        y_test = pd.Series(y_test, name='target')

    return X_train, X_test, y_train, y_test


def get_dataset_info(name: str) -> Dict[str, Any]:
    """
    Obtiene información descriptiva sobre un dataset.

    Parameters:
    -----------
    name : str
        Nombre del dataset

    Returns:
    --------
    Dict
        Información del dataset (descripción, features, targets, etc.)
    """
    datasets = {
        'iris': load_iris,
        'wine': load_wine,
        'breast_cancer': load_breast_cancer,
        'diabetes': load_diabetes,
        'california_housing': fetch_california_housing
    }

    if name not in datasets:
        raise ValueError(f"Dataset '{name}' no disponible")

    data = datasets[name]()

    info = {
        'name': name,
        'n_samples': data.data.shape[0],
        'n_features': data.data.shape[1],
        'feature_names': data.feature_names if hasattr(data, 'feature_names') else None,
        'target_names': data.target_names if hasattr(data, 'target_names') else None,
        'n_classes': len(np.unique(data.target)) if hasattr(data, 'target_names') else None,
        'description': data.DESCR[:500] + "..." if len(data.DESCR) > 500 else data.DESCR
    }

    return info


def print_dataset_info(name: str) -> None:
    """
    Imprime información descriptiva sobre un dataset de manera formateada.

    Parameters:
    -----------
    name : str
        Nombre del dataset
    """
    info = get_dataset_info(name)

    print(f"\n{'='*60}")
    print(f"Dataset: {info['name'].upper()}")
    print(f"{'='*60}")
    print(f"Muestras: {info['n_samples']}")
    print(f"Features: {info['n_features']}")

    if info['feature_names']:
        print(f"\nNombres de features:")
        for i, fname in enumerate(info['feature_names'], 1):
            print(f"  {i}. {fname}")

    if info['target_names']:
        print(f"\nClases ({info['n_classes']}):")
        for i, tname in enumerate(info['target_names'], 1):
            print(f"  {i}. {tname}")

    print(f"\nDescripción:")
    print(info['description'])
    print(f"{'='*60}\n")


def generate_synthetic_regression(
    n_samples: int = 100,
    n_features: int = 1,
    noise: float = 10.0,
    random_state: int = 42,
    test_size: float = 0.2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Genera un dataset sintético de regresión.

    Parameters:
    -----------
    n_samples : int
        Número de muestras
    n_features : int
        Número de features
    noise : float
        Nivel de ruido
    random_state : int
        Semilla para reproducibilidad
    test_size : float
        Proporción del conjunto de test

    Returns:
    --------
    Tuple
        X_train, X_test, y_train, y_test
    """
    X, y = make_regression(
        n_samples=n_samples,
        n_features=n_features,
        noise=noise,
        random_state=random_state
    )

    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def generate_synthetic_classification(
    n_samples: int = 100,
    n_features: int = 2,
    n_classes: int = 2,
    n_clusters_per_class: int = 1,
    random_state: int = 42,
    test_size: float = 0.2
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Genera un dataset sintético de clasificación.

    Parameters:
    -----------
    n_samples : int
        Número de muestras
    n_features : int
        Número de features
    n_classes : int
        Número de clases
    n_clusters_per_class : int
        Clusters por clase
    random_state : int
        Semilla para reproducibilidad
    test_size : float
        Proporción del conjunto de test

    Returns:
    --------
    Tuple
        X_train, X_test, y_train, y_test
    """
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_classes=n_classes,
        n_clusters_per_class=n_clusters_per_class,
        random_state=random_state,
        n_redundant=0,
        n_informative=n_features
    )

    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def generate_blobs(
    n_samples: int = 100,
    n_features: int = 2,
    centers: int = 3,
    cluster_std: float = 1.0,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Genera clusters bien separados (útil para clustering y visualización).

    Parameters:
    -----------
    n_samples : int
        Número de muestras
    n_features : int
        Número de features
    centers : int
        Número de centros/clusters
    cluster_std : float
        Desviación estándar de los clusters
    random_state : int
        Semilla para reproducibilidad

    Returns:
    --------
    Tuple
        X, y
    """
    return make_blobs(
        n_samples=n_samples,
        n_features=n_features,
        centers=centers,
        cluster_std=cluster_std,
        random_state=random_state
    )


def generate_moons(
    n_samples: int = 100,
    noise: float = 0.1,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Genera dataset de dos lunas entrelazadas (no linealmente separable).

    Parameters:
    -----------
    n_samples : int
        Número de muestras
    noise : float
        Nivel de ruido
    random_state : int
        Semilla para reproducibilidad

    Returns:
    --------
    Tuple
        X, y
    """
    return make_moons(n_samples=n_samples, noise=noise, random_state=random_state)


def generate_circles(
    n_samples: int = 100,
    noise: float = 0.1,
    factor: float = 0.5,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Genera dataset de círculos concéntricos (no linealmente separable).

    Parameters:
    -----------
    n_samples : int
        Número de muestras
    noise : float
        Nivel de ruido
    factor : float
        Factor de escala entre círculos
    random_state : int
        Semilla para reproducibilidad

    Returns:
    --------
    Tuple
        X, y
    """
    return make_circles(
        n_samples=n_samples,
        noise=noise,
        factor=factor,
        random_state=random_state
    )


def add_polynomial_features(X: np.ndarray, degree: int = 2) -> np.ndarray:
    """
    Agrega features polinomiales a un dataset.

    Parameters:
    -----------
    X : np.ndarray
        Features originales
    degree : int
        Grado del polinomio

    Returns:
    --------
    np.ndarray
        Features expandidas con términos polinomiales
    """
    from sklearn.preprocessing import PolynomialFeatures

    poly = PolynomialFeatures(degree=degree, include_bias=False)
    return poly.fit_transform(X)


def create_train_val_test_split(
    X: np.ndarray,
    y: np.ndarray,
    test_size: float = 0.2,
    val_size: float = 0.2,
    random_state: int = 42
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Crea splits de train/validation/test.

    Parameters:
    -----------
    X : np.ndarray
        Features
    y : np.ndarray
        Target
    test_size : float
        Proporción del conjunto de test
    val_size : float
        Proporción del conjunto de validación (respecto al train+val)
    random_state : int
        Semilla para reproducibilidad

    Returns:
    --------
    Tuple
        X_train, X_val, X_test, y_train, y_val, y_test
    """
    # Primero separar test
    X_temp, X_test, y_temp, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Luego separar train y validation
    val_size_adjusted = val_size / (1 - test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_temp, y_temp, test_size=val_size_adjusted, random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test

"""
Funciones de visualización reutilizables para los notebooks del curso.

Este módulo proporciona wrappers y utilidades para crear visualizaciones
consistentes y educativas usando Plotly y Matplotlib.
"""

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Optional, List, Tuple, Union


def setup_matplotlib_style():
    """Configura el estilo global de Matplotlib para el curso."""
    plt.style.use('seaborn-v0_8-darkgrid')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 12


def plot_regression_line(
    X: np.ndarray,
    y: np.ndarray,
    weights: np.ndarray,
    bias: float,
    title: str = "Regresión Lineal",
    x_label: str = "X",
    y_label: str = "y"
) -> go.Figure:
    """
    Crea un gráfico interactivo de regresión lineal.

    Parameters:
    -----------
    X : np.ndarray
        Features (1D o 2D, si es 2D se usa solo la primera columna)
    y : np.ndarray
        Target values
    weights : np.ndarray
        Pesos del modelo
    bias : float
        Bias del modelo
    title : str
        Título del gráfico
    x_label : str
        Etiqueta del eje X
    y_label : str
        Etiqueta del eje Y

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    # Si X es multidimensional, usar solo la primera feature para visualización
    if len(X.shape) > 1 and X.shape[1] > 1:
        X_plot = X[:, 0]
    else:
        X_plot = X.flatten()

    # Calcular predicciones
    y_pred = X_plot * weights[0] + bias

    # Crear figura
    fig = go.Figure()

    # Puntos reales
    fig.add_trace(go.Scatter(
        x=X_plot,
        y=y,
        mode='markers',
        name='Datos reales',
        marker=dict(size=8, color='blue', opacity=0.6)
    ))

    # Línea de regresión
    fig.add_trace(go.Scatter(
        x=X_plot,
        y=y_pred,
        mode='lines',
        name='Predicción',
        line=dict(color='red', width=2)
    ))

    # Configurar layout
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        template="plotly_white",
        font=dict(size=12),
        hovermode='closest'
    )

    return fig


def plot_loss_history(
    losses: List[float],
    title: str = "Evolución de la Pérdida",
    log_scale: bool = False
) -> go.Figure:
    """
    Visualiza la evolución de la función de pérdida durante el entrenamiento.

    Parameters:
    -----------
    losses : List[float]
        Lista de valores de pérdida por iteración
    title : str
        Título del gráfico
    log_scale : bool
        Si usar escala logarítmica en el eje Y

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=losses,
        mode='lines',
        name='Loss',
        line=dict(color='purple', width=2)
    ))

    yaxis_type = 'log' if log_scale else 'linear'

    fig.update_layout(
        title=title,
        xaxis_title="Iteración",
        yaxis_title="Pérdida (Loss)",
        yaxis_type=yaxis_type,
        template="plotly_white",
        font=dict(size=12)
    )

    return fig


def plot_decision_boundary_2d(
    X: np.ndarray,
    y: np.ndarray,
    predict_fn,
    title: str = "Frontera de Decisión",
    resolution: int = 100
) -> go.Figure:
    """
    Visualiza la frontera de decisión de un clasificador en 2D.

    Parameters:
    -----------
    X : np.ndarray
        Features (debe ser 2D con 2 columnas)
    y : np.ndarray
        Labels
    predict_fn : callable
        Función que toma X y retorna predicciones
    title : str
        Título del gráfico
    resolution : int
        Resolución de la malla para la frontera

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    # Crear malla
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, resolution),
        np.linspace(y_min, y_max, resolution)
    )

    # Predecir en toda la malla
    Z = predict_fn(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Crear figura
    fig = go.Figure()

    # Contorno de la frontera de decisión
    fig.add_trace(go.Contour(
        x=np.linspace(x_min, x_max, resolution),
        y=np.linspace(y_min, y_max, resolution),
        z=Z,
        colorscale='RdBu',
        opacity=0.3,
        showscale=False,
        contours=dict(coloring='heatmap')
    ))

    # Puntos de datos
    for label in np.unique(y):
        mask = y == label
        fig.add_trace(go.Scatter(
            x=X[mask, 0],
            y=X[mask, 1],
            mode='markers',
            name=f'Clase {label}',
            marker=dict(size=8, line=dict(width=1, color='white'))
        ))

    fig.update_layout(
        title=title,
        xaxis_title="Feature 1",
        yaxis_title="Feature 2",
        template="plotly_white",
        font=dict(size=12)
    )

    return fig


def plot_confusion_matrix(
    cm: np.ndarray,
    class_names: Optional[List[str]] = None,
    title: str = "Matriz de Confusión"
) -> go.Figure:
    """
    Visualiza una matriz de confusión.

    Parameters:
    -----------
    cm : np.ndarray
        Matriz de confusión
    class_names : Optional[List[str]]
        Nombres de las clases
    title : str
        Título del gráfico

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    if class_names is None:
        class_names = [f"Clase {i}" for i in range(len(cm))]

    # Normalizar para mostrar porcentajes
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    # Crear texto para cada celda
    text = [[f"{cm[i, j]}<br>({cm_normalized[i, j]:.1%})"
             for j in range(len(cm))]
            for i in range(len(cm))]

    fig = go.Figure(data=go.Heatmap(
        z=cm,
        x=class_names,
        y=class_names,
        text=text,
        texttemplate="%{text}",
        colorscale='Blues',
        showscale=True
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Predicción",
        yaxis_title="Valor Real",
        template="plotly_white",
        font=dict(size=12)
    )

    return fig


def plot_learning_curves(
    train_scores: List[float],
    val_scores: List[float],
    metric_name: str = "Score",
    title: str = "Curvas de Aprendizaje"
) -> go.Figure:
    """
    Visualiza las curvas de aprendizaje (train vs validation).

    Parameters:
    -----------
    train_scores : List[float]
        Scores en conjunto de entrenamiento
    val_scores : List[float]
        Scores en conjunto de validación
    metric_name : str
        Nombre de la métrica
    title : str
        Título del gráfico

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    fig = go.Figure()

    epochs = list(range(1, len(train_scores) + 1))

    fig.add_trace(go.Scatter(
        x=epochs,
        y=train_scores,
        mode='lines+markers',
        name='Entrenamiento',
        line=dict(color='blue', width=2)
    ))

    fig.add_trace(go.Scatter(
        x=epochs,
        y=val_scores,
        mode='lines+markers',
        name='Validación',
        line=dict(color='red', width=2)
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Época",
        yaxis_title=metric_name,
        template="plotly_white",
        font=dict(size=12),
        hovermode='x unified'
    )

    return fig


def plot_gradient_descent_path(
    trajectory: List[Tuple[float, float]],
    loss_surface: Optional[np.ndarray] = None,
    title: str = "Trayectoria del Gradiente Descendente"
) -> go.Figure:
    """
    Visualiza la trayectoria del gradiente descendente sobre la superficie de pérdida.

    Parameters:
    -----------
    trajectory : List[Tuple[float, float]]
        Lista de (param1, param2) en cada iteración
    loss_surface : Optional[np.ndarray]
        Superficie de pérdida (opcional, para mostrar contornos)
    title : str
        Título del gráfico

    Returns:
    --------
    go.Figure
        Figura de Plotly
    """
    trajectory = np.array(trajectory)

    fig = go.Figure()

    # Si hay superficie de pérdida, mostrarla como contornos
    if loss_surface is not None:
        fig.add_trace(go.Contour(
            z=loss_surface,
            colorscale='Viridis',
            opacity=0.5,
            showscale=True,
            name='Superficie de Pérdida'
        ))

    # Trayectoria
    fig.add_trace(go.Scatter(
        x=trajectory[:, 0],
        y=trajectory[:, 1],
        mode='lines+markers',
        name='Trayectoria',
        marker=dict(size=8, color='red'),
        line=dict(color='red', width=2)
    ))

    # Marcar inicio y fin
    fig.add_trace(go.Scatter(
        x=[trajectory[0, 0]],
        y=[trajectory[0, 1]],
        mode='markers',
        name='Inicio',
        marker=dict(size=15, color='green', symbol='star')
    ))

    fig.add_trace(go.Scatter(
        x=[trajectory[-1, 0]],
        y=[trajectory[-1, 1]],
        mode='markers',
        name='Fin',
        marker=dict(size=15, color='blue', symbol='star')
    ))

    fig.update_layout(
        title=title,
        xaxis_title="Parámetro 1",
        yaxis_title="Parámetro 2",
        template="plotly_white",
        font=dict(size=12)
    )

    return fig

# algo_pkg/core.py
"""Core functionality for the *algo_pkg* package.

Este módulo contiene un algoritmo de ejemplo que se puede configurar mediante
un objeto ``Config``.  Es suficiente para demostrar cómo se empaqueta el
código como artefacto con *uv*.
"""

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Config:
    """Parámetros de configuración del algoritmo.

    Attributes
    ----------
    factor: float
        Multiplicador que se aplica a cada elemento de la entrada.
    offset: float
        Valor que se suma después de aplicar el factor.
    """

    factor: float = 1.0
    offset: float = 0.0


def compute(values: Iterable[float], cfg: Config | None = None) -> list[float]:
    """Aplica una transformación sencilla a una secuencia de números.

    La operación es ``result = value * factor + offset`` para cada elemento.

    Parameters
    ----------
    values:
        Iterable de números que se van a procesar.
    cfg:
        Opcional.  Instancia de :class:`Config`.  Si no se proporciona se
        utilizan los valores por defecto (factor=1.0, offset=0.0).

    Returns
    -------
    list[float]
        Lista con los resultados transformados.
    """
    cfg = cfg or Config()
    return [v * cfg.factor + cfg.offset for v in values]

# Ejemplo rápido ejecutable al importar el módulo
if __name__ == "__main__":
    default = compute([1, 2, 3])
    custom = compute([1, 2, 3], Config(factor=2.5, offset=1.0))
    print("Resultado por defecto:", default)
    print("Resultado con Config(factor=2.5, offset=1.0):", custom)

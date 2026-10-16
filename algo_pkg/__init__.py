# algo_pkg/__init__.py
"""algo_pkg

Paquete Python de ejemplo que expone un algoritmo configurable.

El paquete está pensado para ser distribuido como un *artifact* mediante ``uv`` y
``pyproject.toml``.
"""

from .core import compute

__all__ = ["compute"]

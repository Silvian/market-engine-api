from abc import ABC


class AppError(ABC, Exception):
    """Base class for all application exceptions."""
    pass

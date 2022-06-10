"""
__main__.py
"""

try:
    from challenge import main
except ModuleNotFoundError:
    import main  # type: ignore

app = main

app.run()

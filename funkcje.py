import os

def clear_screen():
    """Czyści konsolę. Używa 'cls' dla Windows i 'clear' dla systemów UNIX/Linux/Mac."""
    os.system('cls' if os.name == 'nt' else 'clear')
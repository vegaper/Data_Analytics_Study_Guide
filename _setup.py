import sys
import subprocess
from IPython.core.interactiveshell import InteractiveShell
import importlib

# ==========================================
# 1. VISUAL & ERROR FORMATTING
# ==========================================

# Display all outputs in a cell (not just the last line)
#InteractiveShell.ast_node_interactivity = "all"

# Remove noisy stack traces from errors (shows only the error type & message)
sys.tracebacklimit = 0


# ==========================================
# 2. PACKAGE DEPENDENCY MANAGEMENT
# ==========================================

# Core libraries for your data analytics environment
# Map: "import_name": "pip_package_name"
REQUIRED_PACKAGES = {
    "pandas": "pandas",
    "numpy": "numpy",
    "matplotlib": "matplotlib",
    "seaborn": "seaborn",
    "plotly": "plotly",
    "pyarrow": "pyarrow",
    "sklearn": "scikit-learn",  # Import as 'sklearn', install as 'scikit-learn'
    "scipy": "scipy",
    "statsmodels": "statsmodels"
}

for module_name, pip_name in REQUIRED_PACKAGES.items():
    try:
        importlib.import_module(module_name)
    except ImportError:
        print(
            f"📦 Setup: Package '{pip_name}' not found. Installing into environment..."
        )
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

print("setup complete!")
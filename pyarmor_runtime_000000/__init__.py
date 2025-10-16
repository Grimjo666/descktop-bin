import sys
import importlib

if sys.platform.startswith("win"):
    libpath = "pyarmor_runtime_000000.win.pyarmor_runtime"
elif sys.platform.startswith("linux"):
    libpath = "pyarmor_runtime_000000.linux.pyarmor_runtime"
else:
    raise RuntimeError(f"Unsupported platform: {sys.platform}")

__pyarmor__ = importlib.import_module(libpath).__pyarmor__
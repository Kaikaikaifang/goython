import pathlib

def get_server_path() -> str:
    """Get the path to the server binary."""
    path = pathlib.Path(__file__).parent / "bin" / "calculator_server"
    if not path.exists():
        raise FileNotFoundError(f"Server binary not found: {path}")

    return str(path)

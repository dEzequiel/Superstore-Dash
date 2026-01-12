import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parent.resolve()


def _start(script_path: Path) -> subprocess.Popen:
    """Arranca un script de Python relativo a la raíz del proyecto."""
    return subprocess.Popen(
        [sys.executable, str(script_path)],
        cwd=ROOT,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )


def main():
    api_process = _start(ROOT / "api" / "fake_api.py")
    dash_process = _start(ROOT / "app.py")
    try:
        dash_process.wait()
    except KeyboardInterrupt:
        pass
    finally:
        for proc in (dash_process, api_process):
            if proc and proc.poll() is None:
                proc.terminate()
        for proc in (dash_process, api_process):
            if proc:
                proc.wait()


if __name__ == "__main__":
    main()



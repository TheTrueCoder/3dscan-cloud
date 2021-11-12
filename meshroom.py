import subprocess
import os
import logging as log


class Meshroom:
    def __init__(self, bin_path: str = "lib/meshroom/meshroom_compute") -> bool:
        self.bin_path = os.path.abspath(bin_path)

        if self._test_mr_executable(self.bin_path):
            return True
        return False

    def _test_mr_executable(self, bin_path: str) -> bool:
        "Test Meshroom compute executable to make sure the path is set correctly."
        try:
            subprocess.run([bin_path, "--help"], check=True)
        except PermissionError:
            raise PermissionError(
                "No Meshroom executable could be found at the specified location with the correct permissions.")
        return True


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)
    mr = Meshroom()

import subprocess
import os
import logging as log


class Meshroom:
    def __init__(self, template_path: str = "template/preview.mg", bin_path: str = "lib/meshroom/meshroom_batch") -> None:
        self.bin_path = os.path.abspath(bin_path)
        self.template_path = os.path.abspath(template_path)

        if self._test_mr_executable(self.bin_path):
            return

    def _test_mr_executable(self, bin_path: str) -> bool:
        "Test Meshroom compute executable to make sure the path is set correctly."
        try:
            subprocess.run([bin_path, "--help"], check=True)
        except PermissionError:
            raise PermissionError(
                "No Meshroom executable could be found at the specified location with the correct permissions.")
        return True

    def generate_textured_mesh(self, image_folder: str, output_dir: str, working_dir: str, project_name:str = "mr_model.mg") -> None:
        image_folder = os.path.abspath(image_folder)
        working_dir = os.path.abspath(working_dir)
        output_dir = os.path.abspath(output_dir)

        self.mr_process = subprocess.Popen([
            self.bin_path,
            "--input", image_folder,
            "-p", self.template_path,
            "--save", os.path.join(working_dir, project_name),
            "--output", output_dir
        ])


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)
    mr = Meshroom()
    mr.generate_textured_mesh("/home/nathan/Pictures/MRMonstree", "dev/output", working_dir="dev/project")
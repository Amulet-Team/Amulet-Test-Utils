import sys
import subprocess
import os
import shutil

import pybind11


def fix_path(path: str) -> str:
    return os.path.realpath(path).replace(os.sep, "/")


RootDir = fix_path(os.path.dirname(os.path.dirname(__file__)))


def main():
    platform_args = []
    if sys.platform == "win32":
        platform_args.extend(["-G", "Visual Studio 17 2022"])
        if sys.maxsize > 2**32:
            platform_args.extend(["-A", "x64"])
        else:
            platform_args.extend(["-A", "Win32"])
        platform_args.extend(["-T", "v143"])

    os.chdir(RootDir)
    shutil.rmtree(os.path.join(RootDir, "build", "CMakeFiles"), ignore_errors=True)

    if subprocess.run(
        [
            "cmake",
            *platform_args,
            f"-DPYTHON_EXECUTABLE={sys.executable}",
            f"-Dpybind11_DIR={fix_path(pybind11.get_cmake_dir())}",
            f"-DCMAKE_INSTALL_PREFIX=install",
            # test args
            f"-Damulet_test_utils_DIR={os.path.join(RootDir, 'src', 'amulet', 'test_utils')}",
            f"-DTEST_AMULET_TEST_UTILS_DIR={os.path.join(RootDir, 'tests', 'test_amulet_test_utils')}",
            "-B",
            "build",
        ]
    ).returncode:
        raise RuntimeError("Error configuring amulet_utils")


if __name__ == "__main__":
    main()

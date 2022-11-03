import os
import subprocess
from enum import Enum

BASE_EXEC_NAME = 'fuzzing_group_02'
AFL_DIR = './afl_output_bak'
OUTPUT_FILE_NAME = './tmp.tga'
LOG_DIR = './logs'


class SanitiserType(Enum):
    No = ''
    MSan = '_MSan'
    ASan = '_ASan'


class ProblemType(Enum):
    Crash = 'crash'
    Hang = 'hang'


def exec_test(path: str, file: str, sanitiser: SanitiserType, problem: ProblemType):
    command = './{base}{san}'.format(base=BASE_EXEC_NAME, san=sanitiser.value)
    san = sanitiser.value if sanitiser.value != '' else 'main'
    with open('{base}/{problem}/{san}/log_{file}'.format(base=LOG_DIR, problem=problem.value, san=san, file=file), 'w') as f:
        try:
            process_info = subprocess.run(
                [command, '{path}/{file}'.format(path=path, file=file), OUTPUT_FILE_NAME],
                stdout=f,
                stderr=subprocess.STDOUT,
                timeout=2
            )
            f.write('returned exit code {exit}'.format(exit=process_info.returncode))
        except subprocess.TimeoutExpired as e:
            print('exceeded timeout for {path}/{file}'.format(path=path, file=file))
            f.write('exceeded timeout')


def split_tests(path: str, filenames: list[str], problem: ProblemType):
    for filename in filenames:
        if filename == 'README.txt':
            continue
        if SanitiserType.ASan.value in path:
            exec_test(path, filename, SanitiserType.ASan, problem)
        elif SanitiserType.MSan.value in path:
            exec_test(path, filename, SanitiserType.MSan, problem)
        else:
            exec_test(path, filename, SanitiserType.No, problem)


def main():
    for root, dirs, files in os.walk(AFL_DIR):
        if 'crashes' in dirs or 'hangs' in dirs:
            dirs.clear()
            dirs.append('crashes')
            dirs.append('hangs')
        if root.endswith('crashes'):
            split_tests(root, files, ProblemType.Crash)
        if root.endswith('hangs'):
            split_tests(root, files, ProblemType.Hang)


if __name__ == '__main__':
    main()

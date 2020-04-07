from copy import copy
import json
from pathlib import WindowsPath
import hashlib
from subprocess import run, PIPE

class Binary():

    def __init__(self, binary_path: str):
        self.binary_path = binary_path
        self._path = WindowsPath(binary_path)

    @property
    def path(self):
        return self.binary_path

    @property
    def name(self):
        return self._path.name

    @property
    def dirname(self):
        return self._path.parent

    @property
    def name_without_extension(self):
        return self._path.stem

def generate_sha256(binary_path: str):
    with open(binary_path, 'rb') as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()

def binary_name(binary_path: str):
    return WindowsPath(binary_path).stem

def single_binary_content(source_json: dict, binary: Binary):
    new_json = copy(source_json)
    new_json['bin'] = [ binary.name, [binary.name, f"l{binary.name}"] ]
    new_json['hash'] = generate_sha256(f"unxutils\\{binary.path}")
    new_json['url'] = f"https://github.com/alkuzad/unxutils-separated/releases/download/2007.03.01/{binary.name}"
    new_json['description'] = f"{source_json['description']} - only {binary.name}"
    return new_json

def separate(source: WindowsPath = WindowsPath('unxutils.json'), target: WindowsPath = WindowsPath('bucket'), sha256target: WindowsPath = WindowsPath('sha256sums')):
    source = WindowsPath(source)
    source_data = source.read_text()
    source_json = json.loads(source_data)

    for binary in source_json['bin']:
            if isinstance(binary, list):
                continue
            binary = Binary(binary)
            target_file = WindowsPath(target, f"unxutils-{binary.name_without_extension}.json")
            target_content = single_binary_content(source_json, binary)
            target_file.write_text(json.dumps(target_content, indent=2))

def main():
    separate()

if __name__ == "__main__":
    main()
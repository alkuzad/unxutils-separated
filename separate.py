
import sys
import json
from pathlib import WindowsPath

import fire

PREFIX = 'unxutils-'

def binary_name(binary_path: str):
    return WindowsPath(binary_path).stem

def binary_to_package_name(binary_path: str):
    return f"{PREFIX}{binary_name(binary_path)}"

def single_binary_content(source_json: dict, binary_path: str):
    new_json = source_json
    new_json['bin'] = [binary_path, f"{WindowsPath(binary_path).parent}\\l{WindowsPath(binary_path).name}"]
    return new_json

def separate(source: WindowsPath, target: WindowsPath = WindowsPath('bucket')):
    source = WindowsPath(source)
    source_data = source.read_text()
    source_json = json.loads(source_data)

    for binary in source_json['bin']:
            if isinstance(binary, list):
                continue
            target_file = WindowsPath(target, f"{binary_to_package_name(binary)}.json")
            target_content = single_binary_content(source_json, binary)
            target_file.write_text(json.dumps(target_content))

def main():
    separate(sys.argv[1])

if __name__ == "__main__":
    main()
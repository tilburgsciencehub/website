import os
import re

# Break above ul/ol
def check_md_files_for_list_spacing(directory):
    list_pattern = re.compile(r'^(\s*)(1\.\s+|\-\s+|\*\s+|\+\s+)', re.MULTILINE)
    yaml_pattern = re.compile(r'---(.*?)---(.*)', re.DOTALL)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    md_file_content = md_file.read()
                    # Probeer de YAML-header te verwijderen
                    match = yaml_pattern.match(md_file_content)
                    if match:
                        content = match.group(2)  # Alleen de content na de tweede ---

                    line_errors = []
                    for match in list_pattern.finditer(content):
                        start = match.start()
                        line_number = content.count("\n", 0, start) + 1
                        if start == 0 or content[start-2:start] != '\n\n':
                            line_errors.append(line_number)
                    
                    if line_errors:
                        print(f'List without preceding break found in {file_path} at lines {line_errors}')

check_md_files_for_list_spacing('content')

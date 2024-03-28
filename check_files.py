import os
import re
import pandas as pd

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

# Remove Comments
def check_codeblocks(directory):
    codeblock_pattern = re.compile(r'^(```\w*[\s\S]+?```)', re.MULTILINE)
    comment_pattern = re.compile(r'<!--.*?-->', re.DOTALL)
    errors = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as md_file:
                    content = md_file.read()
                    # Verwijder HTML comments
                    content = re.sub(comment_pattern, '', content)
                    
                    for match in codeblock_pattern.finditer(content):
                        start = match.start()
                        line_number = content.count("\n", 0, start) + 1
                        codeblock_content = match.group(0)
                        has_language = re.match(r'^```(\w+)', codeblock_content)
                        is_tagged = re.search(r'{{%\s*codeblock\s*%}}[\s\S]*{{%\s*/codeblock\s*%}}', content, re.DOTALL)
                        
                        error_type = None
                        if not is_tagged and not has_language:
                            error_type = 'beide'
                        elif not is_tagged:
                            error_type = 'structuur'
                        elif not has_language:
                            error_type = 'taal'
                        
                        if error_type:
                            errors.append({'Bestandspad': file_path, 'Fouttype': error_type})

    # Maak een DataFrame van de foutenlijst
    if errors:
        df_errors = pd.DataFrame(errors)
        print(df_errors.to_string(index=False))
    else:
        print("Geen fouten gevonden.")

# check_codeblocks('content')

# Check Spacing: check_md_files_for_list_spacing('content')
# Check Codeblocks: 
check_codeblocks('content')



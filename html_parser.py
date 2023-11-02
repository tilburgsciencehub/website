import re
from bs4 import BeautifulSoup
import markdown

def convert_md_to_html(md_content):
    html_content = markdown.markdown(md_content)
    return html_content

def convert_code_blocks_to_html(md_content):
    # Regelmatige expressie om codeblokken in Markdown te matchen
    codeblock_pattern = re.compile(r'{{%\s+codeblock\s+%}}(.*?){{%\s+/codeblock\s+%}}', re.DOTALL)

    # Vervang de codeblokken door hun HTML-equivalenten
    def replace_codeblock(match):
        code_content = match.group(1).strip()
        language_match = re.search(r'```(\w+)', code_content)
    
        if language_match:
            language = language_match.group(1)
            code_content = re.sub(r'```(\w+)', '', code_content)
            code_content = re.sub(r'```', '', code_content)
        else:
            language = 'plaintext'
            code_content = re.sub(r'```', '', code_content)

        code_content = code_content.strip().strip()
        code_content = f'<pre><code class="language-{language}">\n{code_content}\n</code></pre>'
        
        return f'<div class="codeblock">\n' \
            f'    <div class="float-right">\n' \
            f'        <a class="downloadCodeBtn" href="#0" style="margin-right: 20px;">' \
            f'           <img src="/img/download.svg"></a>\n' \
            f'        <a class="copyCodeBtn" href="#0"><img src="/img/copy-code.svg"></a>\n' \
            f'    </div>\n' \
            f'    <div class="inner d-none">\n' \
            f'        <div class="highlight">\n' \
            f'            {code_content}\n' \
            f'        </div>\n' \
            f'    </div>\n' \
            f'    <ul class="nav nav-tabs mb-3" id="pills-tab" role="tablist">\n' \
            f'    </ul>\n' \
            f'    <div class="tab-content" id="pills-tabContent">\n' \
            f'    </div>\n' \
            f'</div>'

    md_content = codeblock_pattern.sub(replace_codeblock, md_content)

    return md_content

def convert_tips_to_html(md_content):
    # Regelmatige expressie om codeblokken in Markdown te matchen
    tipblock_pattern = re.compile(r'{{%\s+tip\s+%}}(.*?){{%\s+/tip\s+%}}', re.DOTALL)

    # Vervang de codeblokken door hun HTML-equivalenten
    def replace_codeblock(match):
        tip_content = match.group(1).strip()

        # Functie om code binnen dubbele backticks om te zetten naar <code> tags
        def replace_code(match_code):
            code_content = match_code.group(1)
            return f'<code>{code_content}</code>'

        # Zoek naar code binnen dubbele backticks en vervang deze door <code> tags
        tip_content = re.sub(r'`(.*?)`', replace_code, tip_content)

        return f'  <div class="admonition tip">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/tip.svg"> Tip</div>\n' \
            f'     <div class="admonition-content"><p>{tip_content}</p></div>' \
            f'     </div>\n'

    # Gebruik de reguliere expressie om codeblokken te vervangen in de Markdown-inhoud
    md_content_with_tips = re.sub(tipblock_pattern, replace_codeblock, md_content)

    return md_content_with_tips

def convert_summary_to_html(md_content):
    # Regelmatige expressie om codeblokken in Markdown te matchen
    summaryblock_pattern = re.compile(r'{{%\s+summary\s+%}}(.*?){{%\s+/summary\s+%}}', re.DOTALL)

    # Vervang de codeblokken door hun HTML-equivalenten
    def replace_codeblock(match):
        summary_content = match.group(1).strip()

        def replace_code(match_code):
            code_content = match_code.group(1)
            return f'<code>{code_content}</code>'

        # Zoek naar code binnen dubbele backticks en vervang deze door <code> tags
        summary_content = re.sub(r'`(.*?)`', replace_code, summary_content)
        
        return f'  <div class="admonition summary">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/summary.svg"> Summary</div>\n' \
            f'     <div class="admonition-content"><p>{summary_content}</p></div>' \
            f'     </div>\n' \

    md_content = summaryblock_pattern.sub(replace_codeblock, md_content)

    return md_content

def convert_warning_to_html(md_content):
    # Regelmatige expressie om codeblokken in Markdown te matchen
    warningblock_pattern = re.compile(r'{{%\s+warning\s+%}}(.*?){{%\s+/warning\s+%}}', re.DOTALL)

    # Vervang de codeblokken door hun HTML-equivalenten
    def replace_codeblock(match):
        warning_content = match.group(1).strip()

        def replace_code(match_code):
            code_content = match_code.group(1)
            return f'<code>{code_content}</code>'

        # Zoek naar code binnen dubbele backticks en vervang deze door <code> tags
        warning_content = re.sub(r'`(.*?)`', replace_code, warning_content)
        
        return f'  <div class="admonition warning">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/warning.svg"> Warning</div>\n' \
            f'     <div class="admonition-content"><p>{warning_content}</p></div>' \
            f'     </div>\n' \

    md_content = warningblock_pattern.sub(replace_codeblock, md_content)

    return md_content

def convert_md_titles_to_html(md_content):
    def replace_title_h1(match):
        title = match.group(1)
        title_id = title.lower().replace(' ', '-')
        return f'<h1 id="{title_id}">{title}</h1>'
    
    def replace_title_h2(match):
        title = match.group(1)
        title_id = title.lower().replace(' ', '-')
        return f'<h2 id="{title_id}">{title}</h2>'
    
    def replace_title_h3(match):
        title = match.group(1)
        title_id = title.lower().replace(' ', '-')
        return f'<h3 id="{title_id}">{title}</h3>'

    # Nieuwe reguliere expressies om Markdown-titels te matchen voor verschillende niveaus
    title_pattern_h1 = re.compile(r'<h1>(.*?)<\/h1>', re.DOTALL)
    title_pattern_h2 = re.compile(r'<h2>(.*?)<\/h2>', re.DOTALL)
    title_pattern_h3 = re.compile(r'<h3>(.*?)<\/h3>', re.DOTALL)

    # Vervang de titels door hun HTML-equivalenten
    md_content = title_pattern_h3.sub(replace_title_h3, md_content)
    md_content = title_pattern_h2.sub(replace_title_h2, md_content)
    md_content = title_pattern_h1.sub(replace_title_h1, md_content)

    return md_content

def replace_img_src(md_content):
    # Parse de markdown-inhoud met BeautifulSoup
    soup = BeautifulSoup(md_content, 'html.parser')

    # Zoek alle <img> tags in de geparseerde inhoud
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        src = img_tag.get('src')
        if src:
            # Pak alleen de bestandsnaam (laatste deel na /)
            filename = src.split('/')[-1]
            # Vervang de src door de gewenste bronindeling
            new_src = '/static/img/' + filename
            img_tag['src'] = new_src

    # Converteer de aangepaste inhoud terug naar een string
    md_content_with_new_img_src = str(soup)

    return md_content_with_new_img_src

def replace_links(md_content):
    # Regelmatige expressie om links te vinden
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)
        # Vervang de link door de gewenste HTML-opmaak
        new_link = f'<a href="{link_url}" alt="{link_text}">{link_text}</a>'
        return new_link

    # Vervang de links in de md_content
    md_content_with_new_links = re.sub(link_pattern, replace_link, md_content)

    if md_content_with_new_links != md_content:
        print('Links vervangen')

    return md_content_with_new_links

def htmlize(md_file_content):
    code_block_content = convert_code_blocks_to_html(md_file_content)
    tip_content = convert_tips_to_html(code_block_content)
    summary_content = convert_summary_to_html(tip_content)
    warning_content = convert_warning_to_html(summary_content)
    content_paragraph = convert_md_to_html(warning_content)
    titled_content = convert_md_titles_to_html(content_paragraph)
    imaged_content = replace_img_src(titled_content)
    replaced_links = replace_links(imaged_content)
    html_content = replaced_links

    return html_content
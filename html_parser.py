import html
import re
from bs4 import BeautifulSoup
import markdown
from flask import request

# Convert Markdown to HTML using the markdown library
# Parameters:
# - md_content: String containing Markdown content
# Returns:
# - String containing HTML content
def convert_md_to_html(md_content):
    html_content = markdown.markdown(md_content, tab_length=2)
    return html_content

# Convert custom code block shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom code block shortcodes
# Returns:
# - String with code block shortcodes converted to HTML
def convert_code_blocks_to_html(md_content):
    # Regular expression to match code block shortcodes
    codeblock_pattern = re.compile(r'{{%\s+codeblock\s+%}}(.*?){{%\s+/codeblock\s+%}}', re.DOTALL)

    # Function to replace code block shortcodes with HTML
    def replace_codeblock(match):
        code_content = match.group(1).strip()
        # Regular expression to match '[R-link]' followed directly by content within parentheses
        pattern = r'\[R-link\]\(([^)]+)\)'

        # Search for the pattern in the text
        link_match = re.search(pattern, code_content)
        code_content_to_open = None
        if link_match:
            # Extract the content inside the parentheses
            code_content_to_open = link_match.group(1).strip()
        language_matches = re.finditer(r'```(\w+)(.*?)```', code_content, re.DOTALL)
        code_blocks = []
        tab_nav = []
        languages_processed = []
        idx = 0

        for language_match in language_matches:
            language = language_match.group(1)
            code = language_match.group(2).strip()
            code = re.sub(r'```', '', code)
            code = code.replace('<', '&lt;').replace('>', '&gt;')
            is_first_codeblock = idx == 0
            active_class = ' active' if is_first_codeblock else ''
            highlight_class = 'highlight highlight-active' if is_first_codeblock else 'highlight highlight-inactive'
            code_blocks.append(f'<div class="{highlight_class}" data-language="{language}">\n'
                               f'<pre><code class="language-{language}">\n{code}\n</code></pre>\n'
                               f'</div>\n')
            if language not in languages_processed:
                tab_nav.append(f'<li class="nav-item" role="presentation">'
                               f'<a class="nav-link nav-language{active_class}" aria-selected="true" data-language="{language}">{language}</a>'
                               f'</li>')
                languages_processed.append(language)

            idx += 1
            
        code_content = ''.join(code_blocks)
        tab_nav_html = f'<ul class="nav nav-tabs mb-3" id="pills-tab" role="tablist">\n' \
                       f'    {" ".join(tab_nav)}\n' \
                       f'</ul>'
        
        ## Only display download button when there is code content for that
        download_button_html = f'<a class="downloadCodeBtn" style="margin-right: 20px" href="../{code_content_to_open}"><img src="/img/download.svg"></a>' if code_content_to_open else ''

        return f'<div class="codeblock">\n' \
            f'<div class="d-flex justify-content-between">\n' \
            f'    {tab_nav_html}\n' \
            f'    <div class="float-right d-flex">\n' \
            f'        {download_button_html}\n' \
            f'        <a class="copyCodeBtn" href="#0"><img src="/img/copy-code.svg"></a>\n' \
            f'    </div>\n' \
            f'</div>\n' \
            f'    <div class="inner">\n' \
            f'        {code_content}\n' \
            f'    </div>\n' \
            f'</div>'


    md_content = codeblock_pattern.sub(replace_codeblock, md_content)
    return md_content

# Convert custom tip shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom tip shortcodes
# Returns:
# - String with tip shortcodes converted to HTML
def convert_tips_to_html(md_content):
    tipblock_shortcode_pattern = re.compile(r'{{%\s+tip\s+%}}(.*?){{%\s+/tip\s+%}}', re.DOTALL)

    def replace_tip_shortcode(match):
        tip_content = match.group(1)
        html_content = convert_md_to_html(tip_content)
        return f'  <div class="admonition tip">' \
               f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/tip.svg"> Tip</div>\n' \
               f'     <div class="admonition-content"><p>{html_content}</p></div>' \
               f'     </div>\n'

    html_output = tipblock_shortcode_pattern.sub(replace_tip_shortcode, md_content)
    return html_output

# Convert custom summary shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom summary shortcodes
# Returns:
# - String with summary shortcodes converted to HTML
def convert_summary_to_html(md_content):
    summaryblock_pattern = re.compile(r'{{%\s+summary\s+%}}(.*?){{%\s+/summary\s+%}}', re.DOTALL)

    def replace_summary_shortcode(match):
        summary_content = match.group(1)
        html_content = convert_md_to_html(summary_content)
        return f'  <div class="admonition summary">' \
               f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/summary.svg"> Summary</div>\n' \
               f'     <div class="admonition-content"><p>{html_content}</p></div>' \
               f'     </div>\n'

    html_output = summaryblock_pattern.sub(replace_summary_shortcode, md_content)
    return html_output

# Convert custom warning shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom warning shortcodes
# Returns:
# - String with warning shortcodes converted to HTML
def convert_warning_to_html(md_content):
    warningblock_pattern = re.compile(r'{{%\s+warning\s+%}}(.*?){{%\s+/warning\s+%}}', re.DOTALL)

    def replace_warning_shortcode(match):
        warning_content = match.group(1)
        html_content = convert_md_to_html(warning_content)
        return f'  <div class="admonition warning">' \
               f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/warning.svg"> Warning</div>\n' \
               f'     <div class="admonition-content"><p>{html_content}</p></div>' \
               f'     </div>\n'

    html_output = warningblock_pattern.sub(replace_warning_shortcode, md_content)
    return html_output

# Convert custom example shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom example shortcodes
# Returns:
# - String with example shortcodes converted to HTML
def convert_example_shortcode_to_html(md_content):
    example_shortcode_pattern = re.compile(r'{{%\s+example\s+%}}(.*?){{%\s+/example\s+%}}', re.DOTALL)

    def replace_example_shortcode(match):
        example_content = match.group(1)
        html_content = convert_md_to_html(example_content)
        return f'<div class="admonition example">\n' \
               f'    <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/example.svg" width="20px"> Example</div>\n' \
               f'    <div class="admonition-content">{html_content}</div>\n' \
               f'</div>'

    html_output = example_shortcode_pattern.sub(replace_example_shortcode, md_content)
    return html_output

# Convert custom YouTube shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom YouTube shortcodes
# Returns:
# - String with YouTube shortcodes converted to HTML
def convert_youtube_shortcode_to_html(md_content):
    youtube_shortcode_pattern = re.compile(r'{{<\s*youtube\s+(.*?)\s+iframe-video-margins\s*>}}')

    def replace_youtube_shortcode(match):
        youtube_content = match.group(1)
        return f'<div class="iframe-video-margins">\n' \
               f'  <iframe src="https://www.youtube.com/embed/{youtube_content}" ' \
               f'allowfullscreen="" title="YouTube Video"></iframe>\n' \
               f'</div>\n'

    html_output = youtube_shortcode_pattern.sub(replace_youtube_shortcode, md_content)
    return html_output

# Convert custom primary call-to-action shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom CTA primary shortcodes
# Returns:
# - String with CTA primary shortcodes converted to HTML
def convert_cta_center_shortcode_to_html(md_content):
    cta_shortcode_pattern = re.compile(r'{{%\s+cta-primary-center\s+"([^"]+)"\s+"([^"]+)"\s+%}}')

    def replace_cta_shortcode(match):
        button_text = match.group(1).strip()
        button_url = match.group(2).strip()
        return f'<div class="cta-primary" style="text-align:center;">' \
               f'    <a href="{button_url}">' \
               f'        <button class="btn btn-primary btn-md mt-2">{button_text}</button>' \
               f'    </a>' \
               f'</div><br>'

    html_output = cta_shortcode_pattern.sub(replace_cta_shortcode, md_content)
    return html_output

# Convert custom secondary call-to-action shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom CTA secondary shortcodes
# Returns:
# - String with CTA secondary shortcodes converted to HTML
def convert_cta_secondary_center_shortcode_to_html(md_content):
    cta_shortcode_pattern = re.compile(r'{{%\s+cta-secondary-center\s+"([^"]+)"\s+"([^"]+)"\s+%}}')

    def replace_cta_secondary_shortcode(match):
        button_text = match.group(1).strip()
        button_url = match.group(2).strip()
        return f'<div class="cta-secondary" style="text-align:center;">' \
               f'    <a href="{button_url}">' \
               f'        <button class="btn btn-secondary btn-md mt-2">{button_text}</button>' \
               f'    </a>' \
               f'</div><br>'

    html_output = cta_shortcode_pattern.sub(replace_cta_secondary_shortcode, md_content)
    return html_output

# Convert custom primary call-to-action shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom CTA primary shortcodes
# Returns:
# - String with CTA primary shortcodes converted to HTML
def convert_cta_shortcode_to_html(md_content):
    cta_shortcode_pattern = re.compile(r'{{%\s+cta-primary\s+"([^"]+)"\s+"([^"]+)"\s+%}}')

    def replace_cta_shortcode(match):
        button_text = match.group(1).strip()
        button_url = match.group(2).strip()
        return f'<div class="cta-primary">' \
               f'    <a href="{button_url}">' \
               f'        <button class="btn btn-primary btn-md mt-2">{button_text}</button>' \
               f'    </a>' \
               f'</div><br>'

    html_output = cta_shortcode_pattern.sub(replace_cta_shortcode, md_content)
    return html_output

# Convert custom KaTeX shortcodes to HTML
# Parameters:
# - input_text: String containing text with custom KaTeX shortcodes
# Returns:
# - String with KaTeX shortcodes converted to HTML
def convert_katex_shortcode_to_html(input_text):
    katex_shortcode_pattern = re.compile(r'{{<katex>}}(.*?){{<\/katex>}}', re.DOTALL)

    def replace_katex_shortcode(match):
        katex_content = match.group(1).replace('"','').strip()
        return f'<span class="katex">{katex_content}</span>'

    html_output = katex_shortcode_pattern.sub(replace_katex_shortcode, input_text)
    return html_output

# Convert fallback code blocks to HTML
# Parameters:
# - md_content: String containing Markdown content with fallback code blocks
# Returns:
# - String with fallback code blocks converted to HTML
def convert_fallback_block_to_html(md_content):
    code_block_pattern = re.compile(r'```(.*?)```', re.DOTALL)

    def replace_code_blocks(match):
        code_content = match.group(1).strip()
        return f'<div class="highlight"><pre class="chroma"><code class="language-fallback" data-lang="fallback">{code_content}</code></pre></div>'

    html_output = code_block_pattern.sub(replace_code_blocks, md_content)
    return html_output

# Convert Markdown tables to HTML
# Parameters:
# - table_md: String containing Markdown table content
# Returns:
# - String with table content converted to HTML
def convert_md_table_to_html(table_md):
    rows = table_md.strip().split('\n')
    html_table = '<table>\n'
    headers = rows[0].split('|')[1:-1]
    html_table += '<tr>' + ''.join(f'<th>{header.strip()}</th>' for header in headers) + '</tr>\n'
    
    for row in rows[2:]:
        columns = row.split('|')[1:-1]
        html_table += '<tr>' + ''.join(f'<td>{column.strip()}</td>' for column in columns) + '</tr>\n'
    html_table += '</table>'
    
    return html_table

# Convert custom table shortcodes to HTML
# Parameters:
# - md_content: String containing Markdown content with custom table shortcodes
# Returns:
# - String with table shortcodes converted to HTML
def convert_tables_to_html(md_content):
    table_pattern = re.compile(r'{{%\s*table\s*%}}(.*?){{%\s*/table\s*%}}', re.DOTALL)
    html_content = re.sub(table_pattern, lambda match: convert_md_table_to_html(match.group(1)), md_content)
    
    return html_content

# Convert Markdown titles to HTML with IDs
# Parameters:
# - md_content: String containing Markdown content with titles
# Returns:
# - String with titles converted to HTML with IDs
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

    title_pattern_h1 = re.compile(r'<h1>(.*?)<\/h1>', re.DOTALL)
    title_pattern_h2 = re.compile(r'<h2>(.*?)<\/h2>', re.DOTALL)
    title_pattern_h3 = re.compile(r'<h3>(.*?)<\/h3>', re.DOTALL)

    md_content = title_pattern_h3.sub(replace_title_h3, md_content)
    md_content = title_pattern_h2.sub(replace_title_h2, md_content)
    md_content = title_pattern_h1.sub(replace_title_h1, md_content)

    return md_content

# Replace image source paths in HTML content
# Parameters:
# - md_content: String containing HTML content with image tags
# Returns:
# - String with updated image source paths
def replace_img_src(md_content):
    soup = BeautifulSoup(md_content, 'html.parser')
    img_tags = soup.find_all('img')

    for img_tag in img_tags:
        src = img_tag.get('src')
        if src:
            filename = src.split('/')[-1]
            new_src = '/static/img/' + filename
            img_tag['src'] = new_src

    md_content_with_new_img_src = str(soup)
    return md_content_with_new_img_src

# Replace video source paths in HTML content
# Parameters:
# - html_content: String containing HTML content with video tags
# Returns:
# - String with updated video source paths
def replace_video_src(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    video_tags = soup.find_all('video')

    for video_tag in video_tags:
        sources = video_tag.find_all('source')
        for source_tag in sources:
            src = source_tag.get('src')
            if src:
                filename = src.split('/')[-1]
                new_src = '/static/img/' + filename
                source_tag['src'] = new_src

    html_content_with_new_video_src = str(soup)
    return html_content_with_new_video_src

# Replace Markdown links with HTML links
# Parameters:
# - md_content: String containing Markdown content with links
# Returns:
# - String with links converted to HTML
def replace_links(md_content):
    root_url = request.host_url.rstrip('/')
    file_extensions = ['.xlsx', '.sh', '.zip', '.bib', '.tex', '.docx', '.bat', '.csv', '.txt', '.rda', '.rdata', '.pptx', '.rmd', '.py', '.r', '.history', '.pdf', '.dta']
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)
        if link_url.startswith('files/'):
            link_url = f'{root_url}/static/{link_url}'
        new_link = f'<a href="{link_url}" alt="{link_text}">{link_text}</a>'
        return new_link

    md_content_with_new_links = re.sub(link_pattern, replace_link, md_content)
    return md_content_with_new_links

# Remove empty <pre><code></code></pre> tags from HTML content
# Parameters:
# - html_content: String containing HTML content
# Returns:
# - String with empty <pre><code></code></pre> tags removed
def remove_empty_pre_code_tags(html_content):
    empty_pre_code_pattern = re.compile(r'<pre><code>\s*</code></pre>')
    cleaned_content = re.sub(empty_pre_code_pattern, '', html_content)
    return cleaned_content

def r_to_html_plaintext(r_content):
    # Escape HTML special characters to display as plain text
    escaped_content = html.escape(r_content)
    # Wrap the content in <pre> and <code> tags for HTML
    html_content = f"<pre><code>{escaped_content}</code></pre>"
    return html_content
# Main function to convert Markdown file content to HTML
# Parameters:
# - md_file_content: String containing Markdown file content
# Returns:
# - String with all shortcodes and Markdown converted to HTML
def htmlize(md_file_content):
    transformations = [
        convert_code_blocks_to_html,
        convert_tips_to_html,
        convert_summary_to_html,
        convert_warning_to_html,
        convert_cta_shortcode_to_html,
        convert_cta_center_shortcode_to_html,
        convert_cta_secondary_center_shortcode_to_html,
        convert_example_shortcode_to_html,
        convert_youtube_shortcode_to_html,
        convert_fallback_block_to_html,
        replace_links,
        convert_md_to_html,
        convert_tables_to_html,
        convert_katex_shortcode_to_html,
        convert_md_titles_to_html,
        replace_img_src,
        replace_video_src,
        remove_empty_pre_code_tags
    ]

    html_content = md_file_content
    for transform_func in transformations:
        html_content = transform_func(html_content)

    return html_content

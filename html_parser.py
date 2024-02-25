import re
from bs4 import BeautifulSoup
import markdown

# Markdown Basic Conversion
def convert_md_to_html(md_content):
    html_content = markdown.markdown(md_content, tab_length=2)
    return html_content

# Shortcodes
def convert_code_blocks_to_html(md_content):
    # Regelmatige expressie om codeblokken in Markdown te matchen
    codeblock_pattern = re.compile(r'{{%\s+codeblock\s+%}}(.*?){{%\s+/codeblock\s+%}}', re.DOTALL)

    # Vervang de codeblokken door hun HTML-equivalenten
    def replace_codeblock(match):
        code_content = match.group(1).strip()
        language_matches = re.finditer(r'```(\w+)(.*?)```', code_content, re.DOTALL)
        code_blocks = []

        tab_nav = []  # Lijst om tabbladnavigatie bij te houden

        for idx, language_match in enumerate(language_matches):
            language = language_match.group(1)
            code = language_match.group(2).strip()
            code = re.sub(r'```', '', code)
            
            # Bepaal of dit het eerste codeblok is
            is_first_codeblock = idx == 0
            
            active_class = ' active' if is_first_codeblock else ''
            highlight_class = 'highlight active' if is_first_codeblock else 'highlight inactive'
            
            code_blocks.append(f'<div class="{highlight_class}" data-language="{language}">\n'
                            f'<pre><code class="language-{language}">\n{code}\n</code></pre>\n'
                            f'</div>\n')

            # Voeg een tabblad toe voor elke taal
            tab_nav.append(f'<li class="nav-item" role="presentation">'
                        f'<a class="nav-link nav-language{active_class}" aria-selected="true" data-language="{language}">{language}</a>'
                        f'</li>')

        code_content = ''.join(code_blocks)

        # Genereer de tabbladnavigatie
        tab_nav_html = f'<ul class="nav nav-tabs mb-3" id="pills-tab" role="tablist">\n' \
                       f'    {" ".join(tab_nav)}\n' \
                       f'</ul>'

        return f'<div class="codeblock">\n' \
            f'<div class="d-flex justify-content-between">\n' \
            f'    {tab_nav_html}\n' \
            f'    <div class="float-right d-flex align-items-center">\n' \
            f'        <a class="copyCodeBtn" href="#0"><img src="/img/copy-code.svg"></a>\n' \
            f'    </div>\n' \
            f'</div>\n' \
            f'    <div class="inner">\n' \
            f'        {code_content}\n' \
            f'    </div>\n' \
            f'</div>'

    md_content = codeblock_pattern.sub(replace_codeblock, md_content)

    return md_content


def convert_tips_to_html(md_content):
    # Definieer een reguliere expressie om de Markdown voorbeeldblokken te matchen
    tipblock_shortcode_pattern = re.compile(r'{{%\s+tip\s+%}}(.*?){{%\s+/tip\s+%}}', re.DOTALL)

    # Vervang de Markdown voorbeeldblokken door de juiste HTML-opmaak
    def replace_tip_shortcode(match):
        
        tip_content = match.group(1)
        html_content = convert_md_to_html(tip_content)

        return f'  <div class="admonition tip">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/tip.svg"> Tip</div>\n' \
            f'     <div class="admonition-content"><p>{html_content}</p></div>' \
            f'     </div>\n'

    # Gebruik de reguliere expressie om de Markdown voorbeeldblokken te vervangen
    html_output = tipblock_shortcode_pattern.sub(replace_tip_shortcode, md_content)

    return html_output

def convert_summary_to_html(md_content):
    # Definieer een reguliere expressie om de Markdown voorbeeldblokken te matchen
    summaryblock_pattern = re.compile(r'{{%\s+summary\s+%}}(.*?){{%\s+/summary\s+%}}', re.DOTALL)

    # Vervang de Markdown voorbeeldblokken door de juiste HTML-opmaak
    def replace_summary_shortcode(match):
        
        summary_content = match.group(1)
        html_content = convert_md_to_html(summary_content)

        return f'  <div class="admonition summary">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/summary.svg"> Summary</div>\n' \
            f'     <div class="admonition-content"><p>{html_content}</p></div>' \
            f'     </div>\n' \

    # Gebruik de reguliere expressie om de Markdown voorbeeldblokken te vervangen
    html_output = summaryblock_pattern.sub(replace_summary_shortcode, md_content)

    return html_output

def convert_warning_to_html(md_content):
    # Definieer een reguliere expressie om de Markdown voorbeeldblokken te matchen
    warningblock_pattern = re.compile(r'{{%\s+warning\s+%}}(.*?){{%\s+/warning\s+%}}', re.DOTALL)

    # Vervang de Markdown voorbeeldblokken door de juiste HTML-opmaak
    def replace_warning_shortcode(match):
        
        warning_content = match.group(1)
        html_content = convert_md_to_html(warning_content)

        return f'  <div class="admonition warning">' \
            f'     <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/warning.svg"> Warning</div>\n' \
            f'     <div class="admonition-content"><p>{html_content}</p></div>' \
            f'     </div>\n' \

    # Gebruik de reguliere expressie om de Markdown voorbeeldblokken te vervangen
    html_output = warningblock_pattern.sub(replace_warning_shortcode, md_content)

    return html_output

def convert_example_shortcode_to_html(md_content):
    # Definieer een reguliere expressie om de Markdown voorbeeldblokken te matchen
    example_shortcode_pattern = re.compile(r'{{%\s+example\s+%}}(.*?){{%\s+/example\s+%}}', re.DOTALL)

    # Vervang de Markdown voorbeeldblokken door de juiste HTML-opmaak
    def replace_example_shortcode(match):
        
        example_content = match.group(1)
        html_content = convert_md_to_html(example_content)

        return f'<div class="admonition example">\n' \
               f'    <div class="font-weight-bold mb-3"><img class="align-bottom mr-2" src="/img/example.svg" width="20px"> Example</div>\n' \
               f'    <div class="admonition-content">{html_content}</div>\n' \
               f'</div>'

    # Gebruik de reguliere expressie om de Markdown voorbeeldblokken te vervangen
    html_output = example_shortcode_pattern.sub(replace_example_shortcode, md_content)

    return html_output

def convert_youtube_shortcode_to_html(md_content):
    # Definieer een reguliere expressie om YouTube-shortcodes te matchen
    youtube_shortcode_pattern = re.compile(r'{{<\s*youtube\s+(.*?)\s+iframe-video-margins\s*>}}')

    # Vervang de Markdown voorbeeldblokken door de juiste HTML-opmaak
    def replace_youtube_shortcode(match):
        
        youtube_content = match.group(1)

        return f'<div class="iframe-video-margins">\n' \
               f'  <iframe src="https://www.youtube.com/embed/{youtube_content}" ' \
               f'allowfullscreen="" title="YouTube Video"></iframe>\n' \
               f'</div>\n'

    # Gebruik de reguliere expressie om de Markdown voorbeeldblokken te vervangen
    html_output = youtube_shortcode_pattern.sub(replace_youtube_shortcode, md_content)

    return html_output

def convert_cta_center_shortcode_to_html(md_content):
    # Definieer een reguliere expressie om de shortcode te matchen
    cta_shortcode_pattern = re.compile(r'{{%\s+cta-primary-center\s+"([^"]+)"\s+"([^"]+)"\s+%}}')

    # Vervang de shortcode door de juiste HTML-opmaak
    def replace_cta_shortcode(match):
        button_text = match.group(1).strip()
        button_url = match.group(2).strip()

        return f'<div class="cta-primary" style="text-align:center;">' \
               f'    <a href="{button_url}">' \
               f'        <button class="btn btn-primary btn-md mt-2">{button_text}</button>' \
               f'    </a>' \
               f'</div><br>'

    # Gebruik de reguliere expressie om de shortcode te vervangen
    html_output = cta_shortcode_pattern.sub(replace_cta_shortcode, md_content)

    return html_output

def convert_cta_shortcode_to_html(md_content):
    # Definieer een reguliere expressie om de shortcode te matchen
    cta_shortcode_pattern = re.compile(r'{{%\s+cta-primary\s+"([^"]+)"\s+"([^"]+)"\s+%}}')

    # Vervang de shortcode door de juiste HTML-opmaak
    def replace_cta_shortcode(match):
        button_text = match.group(1).strip()
        button_url = match.group(2).strip()

        return f'<div class="cta-primary">' \
               f'    <a href="{button_url}">' \
               f'        <button class="btn btn-primary btn-md mt-2">{button_text}</button>' \
               f'    </a>' \
               f'</div><br>'

    # Gebruik de reguliere expressie om de shortcode te vervangen
    html_output = cta_shortcode_pattern.sub(replace_cta_shortcode, md_content)

    return html_output

def convert_katex_shortcode_to_html(input_text):
    # Definieer een reguliere expressie om KaTeX-shortcodes te matchen (over meerdere regels)
    katex_shortcode_pattern = re.compile(r'{{<katex>}}(.*?){{<\/katex>}}', re.DOTALL)

    # Vervang de KaTeX-shortcodes door de juiste HTML-opmaak
    def replace_katex_shortcode(match):
        katex_content = match.group(1).replace('"','').strip()

        return f'<span class="katex">{katex_content}</span>'

    # Gebruik de reguliere expressie om de KaTeX-shortcodes te vervangen
    html_output = katex_shortcode_pattern.sub(replace_katex_shortcode, input_text)

    return html_output

def convert_fallback_block_to_html(md_content):
    # Definieer een reguliere expressie om Markdown-codeblokken te matchen
    code_block_pattern = re.compile(r'```(.*?)```', re.DOTALL)

    # Vervang de Markdown-codeblokken door de juiste HTML-opmaak
    def replace_code_blocks(match):
        code_content = match.group(1).strip()
        return f'<div class="highlight"><pre class="chroma"><code class="language-fallback" data-lang="fallback">{code_content}</code></pre></div>'

    # Gebruik de reguliere expressie om de Markdown-codeblokken te vervangen
    html_output = code_block_pattern.sub(replace_code_blocks, md_content)

    return html_output

# Extra HTML Functions
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

def replace_video_src(html_content):
    # Parse de HTML-inhoud met BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Zoek alle <video> tags in de geparseerde inhoud
    video_tags = soup.find_all('video')

    for video_tag in video_tags:
        sources = video_tag.find_all('source')
        for source_tag in sources:
            src = source_tag.get('src')
            if src:
                # Pak alleen de bestandsnaam (laatste deel na /)
                filename = src.split('/')[-1]
                # Vervang de src door de gewenste bronindeling
                new_src = '/static/img/' + filename
                source_tag['src'] = new_src

    # Converteer de aangepaste inhoud terug naar een string
    html_content_with_new_video_src = str(soup)

    return html_content_with_new_video_src

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

    return md_content_with_new_links

# Html Parse Function
def htmlize(md_file_content):
    transformations = [
        convert_code_blocks_to_html,
        convert_tips_to_html,
        convert_summary_to_html,
        convert_warning_to_html,
        convert_cta_shortcode_to_html,
        convert_cta_center_shortcode_to_html,
        convert_example_shortcode_to_html,
        convert_youtube_shortcode_to_html,
        convert_fallback_block_to_html,
        convert_md_to_html,
        replace_links,
        convert_katex_shortcode_to_html,
        convert_md_titles_to_html,
        replace_img_src,
        replace_video_src
    ]

    html_content = md_file_content
    for transform_func in transformations:
        html_content = transform_func(html_content)

    return html_content
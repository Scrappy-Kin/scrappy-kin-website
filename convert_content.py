#!/usr/bin/env python3
"""
Convert markdown content files to HTML for Scrappy Kin website
"""

import re
from pathlib import Path

def markdown_to_html(md_text):
    """Convert simple markdown to HTML"""
    html = md_text
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h2 class="text-3xl font-bold mb-4 mt-8">\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h3 class="text-2xl font-semibold mb-3 mt-6">\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h4 class="text-xl font-semibold mb-2 mt-4">\1</h4>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Convert bare URLs to clickable links (but not if already in markdown link format or HTML)
    # Match URLs that aren't already wrapped in <a> tags or markdown []()
    html = re.sub(r'(?<!["\(>])https?://[^\s<>\)]+(?!["\)<])', r'<a href="\g<0>" target="_blank" rel="noopener noreferrer">\g<0></a>', html)
    
    # Tables - process before lists and paragraphs
    lines = html.split('\n')
    result = []
    in_table = False
    table_rows = []
    
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and line.strip().endswith('|'):
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(line)
            # Check if next line is separator or end of table
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if not (next_line.startswith('|') and next_line.endswith('|')):
                    # End of table
                    result.append(convert_table(table_rows))
                    in_table = False
                    table_rows = []
            else:
                # Last line
                result.append(convert_table(table_rows))
                in_table = False
        else:
            if in_table:
                result.append(convert_table(table_rows))
                in_table = False
                table_rows = []
            result.append(line)
    
    html = '\n'.join(result)
    
    # Lists - unordered
    lines = html.split('\n')
    in_list = False
    result = []
    for line in lines:
        if line.strip().startswith('- '):
            if not in_list:
                result.append('<ul class="list-disc pl-6 mb-4 space-y-2">')
                in_list = True
            content = line.strip()[2:]
            result.append(f'<li>{content}</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            result.append(line)
    if in_list:
        result.append('</ul>')
    html = '\n'.join(result)
    
    # Paragraphs (but not HTML tags or table markers)
    html = re.sub(r'^(?!<|---|>|\|)([^<>]+)$', r'<p class="mb-4">\1</p>', html, flags=re.MULTILINE)
    
    # Horizontal rules
    html = re.sub(r'^---$', r'<hr class="my-8 border-gray-300">', html, flags=re.MULTILINE)
    
    # Clean up empty paragraphs
    html = re.sub(r'<p class="mb-4"></p>', '', html)
    html = re.sub(r'<p class="mb-4">\s*</p>', '', html)
    
    return html

def convert_table(table_rows):
    """Convert markdown table rows to HTML table"""
    if not table_rows:
        return ''
    
    # Parse table
    header_row = None
    data_rows = []
    
    for i, row in enumerate(table_rows):
        cells = [cell.strip() for cell in row.strip('|').split('|')]
        if i == 0:
            header_row = cells
        elif i == 1 and all(set(cell.strip()) <= {'-', ':', ' '} for cell in cells):
            # Skip separator row
            continue
        else:
            data_rows.append(cells)
    
    # Build HTML
    html = '<div class="overflow-x-auto my-6">\n'
    html += '<table class="min-w-full border-collapse border border-gray-300">\n'
    
    # Header
    if header_row:
        html += '<thead class="bg-gray-100">\n<tr>\n'
        for cell in header_row:
            html += f'<th class="border border-gray-300 px-4 py-2 text-left font-semibold">{cell}</th>\n'
        html += '</tr>\n</thead>\n'
    
    # Body
    if data_rows:
        html += '<tbody>\n'
        for row in data_rows:
            html += '<tr>\n'
            for cell in row:
                html += f'<td class="border border-gray-300 px-4 py-2">{cell}</td>\n'
            html += '</tr>\n'
        html += '</tbody>\n'
    
    html += '</table>\n</div>'
    return html

def create_tos_html():
    """Create TOS HTML page"""
    tos_md = Path('content/TERMS_OF_SERVICE.md').read_text()
    
    # Remove title (we'll add it in HTML)
    tos_md = re.sub(r'^# Terms of Service\n\n', '', tos_md)
    
    tos_html = markdown_to_html(tos_md)
    
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service - Scrappy Kin</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <a href="/" class="text-2xl font-bold text-gray-900">Scrappy Kin</a>
                </div>
                <div class="flex items-center space-x-8">
                    <a href="/tos.html" class="text-gray-900 font-semibold">Terms of Service</a>
                    <a href="/privacy.html" class="text-gray-600 hover:text-gray-900 transition">Privacy Policy</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">Terms of Service</h1>
        
        <div class="prose prose-lg max-w-none text-gray-700">
{tos_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="flex justify-between items-center">
                <p class="text-gray-600">&copy; 2025 Scrappy Kin. All rights reserved.</p>
                <div class="flex space-x-6">
                    <a href="/tos.html" class="text-gray-900 font-semibold">Terms</a>
                    <a href="/privacy.html" class="text-gray-600 hover:text-gray-900 transition">Privacy</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="/js/main.js"></script>
</body>
</html>'''
    
    Path('public/tos.html').write_text(template)
    print("✓ Created tos.html")

def create_privacy_html():
    """Create Privacy Policy HTML page"""
    privacy_md = Path('content/PRIVACY_POLICY.md').read_text()
    
    # Remove title (we'll add it in HTML)
    privacy_md = re.sub(r'^# Privacy Policy\n\n', '', privacy_md)
    
    privacy_html = markdown_to_html(privacy_md)
    
    template = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy - Scrappy Kin</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body class="bg-gray-50">
    <!-- Navigation -->
    <nav class="bg-white shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16">
                <div class="flex items-center">
                    <a href="/" class="text-2xl font-bold text-gray-900">Scrappy Kin</a>
                </div>
                <div class="flex items-center space-x-8">
                    <a href="/tos.html" class="text-gray-600 hover:text-gray-900 transition">Terms of Service</a>
                    <a href="/privacy.html" class="text-gray-900 font-semibold">Privacy Policy</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h1 class="text-4xl font-bold text-gray-900 mb-8">Privacy Policy</h1>
        
        <div class="prose prose-lg max-w-none text-gray-700">
{privacy_html}
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-gray-200 mt-20">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div class="flex justify-between items-center">
                <p class="text-gray-600">&copy; 2025 Scrappy Kin. All rights reserved.</p>
                <div class="flex space-x-6">
                    <a href="/tos.html" class="text-gray-600 hover:text-gray-900 transition">Terms</a>
                    <a href="/privacy.html" class="text-gray-900 font-semibold">Privacy</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="/js/main.js"></script>
</body>
</html>'''
    
    Path('public/privacy.html').write_text(template)
    print("✓ Created privacy.html")

if __name__ == '__main__':
    create_tos_html()
    create_privacy_html()
    print("\n✅ All HTML files generated successfully!")

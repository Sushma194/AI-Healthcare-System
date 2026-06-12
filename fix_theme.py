from pathlib import Path

base = Path('AI_Healthcare_System')
for path in [base / 'app.py', *sorted((base / 'pages').glob('*.py'))]:
    text = path.read_text(encoding='utf-8')
    if 'def load_theme()' in text:
        continue

    lines = text.splitlines()
    i = 0
    while i < len(lines) and (lines[i].startswith('import ') or lines[i].startswith('from ') or not lines[i].strip()):
        i += 1

    insert = [
        '',
        'def load_theme():',
        '    with open("assets/styles.css", "r", encoding="utf-8") as f:',
        '        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)',
        '',
        'load_theme()',
        ''
    ]

    if 'import streamlit as st' not in text:
        lines = ['import streamlit as st'] + lines
        i += 1

    new_text = '\n'.join(lines[:i] + insert + lines[i:])
    path.write_text(new_text, encoding='utf-8')

import sys
import os
import json
import re
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

class PyBat:
    def __init__(self):
        self.console = Console()
        # Primary: J2_ROOT env var | Fallback: ~/.j2
        self.j2_root = os.environ.get('J2_ROOT', os.path.expanduser("~/.j2"))
        self.syntax_file = os.path.join(self.j2_root, 'python', 'syntax.json')
        self.syntax_rules = self._load_syntax(self.syntax_file)

    def _load_syntax(self, path):
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                self.console.print(f"[yellow]Warning: Syntax load error: {e}[/yellow]")
        return {}

    def apply_highlight(self, code, extension, filename):
        rule = self.syntax_rules.get(filename, self.syntax_rules.get(extension, {}))
        while "copy_from" in rule:
            rule = self.syntax_rules.get(rule["copy_from"], {})

        text = Text(code)
        if not rule: return text
        colors = rule.get("color_map", {})

        # 1. Tags (XML Style)
        if extension in ['.qrc', '.vcxproj', '.xml']:
            text.highlight_regex(r'<[^>]+>', colors.get("keywords", "bold bright blue"))
        else:
            # 2. Keywords & Builtins
            if "keywords" in rule:
                kw_pattern = r'\b(' + '|'.join(map(re.escape, rule["keywords"])) + r')\b'
                text.highlight_regex(kw_pattern, colors.get("keywords", "bold bright magenta"))

            # Built-ins
            if "builtins" in rule:
                bi_pattern = r'\b(' + '|'.join(map(re.escape, rule["builtins"])) + r')\b'
                text.highlight_regex(bi_pattern, colors.get("builtins", "bright cyan"))

        # 3. Variables (New Logic for Shell Scripts)
        if extension in ['.bat', '.cmd']:
            text.highlight_regex(r'%[\w~:$!%]+%?', "italic bright blue")
        elif extension in ['.sh', '.zsh', '.fish', '.csh']:
            text.highlight_regex(r'\$[\w{}#?*!@-]+', "italic bright blue")

        # 4. Strings
        text.highlight_regex(r'".*?"|\'.*?\'', colors.get("string", "bright yellow"))

        # 5. Comments (Context Aware)
        if extension in ['.bat', '.cmd']:
            text.highlight_regex(r'(?i)^\s*rem\s+.*$', colors.get("comment", "dim green"))
            text.highlight_regex(r'^\s*::.*$', colors.get("comment", "dim green"))
        elif extension in ['.qrc', '.vcxproj']:
            text.highlight_regex(r'', colors.get("comment", "dim green"))
        elif extension in ['.py', '.pro', '.cmake'] or filename in ['Makefile', 'CMakeLists.txt', 'env.bash', 'env.sh']:
            text.highlight_regex(r'#.*$', colors.get("comment", "dim green"))
        else:
            text.highlight_regex(r'//.*$', colors.get("comment", "dim green"))
            text.highlight_regex(r'/\*.*?\*/', colors.get("comment", "dim green"))

        return text

    def display(self, filepath):
        if not os.path.isfile(filepath):
            self.console.print(f"[bold red]Error:[/bold red] File not found: {filepath}")
            return
        fname = os.path.basename(filepath)
        ext = os.path.splitext(fname)[1].lower()
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            highlighted = self.apply_highlight(content, ext, fname)
            final_text = Text()
            lines = highlighted.split('\n')
            for i, line in enumerate(lines, 1):
                final_text.append(f"{i:3} │ ", style="dim")
                final_text.append(line)
                if i < len(lines): final_text.append("\n")
            self.console.print(Panel(final_text, title=f"[bold cyan]{fname}[/bold cyan]", border_style="blue", title_align="left"))
        except Exception as e:
            self.console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: pybat <filename>")
    else: PyBat().display(sys.argv[1])
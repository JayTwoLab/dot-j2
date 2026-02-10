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
        """Loads syntax configuration safely."""
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                self.console.print(f"[yellow]Warning: Syntax load error: {e}[/yellow]")
        return {}

    def apply_highlight(self, code, extension, filename):
        """Processes text and applies styles based on matched rules."""
        # Match by filename (e.g., Makefile) or extension
        rule = self.syntax_rules.get(filename, self.syntax_rules.get(extension, {}))
        
        # Resolve 'copy_from' links
        while "copy_from" in rule:
            rule = self.syntax_rules.get(rule["copy_from"], {})

        text = Text(code)
        if not rule:
            return text

        colors = rule.get("color_map", {})

        # 1. XML/Tag Highlighting (Special handling for tags)
        if extension in ['.qrc', '.vcxproj', '.xml']:
            text.highlight_regex(r'<[^>]+>', colors.get("keywords", "bold blue"))
        else:
            # Standard Keywords & Built-ins
            for key in ["keywords", "builtins"]:
                if key in rule:
                    pattern = r'\b(' + '|'.join(map(re.escape, rule[key])) + r')\b'
                    text.highlight_regex(pattern, colors.get(key, "bold"))

        # 2. Strings
        text.highlight_regex(r'".*?"|\'.*?\'', colors.get("string", "yellow"))

        # 3. Context-Aware Comments
        # Define patterns
        hash_comment = [r'#.*$']
        c_comment = [r'//.*$', r'/\*.*?\*/']
        xml_comment = [r'']

        if extension in ['.py', '.pro', '.cmake'] or filename in ['Makefile', 'CMakeLists.txt']:
            patterns = hash_comment
        elif extension in ['.qrc', '.vcxproj']:
            patterns = xml_comment
        else:
            patterns = c_comment

        for p in patterns:
            text.highlight_regex(p, colors.get("comment", "dim green"))

        return text

    def display(self, filepath):
        """Reads file and prints styled output in a panel."""
        if not os.path.isfile(filepath):
            self.console.print(f"[bold red]Error:[/bold red] File not found: [white]{filepath}[/white]")
            return

        fname = os.path.basename(filepath)
        ext = os.path.splitext(fname)[1].lower()
        
        try:
            # Read with replacement for broken encodings
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            
            highlighted = self.apply_highlight(content, ext, fname)
            
            # Combine with line numbers
            final_text = Text()
            lines = highlighted.split('\n')
            for i, line in enumerate(lines, 1):
                final_text.append(f"{i:3} │ ", style="dim")
                final_text.append(line)
                if i < len(lines):
                    final_text.append("\n")

            # Final Panel Output
            self.console.print(Panel(
                final_text, 
                title=f"[bold cyan]{fname}[/bold cyan]", 
                # subtitle=f"[dim]Root: {self.j2_root}[/dim]",
                title_align="left",
                border_style="blue"
            ))
        except Exception as e:
            self.console.print(f"[bold red]Critical Error:[/bold red] {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: pybat <filename>")
    else:
        PyBat().display(sys.argv[1])
        
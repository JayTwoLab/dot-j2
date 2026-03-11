import os
import json
import time
import configparser
import psutil
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def load_config():
    config = configparser.ConfigParser()
    
    # Get the directory where the script is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(base_path, 'process_config.ini')
    
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"'{config_file}' not found at {config_file}")
        
    config.read(config_file, encoding='utf-8')
    interval = int(config['SETTINGS']['check_interval'])
    
    # Also resolve the JSON file path relative to the script directory
    json_filename = config['SETTINGS']['process_list_file']
    json_file = os.path.join(base_path, json_filename)
    
    theme = config['SETTINGS'].get('theme', 'dark').lower()
    return interval, json_file, theme

def load_process_list(json_file):
    if not os.path.exists(json_file):
        raise FileNotFoundError(f"Process list file not found at {json_file}")
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_theme_colors(theme):
    if theme == 'light':
        return [Fore.BLACK, Fore.BLUE, Fore.RED, Fore.MAGENTA, Fore.GREEN]
    else:
        return [Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA, Fore.LIGHTBLUE_EX]

def assign_group_colors(process_targets, theme_colors):
    group_color_map = {}
    unique_groups = list(dict.fromkeys([t.get('group', 'DEFAULT') for t in process_targets]))
    
    for i, group in enumerate(unique_groups):
        group_color_map[group] = theme_colors[i % len(theme_colors)]
    
    return group_color_map

def check_processes(process_targets, group_colors):
    running_processes = []
    for proc in psutil.process_iter(['name', 'cmdline']):
        try:
            running_processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"\n[Check Time: {current_time}]")
    print("-" * 65)
    print(f"{'GROUP':<15} | {'PROCESS NAME':<25} | {'STATUS'}")
    print("-" * 65)

    for target in process_targets:
        group = target.get('group', 'DEFAULT')
        name = target.get('name')
        arg = target.get('arg')
        color = group_colors.get(group, Fore.WHITE)

        count = 0
        for p in running_processes:
            if p['name'] == name:
                if arg:
                    cmdline_str = " ".join(p['cmdline']) if p['cmdline'] else ""
                    if arg in cmdline_str:
                        count += 1
                else:
                    count += 1

        status = f"O ({count})" if count > 0 else "X"
        arg_display = f" ({arg})" if arg else ""
        
        line = f"[{group:13}] | {name + arg_display:<25} | {status}"
        print(f"{color}{line}{Style.RESET_ALL}")

def main():
    try:
        interval, json_file, theme = load_config()
        process_targets = load_process_list(json_file)
        
        theme_colors = get_theme_colors(theme)
        group_colors = assign_group_colors(process_targets, theme_colors)

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            check_processes(process_targets, group_colors)
            print(f"\n(Theme: {theme.upper()} | Interval: {interval}s | Press Ctrl+C to exit)")
            time.sleep(interval)
            
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except KeyError as e:
        print(f"Error: Invalid format in process_config.ini. {e}")
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()
    
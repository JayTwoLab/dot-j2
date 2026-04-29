# dot-j2

> [Korean](README.ko.md)

- Provides environment configuration scripts (`env.*`) that can be used across various shell environments.
- Each script sets environment variables based on the `.j2` directory, helping to maintain a consistent execution environment for the project.

## Environment Setup by Shell

- Below are the environment configuration files and how to apply them for each OS/shell.

### 1. Bash (Linux/macOS)
- File: `.j2/env.sh`
- Usage:
  ```sh
  cd .j2
  source env.sh
  ```

### 2. Zsh (Linux/macOS)
- File: `.j2/env.zsh`
- Usage:
  ```zsh
  cd .j2
  source env.zsh
  ```

### 3. Ksh (KornShell)
- File: `.j2/env.ksh`
- Usage:
  ```ksh
  cd .j2
  . env.ksh
  ```

### 4. Fish Shell
- File: `.j2/env.fish`
- Usage:
  ```fish
  cd .j2
  source env.fish
  ```

### 5. Csh (C Shell)
- File: `.j2/env.csh`
- Usage:
  ```csh
  cd .j2
  source env.csh
  ```

### 6. PowerShell (Windows)
- File: `.j2/env.ps1`
- Usage:
  ```powershell
  cd .j2
  . .\env.ps1
  ```

### 7. Batch (Windows CMD)
- File: `.j2/env.bat`
- Usage:
  ```cmd
  cd .j2
  .\env.bat
  ```

## Common Behavior
- Each script sets the `J2_ROOT` environment variable based on the current directory.
- Adds `.j2/bin` and `.j2/lib` to `PATH` and `LD_LIBRARY_PATH` (or `PATH` on Windows).
- Displays a warning message if the `.j2` directory does not exist.
- After applying the environment, prints "J2 Environment Activated." along with the current `J2_ROOT` path.

## Notes
- Each script only works in its respective shell. Use the appropriate file for your environment.
- To apply the environment settings permanently, you can add the commands above to your shell profile (e.g., `.bashrc`, `.zshrc`, etc.).

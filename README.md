# dot-j2

- 이 저장소는 다양한 쉘 환경에서 사용할 수 있는 환경 설정 스크립트(`env.*`)를 제공합니다. 
- 각 스크립트는 `.j2` 디렉터리를 기준으로 환경 변수를 설정하여, 프로젝트의 실행 환경을 일관되게 구성할 수 있도록 도와줍니다.

## 환경별 설정 방법

- 아래는 각 운영체제/쉘 환경에 맞는 환경 설정 파일과 적용 방법입니다.

### 1. Bash (Linux/macOS)
- 파일: `.j2/env.sh`
- 적용 방법:
  ```sh
  cd .j2
  source env.sh
  ```

### 2. Zsh (Linux/macOS)
- 파일: `.j2/env.zsh`
- 적용 방법:
  ```zsh
  cd .j2
  source env.zsh
  ```

### 3. Ksh (KornShell)
- 파일: `.j2/env.ksh`
- 적용 방법:
  ```ksh
  cd .j2
  . env.ksh
  ```

### 4. Fish Shell
- 파일: `.j2/env.fish`
- 적용 방법:
  ```fish
  cd .j2
  source env.fish
  ```

### 5. Csh (C Shell)
- 파일: `.j2/env.csh`
- 적용 방법:
  ```csh
  cd .j2
  source env.csh
  ```

### 6. PowerShell (Windows)
- 파일: `.j2/env.ps1`
- 적용 방법:
  ```powershell
  cd .j2
  . .\env.ps1
  ```

### 7. Batch (Windows CMD)
- 파일: `.j2/env.bat`
- 적용 방법:
  ```cmd
  cd .j2
  .\env.bat
  ```

## 공통 동작
- 각 스크립트는 현재 디렉터리를 기준으로 `J2_ROOT` 환경 변수를 설정합니다.
- `PATH`와 `LD_LIBRARY_PATH`(또는 Windows의 경우 `PATH`)에 `.j2/bin` 및 `.j2/lib`를 추가합니다.
- `.j2` 디렉터리가 없을 경우 경고 메시지를 출력합니다.
- 환경 적용 후, "J2 Environment Activated."와 현재 `J2_ROOT` 경로를 출력합니다.

## 참고
- 각 스크립트는 해당 쉘에서만 동작합니다. 자신의 환경에 맞는 파일을 사용하세요.
- 환경 설정을 영구적으로 적용하려면, 각자의 쉘 프로필(`.bashrc`, `.zshrc` 등)에 위 명령을 추가할 수 있습니다.

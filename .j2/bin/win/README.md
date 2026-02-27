# Windows 환경 설정 안내

이 폴더는 Windows 환경에서 dot-j2 프로젝트를 사용할 때 필요한 환경 설정 스크립트와 관련 정보를 제공합니다.

## 환경 설정 방법

아래는 Windows 환경에서 사용할 수 있는 환경 설정 파일과 적용 방법입니다.

### 1. PowerShell
- 파일: `.j2/env.ps1`
- 적용 방법:
  ```powershell
  cd ..\..
  cd .j2
  .\env.ps1
  ```

### 2. Batch (CMD)
- 파일: `.j2/env.bat`
- 적용 방법:
  ```cmd
  cd ..\..
  cd .j2
  env.bat
  ```

## 공통 동작
- 각 스크립트는 현재 디렉터리를 기준으로 `J2_ROOT` 환경 변수를 설정합니다.
- `PATH`에 `.j2\bin` 및 `.j2\lib`를 추가합니다.
- `.j2` 디렉터리가 없을 경우 경고 메시지를 출력합니다.
- 환경 적용 후, "J2 Environment Activated."와 현재 `J2_ROOT` 경로를 출력합니다.

## 참고
- 각 스크립트는 해당 쉘에서만 동작합니다. 자신의 환경에 맞는 파일을 사용하세요.
- 환경 설정을 영구적으로 적용하려면, PowerShell 프로필 또는 CMD의 자동 실행 배치 파일에 위 명령을 추가할 수 있습니다.

---

# Windows용 eza 명령어 래퍼 안내

이 폴더에는 Windows 환경에서 [eza](https://github.com/eza-community/eza) 명령어를 다양한 옵션으로 실행할 수 있도록 만든 배치 파일(cmd) 래퍼들이 포함되어 있습니다.

각 파일은 eza 명령어를 편리하게 호출할 수 있도록 옵션을 미리 지정해두었으며, 디렉터리/파일 목록을 다양한 방식으로 출력할 수 있습니다.

## 파일별 설명 및 사용법

### 1. ela.cmd
- 기능: eza를 간단한 목록 형태로 출력하며, 아이콘, git 정보, 디렉터리 우선 정렬을 포함합니다.
- 실행 예:
  ```cmd
  ela.cmd [옵션/경로]
  ```
- 내부 명령:
  ```bat
  eza -abgh --icons --git --group-directories-first %*
  ```

### 2. elh.cmd
- 기능: eza를 상세 목록(-l)과 전체(-a), 아이콘, 총 크기, 디렉터리 우선 정렬로 출력합니다.
- 실행 예:
  ```cmd
  elh.cmd [옵션/경로]
  ```
- 내부 명령:
  ```bat
  eza -a -l --icons --total-size --group-directories-first %*
  ```

### 3. ell.cmd
- 기능: eza를 전체(-a), 상세(-l), git 정보, 사용자 정보, 아이콘, 디렉터리 우선 정렬로 출력합니다.
- 실행 예:
  ```cmd
  ell.cmd [옵션/경로]
  ```
- 내부 명령:
  ```bat
  eza -alghu --icons --git --group-directories-first %*
  ```

### 4. els.cmd
- 기능: eza를 전체(-a), 아이콘, 디렉터리 우선 정렬로 출력합니다. (주석된 옵션 참고)
- 실행 예:
  ```cmd
  els.cmd [옵션/경로]
  ```
- 내부 명령:
  ```bat
  eza -a --icons --group-directories-first %*
  ```

### 5. elt.cmd
- 기능: eza를 트리 형태로 2단계까지 출력하며, 아이콘을 포함합니다.
- 실행 예:
  ```cmd
  elt.cmd [옵션/경로]
  ```
- 내부 명령:
  ```bat
  eza -a --tree --level=2 --icons %*
  ```

## 참고
- 모든 .cmd 파일은 eza가 PATH에 등록되어 있어야 정상 동작합니다.
- 추가 옵션은 각 .cmd 파일에 인자로 전달할 수 있습니다.
- eza 설치 및 사용법은 공식 문서를 참고하세요.

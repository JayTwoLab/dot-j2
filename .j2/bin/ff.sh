#!/bin/bash
dir="$1"

# Usage: ff.sh [options] <directory> <regex>
#   -d: search directories only
#   -f: search files only (default)
#   -name <pattern>: glob filename match (e.g. '*.txt')
#   -iname <pattern>: case-insensitive glob filename match
#   -size <n>: file size (e.g. +10M, -1k)
#   -mtime <n>: modified time in days (e.g. -1, +7)
#   -maxdepth <n>: max search depth
#   -mindepth <n>: min search depth
#   -perm <mode>: permission bits (e.g. 755, -u+x)
#   -user <name>: owner
#   -group <name>: group
#   -empty: empty files/dirs
#   -exec <cmd>: execute command (use '{}' for file)
#   -o <find-args>: custom find options (quoted)
# Finds files or directories in <directory> matching <regex> (regular expression for name)

usage() {
  echo "Usage: $0 [options] <directory> <regex>"
  echo "  -d: search directories only"
  echo "  -f: search files only (default)"
  echo "  -name <pattern>: glob filename match (e.g. '*.txt')"
  echo "  -iname <pattern>: case-insensitive glob filename match"
  echo "  -size <n>: file size (e.g. +10M, -1k)"
  echo "  -mtime <n>: modified time in days (e.g. -1, +7)"
  echo "  -maxdepth <n>: max search depth"
  echo "  -mindepth <n>: min search depth"
  echo "  -perm <mode>: permission bits (e.g. 755, -u+x)"
  echo "  -user <name>: owner"
  echo "  -group <name>: group"
  echo "  -empty: empty files/dirs"
  echo "  -exec <cmd>: execute command (use '{}' for file)"
  echo "  -o <find-args>: custom find options (quoted)"
  exit 1
}

# Default search type
find_type="-type f"
find_args=()
custom_find_args=""

# Option parsing
while [[ $# -gt 0 ]]; do
  case "$1" in
    -d)
      find_type="-type d"; shift ;;
    -f)
      find_type="-type f"; shift ;;
    -name)
      find_args+=( -name "$2" ); shift 2 ;;
    -iname)
      find_args+=( -iname "$2" ); shift 2 ;;
    -size)
      find_args+=( -size "$2" ); shift 2 ;;
    -mtime)
      find_args+=( -mtime "$2" ); shift 2 ;;
    -maxdepth)
      find_args+=( -maxdepth "$2" ); shift 2 ;;
    -mindepth)
      find_args+=( -mindepth "$2" ); shift 2 ;;
    -perm)
      find_args+=( -perm "$2" ); shift 2 ;;
    -user)
      find_args+=( -user "$2" ); shift 2 ;;
    -group)
      find_args+=( -group "$2" ); shift 2 ;;
    -empty)
      find_args+=( -empty ); shift ;;
    -exec)
      find_args+=( -exec "$2" {} \; ); shift 2 ;;
    -o)
      custom_find_args="$2"; shift 2 ;;
    --)
      shift; break ;;
    -h|--help)
      usage ;;
    *)
      break ;;
  esac
done

# Now, the remaining args should be <directory> <regex>
if [ "$#" -ne 2 ]; then
  usage
fi

dir="$1"
regex="$2"

if [ -n "$custom_find_args" ]; then
  eval find "$dir" $find_type "${find_args[@]}" $custom_find_args | grep -E "$regex"
else
  find "$dir" $find_type "${find_args[@]}" | grep -E "$regex"
fi

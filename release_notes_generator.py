import argparse
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# Regex to parse Conventional Commits: type(scope): description
COMMIT_PATTERN = re.compile(r'^(\w+)(?:\(([^)]+)\))?:\s*(.+)$')

# Mapping commit types to human-readable section headers
TYPE_MAP = {
    'feat': 'New Features',
    'fix': 'Bug Fixes',
    'docs': 'Documentation',
    'style': 'Styles',
    'refactor': 'Code Refactoring',
    'perf': 'Performance Improvements',
    'test': 'Tests',
    'chore': 'Chores',
    'build': 'Build System',
    'ci': 'CI/CD'
}

def get_git_log(repo_path, range_spec):
    """
    Runs git log and returns raw output.
    range_spec example: 'v1.0.0..HEAD' or 'HEAD'
    """
    cmd = ["git", "-C", str(repo_path), "log", "--pretty=format:%s", range_spec]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        return output.decode('utf-8').split('\n')
    except subprocess.CalledProcessError as e:
        print(f"Error running git log: {e.output.decode()}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'git' command not found. Is it installed?")
        sys.exit(1)


def parse_commits(commit_lines):
    """
    Parses lines into categories based on Conventional Commits.
    Returns a dict: {category: [list of messages]}
    """
    categorized = defaultdict(list)
    
    for line in commit_lines:
        line = line.strip()
        if not line:
            continue
            
        match = COMMIT_PATTERN.match(line)
        if match:
            c_type, c_scope, c_desc = match.groups()
            
            # Use the mapped title or fallback to "Other"
            header = TYPE_MAP.get(c_type, 'Other Changes')
            
            # Format: **scope:** description (if scope exists)
            if c_scope:
                entry = f"**{c_scope}:** {c_desc}"
            else:
                entry = c_desc
                
            categorized[header].append(entry)
        else:
            # Commits that don't follow the convention go to "Other"
            categorized['Other Changes'].append(line)
            
    return categorized


def generate_markdown(version, categories):
    """Generates the final Markdown string."""
    md = [f"# Release Notes: {version}", f"_{date.today().isoformat()}_", ""]
    
    # Order keys based on importance
    priority_order = [
        'New Features', 
        'Bug Fixes', 
        'Performance Improvements', 
        'Documentation',
        'Code Refactoring'
    ]
    
    # Add priority items first
    for header in priority_order:
        if header in categories and categories[header]:
            md.append(f"## {header}")
            for item in categories[header]:
                md.append(f"- {item}")
            md.append("")
            del categories[header] # Remove processed
            
    # Add remaining items
    for header, items in categories.items():
        if items:
            md.append(f"## {header}")
            for item in items:
                md.append(f"- {item}")
            md.append("")
            
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser(description="Automated Release Notes Generator")
    parser.add_argument("repo", help="Path to local git repository")
    parser.add_argument("--start", help="Start tag/commit (exclusive)", default=None)
    parser.add_argument("--end", help="End tag/commit (inclusive)", default="HEAD")
    parser.add_argument("--version", help="Version name for the title", default="Draft Release")
    parser.add_argument("--output", help="Output markdown file", default="RELEASE_NOTES.md")
    
    args = parser.parse_args()
    
    # Determine range
    git_range = f"{args.start}..{args.end}" if args.start else args.end
    
    print(f"[INFO] Reading git log from {args.repo} ({git_range})...")
    raw_commits = get_git_log(args.repo, git_range)
    
    categories = parse_commits(raw_commits)
    markdown = generate_markdown(args.version, categories)
    
    Path(args.output).write_text(markdown, encoding='utf-8')
    print(f"[OK] Release notes generated: {args.output}")

if __name__ == "__main__":
    main()
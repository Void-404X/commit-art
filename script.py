import os
import subprocess
import random
import datetime

def run_command(command, repo_path):
    subprocess.run(command, shell=True, cwd=repo_path, check=True)

def generate_commits(repo_path, start_date, end_date, max_commits_per_day=5):
    delta_days = (end_date - start_date).days
    
    for day in range(delta_days + 1):
        commit_date = start_date + datetime.timedelta(days=day)
        num_commits = random.randint(0, max_commits_per_day)
        
        for _ in range(num_commits):
            with open(os.path.join(repo_path, "file.txt"), "a") as f:
                f.write(f"Commit on {commit_date}\n")
            
            run_command("git add file.txt", repo_path)
            run_command(f"GIT_COMMITTER_DATE='{commit_date.isoformat()}' git commit -m 'Auto commit' --date '{commit_date.isoformat()}'", repo_path)

def main():
    print("### GitHub Commit Generator ###")
    print("1. Убедитесь, что у вас установлен Git и Python.")
    print("2. Запустите этот скрипт в терминале: python script.py")
    print("3. После выполнения используйте команды для загрузки в GitHub.")
    
    repo_path = "github-commit-art"
    os.makedirs(repo_path, exist_ok=True)
    
    run_command("git init", repo_path)
    with open(os.path.join(repo_path, "file.txt"), "w") as f:
        f.write("Initial commit\n")
    
    run_command("git add file.txt", repo_path)
    run_command("git commit -m 'Initial commit'", repo_path)
    
    start_date = datetime.datetime(2024, 1, 1)
    end_date = datetime.datetime(2024, 3, 20)
    
    generate_commits(repo_path, start_date, end_date)
    
    print("### Коммиты созданы! ###")
    print("Теперь выполните следующие команды, чтобы загрузить изменения в GitHub:")
    print("cd github-commit-art")
    print("git branch -M main")
    print("git remote add origin <your-repo-url>")
    print("git push -u origin main")

if __name__ == "__main__":
    main()

import os
import subprocess

translator_dir = 'aqua-language/src/translator/'
nextjs_app_dir = 'nextjs-app/'

# Execute all Python files in the translator directory
for filename in os.listdir(translator_dir):
    if filename.endswith('.py') and filename.startswith('aqua'):
        file_path = os.path.join(translator_dir, filename)
        print(f"Executing {file_path}...")
        subprocess.run(['python3', file_path])

# Start the Next.js app
os.chdir(nextjs_app_dir)
subprocess.run(['npm', 'run', 'dev'])  # Use ['yarn', 'dev'] if you're using Yarn

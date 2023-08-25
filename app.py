from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Run the Ansible playbook using subprocess
        playbook_output = run_ansible_playbook()
        return render_template("index.html", output=playbook_output)
    
    return render_template("index.html", output=None)

def run_ansible_playbook():
    try:
        # Replace with the actual command to run your Ansible playbook
        playbook_command = "ansible-playbook my_playbook.yml"
        result = subprocess.run(playbook_command, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error:\n{result.stderr}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


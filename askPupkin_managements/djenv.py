import os
import sys
import subprocess
import shutil

MANAGEMENT_DIR = "./askPupkin_managements/"

REQUIREMENTS = f"{MANAGEMENT_DIR}/req.txt"

ENV = f"{MANAGEMENT_DIR}/env"

ACTIVATE_ENV_WIN = f"{MANAGEMENT_DIR}/env/scripts/activate_this.py"

ACTIVATE_ENV_UNIX = f"{MANAGEMENT_DIR}/env/bin/activate_this.py"

def activate_env():
    if os.path.exists(ACTIVATE_ENV_WIN):
        exec(open(ACTIVATE_ENV_WIN).read(), {'__file__': ACTIVATE_ENV_WIN})
    elif os.path.exists(ACTIVATE_ENV_UNIX):
        exec(open(ACTIVATE_ENV_UNIX).read(), {'__file__': ACTIVATE_ENV_UNIX})
    else:
        raise FileNotFoundError("The virtual environment activation file does not exist")
    
def check_env_exists():
    if not os.path.exists(ENV):
        try: import pip
        except: raise EnvironmentError("PIP package is not installed")

        try: import virtualenv
        except:
            pip.main(["install", "virtualenv"])
            import virtualenv

        if not os.path.exists(REQUIREMENTS):
            raise FileNotFoundError("The requirements file is not exist")
        
        virtualenv.cli_run([ENV])
        activate_env()

        try:
            subprocess.run(["pip", "install", "-r", REQUIREMENTS], check=True)
        except Exception as e:
            shutil.rmtree(ENV)
            raise EnvironmentError("Installation error: ", e.args)

def check_env_active():
    if sys.prefix == sys.base_prefix:
        activate_env()

def update_requirements():
    os.system(f"pip freeze > {REQUIREMENTS}")
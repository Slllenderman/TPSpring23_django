import os
import sys

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
        raise Exception("The virtual environment activation file does not exist")
    
def check_env_exists():
    if not os.path.exists(ENV):
        if not os.path.exists(REQUIREMENTS):
            raise Exception("The requirements file is not exist")
        os.system(f"python -m virtualenv {ENV}")
        activate_env()
        os.system(f"pip install -r {REQUIREMENTS}")

def check_env_active():
    if sys.prefix == sys.base_prefix:
        activate_env()

def update_requirements():
    os.system(f"pip freeze > {REQUIREMENTS}")
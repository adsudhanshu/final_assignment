import os
import subprocess
from dotenv import load_dotenv, set_key
from sqlalchemy import create_engine,text
from sqlalchemy.orm import sessionmaker
import time


def project_setup_chain(inputs):
    project_root = inputs.project_root

    # Step 1: Create the folder structure
    create_project_structure(project_root)

    # Step 2: Set up the virtual environment and install dependencies
    setup_virtual_environment(project_root)

    # Step 3: Set up PostgreSQL with Podman container
    setup_postgresql_with_podman()

    # Step 4: Set up the .env file with database connection string
    setup_env_file(project_root)

    # Step 5: Set up database connection with SQLAlchemy
    session_local = setup_database_connection()

    test_database_connection(session_local)

    return {"status": "success", "message": "Project setup complete!"}


# Helper Functions used in the above step:

def create_project_structure(project_root):
    directories = [
        "app/api/routes",
        "app/models",
        "app/services",
        "tests",
    ]
    
    for directory in directories:
        os.makedirs(os.path.join(project_root, directory), exist_ok=True)


def setup_virtual_environment(project_root):
    env_dir = os.path.join(project_root, "venv")
    if not os.path.exists(env_dir):
        subprocess.check_call([f"py","-m","venv",env_dir])

    pip_path = os.path.join(env_dir,"Scripts","pip.exe")

    generate_requirements_txt(project_root)
    # Activate the environment (you can also use subprocess to activate it)
    requirements_path = os.path.join(project_root, "requirements.txt")
    subprocess.check_call([pip_path,"install","-r",requirements_path])


def generate_requirements_txt(project_root):
    requirements = [
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "psycopg2",
        "alembic",
        "python-dotenv",
        "pytest"
    ]
    
    with open(os.path.join(project_root, "requirements.txt"), "w") as f:
        for req in requirements:
            f.write(f"{req}\n")


def setup_postgresql_with_podman():
    try:
        # First, check if the container is running
        result = subprocess.check_output(["podman", "ps", "-q", "-f", "name=postgres-container"])
        if result:
            print("PostgreSQL container is already running.")
        else:
            print("PostgreSQL container is not running.")
            # If the container is stopped, start it
            subprocess.check_call(["podman", "start", "postgres-container"])
            print("PostgreSQL container started.")
    except subprocess.CalledProcessError:
        # If the container is not found (either stopped or doesn't exist), create and start a new one
        print("PostgreSQL container does not exist. Creating and starting the container...")
        try:
            subprocess.check_call([
                "podman", "run", "--name", "postgres-container", "-d",
                "-e", "POSTGRES_PASSWORD=mysecretpassword",
                "-e", "POSTGRES_DB=mydatabase", 
                "-p", "5432:5432",
                "postgres:latest"
            ])
            print("PostgreSQL container started successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating PostgreSQL container: {e}")
            return False
    time.sleep(5)
    return True



def setup_database_connection():
    load_dotenv()

    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mysecretpassword@localhost:5432/mydatabase")
    
    engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20, pool_timeout=30)
    
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return SessionLocal

def test_database_connection(SessionLocal):
    try:
        db=SessionLocal()
        db.execute(text("Select 1"))
        db.close()
        print("Database connection successful")
    except Exception as e:
        print("Database connection failed",str(e))


def setup_env_file(project_root):
    dotenv_path = os.path.join(project_root, ".env")

    if not os.path.exists(dotenv_path):
        open(dotenv_path, 'w').close()

    load_dotenv(dotenv_path)

    set_key(dotenv_path, "DATABASE_URL", "postgresql://postgres:mysecretpassword@localhost:5432/mydatabase")

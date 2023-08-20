import os
import dotenv

dotenv.load_dotenv()

def get_env(key):
	return os.environ.get(key)


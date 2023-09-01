""" Helper functions for the application """
import os
import dotenv

dotenv.load_dotenv()

def get_env(key):
	""" Get environment variable """
	return os.environ.get(key)


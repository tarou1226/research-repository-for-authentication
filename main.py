import random
import sys

random_version = random.getstate()[0]
print("PYTHON_VERSION:" + str(sys.version))
print("RANDOM_VERSION:" + str(random_version))
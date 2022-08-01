import os
import platform

# Get current project
def getPwd(file_name=None):
  pwd = os.getcwd()

  if file_name is not None:
    pwd += f'/{file_name}'

  return pwd

# Get current project +  new folder
def getDirCurrent(dir_name, file_name=None):

  dir = getPwd()
  dir += f'/{dir_name}'

  if file_name is not None:
    dir += dir+f'/{file_name}'

  return dir

def loadVaribleEnv(name):
  return os.getenv(name)

def loaddriver():

  os = platform.system()

  if os == 'Darwin':
    return 'chromedriver_macos_intel'

  elif os == 'Windows':
    return 'chromedriver.exe'

  elif os == 'Linux':
    return 'chromedriver_linux'

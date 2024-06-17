import json

__ignore = set()
__rename = dict()
__init = False

def init():
   global __init, __rename

   try:
      with open('ignore.cfg') as cfg:
         for line in cfg.readlines():
            __ignore.add(line.strip())
   except:
      print('Failed to load ignore.cfg')

   try:
      with open('rename.json') as cfg:
         __rename = json.load(cfg)
   except:
      print('Failed to load rename.json')

   __init = True

def get_ignore():
   if not __init:
      init()
   return set(__ignore)

def get_rename():
   if not __init:
      init()
   return dict(__rename)

def add_ignore(item):
   __ignore.add(item)

def add_rename(prev, name):
   __rename[prev] = name

def save():
   if not __init:
      return
   
   with open('ignore.cfg', 'w') as cfg:
      for s in __ignore:
         cfg.write(f"{s}\n")
   with open('rename.json', 'w') as cfg:
      json.dump(__rename, cfg)
__ignore = set()

def init():
   try:
      with open('ignore.cfg') as cfg:
         for line in cfg.readlines():
            __ignore.add(line.strip())
   except:
      print('Failed to load ignore.cfg')

def get():
   return set(__ignore)

def add(item):
   __ignore.add(item)

def save():
   with open('ignore.cfg', 'w') as cfg:
      for s in __ignore:
         cfg.write(f"{s}\n")
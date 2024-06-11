import os
from os import path

def get_forms():
   # The root folder needs to be added manually
   forms = [{
      'id': 'forms',
      'name': 'Forms',
      'parent': ''
   }]
   for fileTup in os.walk('forms'):
      # Add folders
      for folder in fileTup[1]:
         forms.append({
            'id': path.join(fileTup[0], folder),
            'name': folder,
            'parent': fileTup[0]
         })
      # Add files
      for file in fileTup[2]:
         forms.append({
            'id': path.join(fileTup[0], file),
            'name': file,
            'parent': fileTup[0]
         })
      
   return forms

def get_write_stream(filename, subfolder=''):
   partialPath = 'output'
   if len(subfolder) > 0:
      partialPath = path.join(partialPath, subfolder)
   file = path.join(partialPath, filename)
   # Make sure the folder exists
   directory = path.dirname(file)
   if not path.exists(directory):
      os.makedirs(directory)
   return open(file, 'wb')
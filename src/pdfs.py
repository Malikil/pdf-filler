from pypdf import PdfReader, PdfWriter
from files import get_write_stream

import json

def get_fields(filenames):
   for file in filenames:
      reader = PdfReader(file)
      fields = reader.get_fields()
      with open('temp.json', 'w') as outfile:
         fields = {k: v for k, v in fields.items() if '/FT' in v and v['/FT'] == '/Tx'}
         json.dump(
            fields,
            outfile,
            indent=4,
            default=lambda v: str(v)
         )
      allFieldLen = len(fields)
      fields = reader.get_form_text_fields()
      formTextFieldLen = len(fields)
      print(str(allFieldLen) + ' ' + str(formTextFieldLen))
      return fields

def write_fields(filenames, data):
   for file in filenames:
      reader = PdfReader(file)
      # We can only fill in forms page-by-page
      # Organize fields into which page they appear on
      # pageFields = {}
      # fields = reader.get_fields()
      # for key in data:
      #    # Find which page(s) this field appears on
      #    field = fields[key]
      #    pages = reader.get_pages_showing_field(field)
      #    for page in pages:
      #       # Use page number as an identifier
      #       # If we haven't seen this page yet, create an entry for it on the page list
      #       if page.page_number not in pageFields:
      #          pageFields[page.page_number] = {
      #             'page': page,
      #             'fieldData': {}
      #          }
      #       # Add data to the page entry in pageFields dict
      #       pageFields[page.page_number]['fieldData'][key] = data[key]

      # Set up the writer
      writer = PdfWriter(clone_from=reader)
      writer.update_page_form_field_values(
         page=None, # Fill all pages
         fields=data,
         auto_regenerate=False
      )
      # Write values
      # for pageNo in pageFields:
      #    pageData = pageFields[pageNo]
      #    print(pageData)
      #    writer.update_page_form_field_values(
      #       pageData['page'],
      #       pageData['fieldData'],
      #       auto_regenerate=False
      #    )
      
      with get_write_stream(file) as output_stream:
         writer.write(output_stream)

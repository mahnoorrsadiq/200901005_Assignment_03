import xml.etree.ElementTree as ET
from openpyxl.workbook import Workbook

# Parse the XML file
tree = ET.parse(r'C:\Users\hp\Downloads\compiler.xml')
root = tree.getroot()

# Create an Excel workbook
workbook = Workbook()
sheet = workbook.active

# Add the headers to the sheet
sheet.append(['Book_Id', 'Author_Name', 'Title', 'Genre', 'Price', 'Publish_date', 'Description'])

# Iterate through the XML elements and extract the information
for book in root.findall('book'):
    book_id = book.get('id')
    author_name = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text

    # Add the data to the sheet
    sheet.append([book_id, author_name, title, genre, price, publish_date, description])

# Save the workbook
workbook.save('data.xlsx')
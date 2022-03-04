from filestack import Client
# from flask import current_app
# api = current_app.config['IMAGE_UPLOAD_API']

api = 'A2lNvkX8qQcux4kiJrx50z'
client = Client(api)
file = client.upload(filepath='./static/assets/img/product-review.png')
print(file.url)

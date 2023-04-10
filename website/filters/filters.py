from flask import current_app as app, url_for

@app.template_filter('image_url')
def reverse_filter(s):
    if s is not None:
        return s
    else:  
        return url_for('static', filename='assets/img/product_photo/Default.svg')

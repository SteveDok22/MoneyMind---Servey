"""
Flask web server for Heroku deployment with Code Institute terminal template
"""

import sys
from flask import Flask, render_template
from os import environ

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        host=environ.get('IP', '0.0.0.0'),
        port=int(environ.get('PORT', 8000)),
        debug=False
    )
```

---

### **📄 FILE 6: Update `Procfile`**

Replace your `Procfile` content with:
```
web: node index.js
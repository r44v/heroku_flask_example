# Push python flask app to heroku

## Setup

**Initial steps**

```
heroku login
git init
git add *
git commit -m "initial commit"
heroku create
git push heroku master
```

**For changes**

```
git add *
git commit -m "initial commit"
heroku create
git push heroku master
```

## Minimal needed files

**Procfile**

```
web: gunicorn -b 0.0.0.0:$PORT app:app
```

**requirements.txt**

```
flask
gunicorn
```

**app.py**

```python
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = {
        "welcome": "it works"
    }
    return jsonify(data)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
```

## Other usefull heroko commands

**Tail logs**

```
heroku logs --tail --app "<app name>"
```

**View app scale**

```
heroku ps --app "<app name>
```

**Open app in browser**

```
heroku open --app "<app name>
```

**Open ssh to app**

```
heroku ps:exec --app "<app name>
```

**Scale on / Scale off**

```
heroku ps:scale web=1 --app "<app name>
heroku ps:scale web=0 --app "<app name>
```

**List all apps**

```
heroku apps
```
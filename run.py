from flask import Flask

app = Flask('__name__')

@app.route('/')
def index():
  return "if u read this ur gay lol"
 
if __name__ == '__main__':
  app.run()

from app import app
@app.route('/home')
def home():
  return '<h2> Welcome to Flask Mastery Series </h2>'

if __name__ == '__main__':
  app.run(debug=True)

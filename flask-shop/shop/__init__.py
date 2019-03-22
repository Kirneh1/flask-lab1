from flask import Flask 


from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "<a278e205217ab7b227ff234f0eb88757c1b356d9b2ef1d8b>"


from shop import routes

# Note: type 'app.config[..]' as one line, it is split into

# multiple lines in this document to fit on the page

# {USERNAME} and {YOUR_DATABASE} are your Cardiff username


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1868851:aA9qqczMhE58vQZ@csmysql.cs.cf.ac.uk:3306/c1868851'

db = SQLAlchemy(app)



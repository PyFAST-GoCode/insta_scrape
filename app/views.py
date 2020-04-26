import os
from flask import Flask, render_template
from app import app

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/insta_scraper"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/insta_scraper"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

# app = Flask(__name__)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

# @app.route('/posts', methods=['POST', 'GET'])
# def handle_posts():
#     if request.mehtod == 'POST':
#         args = request.args
#         post = Post()

if __name__ == '__main__':
    app.run(debug=True)





# import os
# from flask import Flask, render_template, send_file, make_response, request, abort, jsonify
# app = Flask(__name__)
#
#
#
# @app.route('/')
# def main():
#     return 'Hello World!'
#

# if __name__ == '__main__':
#     app.config['DEBUG'] = True
#     app.run()




# @app.route('/')
# def index():
#     return render_template('root_path.html')
#
# @app.route('/insta_posts', methods=['GET', 'POST'])
# def create():
#     if request.method == "POST":
#         args = request.args
#         condition = Condition(args['date'], args['text'], args['url'])
#         db.session.add(post)
#         db.session.commit()
#     else:
#         return "400"
#
#
# # @app.route('/conditions_map/v1', methods=['GET'])
# # def conditions_map_v1():
# #     args = request.args
# #     render_map(args['condition'])
# #     plt.savefig("MeMD_Map.png")
# #     return send_file('MeMD_Map.png', mimetype='image/gif')
# #
# # @app.route('/conditions_map/v2', methods=['GET'])
# # def conditions_map_v2():
# #     args = request.args
# #     plot_map(args['condition'])
# #     plt.savefig("MeMD_Map.png")
# #     return send_file('MeMD_Map.png', mimetype='image/gif')
#

from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
import google_api_handler

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database_app.db'
db = SQLAlchemy(app)


class BookModel(db.Model):
    """Data Base model """
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    authors = db.Column(db.String)
    published_date = db.Column(db.String)
    categories = db.Column(db.String)
    average_rating = db.Column(db.String)
    ratings_count = db.Column(db.String)
    thumbnail = db.Column(db.String)

    def __repr__(self):
        return f"{self.id}" \
               f"{self.title}" \
               f"{self.authors}" \
               f"{self.published_date}" \
               f"{self.categories}" \
               f"{self.average_rating}" \
               f"{self.ratings_count}" \
               f"{self.thumbnail}"


def check_db():
    """Creates database if it doesnt exist"""
    if not database_exists('sqlite:///database_app.db'):
        return db.create_all()
    else:
        print("Database already exists")


check_db()

# Argument parsers
book_put_args = reqparse.RequestParser()
book_put_args.add_argument('id', type=str, help='id missing')
book_put_args.add_argument('title', type=str, help='title missing')
book_put_args.add_argument('authors', type=str, help='authors missing')
book_put_args.add_argument('published_date', type=str, help='published date missing')
book_put_args.add_argument('categories', type=str, help='categories missing')
book_put_args.add_argument('average_rating', type=str, help='average rating missing')
book_put_args.add_argument('ratings_count', type=str, help='ratings count missing')
book_put_args.add_argument('thumbnail', type=str, help='thumbnail missing')

# Serialize my returns
resource_fields = {
    'id': fields.String,
    'title': fields.String,
    'authors': fields.String,
    'published_date': fields.String,
    'categories': fields.String,
    'average_rating': fields.String,
    'ratings_count': fields.String,
    'thumbnail': fields.String
}


@app.route('/')
def get_docs():
    """Displays poor documentation"""
    return {
        0: 'Using the API:',
        1: 'GET, http://127.0.0.1:5000/books',
        2: 'GET/PUT, http://127.0.0.1:5000/books/id/2SYREAAAQBA',
        3: 'GET, http://127.0.0.1:5000/books/authors/Bramlett'
    }


# TODO: sorting and filtering by published date
#  /books?published_date=1995, /books?sort=-published_date
#  query.filter_by(authors=book_author).all()
#  from sqlalchemy import desc
#  query.order_by(desc(table1.mycol))

class BooksList(Resource):
    """
    API class to represent the book list
    Attributes: Resource from flask_restful library
    Methods: get: returns list of books from local database
    """

    @marshal_with(resource_fields)
    def get(self):
        books = BookModel.query.all()
        if not books:
            abort(404, message="Could not find matching elements")
        result = []
        for book in books:
            book_data = {
                'id': book.id,
                'title': book.title,
                'authors': book.authors,
                'published_date': book.published_date,
                'categories': book.categories,
                'average_rating': book.average_rating,
                'ratings_count': book.ratings_count,
                'thumbnail': book.thumbnail
            }
            result.append(book_data)
        return result, 200


class BooksId(Resource):
    """
    API class to represent the book with id requests
    Attributes: Resource from flask_restful library
    Methods: get: returns book by id, put: adds next book to database
    """

    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message="Could not find book with that id")
        return result, 200

    @marshal_with(resource_fields)
    def put(self, book_id):
        args = book_put_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if result:
            abort(409, message="Book id taken")
        book = BookModel(
            id=book_id,
            title=args['title'],
            authors=args['authors'],
            published_date=args['published_date'],
            categories=args['categories'],
            average_rating=args['average_rating'],
            ratings_count=args['ratings_count'],
            thumbnail=args['thumbnail']
        )
        db.session.add(book)
        db.session.commit()
        return book, 201


class BooksAuthor(Resource):
    """
    API class to represent the book with author name requests
    Attributes: Resource from flask_restful library
    Methods: get: returns book by author name
    """

    @marshal_with(resource_fields)
    def get(self, book_author):
        result = BookModel.query.filter_by(authors=book_author).all()
        if not result:
            abort(404, message="Could not find book with that author")
        return result, 200


# Routes for class-based API elements
api.add_resource(BooksList, "/books")
api.add_resource(BooksId, "/books/id/<string:book_id>")
api.add_resource(BooksAuthor, "/books/authors/<string:book_author>")

if __name__ == '__main__':
    app.run(debug=True)

# makes query to google books API
google_api_handler

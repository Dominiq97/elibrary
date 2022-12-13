from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from library_manager.models import Book, Publisher

# Book mapping
@registry.register_document
class BookDocument(Document):
    title = fields.TextField(
        attr = 'title',
        fields = {
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )

    author = fields.TextField(
        attr = 'author',
        fields = {
            'raw': fields.TextField(),
            'suggest': fields.CompletionField(),
        }
    )

    publisher = fields.ObjectField(
        attr = 'publisher',
        properties = {
            'name': fields.TextField(
                attr = 'name',
                fields = {
                    'raw': fields.TextField(),
                }
            ),
            'address': fields.TextField(
                attr = 'address',
                fields = {
                    'raw': fields.TextField(),
                }
            )
        }
    )

    year = fields.TextField(
        attr = 'year',
        fields = {
            'raw': fields.TextField()
        }
    )

    stock = fields.TextField(
        attr = 'stock',
        fields = {
            'raw': fields.IntegerField()
        }
    )

    price = fields.TextField(
        attr = 'price',
        fields = {
            'raw': fields.IntegerField()
        }
    )

    class Index:
        name = 'books'

    class Django:
        model = Book


# Publisher mapping
# @registry.register_document
# class PublisherDocument(Document):
#     name = fields.TextField(
#         attr = 'name',
#         fields = {
#             'raw': fields.TextField(),
#             'suggest': fields.CompletionField(),
#         }
#     )

#     address = fields.TextField(
#         attr = 'address',
#         fields = {
#             'raw': fields.TextField(),
#         }
#     )

#     class Index:
#         name = 'publishers'

#     class Django:
#         model = Publisher
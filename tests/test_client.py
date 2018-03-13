from apistar import http, App, Client, Document, Link, TestClient


def hello_world():
    return http.Response({'hello': 'world'})


document = Document(
    url='http://testserver',
    content=[
        Link(url='/', method='GET', handler=hello_world)
    ]
)
app = App(document)
session = TestClient(app)


def test_client_request():
    client = Client(document=document, session=session)
    assert client.request('hello_world') == {'hello': 'world'}
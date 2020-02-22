docker run --rm \
-v "${PWD}:/local" openapitools/openapi-generator-cli generate \
-i https://raw.githubusercontent.com/OAI/OpenAPI-Specification/master/examples/v3.0/petstore.yaml \
-g python-flask \
-o /local/src/python-flask

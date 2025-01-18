from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:pPBjUjjFrEdpPocLfGBhfeKt:5b06832cdc8a50f7ae533c187d5ca9b730472298b3d9a2d4f90e243dc4677175")
db = client.get_database_by_api_endpoint(
  "https://e43ad1b3-ac50-408d-ab3d-d06d633c4abc-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")

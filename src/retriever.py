class Retriever:

    def __init__(self, docs):

        self.docs = docs


    def search(self, query):

        query = query.lower()

        for doc in self.docs:

            if query.split()[0] in doc["text"].lower():

                return doc

        return self.docs[0]

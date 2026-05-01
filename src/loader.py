import os


def load_documents(folder_path):

    docs = []

    for root, dirs, files in os.walk(
        folder_path
    ):

        for file in files:

            path = os.path.join(
                root,
                file
            )

            with open(
                path,
                encoding="utf8"
            ) as f:

                docs.append({

                    "source": file,

                    "text":
                        f.read()
                })

    return docs


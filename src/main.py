import pandas as pd

from loader import load_documents
from retriever import Retriever
from agent import triage


docs = load_documents(
    "../data"
)

retriever = Retriever(
    docs
)

tickets = pd.read_csv(
    "../support_tickets.csv"
)

results = []

for _, row in tickets.iterrows():

    results.append(

        triage(
            row,
            retriever
        )
    )

pd.DataFrame(
    results
).to_csv(
    "../output/predictions.csv",
    index=False
)

print("Done")

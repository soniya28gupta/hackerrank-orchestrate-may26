from classifier import classify_request
from safety import should_escalate


def triage(ticket, retriever):

    issue = ticket["issue"]

    request_type = classify_request(issue)

    if should_escalate(issue):

        return {

            "status": "escalated",

            "product_area": "support",

            "response": "Your case needs human review.",

            "justification": "Sensitive issue.",

            "request_type": request_type
        }

    doc = retriever.search(issue)

    return {

        "status": "replied",

        "product_area": "support",

        "response": doc["text"][:200],

        "justification": "Matched support corpus.",

        "request_type": request_type
    }

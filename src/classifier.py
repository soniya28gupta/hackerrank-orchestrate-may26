def classify_request(text):

    text = text.lower()

    if "bug" in text:

        return "bug"

    if "feature" in text:

        return "feature_request"

    if len(
        text.strip()
    ) < 5:

        return "invalid"

    return "product_issue"

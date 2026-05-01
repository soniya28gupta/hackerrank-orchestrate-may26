HIGH_RISK = [

    "fraud",

    "billing",

    "payment",

    "security",

    "locked"
]


def should_escalate(
    text
):

    text = text.lower()

    for word in HIGH_RISK:

        if word in text:

            return True

    return False

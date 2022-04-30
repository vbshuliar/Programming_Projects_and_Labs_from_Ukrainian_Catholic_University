"""User's tokens."""


def oauth():
    """Authorization."""
    print("\nConsumer key:\n")
    consumer_key = input(">>>")
    print("\nConsumer secret:\n")
    consumer_secret = input(">>>")
    print("\nToken key:\n")
    token_key = input(">>>")
    print("\nToken secret\n")
    token_secret = input(">>>")
    return {"consumer_key": f"{consumer_key}",
            "consumer_secret": f"{consumer_secret}",
            "token_key": f"{token_key}",
            "token_secret": f"{token_secret}"}

from datetime import datetime


def getpartofday(hour):
    return (
        "light" if 5 <= hour <= 18
        else
        "dark"
    )


hr = datetime.now().hour
print(hr)
print(f"Its {getpartofday(hr)} now.")

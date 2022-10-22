import datetime


class MyPackage:
    def __init__(self, package, date_added=None):
        self.package = package
        self.date_added = date_added if date_added is not None else datetime.datetime.now().isoformat()

    def __repr__(self) -> str:
        return f"{self.package}, {self.date_added}"

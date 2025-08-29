class Vertex:
    def __init__(self, name: str) -> None:
        self.name = name
        # ... other state

    def __repr__(self) -> str:
        return self.name

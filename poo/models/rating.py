class Rating:

    def __init__(self, client: str, score: float):
        self._client = client
        self._score = score

    def __str__(self) -> str:
        return f"{self._score}/5 - {self._client or 'Sem comentário'}"
    
    def get_score(self) -> float:
        return self._score
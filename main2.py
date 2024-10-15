from model import CountLettersResponse
from datetime import datetime

if __name__ == '__main__':
    response = CountLettersResponse(
        counted_at=datetime.now(),
        counters={
            "a": 1,
            "b": 2
        }
    )
    print(response.json())

from fastapi import FastAPI, Query
import firebase_admin
from firebase_admin import credentials, db
from pyrebase import initialize_app

# Initialize Firebase Admin SDK
cred = credentials.Certificate("your-firebase-adminsdk.json")
firebase = initialize_app(cred, {"databaseURL": "https://your-firebase-url.firebaseio.com"})

app = FastAPI()


@app.get("/search")
async def search_lcs(subsequence: str = Query(..., title="LCS Subsequence")):

    ref = db.reference("users")
    data = ref.get()

    result = []
    for key, value in data.items():
        name = value.get("name", "")
        unique_id = value.get("unique_id", "")
        if unique_id and lcs(subsequence, unique_id):
            result.append(name)

    return result


def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]
    return lcs_length == len(subsequence)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

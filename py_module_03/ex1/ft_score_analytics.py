import sys

if __name__ == "__main__":
    i: int = 1
    scores: list = []
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        try:
            while i < len(sys.argv):
                scores.append(int(sys.argv[i]))
                i += 1
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(sys.argv) - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {(sum(scores) / (len(sys.argv) - 1)):.1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError as e:
            print("Oops you insert wrong data type: ", e)

import pandas as pd
import operator
import time

csvPath = "facts.csv"

def main():
    df = pd.read_csv(csvPath, usecols=["song_id", "user_id"])
    groups = df.groupby("user_id")

    users = dict()
    user_ids = df.user_id.unique()[0:100]
    for uid in user_ids:
        users[uid] = set(groups.get_group(uid).song_id.unique())

    results = dict()

    start_time = time.time()
    for comparedUser, group in groups:
        comparedUserSongs = set(group.song_id.unique())
        for user, songs in users.items():
            if user in results:
                results[user].append((comparedUser, len(comparedUserSongs.intersection(songs)) / len(comparedUserSongs.union(songs))))
            else:
                results[user] = [((comparedUser, len(comparedUserSongs.intersection(songs)) / len(comparedUserSongs.union(songs))))]
    print("Elapsed time: {}".format(time.time() - start_time))

    with open('results.txt', 'w') as file:
        for key, val in results.items():
            sort_result = sorted(val, key=lambda tup: tup[1], reverse=True)
            file.write("User = {}\n".format(key))
            for tup in sort_result[:100]:
                file.write("{} {}\n".format(tup[0],tup[1]))

if __name__ == "__main__":
    main()
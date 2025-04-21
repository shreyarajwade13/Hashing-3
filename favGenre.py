"""
TC - O(T + S + U .G)
SC - O(T + U .G)
"""
def favorite_genre(user_songs, song_genres):
    # Step 1: Create song → genre mapping
    song_to_genre = {}
    for genre, songs in song_genres.items():
        for song in songs:
            song_to_genre[song] = genre

    result = {}

    # Step 2: For each user, count genre frequencies
    for user, songs in user_songs.items():
        genre_count = defaultdict(int)
        max_count = 0

        for song in songs:
            genre = song_to_genre.get(song)
            if genre:
                genre_count[genre] += 1
                max_count = max(max_count, genre_count[genre])

        # Step 3: Find genre(s) with max count
        favorite_genres = [genre for genre, count in genre_count.items() if count == max_count]
        result[user] = favorite_genres

    return result

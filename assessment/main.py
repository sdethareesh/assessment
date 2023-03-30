from collections import defaultdict, deque


class User:
    def __init__(self, user_name):
        self.user_name = user_name

    def __str__(self) -> str:
        return self.user_name


class Song:
    def __init__(self, song_name):
        self.song_name = song_name

    def __str__(self) -> str:
        return self.song_name


class MusicPlayer:
    def __init__(self, N):
        self.user_recently_played_song_map = defaultdict(deque)
        self.N = N

    def play_song(self, user_obj, song_obj):
        q = self.user_recently_played_song_map[user_obj]
        if len(q) == self.N:
            q.popleft()

        q.append(song_obj)

    def print_user_recently_played_song_map(self):
        for user, songs in self.user_recently_played_song_map.items():
            print(f"{user.user_name}", end=" -> ")
            for song in songs:
                print(f"{song.song_name}", end=" ")
            print()


# user1 = User("Hareesh")
# s1 = Song("s1")
# s2 = Song("s2")
# s3 = Song("s3")
# s4 = Song("s4")
# s5 = Song("s5")
#
# music_player = MusicPlayer(3)
# music_player.play_song(user1, s1)
# music_player.print_user_recently_played_song_map()
# assert music_player.user_recently_played_song_map[user1][0] == s1
# music_player.play_song(user1, s2)
# music_player.print_user_recently_played_song_map()
# assert music_player.user_recently_played_song_map[user1][0] == s1 and music_player.user_recently_played_song_map[user1][
#     1] == s2
# music_player.play_song(user1, s3)
# q = music_player.user_recently_played_song_map[user1]
# assert q[0] == s1
# assert q[1] == s2
# assert q[2] == s3
# music_player.print_user_recently_played_song_map()
# music_player.play_song(user1, s4)
# music_player.print_user_recently_played_song_map()
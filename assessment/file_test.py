from collections import deque

from main import User, Song, MusicPlayer


def test_play_song():
    user1 = User("Hareesh")
    user2 = User("abc")
    s1 = Song("s1")
    s2 = Song("s2")
    s3 = Song("s3")
    s4 = Song("s4")
    s5 = Song("s5")
    music_player = MusicPlayer(3)
    music_player.play_song(user1, s1)
    assert music_player.user_recently_played_song_map[user1][0] == s1
    music_player.play_song(user1, s2)
    assert music_player.user_recently_played_song_map[user1][0] == s1 and \
           music_player.user_recently_played_song_map[user1][1] == s2
    music_player.play_song(user1, s3)
    assert music_player.user_recently_played_song_map[user1][0] == s1 and \
           music_player.user_recently_played_song_map[user1][1] == s2 and \
           music_player.user_recently_played_song_map[user1][2] == s3
    music_player.play_song(user1, s4)
    assert music_player.user_recently_played_song_map[user1][0] == s2 and \
           music_player.user_recently_played_song_map[user1][1] == s3 and \
           music_player.user_recently_played_song_map[user1][2] == s4
    music_player.play_song(user2, s5)
    print(music_player.user_recently_played_song_map)
    assert music_player.user_recently_played_song_map[user1][0] == s2 and \
           music_player.user_recently_played_song_map[user1][1] == s3 and \
           music_player.user_recently_played_song_map[user1][
               2] == s4

def test_play_song_with_invalid_user():
    s1 = Song("s1")
    music_player = MusicPlayer(3)
    try:
        music_player.play_song("invalid_user", s1)
    except Exception as e:
        assert str(e) == "Invalid user object"
#
#
def test_play_song_with_invalid_song():
    user1 = User("Hareesh")
    music_player = MusicPlayer(3)
    try:
        music_player.play_song(user1, "invalid_song")
    except Exception as e:
        assert str(e) == "Invalid song object"
#
#
def test_music_player_with_invalid_limit():
    try:
        MusicPlayer(0)
    except Exception as e:
        assert str(e) == "Limit should be a positive integer"

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

def space():
    print("-" * 20)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

death_w_dignity = ["I forgive you mother I can hear you",
                   "and I long to be near you",
                   "But every road leads to an end",
                   "Yes every road leads to an end",
                   "Your apparition passes through me",
                   "in the willows and five red hens",
                   "You'll never see us again",
                   "You'll never see us again"]

space()

happy_bday.sing_me_a_song()

space()

bulls_on_parade.sing_me_a_song()

space()

Song(death_w_dignity).sing_me_a_song()

space()

Sufjan_song = Song(death_w_dignity).sing_me_a_song()

space()

Sufjan_song = Song(death_w_dignity)
Sufjan_song.sing_me_a_song()

space()

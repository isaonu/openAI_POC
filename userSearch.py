

class UserSearches:

    def audio_with_topic(self, summaries, topic):
        something_found = False
        size = len(summaries)
        for i, talk in enumerate(summaries):
            if topic in talk[2]:
                something_found = True
                print(f"The topic you are looking for maybe in {talk[0]}")
            elif not something_found and i == size-1:
                print(f"What you are looking may not be in the audios")
                return False
        return True



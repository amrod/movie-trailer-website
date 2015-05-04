import webbrowser


class Movie(object):

    def __init__(self, title, storyline, poster_img, trailer_youtube):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
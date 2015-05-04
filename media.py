import webbrowser


class Movie(object):
    """
    Hold information about movies.
    """

    def __init__(self, title, storyline, poster_img, trailer_youtube):
        """
        Initializes the movie object with required properties.

        :param title: Movie's title
        :param storyline: Movie's storyline summary
        :param poster_img: URL to the movie's poster image
        :param trailer_youtube: YouTube URL to the movie's trailer
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        Opens the movie's trailer URL in the default web browser.
        :return: None
        """
        webbrowser.open(self.trailer_youtube_url)
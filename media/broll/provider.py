from media.broll.providers.pexels_provider import PexelsProvider


class Broll:
    provider = PexelsProvider()

    @classmethod
    def search_videos(cls, query: str, per_page: int = 3):
        return cls.provider.search_videos(query, per_page)

    @classmethod
    def download_video(cls, url, output_file):
        return cls.provider.download_video(url, output_file)

    @classmethod
    def get_best_video_url(cls, video):
        return cls.provider.get_best_video_url(video)
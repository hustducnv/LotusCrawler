from scrapy import Spider, Request
from pandas import read_csv
from ..items import PostItem
from configs import *


class PostImageSpider(Spider):
    name = 'PostImageSpider'

    def start_requests(self):
        post_links_path = os.path.join(CORE_DATA_DIR, 'post_links.csv')
        df = read_csv(
            post_links_path,
            dtype={'link_share': str, 'post_id': str}
        )
        start_idx = 0
        # end_idx = len(df)-1
        end_idx = 5
        for i in range(start_idx, end_idx+1):
            url, post_id = df.iloc[i]
            # url = 'https://lotus.vn/w/post/784681852643016704.htm'
            yield Request(url=url, callback=self.parse, cb_kwargs=dict(post_id=post_id))

    def parse(self, response, **kwargs):
        post = PostItem()
        post['post_id'] = kwargs['post_id']
        t = response.xpath('/html/head/meta[@property="og:image:url"]/@content').extract()
        if len(t) > 0:
            post['thumbnail_url'] = t[0]
        else:
            post['thumbnail_url'] = None
        yield post

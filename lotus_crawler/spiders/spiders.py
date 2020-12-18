from scrapy import Spider, Request
from pandas import read_csv
import requests
from lotus_crawler.items import PostItem
from configs import *


class PostThumbSpider(Spider):
    handle_httpstatus_list = [404]
    name = 'PostThumbSpider'

    def start_requests(self):
        post_links_path = os.path.join(CORE_DATA_DIR, 'post_links.csv')
        df = read_csv(
            post_links_path,
            dtype={'link_share': str, 'post_id': str}
        )
        start_idx = START_IDX
        # end_idx = len(df)-1
        end_idx = END_IDX
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
            # try:
            #     self.get_and_save_image(t[0], os.path.join(IMAGES_DIR, post['post_id']))
            # except:
            #     pass
        else:
            post['thumbnail_url'] = None
        yield post

    # def get_and_save_image(self, url, save_to):
    #     res = requests.get(url)
    #     if res.ok:
    #         with open(save_to, 'wb') as f:
    #             f.write(res.content)





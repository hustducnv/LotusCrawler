###### **RUN PostThumbSpider for get thumb url**:
- in _config.py_ edit START_IDX and END_IDX
- open terminal _project base dir_: _scrapy crawl PostThumbSpider -o post_thumb_links\_{START_IDX}\_to\_{END_IDX}.csv_
- eg. _scrapy crawl PostThumbSpider -o post_thumb_links\_0\_to\_5.csv_


- Duc: 0-50k, 50k-100k
- Quyen: 100k-150k, 150k-200k
- Dinh: 200k-250k, 250k-300k
- An: 300k-340k, 340k-380879
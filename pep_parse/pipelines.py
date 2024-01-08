import datetime
from collections import Counter

from pep_parse.settings import BASE_DIR, TIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = Counter()

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.counter.values())
        result_dir = BASE_DIR / 'results'
        result_dir.mkdir(exist_ok=True)

        doc_time = datetime.datetime.now().strftime(TIME_FORMAT)
        filename = f'status_summary_{doc_time}.csv'

        result_path = result_dir / filename

        with open(result_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for pep, count in self.counter.items():
                f.write(f'{pep},{count}\n')
            f.write(f'Total,{total}\n')

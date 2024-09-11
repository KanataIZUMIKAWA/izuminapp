from config.settings import BASE_DIR
from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = "定数ファイルの生成。すでにあるファイルは上書きしない。"
    
    def handle(self, *args, **options) :
        CONST_INFO = {
            'ai.py': 'GENEINFO = {\n    "WORD_COUNT": 1440480,\n    "SONG_COUNT": 3000,\n    "GENE_DATE": "2024年9月9日",\n}',
            'ban.py': 'BAN_LIST = []',
            'gpt.txt': '',
            'news.md': '[テストニュース1](https://example.com/)\n\n**テストニュース2**',
            'version.py': 'VERSION = "dev"'
        }
        for file_name, text in CONST_INFO.items():
            const_path = os.path.join(BASE_DIR, 'subekashi/constants/dynamic', file_name)
            if os.path.exists(const_path):
                continue
            
            file = open(const_path, 'w', encoding='utf-8')
            file.write(text)
            file.close()
            self.stdout.write(self.style.SUCCESS(f"ファイル{file_name}を作成しました。"))
            
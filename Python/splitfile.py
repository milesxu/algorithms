''' split one file into many. '''
import os.path
from datetime import date
import string


def split_file(file_path: str):
    ''' split files outported by youdao note. '''
    day = date.today().isoformat()
    puncdict = str.maketrans('', '', string.punctuation)
    insert_path = os.path.dirname(file_path)
    output_file = None
    line_num = [0]
    with open(file_path, encoding='utf-8') as file:
        lines, idx = file.readlines(), 0
        # convenient, but cannot cope with difficult transactions.
        # for i, line in enumerate(file):
        while idx < len(lines):
            if (lines[idx].startswith('###') or
                    lines[idx].endswith('.note\n')) and idx - 2 > line_num[-1]:
                line_num.append(idx)
                if output_file:
                    output_file.close()
                while True:
                    title = lines[idx].lstrip('# ').rstrip('\n')
                    if title.endswith('.note'):
                        title = title[:-5]
                    if title:
                        break
                    idx += 1
                filename = day + '-' + \
                    title.translate(puncdict).replace(' ', '-') + '.md'
                output_file = open(
                    os.path.join(insert_path, filename), 'a', encoding='utf-8')
                output_file.write('---\n')
                output_file.write('layout: post\n')
                title = title.replace("'", "''")
                output_file.write('title: \'' + title + '\'\n')
                output_file.write('categories:\n')
                output_file.write('- zambianmeat\n')
                output_file.write('- meat\n')
                output_file.write('---\n')
                output_file.write('\n')
            elif output_file:
                temp = lines[idx].replace('`', '\'')
                if len(temp) > 3 and not temp.strip('-\n'):
                    temp = '\n---\n'
                output_file.write(temp)
            idx += 1

        if not output_file.closed:
            output_file.close()


if __name__ == '__main__':
    zambianmeat = 'G:/Sites/zambianmeat/2016-02-28-ZambianMeat.md'
    split_file(zambianmeat)

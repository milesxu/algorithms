import os
import os.path
import hashlib
from datetime import datetime
import mimetypes
from typing import List
from pymongo import MongoClient
import bson
from bson.objectid import ObjectId


class Archiver:
    """
    Use MongoDB to manage image and other files.
    """
    bson_limit = (1 << 20) * 16
    seq_limit = (1 << 20) * 12

    def __init__(self, conn: str=None):
        self.client = MongoClient(conn)
        self.Image = self.client.Image.Default

    @staticmethod
    def create_item(root: str, file: str):
        """
        Based on file information, create dictionary which is to be inserted.
        """
        full_path = os.path.join(root, file)
        stat = os.stat(full_path)
        info = \
            {
                'path': root,
                'filename': file,
                'content_type': mimetypes.guess_type(file),
                'length': stat.st_size,
                'creation_time': stat.st_ctime,
                'last_access_time': stat.st_atime,
                'last_modify_time': stat.st_mtime,
                'upload_time': datetime.now()
            }
        with open(full_path, 'rb') as data:
            info['data'] = data.read()
        md5 = hashlib.md5()
        md5.update(info['data'])
        info['md5'] = bson.binary.Binary(md5.hexdigest().encode(),
                                         bson.binary.MD5_SUBTYPE)
        return info

    def delete_stored(self, id_list: List[ObjectId], validate: bool=True):
        """
        delete files that were successfully inserted into DB.
        """
        columns = {'path': 1, 'filename': 1}
        if validate:
            columns['md5'] = 1
        for oid in id_list:
            item = self.Image.find_one({'_id': oid}, columns)
            full_path = os.path.join(item['path'], item['filename'])
            if not os.path.exists(full_path):
                continue
            if validate:
                md5 = hashlib.md5()
                with open(full_path, 'rb') as file:
                    md5.update(file.read())
                if item['md5'].decode() != md5.hexdigest():
                    continue
            os.remove(full_path)

    def bulk_insert(self,
                    directory: str,
                    file_type: str='image',
                    delete: bool=False):
        """
        insert files of specified type in given directory to DB.
        """
        file_list, total_size, id_list = [], 0, []
        for root, dirs, files in os.walk(directory):
            for file in files:
                full_path = os.path.join(root, file)
                guessed_type = mimetypes.guess_type(file)[0]
                if os.path.getsize(full_path) >= Archiver.bson_limit or \
                        guessed_type is None or \
                        (file_type and not guessed_type.startswith(file_type)):
                    continue
                item = Archiver.create_item(root, file)
                if item['length'] >= Archiver.seq_limit:
                    result = self.Image.insert_one(item)
                    id_list.append(result.inserted_id)
                    continue
                elif item['length'] + total_size > Archiver.seq_limit:
                    results = self.Image.insert_many(file_list)
                    id_list += results.inserted_ids
                    file_list.clear()
                    total_size = 0
                file_list.append(item)
                total_size += item['length']
        if file_list:
            id_list += self.Image.insert_many(file_list).inserted_ids

        if id_list and delete:
            self.delete_stored(id_list)

        return id_list

    def find_between(self,
                     start: datetime,
                     stop: datetime=None,
                     name: str='upload_time'):
        """
        Find items upload in a specified time interval. must have a datetime
        attribute.
        """
        if stop is None:
            stop = datetime.now().replace(
                hour=0, minute=0, second=0, microsecond=0)
        id_list = []
        for item in self.Image.find({
                name: {
                    '$exists': 'true',
                    '$gte': start,
                    '$lt': stop
                }
        }, {'_id': 1}):
            id_list.append(item['_id'])
        return id_list


if __name__ == '__main__':
    archiver = Archiver()
    #print(
    #    archiver.create_item('D:/Downloads',
    #                         '0064qpHlgw1fb0z8d26p7j33sg5oghe0.jpg'))
    archiver.bulk_insert('D:/Downloads/TempDown', delete=True)

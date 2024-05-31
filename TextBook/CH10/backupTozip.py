import zipfile
import os

def backup_to_zip(folder):
    # ディレクトリ全体をZIPファイルにバックアップする
    folder = os.path.abspath(folder) # foloderを絶対パスにする
    
    # 既存のファイル名からファイル名の連番を決める
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # ZIPファイルを作成する
    print(f'Creating {zip_filename}')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # ディレクトリのツリーを渡り歩いてその中のファイルを圧縮する
    new_base = os.path.basename(folder) + '_'
    for foldername, subfolders, filename in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # 現在のディレクトリをZIPファイルに追加する
        for filename in filename:
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')

backup_to_zip(r'/delicious')

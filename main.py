import requests

class YaUploader:
    """Принимает на вход путь до файла на компьютере и 
    сохраняет на Яндекс.Диск с таким же именем"""

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""

        file_name = file_path.split('/', )[-1]
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            "path": f"Загрузки/{file_name}",
            "overwrite": "true"
        }
        headers = {
            'Authorization': token
        }

        response_get = requests.get(url, params=params, headers=headers)
        url_for_upload = response_get.json().get('href', '')

        with open("file.jpg", "rb") as file:
            response_put = requests.put(url_for_upload, files={"file": file})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    # В path_to_file необходимо указать актуальный путь до файла на компьютере
    # в token нужно прописать токен пользователя
    path_to_file = 'file.jpg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

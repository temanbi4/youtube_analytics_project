from src.channel import Channel

if __name__ == '__main__':
    MaxKatz = Channel('UCUGfDbfRIx51kJGGHIFo8Rw')
    # получаем значения атрибутов
    print(MaxKatz.title)  # MaxKatz
    print(MaxKatz.video_count)  # 685 (может уже больше)
    print(MaxKatz.url)  # https://www.youtube.com/channel/UCUGfDbfRIx51kJGGHIFo8Rw

    # менять не можем
    MaxKatz.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    MaxKatz.to_json('MaxKatz.json')

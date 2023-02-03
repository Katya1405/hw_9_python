import emoji

reaction = input('Поставить лайк публикации? ')
if reaction == 'Да':
    print(emoji.emojize(("Вам понравилась публикация :red_heart:")))
else: print(emoji.emojize("Вам не понравилась публикация :thumbs_down:"))



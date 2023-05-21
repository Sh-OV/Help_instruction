git push: отказано в разрешении (открытый ключ) (git push: permission denied (public key))
Я пытаюсь отправить файл в репозиторий git друга, но ошибки в открытом ключе.

git push origin testbranch Permission denied (publickey). fatal: Could not read from remote repository. Где и как мы определяем открытые / закрытые ключи?

git remote -v ВОЗВРАТ:

origin git@github.com:Sesamzaad/NET.git (fetch) origin git@github.com:Sesamzaad/NET.git (push) Любая помощь приветствуется.

Я столкнулся с той же проблемой, и вот что я сделал, что сработало для меня.
Используйте ssh вместо http. Удалите источник, если его http.

git remote rm origin Добавить URL-адрес ssh

git remote add origin git@github.com:/.git Сгенерируйте ssh-ключ внутри .ssh/ папки. Он запросит путь и пароль, где вы можете просто нажать enter и продолжить.

cd ~/.ssh ssh-keygen Скопируйте ключ. Вы можете просмотреть свой ключ с помощью -

cat ~/.ssh/id_rsa.pub Если вы не указали другой путь, то это будет путь по умолчанию.

Добавьте этот ключ в свою учетную запись github.

Далее выполните -

ssh -T git@github.com Вы получите приветственное сообщение в своей консоли.

Напишите в консоле проекта: git push -u origin master
теперь работает!
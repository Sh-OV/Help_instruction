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

________________________________________________________________________________

# Ошибка: отказано в разрешении (publickey)

## Следует ли использовать sudo команду или повышенные привилегии с Git?
Вы не должны использовать sudo команду или повышенные привилегии, такие как права администратора, с Git. Если у вас есть очень веская причина, которую вы должны использовать sudo, убедитесь, что вы используете ее с каждой командой (вероятно, просто лучше использовать su, чтобы получить оболочку от имени root в этот момент). Если вы создаете SSH-ключи безsudo, а затем пытаетесь использовать команду like sudo git push, вы не будете использовать те же ключи, которые вы сгенерировали.

## Убедитесь, что вы подключаетесь к правильному серверу
Печатать сложно, мы все это знаем. Обратите внимание на то, что вы вводите; вы не сможете подключиться к "githib.com " или "guthub.com ". В некоторых случаях корпоративная сеть также может вызвать проблемы с разрешением записи DNS.

Чтобы убедиться, что вы подключаетесь к правильному домену, вы можете ввести следующую команду:

$ ssh -vT git@github.com
> OpenSSH_8.1p1, LibreSSL 2.7.3
> debug1: Reading configuration data /Users/YOU/.ssh/config
> debug1: Reading configuration data /etc/ssh/ssh_config
> debug1: /etc/ssh/ssh_config line 47: Applying options for *
> debug1: Connecting to github.com port 22.
Соединение должно быть установлено через порт 22, если вы не переопределяете настройки для использования SSH через HTTPS.

## Всегда используйте пользователя "git"
Все подключения, в том числе для удаленных URL-адресов, должны выполняться от имени пользователя "git". Если вы попытаетесь подключиться под своим именем пользователя на GitHub, это не удастся:

$ ssh -T GITHUB-USERNAME@github.com
> Permission denied (publickey).
Если ваше соединение не удалось и вы используете удаленный URL-адрес с вашим именем пользователя на GitHub, вы можете изменить удаленный URL-адрес, чтобы использовать пользователя "git".

Вы должны подтвердить свое соединение, введя:

$ ssh -T git@github.com
> Hi USERNAME! You've successfully authenticated...
Убедитесь, что у вас есть используемый ключ
Если у вас установлен GitHub Desktop, вы можете использовать его для клонирования репозиториев и не иметь дело с SSH-ключами.

Если вы используете Git Bash, включите ssh-agent:

# start the ssh-agent in the background
$ eval "$(ssh-agent -s)"
> Agent pid 59566
Если вы используете другое приглашение терминала, например Git для Windows, включите ssh-agent:

# start the ssh-agent in the background
$ eval $(ssh-agent -s)
> Agent pid 59566
Убедитесь, что у вас сгенерирован закрытый ключ и загружен в SSH.

$ ssh-add -l -E sha256
> 2048 SHA256:274ffWxgaxq/tSINAykStUL7XWyRNcRTlcST1Ei7gBQ /Users/USERNAME/.ssh/id_rsa (RSA)
ssh-addКоманда должна распечатать длинную строку цифр и букв. Если он ничего не печатает, вам нужно будет сгенерировать новый SSH-ключ и связать его с GitHub.

Совет: В большинстве систем закрытые ключи по умолчанию (~/.ssh/id_rsa и ~/.ssh/identity) автоматически добавляются в агент аутентификации SSH. Вам не нужно запускатьssh-add path/to/key, если вы не переопределите имя файла при создании ключа.

Получение более подробной информации
Вы также можете проверить, используется ли ключ, попытавшись подключиться к git@github.com:

$ ssh -vT git@github.com
> ...
> debug1: identity file /Users/YOU/.ssh/id_rsa type -1
> debug1: identity file /Users/YOU/.ssh/id_rsa-cert type -1
> debug1: identity file /Users/YOU/.ssh/id_dsa type -1
> debug1: identity file /Users/YOU/.ssh/id_dsa-cert type -1
> ...
> debug1: Authentications that can continue: publickey
> debug1: Next authentication method: publickey
> debug1: Trying private key: /Users/YOU/.ssh/id_rsa
> debug1: Trying private key: /Users/YOU/.ssh/id_dsa
> debug1: No more authentication methods to try.
> Permission denied (publickey).
В том примере у нас не было никаких ключей для использования по SSH. "-1" в конце строк "идентификационный файл" означает, что SSH не смог найти файл для использования. Позже в строках "Пытаюсь использовать закрытый ключ" также указывается, что файл не найден. Если бы файл существовал, эти строки были бы "1" и "Предоставление открытого ключа" соответственно:

$ ssh -vT git@github.com
> ...
> debug1: identity file /Users/YOU/.ssh/id_rsa type 1
> ...
> debug1: Authentications that can continue: publickey
> debug1: Next authentication method: publickey
> debug1: Offering RSA public key: /Users/YOU/.ssh/id_rsa
Убедитесь, что открытый ключ прикреплен к вашей учетной записи
Вы должны предоставить свой открытый ключ GitHub, чтобы установить безопасное соединение.

Откройте командную строку.

Запустите SSH agent в фоновом режиме.

$ ssh-agent -s
> Agent pid 59566
Найдите и запишите отпечаток вашего открытого ключа.

$ ssh-add -l -E sha256
> 2048 SHA256:274ffWxgaxq/tSINAykStUL7XWyRNcRTlcST1Ei7gBQ /Users/USERNAME/.ssh/id_rsa (RSA)
В правом верхнем углу любой страницы щелкните фотографию своего профиля, затем нажмите "Настройки".

Скриншот меню учетной записи GitHub, показывающий параметры для пользователей для просмотра и редактирования их профиля, содержимого и настроек. Пункт меню "Настройки" выделен темно-оранжевым цветом.

В разделе "Доступ" на боковой панели нажмите  ключи SSH и GPG.

Сравните список ключей SSH с выводом ssh-add команды.

Если вы не видите свой открытый ключ в GitHub, вам нужно добавить свой SSH-ключ в GitHub, чтобы связать его с вашим компьютером.

Предупреждение: Если вы видите на GitHub незнакомый вам SSH-ключ, немедленно удалите его и обратитесь в службу поддержки GitHub за дополнительной помощью. Неопознанный открытый ключ может указывать на возможную проблему безопасности. Для получения дополнительной информации см. раздел "Проверка ваших SSH-ключей".

Помощь и поддержка
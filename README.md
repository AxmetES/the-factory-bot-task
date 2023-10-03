## the factory bot task.

### get start

#### clone rep.
```bash
git clone git@github.com:AxmetES/the_factory_bot_task_compose.git
```

#### move to rep.
```bash
cd the_factory_bot_task_compose
```

add ```.env``` file.
for example:

```POSTGRES_USER=admin```

```POSTGRES_PASSWORD=admin```

```POSTGRES_DB=db```

```POSTGRES_HOST=db```

```JWT_SECRET=03903af3ddb83d09f3e23e6424f47fcb```

```ALGORITHM=HS256```

```BOT_TOKEN=```{[token from bot father](https://t.me/botfather).}


#### run
```bash
docker-compose build
```

```bash
docker-compose up
```

#### usage

url on digital ocean:

[http://104.248.42.254:8000/docs]()

1. POST request ```/user/signup```:

    fill in the fields
    ```
    {
      "login": "your_login",
      "password": "your_password",
      "username": "username"
    }
    ```
    response:
    ```
    {
      "access token": "eyJhbG.........76ndrM"
    }
    ```
2. POST request ```/user/login```:
    ```
    {
      "login": "your_login",
      "password": "your_password"
    }
    ```
    response:
    ```
    {
      "access token": "eyJhbG.........76ndrM"
    }
    ```
   
#### Next step

find bot by name:

https://t.me/answer_by_tokin_bot

if everything goes well you will receive an answer:

```
U are registered.
```

#### Authorize

use the token you received earlier for authorization

3. GET request ```/message/```:

fill out the form to send a text.
send text.

You will receive the sent text in a telegram bot
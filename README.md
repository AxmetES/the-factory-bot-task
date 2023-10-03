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


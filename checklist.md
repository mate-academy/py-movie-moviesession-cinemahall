# Сheck Your Code Against the Following Points

## Don't Push db files
Make sure you don't push db files (files with `.sqlite`, `.db3`, etc. extension).

## Don't Forget to Add Migrations to your PR
This is a required for the tests to pass.

## Code Efficiency
1. Don't load the DB when it's not needed.

Good example:
```python
id_ = 1

Player.objects.create(
    name="John",
    team_id=id_
)
```

Bad example:
```python
id_ = 1

Player.objects.create(
    name="John",
    team=Team.objects.get(id=id_)
)
```

2. Don't overuse f-string.

Good example:
```python
class Player(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name
```

Bad example:
```python
class Player(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name}"
```

3. Don't use `.filter()` when you need to get one item, use `.get()` instead.

Good example:
```python
player_id = 1

Player.objects.get(id=player_id)
```

Bad example:
```python
player_id = 1

Player.objects.filter(id=player_id)
```

4. **Please note:** the `.get()` method returns a single object, not a `QuerySet`.

Good example:
```python
player_id = 1

def get_player_by_id(player_id: int) -> Player:
    return Player.objects.get(id=player_id)
```

Bad example:
```python
player_id = 1

def get_player_by_id(player_id: int) -> QuerySet:
    return Player.objects.get(id=player_id)
```

5. Use the `.set()` method to add a couple of many-to-many relationships (imagine `skills` is `ManyToManyField`).

Good example:
```python
player = Player.objects.get(id=1)
skills_ids = [1, 2, 3]

player.skills.set(skills_ids)
```

Bad example:
```python
player = Player.objects.get(id=1)
skills_ids = [1, 2, 3]

for id_ in skills_ids:
    player.skills.add(id_)
```

## Code Style
1. Use one style of quotes in your code. Double quotes are preferable.
2. Use the correct `related_name`. In the majority of cases, the name of the model in plural will be just right.

Good example:
```python
class Team(models.Model):
    pass

class Player(models.Model):
    name = models.CharField(max_length=63)
    team = models.ForeignKey(Team, related_name="players")
```

Bad example:
```python
class Team(models.Model):
    pass

class Player(models.Model):
    name = models.CharField(max_length=63)
    team = models.ForeignKey(Team, related_name="teams")
```

## Clean Code
Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.

![FastAPI logo](https://geekflare.com/wp-content/uploads/2019/07/fast-api-logo.png)
# FastAPI example

## Start server
1. Start
```bash
$ uvicorn main:app
```
2. Automtic Reload
```bash
$ uvicorn main:app --reload
```
3. Change port
```bash
$ uvicorn main:app --port 3000
```
> You can change 3000

## Access to doc
In search bar write: `localhost:port/redoc`

## Use of Type Hints:
```python
@app.get('/user/{user_id}')
def show_user(user_id: int):
    actions...
```
Check the value and return error if `user_id` isn't a integer
from fastapi import HTTPException

server_internal = HTTPException(status_code=500, detail={'code': "E_SERVER_INTERNAL",'msg': "something happens on server"})

password_is_invalid = HTTPException(status_code=403, detail={'code': "E_NOT_ACCESS", 'msg': "passwords is not match"})

user_isnt_exist = lambda username: HTTPException(status_code=403, detail={'code': 'E_NOT_ACCESS', 'msg': f'user with name {username} user isnt exist'})

user_exist = lambda username: HTTPException(status_code=403, detail={'code': 'E_NOT_ACCESS', 'msg': f'user with name {username} is exist'})

doc_isnt_exist = lambda id: HTTPException(status_code=404, detail={'code': "E_NOT_FOUND", 'msg': f'cannot find doc by this id {id}'})

doc_is_exist = lambda id: HTTPException(status_code=404, detail={'code': "E_NOT_FOUND", 'msg': f'cannot find doc by this id {id}'})

todo_is_complete = HTTPException(status_code=403, detail={'code': 'E_NOT_ACCESS', 'msg': 'cannot edit completed todo'})

user_is_broken = HTTPException(status_code=403, detail={'code': 'E_NOT_ACCESS','msg': 'logged in user is broken'})
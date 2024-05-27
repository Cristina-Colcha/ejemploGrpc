import grpc
from concurrent import futures
import user_pb2
import user_pb2_grpc

users_db = {
    1: {"name": "John Doe", "email": "john.doe@example.com"},
    2: {"name": "Jane Smith", "email": "jane.smith@example.com"},
    3: {"name": "JoseSmith", "email": "jose.smith@example.com"}
}

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        user_id = request.user_id
        if user_id in users_db:
            user = users_db[user_id]
            return user_pb2.UserResponse(user_id=user_id, name=user["name"], email=user["email"])
        else:
            context.set_details(f'User with id {user_id} not found')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return user_pb2.UserResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

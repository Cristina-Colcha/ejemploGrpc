import grpc
import user_pb2
import user_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        user_id = 3
        response = stub.GetUser(user_pb2.UserRequest(user_id=user_id))
        if response.name:
            print(f'User ID: {response.user_id}')
            print(f'Name: {response.name}')
            print(f'Email: {response.email}')
        else:
            print('User not found')

if __name__ == '__main__':
    run()

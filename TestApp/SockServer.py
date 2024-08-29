import socket


def get_all_ip():
    hostname = socket.gethostname()
    ip_list = []
    # 获取IP地址信息
    addr_infos = socket.getaddrinfo(hostname, None)
    for addr in addr_infos:
        ip_list.append(addr[4][0])
    # print(ip_list)
    return ip_list

# 设置服务器主机和端口
HOST = '172.20.10.7'
PORT = 65432

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        print("*************Recv not data***************")
                        break
                    print(f"Received data: {data.decode()}")
                    # 向客户端回传数据
                    response = f"Server received: {data.decode()}"
                    conn.sendall(response.encode())
                    print(f"Sent response: {response}")
                    
if __name__ == "__main__":
    print("Hostname : ",socket.gethostname())
    print("Host : ",socket.gethostbyname(socket.gethostname()))
    ips = get_all_ip()
    print("IPS : ",ips)
    while(True):
        start_server()

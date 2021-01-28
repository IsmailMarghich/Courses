#include <stdio.h>

#include <sys/socket.h>
#include <netinet/in.h>

#include <unistd.h>
#include <stdlib.h>
#include <memory.h>
//in C we can access the internet, and write clients and servers using sockets
//we will be using sockets, sockets are virtual endpoints of networks, with these socket we can form a connection with other computers

//in this file we will create a server which takes an integer from client 1, decrements the number
//and then sends the integer to client2, which prints it out
short socketCreate(void) { //function to create socket
    short hSocket;
    printf("Created the socket\n");
    hSocket = socket(AF_INET, SOCK_STREAM, 0);
    return hSocket;
}


int bindCreatedSocket(int hSocket) { //binding to a port so a client can connect to it
    int iRetval = -1;
    int clientPort = 12345;

    struct sockaddr_in remote = {0};

    /* Internet address family */
    remote.sin_family = AF_INET;

    /* Any incoming interface */
    remote.sin_addr.s_addr = htonl(INADDR_ANY);
    remote.sin_port = htons(clientPort); /* Local port */

    iRetval = bind(hSocket, (struct sockaddr *) &remote, sizeof(remote));
    return iRetval;
}

int main(int argc, char *argv[]) {
    int socket_desc = 0, sock = 0, clientLen = 0;
    struct sockaddr_in client;
    char client_message[200] = {0};
    char message[100] = {0};

    //Create socket
    socket_desc = socketCreate();

    if (socket_desc == -1) {
        printf("Could not create socket");
        return 1;
    }

    printf("Socket created\n");

    //Bind
    if (bindCreatedSocket(socket_desc) < 0) {
        //print the error message
        perror("bind failed.");
        return 1;
    }

    printf("bind done\n");

    //Listen
    listen(socket_desc, 3);

    printf("Waiting for incoming connections...\n");
    clientLen = sizeof(struct sockaddr_in);

    //accept connection from an incoming client
    sock = accept(socket_desc, (struct sockaddr *) &client, (socklen_t *) &clientLen);

    if (sock < 0) {
        perror("accept failed");
        return 1;
    }

    printf("Connection accepted\n");
    memset(client_message, '\0', sizeof client_message);
    memset(message, '\0', sizeof message);

    //Receive a reply from the client
    if (recv(sock, client_message, 200, 0) < 0) {
        printf("recv failed");
    }

    printf("Received from Client: %s\n", client_message);

    int i = atoi(client_message);
    i--;
    sprintf(message, "%d", i);

    close(sock);

    printf("Waiting for incoming connections...\n");

    //accept connection from an incoming client
    sock = accept(socket_desc, (struct sockaddr *) &client, (socklen_t *) &clientLen);

    if (sock < 0) {
        perror("accept failed");
        return 1;
    }

    printf("Connection accepted\n");

    // Send some data
    if (send(sock, message, strlen(message), 0) < 0) {
        printf("Send failed");
        return 1;
    }

    return 0;


}
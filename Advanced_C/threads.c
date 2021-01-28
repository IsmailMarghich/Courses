#include <stdio.h>
#include <pthread.h>

//with threads we can divide a computational loads over multiple logical cores of the CPU, this means performance will increase
//by default C runs on one thread, so the code is run only one instruction at a time, but we can increase this with threads
//because there are many different operating systems and languages out there, a standard interface was made for threads
//we are going to be using POSIX threads to create multi threaded C programs, which will allow us to run prorgams faster
pthread_mutex_t lock = NULL;
int lockvariable = 0; //this is a global variable which we will try to edit with our threads
void *threadedfunction() //our function which we will thread, we need a pointer
{
    lockvariable *= 2;
    printf("\nthread id: %d\n", pthread_self()); //with pthread_self we can get the thread id of a thread
    return NULL;
}

void *
mutexfunction() //sometimes multiple threads are working on the same variable, to synchronize the threads we can use mutexes

{
    pthread_mutex_init(&lock, NULL); //we initialize a mutex in this thread
    pthread_mutex_lock(&lock);       //we lock this thread
    for (int i = 0; i < 10; i++)
        lockvariable++; //we add 10 to our global variable
    printf("\nthread id: %d\n", pthread_self());
    pthread_mutex_unlock(&lock); //we unlock our thread, now the other function can multiply it by 2
    return NULL;

}

int main() {
    pthread_t thread = 0; //declaring our thread datatype
    pthread_t mutexthread = 0; //declaring our mutex thread
    pthread_create(&mutexthread, NULL, mutexfunction, NULL);
    pthread_create(&thread, NULL, threadedfunction, NULL);

    //pthread_exit(NULL); //with pthread exit function we can stop the thread
    //with the pthread create function we can create threads, it takes 4 arguments. 1. is type pthread_t, which is a thread datatype
    //2. is whether to use specific attributes, NULL is for default attributes, 3. name of function that will be executed once thread is created
    //4. the 4th argument is used to pass arguments to a start_routine function, or to return variables
    pthread_join(mutexthread, NULL);
    pthread_join(thread,
                 NULL); //this function wll join the thread with the main thread, so they can both run at the same time
    printf("%d",
           lockvariable); //this will print 20, because first it adds 10 with the mutex function, then it multiplies by 2
    pthread_exit(thread); //to be safe, we manually close the thread with pthread exit function
    pthread_exit(mutexthread);
    return 0;
}

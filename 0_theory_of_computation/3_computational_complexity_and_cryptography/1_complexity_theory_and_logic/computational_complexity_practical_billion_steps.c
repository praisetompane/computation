/*
    given:
        since modern computers can execute >1 billion instructions per second.
    objective:
        Does it a modern computer 10 seconds to iterate 10000000000 times?
*/

#include <time.h>
#include <stdio.h>

void main()
{

    time_t raw_time;
    struct tm *start_time;
    struct tm *end_time;
    time(&raw_time);
    start_time = localtime(&raw_time);

    printf("starting computation at: %s\n", asctime(start_time));

    /*
    upto 1 000 000 000, the iteration runs very very quickly.
    once you get to 10 000 000 000, it takes a while.
    Q: what is going on in the machine, that at this point it struggles?
    */
    long long n = 1000000000;
    for (int i = 0; i < n; i++)
    {
        i + 1; // check how quick this is?
    }
    end_time = localtime(&raw_time);
    printf("computation completed at: %s\n", asctime(end_time));
    printf("end_time - start_time = %s\n", difftime(start_time, end_time)); // this is not correct, difftime expects time_t, see warnings
}
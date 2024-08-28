#include <stdio.h>

extern void tcp_client_main(void);
extern void init_blink(void);

void app_main(void)
{
    init_blink();


    tcp_client_main();
}

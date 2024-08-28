#include <stdio.h>
#include "main.h"

extern void tcp_client_main(void);
extern void init_blink(void);
extern void tcp_client_init(void);
extern void app_blink(void);
extern int startSockCli(void);
extern int tcpSockSend(void);
extern void closeSock(void);

static const char *TAG = "main";
int sock_sts = -1;

void app_main(void)
{
    int errSts;
    init_blink();
    tcp_client_init();
    sock_sts = startSockCli();

    while(1)
    {
        if(sock_sts >= 0)
        {
            errSts = tcpSockSend();
            ESP_LOGE(TAG, "tcpSockSend err : %d", errSts);
        }
        else
        {
            closeSock();
            sock_sts = startSockCli();
        }

        //tcp_client_main();

        
        app_blink();
        vTaskDelay(CONFIG_TASK_PERIOD / portTICK_PERIOD_MS);
    }
}

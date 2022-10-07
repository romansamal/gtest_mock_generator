#ifndef _HTTP_WRAPPER_H
#define _HTTP_WRAPPER_H

#include "infra_types.h"
#include "infra_defs.h"
#include "wrappers_defs.h"

int HAL_SetProductKey(char *product_key);
int HAL_SetProductSecret(char *product_secret);
int HAL_SetDeviceName(char *device_name);
int HAL_SetDeviceSecret(char *device_secret);
void *HAL_Malloc(uint32_t size);
void HAL_Free(void *ptr);
void HAL_Printf(char *fmt);
int HAL_Snprintf(char *str, int len, char *fmt);
uint64_t HAL_UptimeMs(void);
void HAL_SleepMs(uint32_t ms);

#endif /* #ifndef _HTTP_WRAPPER_H */
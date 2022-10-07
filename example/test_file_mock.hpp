#pragma once
#include <gmock/gmock.h>
#include <gtest/gtest.h>

extern "C"
{
	#include "test_file.h"
}

class test_file
{
public:
	virtual ~test_file() = 0;

	virtual int HAL_SetProductKey(
		char *product_key) = 0;

	virtual int HAL_SetProductSecret(
		char *product_secret) = 0;

	virtual int HAL_SetDeviceName(
		char *device_name) = 0;

	virtual int HAL_SetDeviceSecret(
		char *device_secret) = 0;

	virtual void *HAL_Malloc(
		uint32_t size) = 0;

	virtual void HAL_Free(
		void *ptr) = 0;

	virtual void HAL_Printf(
		char *fmt) = 0;

	virtual int HAL_Snprintf(
		char *str,
		int len,
		char *fmt) = 0;

	virtual uint64_t HAL_UptimeMs() = 0;

	virtual void HAL_SleepMs(
		uint32_t ms) = 0;

};

class test_file_mock : public test_file
{
public:
	~test_file_mock() override;

	MOCK_METHOD1(HAL_SetProductKey,
				int(
				char *product_key));

	MOCK_METHOD1(HAL_SetProductSecret,
				int(
				char *product_secret));

	MOCK_METHOD1(HAL_SetDeviceName,
				int(
				char *device_name));

	MOCK_METHOD1(HAL_SetDeviceSecret,
				int(
				char *device_secret));

	MOCK_METHOD1(*HAL_Malloc,
				void(
				uint32_t size));

	MOCK_METHOD1(HAL_Free,
				void(
				void *ptr));

	MOCK_METHOD1(HAL_Printf,
				void(
				char *fmt));

	MOCK_METHOD3(HAL_Snprintf,
				int(
				char *str,
				int len,
				char *fmt));

	MOCK_METHOD0(HAL_UptimeMs,
				uint64_t());

	MOCK_METHOD1(HAL_SleepMs,
				void(
				uint32_t ms));

};

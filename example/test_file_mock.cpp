#include "test_file_mock.hpp"

namespace mock_objects
{
	extern std::unique_ptr<test_file_mock> test_fileMock;
};

test_file::~test_file()
{}

test_file_mock::~test_file_mock()
{}

int HAL_SetProductKey(
	char *product_key)
{
	return mock_objects::test_fileMock->HAL_SetProductKey(*product_key);
}

int HAL_SetProductSecret(
	char *product_secret)
{
	return mock_objects::test_fileMock->HAL_SetProductSecret(*product_secret);
}

int HAL_SetDeviceName(
	char *device_name)
{
	return mock_objects::test_fileMock->HAL_SetDeviceName(*device_name);
}

int HAL_SetDeviceSecret(
	char *device_secret)
{
	return mock_objects::test_fileMock->HAL_SetDeviceSecret(*device_secret);
}

void *HAL_Malloc(
	uint32_t size)
{
	return mock_objects::test_fileMock->*HAL_Malloc(size);
}

void HAL_Free(
	void *ptr)
{
	return mock_objects::test_fileMock->HAL_Free(*ptr);
}

void HAL_Printf(
	char *fmt)
{
	return mock_objects::test_fileMock->HAL_Printf(*fmt);
}

int HAL_Snprintf(
	char *str,
	int len,
	char *fmt)
{
	return mock_objects::test_fileMock->HAL_Snprintf(*str, len, *fmt);
}

uint64_t HAL_UptimeMs()
{
	return mock_objects::test_fileMock->HAL_UptimeMs();
}

void HAL_SleepMs(
	uint32_t ms)
{
	return mock_objects::test_fileMock->HAL_SleepMs(ms);
}


# Build Lists
# Modify this file to control which files/modules should be built

DRIVERS = [
    # 'gpio/*.c',
    # 'systick/st/stm32f7_systick.c',
    #'usart/st/stm32f7_usart.c',
]

DRIVERS_CPPPATH = []

HAL = [
    'pin/*.c',
    'serial/*.c',
    'systick/*.c',
    'sd/*.c',
]

HAL_CPPPATH = []

MODULES = [
    'Console/*.c',
    'System/*.c',
    'IPC/*.c',
    'SysCmd/syscmd.c',
    'SysCmd/cmd_sys.c',
    'SysCmd/cmd_mcn.c',
    'File_Manager/*.c',
    "Log/boot_log.c",
]

MODULES_CPPPATH = []

LIBS = [
    'cm_backtrace',
]
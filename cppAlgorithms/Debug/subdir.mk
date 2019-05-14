################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../helloworld.cpp \
../kuaisu_paisu_2.cpp \
../kuaisu_paixu.cpp \
../stdafx.cpp 

OBJS += \
./helloworld.o \
./kuaisu_paisu_2.o \
./kuaisu_paixu.o \
./stdafx.o 

CPP_DEPS += \
./helloworld.d \
./kuaisu_paisu_2.d \
./kuaisu_paixu.d \
./stdafx.d 


# Each subdirectory must supply rules for building sources it contributes
%.o: ../%.cpp
	@echo 'Building file: $<'
	@echo 'Invoking: Cross G++ Compiler'
	g++ -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '



cmake_minimum_required (VERSION 3.2)
project(OpenTreadmill)

set(THIRD_PARTY_LIBRARY_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/3rdParty)
#Zmq Library
add_subdirectory(${THIRD_PARTY_LIBRARY_DIRECTORY}/libzmq)
#WiringPi doesn't come with a CMakelists file so get enough for us to use
include(${THIRD_PARTY_LIBRARY_DIRECTORY}/WiringPi.Cmake.txt)

set(CONTROLLER_SOURCE_DIR ${CMAKE_CURRENT_LIST_DIR}/controller/Source)
set(CONTROLLER_SOURCE)
#These backends are the code used for the device specific setup in order
#to use the abstract interface
set(CONTROLLER_BACKEND_SOURCE
	${CONTROLLER_SOURCE_DIR}/Backends/Icon/MC2100LTS-30.hpp
	${CONTROLLER_SOURCE_DIR}/Backends/Icon/MC2100LTS-30.cpp
	)
list(APPEND CONTROLLER_SOURCE ${CONTROLLER_BACKEND_SOURCE})

set(CONTROLLER_SHARED_SOURCE
	${CONTROLLER_SOURCE_DIR}/controller.h
	${CONTROLLER_SOURCE_DIR}/controller.cpp
	${CONTROLLER_SOURCE_DIR}/gpio.h
	${CONTROLLER_SOURCE_DIR}/gpio.cpp
	)
list(APPEND CONTROLLER_SHARED_SOURCE ${CONTROLLER_BACKEND_SOURCE})

#Third part Libraries
add_executable(controller ${CONTROLLER_SHARED_SOURCE})
target_link_libraries(controller PUBLIC libzmq-static WiringPi)
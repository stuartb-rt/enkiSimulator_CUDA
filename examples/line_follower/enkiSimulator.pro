TEMPLATE = app
TARGET = enkisimulator
INCLUDEPATH += .

INCLUDEPATH += /usr/local/include/enki
#INCLUDEPATH += /home/sama/Documents/CLDL/include		#original CLDL headers
INCLUDEPATH += /home/sama/CLDL_CUDA/include			#CLDL_CUDA headers

# Input
HEADERS += Racer.h \
    bandpass.h \
    globals.h \
    parameters.h

SOURCES += run.cpp \
    Racer.cpp \
    bandpass.cpp

QT += opengl widgets
CONFIG          += qt warn_on debuge debug
QMAKE_CXXFLAGS += -std=c++0x -march=native -Wunused -pedantic -lenki
QMAKE_LFLAGS += -lenki

LIBS	+= /usr/local/lib/libenki.a
#LIBS	+= /usr/local/lib/libCLDL_STATIC.a
#LIBS    += /home/sama/Documents/CLDL/libcldl_static.a		#original CLDL lib
LIBS    += /home/sama/CLDL_CUDA/libCLDL_STATIC.a		#CLDL_CUDA lib

#copydata.commands = $(COPY_DIR) $$PWD/cc.png $$OUT_PWD

#first.depends = $(first) copydata
#export(first.depends)
#export(copydata.commands)
#QMAKE_EXTRA_TARGETS += first copydata


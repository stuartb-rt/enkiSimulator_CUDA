TEMPLATE = app
TARGET = enkisimulator
INCLUDEPATH += .

CUDA_DIR = $$system(which nvcc | sed 's,/bin/nvcc$,,')

INCLUDEPATH += /usr/local/include/enki
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
CONFIG += qt warn_on debuge debug
QMAKE_CXXFLAGS += -std=c++0x -march=native -Wunused -pedantic -lenki
QMAKE_LFLAGS += -lenki

LIBS	+= /usr/local/lib/libenki.a
LIBS    += /home/sama/CLDL_CUDA/build/libCLDL.a			#CLDL_CUDA lib
LIBS += -lcudart
LIBS += -lcurand

cuda.output = ${OBJECTS_DIR}${QMAKE_FILE_BASE}_cuda.obj

cuda.commands = nvcc -c -Xcompiler $$join(QMAKE_CXXFLAGS,",") $$join(INCLUDEPATH,'" -I "','-I "','"') ${QMAKE_FILE_NAME} -o ${QMAKE_FILE_OUT}
cuda.depends = nvcc -M -Xcompiler $$join(QMAKE_CXXFLAGS,",") $$join(INCLUDEPATH,'" -I "','-I "','"') ${QMAKE_FILE_NAME} | sed "s,^.*: ,," | sed "s,^ *,," | tr -d '\\n'

cuda.input = CUDA_SOURCES

QMAKE_EXTRA_UNIX_COMPILERS += cuda



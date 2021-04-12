#ifndef PARAMETERS_H
#define PARAMETERS_H

#endif // PARAMETERS_H

#define STEPSCOUNT 5000
// Network Structure
#define nPROPAGATIONS 1
#define LEARNINGRATE 0.1

#define NLAYERS 11
    #define N1 22
    #define N2 20
    #define N3 18
    #define N4 16
    #define N5 14
    #define N6 12
    #define N7 10
    #define N8 8
    #define N9 6
    #define N10 4
    #define N11 2

// Predictor Array
#define ROW1P 12
#define ROW1N 24
#define ROW1S 2

#define ROW2P 14
#define ROW2N 18
#define ROW2S 2

#define ROW3P 16
#define ROW3N 12
#define ROW3S 2

// Error Arrays
#define SENSORLEFT 8
#define SENSORRIGHT -8

// Filter Specifications
#define NFILTERS 5
#define MINT 3 //3
#define MAXT 10 //10
#define DAMPINGCOEFF 0.51

// Robot speed
#define SPEED 30 // for reflex it is 60
#define ERRORGAIN 150 // for reflex it is 200

#define NETWORKGAIN 10
#define PREDGAIN 100



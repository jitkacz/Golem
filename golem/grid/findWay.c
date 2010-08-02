/* ***************************************************** */
/*              AUTHOR: Daniel Svec                      */
/*              NAME: Golem - findWay                    */
/*              LAST CHANGE: 1.8.2010                    */
/* ***************************************************** */

#include <Python.h>

// The function find the fastest road in table
//
// name: _findWay
// @param
// int currentCoordinates[2]
// int finishCoordinates[2]
// table of integers (bigger than zero)
//
// @return
PyObject* findWay(PyObject* self, PyObject* args) {
    PyObject *table;

    long currentCoordinates[2];
    long finishCoordinates[2];

    //Load parameters
    if (!PyArg_ParseTuple(args, "(ii)(ii)O", &currentCoordinates[0], &currentCoordinates[1], &finishCoordinates[0], &finishCoordinates[1], &table))
        return NULL;

    long tableSize[2] = {PyList_Size(PyList_GetItem(table, 0)), PyList_Size(table)};
    long map[tableSize[0]][tableSize[1]];

    //Convert table from python list to array
    int y = 0;
    int x = 0;
    for (y; y < tableSize[1]; ++y) {
        x = 0;
        for (x; x < tableSize[0]; ++x) {
            map[x][y] = PyInt_AsLong(PyList_GetItem(PyList_GetItem(table, y) ,x));
        }
    }

    //Treatment of the case the target coordinates are equal to zero
    if (map[finishCoordinates[0]][finishCoordinates[1]] == 0)
        return Py_False;

    //Treatment of the case the target coordinates are greater then table
    if (finishCoordinates[0] > tableSize[0]-1 || finishCoordinates[1] > tableSize[1]-1)
        return Py_False;

    //Create python list with coordinates of the fastest way
    PyObject* theFastesWay = PyList_New(0);

    //Find the fastest way
    int i = 0;
    int finalWayOverZero = 0;

    while (!(currentCoordinates[0] == finishCoordinates[0] && currentCoordinates[1] == finishCoordinates[1])) {
        //Retrieving values and symptoms in all conditions
        long plusX;
        long plusY;

        int symptomX = 0;
        int symptomY = 0;

        if (currentCoordinates[0] != finishCoordinates[0] && currentCoordinates[0] < tableSize[0]-1 && currentCoordinates[1] != finishCoordinates[1] && currentCoordinates[1] < tableSize[1]-1) {
            plusX = map[currentCoordinates[0]+1][currentCoordinates[1]];
            plusY = map[currentCoordinates[0]][currentCoordinates[1]+1];
        } else if (currentCoordinates[0] != finishCoordinates[0] && currentCoordinates[0] == tableSize[0]-1 && currentCoordinates[1] != finishCoordinates[1] && currentCoordinates[1] == tableSize[1]-1) {
            plusX = -1;
            plusY = -1;
        } else if (currentCoordinates[0] >= finishCoordinates[0] && currentCoordinates[0] < tableSize[0]-1 && currentCoordinates[1] != finishCoordinates[1] && currentCoordinates[1] < tableSize[1]-1) {
            plusX = map[currentCoordinates[0]+1][currentCoordinates[1]];
            plusY = map[currentCoordinates[0]][currentCoordinates[1]+1];
            symptomX = 1;
        } else if (currentCoordinates[0] == tableSize[0]-1 && currentCoordinates[1] != finishCoordinates[1] && currentCoordinates[1] < tableSize[1]-1) {
            plusX = -1;
            plusY = map[currentCoordinates[0]][currentCoordinates[1]+1];
        } else if (currentCoordinates[0] != finishCoordinates[0] && currentCoordinates[0] < tableSize[0]-1 && currentCoordinates[1] >= finishCoordinates[1] && currentCoordinates[1] < tableSize[1]-1) {
            plusX = map[currentCoordinates[0]+1][currentCoordinates[1]];
            plusY = map[currentCoordinates[0]][currentCoordinates[1]+1];
            symptomY = 1;
        } else if (currentCoordinates[0] != finishCoordinates[0] && currentCoordinates[0] < tableSize[0]-1 && currentCoordinates[1] == tableSize[1]-1) {
            plusX = map[currentCoordinates[0]+1][currentCoordinates[1]];
            plusY = -1;
        }
        //Selection of movement
        if (plusX == 0 && plusY == 0) {
            return Py_None;
        } else if (plusX == -1 && plusY == -1) {
            return Py_None;
        } else if (plusX == 0 && symptomY == 0 && plusY != 0) {
            ++currentCoordinates[1];
        } else if (plusY == 0 && symptomX == 0 && plusX != 0) {
            ++currentCoordinates[0];
        } else if (plusX == 0 && symptomY == 1 && plusY != 0) {
            //Bypassing zero at position x + 1, when standing on the target y coordinate
            PyObject* wayDown = PyList_New(0);
            PyObject* wayUp = PyList_New(0);
            int possibilityDown = 0;
            int possibilityUp = 0;
            int stepsDown = 0;
            int valueWayDown = 0;
            int stepsUp = 0;
            int valueWayUp = 0;
            //Passes the possibility to circumvent the bottom
            long currentX = currentCoordinates[0];
            long currentY = currentCoordinates[1];
            //Until it is zero at x+1 comes down
            while (map[currentX+1][currentY] == 0) {
                if (currentY < tableSize[1]-1) {
                    ++stepsDown;
                    ++currentY;
                    PyObject* buffer = PyList_New(0);
                    PyList_Append(buffer, PyInt_FromLong(currentX));
                    PyList_Append(buffer, PyInt_FromLong(currentY));
                    PyList_Append(wayDown, buffer);
                    valueWayDown += map[currentX][currentY];
                } else {
                    possibilityDown = 0;
                    break;
                }
                possibilityDown = 1;
            }
            //Until it is zero at y-1 comes right
            if (currentX < tableSize[0]-1 && possibilityDown == 1) {
                while (map[currentX+1][currentY-1] == 0 && currentX < tableSize[0]-1 && map[currentX+1][currentY] != 0) {
                    if (currentX < tableSize[0]-1) {
                        ++stepsDown;
                        ++currentX;
                        PyObject* buffer = PyList_New(0);
                        PyList_Append(buffer, PyInt_FromLong(currentX));
                        PyList_Append(buffer, PyInt_FromLong(currentY));
                        PyList_Append(wayDown, buffer);
                        valueWayDown += map[currentX][currentY];
                    } else {
                        possibilityDown = 0;
                        break;
                    }
                    possibilityDown = 1;
                }
                if (!(currentX < tableSize[0]-1))
                    possibilityDown = 0;
                if (map[currentX+1][currentY] == 0) {
                    possibilityDown = 0;
                }
            } else
                possibilityDown = 0;
            //Passes the possibility of circumventing the hill
            currentX = currentCoordinates[0];
            currentY = currentCoordinates[1];
            //Until it is zero at x+1 comes up
            while (map[currentX+1][currentY] == 0) {
                if (currentY-1 >= 0) {
                    ++stepsUp;
                    --currentY;
                    PyObject* buffer = PyList_New(0);
                    PyList_Append(buffer, PyInt_FromLong(currentX));
                    PyList_Append(buffer, PyInt_FromLong(currentY));
                    PyList_Append(wayUp, buffer);
                    valueWayUp += map[currentX][currentY];
                } else {
                    possibilityUp = 0;
                    break;
                }
                possibilityUp = 1;
            }
            //Until it is zero at y+1 comes right
            if (currentX < tableSize[0]-1 && possibilityUp == 1) {
                while (map[currentX+1][currentY+1] == 0) {
                    if (currentX < tableSize[0]-1) {
                        ++stepsUp;
                        ++currentX;
                        PyObject* buffer = PyList_New(0);
                        PyList_Append(buffer, PyInt_FromLong(currentX));
                        PyList_Append(buffer, PyInt_FromLong(currentY));
                        PyList_Append(wayUp, buffer);
                        valueWayUp += map[currentX][currentY];
                    } else {
                        possibilityUp = 0;
                        break;
                    }
                    possibilityUp = 1;
                }
                if (map[currentX+1][currentY] == 0) {
                    possibilityUp = 0;
                }
            } else
                possibilityUp = 0;
            //Saves the grid, the number of steps and amount for each trip separately
            //Choice way
            if (valueWayDown > valueWayUp && possibilityDown == 1)
                finalWayOverZero = 1;
            else if (valueWayDown == valueWayUp && possibilityDown == 1 && possibilityUp == 1) {
                if (stepsDown > stepsUp)
                    finalWayOverZero = 1;
                else
                    finalWayOverZero = 2;
            } else if (valueWayUp > valueWayDown && possibilityUp == 1)
                finalWayOverZero = 2;
            else if (possibilityUp == 0 && possibilityDown == 1)
                finalWayOverZero = 1;
            else if (possibilityUp == 1 && possibilityDown == 0)
                finalWayOverZero = 2;
            else if (possibilityUp == 0 && possibilityDown == 0)
                finalWayOverZero = 0;
            switch (finalWayOverZero) {
                case 1:
                    i = 0;
                    for (i; i < PyList_Size(wayDown)-1; ++i) {
                        PyObject* buffer = PyList_New(0);
                        PyList_Append(buffer, PyList_GetItem(PyList_GetItem(wayDown, i), 0));
                        PyList_Append(buffer, PyList_GetItem(PyList_GetItem(wayDown, i), 1));
                        PyList_Append(theFastesWay, buffer);
                    }
                    currentCoordinates[0] = PyInt_AsLong(PyList_GetItem(PyList_GetItem(wayDown, i-1), 0));
                    currentCoordinates[1] = PyInt_AsLong(PyList_GetItem(PyList_GetItem(wayDown, i-1), 1));
                    break;
                case 2:
                    i = 0;
                    for (i; i < PyList_Size(wayUp)-1; ++i) {
                        PyObject* buffer = PyList_New(0);
                        PyList_Append(buffer, PyList_GetItem(PyList_GetItem(wayUp, i), 0));
                        PyList_Append(buffer, PyList_GetItem(PyList_GetItem(wayUp, i), 1));
                        PyList_Append(theFastesWay, buffer);
                    }
                    currentCoordinates[0] = PyInt_AsLong(PyList_GetItem(PyList_GetItem(wayUp, i-1), 0));
                    currentCoordinates[1] = PyInt_AsLong(PyList_GetItem(PyList_GetItem(wayUp, i-1), 1));
                    break;
                case 0:
                    return Py_None;
            }
        } else if (plusY == 0 && symptomX == 1 && plusX != 0) {
            // TODO #1 - Circumvention of zero if x+1 is zero and the target y
            puts("TODO #1");
            return Py_None;
        } else if (plusY != 0 && plusX != 0 && symptomY == 0 && symptomX == 0) {
            if (plusX > plusY)
                ++currentCoordinates[0];
            else if (plusX < plusY)
                ++currentCoordinates[1];
            else if (plusX == plusY) {
                if (currentCoordinates[0] > currentCoordinates[1])
                    ++currentCoordinates[1];
                else
                    ++currentCoordinates[0];
            }
        } else if (plusY != 0 && plusX != 0 && symptomY == 0 && symptomX == 1)
            ++currentCoordinates[1];
        else if (plusY != 0 && plusX != 0 && symptomY == 1 && symptomX == 0)
            ++currentCoordinates[0];
        //Saves the final path
        PyObject* buffer = PyList_New(0);
        PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
        PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
        PyList_Append(theFastesWay, buffer);
        //Treatment of the case that the zero crossing point passes the target
        if (currentCoordinates[0] >= tableSize[0] || currentCoordinates[1] >= tableSize[1]) {
            switch (finalWayOverZero) {
                case 1:
                    while (currentCoordinates[1] != finishCoordinates[1]) {
                        if (map[currentCoordinates[0]][currentCoordinates[1]-1] != 0) {
                            --currentCoordinates[1];
                            PyObject* buffer = PyList_New(0);
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                            PyList_Append(theFastesWay, buffer);
                        } else {
                            if (currentCoordinates[0] < tableSize[0]-1) {
                                ++currentCoordinates[0];
                                PyObject* buffer = PyList_New(0);
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                                PyList_Append(theFastesWay, buffer);
                            } else
                                return Py_None;
                        }
                    }
                    while (currentCoordinates[0] != finishCoordinates[0]) {
                        if (map[currentCoordinates[0]-1][currentCoordinates[1]] != 0) {
                            --currentCoordinates[0];
                            PyObject* buffer = PyList_New(0);
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                            PyList_Append(theFastesWay, buffer);
                        } else
                            return Py_None;
                    }
                    break;
                case 2:
                    while (currentCoordinates[0] != finishCoordinates[0]) {
                        if (map[currentCoordinates[0]-1][currentCoordinates[1]] != 0) {
                            --currentCoordinates[0];
                            PyObject* buffer = PyList_New(0);
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                            PyList_Append(theFastesWay, buffer);
                        } else {
                            if (currentCoordinates[1] < tableSize[1]-1) {
                                ++currentCoordinates[1];
                                PyObject* buffer = PyList_New(0);
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                                PyList_Append(theFastesWay, buffer);
                            } else
                                return Py_None;
                        }
                    }
                    while (currentCoordinates[1] != finishCoordinates[1]) {
                        if (map[currentCoordinates[0]][currentCoordinates[1]+1] != 0) {
                            ++currentCoordinates[1];
                            PyObject* buffer = PyList_New(0);
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                            PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                            PyList_Append(theFastesWay, buffer);
                        } else
                            if (currentCoordinates[0] < tableSize[0]-1) {
                                ++currentCoordinates[0];
                                PyObject* buffer = PyList_New(0);
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[0]));
                                PyList_Append(buffer, PyInt_FromLong(currentCoordinates[1]));
                                PyList_Append(theFastesWay, buffer);
                            } else
                                return Py_None;
                    }
                    break;
            }
        }
    }
    Py_INCREF(Py_None);
    return theFastesWay;
}
PyMethodDef findWay_methods[] = {
    {"findWay", findWay, METH_VARARGS, "findWay"},
    {NULL, NULL, 0, NULL}
};
PyMODINIT_FUNC initfindWay(void) {
    Py_InitModule3("findWay", findWay_methods, "findWay");
}

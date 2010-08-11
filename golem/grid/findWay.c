/* ***************************************************** */
/*              AUTHOR: Daniel Švec                      */
/*              NAME: Golem - findWay                    */
/*              LAST CHANGE: 11.8.2010                   */
/* ***************************************************** */

#include <Python.h>

#define INFINITY_VALUE 1000000

// Structure to store information about node
struct node {
    int x, y, value, neighbors[4];
};

// Function finds the shortest path in forwarding the weighted graph
PyObject* findWay(PyObject* self, PyObject* args) {
    // Variables for loaded parameters
    PyObject *enteredTable;
    long initialCoordinates[2];
    long finishCoordinates[2];
    if (!PyArg_ParseTuple(args, "(ii)(ii)O", &initialCoordinates[0], &initialCoordinates[1], &finishCoordinates[0], &finishCoordinates[1], &enteredTable))
        return NULL;
    // Most of the variables defining
    long sizeX = PyList_Size(PyList_GetItem(enteredTable, 0));
    long sizeY = PyList_Size(enteredTable);
    int nodeCount = 0;
    int initialNode;
    int finishNode;
    int y = 0;
    int i = 0;
    // Convert the given graph into a graph for the algorithm
    int convertedTable[sizeX][sizeY];
    for (y; y < sizeY; ++y) {
        int x = 0;
        for (x; x < sizeX; ++x) {
            long value = PyInt_AsLong(PyList_GetItem(PyList_GetItem(enteredTable, y) ,x));
            if (value == 0)
                convertedTable[x][y] = -1;
            else {
                unsigned int convertedValue = 65535/value;
                convertedTable[x][y] = convertedValue;
                ++nodeCount;
            }
        }
    }
    // Treatment of error cases
    if (convertedTable[finishCoordinates[0]][finishCoordinates[1]] == -1 || convertedTable[initialCoordinates[0]][initialCoordinates[1]] == -1) {
        return Py_False;
    }
    if (initialCoordinates[0] == finishCoordinates[0] && initialCoordinates[1] == finishCoordinates[1])
        return PyList_New(0);
    i = 0;
    y = 0;
    // Nonzero retrieve all nodes of the graph
    struct node nodes[nodeCount];
    for (y; y < sizeY; ++y) {
        int x = 0;
        for (x; x < sizeX; ++x) {
            if (convertedTable[x][y] != -1) {
                nodes[i].x = x;
                nodes[i].y = y;
                nodes[i].value =  convertedTable[x][y];
                if (initialCoordinates[0] == x && initialCoordinates[1] == y)
                    initialNode = i;
                if (finishCoordinates[0] == x && finishCoordinates[1] == y)
                    finishNode = i;
                ++i;
            }
        }
    }
    i = 0;
    // Retrieve the neighbors for each node
    for (i; i < nodeCount; ++i) {
        nodes[i].neighbors[0] = -1;
        nodes[i].neighbors[1] = -1;
        nodes[i].neighbors[2] = -1;
        nodes[i].neighbors[3] = -1;
    }
    i = 0;
    for (i; i < nodeCount; ++i) {
        int x = 0;
        for (x; x < nodeCount; ++x) {
            if (nodes[x].x == nodes[i].x-1 && nodes[x].y == nodes[i].y)
                nodes[i].neighbors[0] = x;
            if (nodes[x].x == nodes[i].x+1 && nodes[x].y == nodes[i].y)
                nodes[i].neighbors[1] = x;
            if (nodes[x].x == nodes[i].x && nodes[x].y == nodes[i].y-1)
                nodes[i].neighbors[2] = x;
            if (nodes[x].x == nodes[i].x && nodes[x].y == nodes[i].y+1)
                nodes[i].neighbors[3] = x;
        }
    }
    // Last modified graph before searching
    int graph[nodeCount][nodeCount];
    i = 0;
    for (i; i < nodeCount; ++i) {
        int x = 0;
        for (x; x < nodeCount; ++x) {
            if (x == nodes[i].neighbors[0])
                graph[i][x] = nodes[nodes[i].neighbors[0]].value;
            else if (x == nodes[i].neighbors[1])
                graph[i][x] = nodes[nodes[i].neighbors[1]].value;
            else if (x == nodes[i].neighbors[2])
                graph[i][x] = nodes[nodes[i].neighbors[2]].value;
            else if (x == nodes[i].neighbors[3])
                graph[i][x] = nodes[nodes[i].neighbors[3]].value;
            else
                graph[i][x] = -1;
        }
    }
    // Auxiliary variables for the algorithm
    int journey[nodeCount];
    int definitive[nodeCount];
    int previous[nodeCount];
    int queue[nodeCount];
    int queueSize = 0;
    i = 0;
    for (i; i < nodeCount; ++i) {
        journey[i] = INFINITY_VALUE;
        definitive[i] = 0;
        queue[i] = -1;
        previous[i] = -1;
    }
    journey[initialNode] = 0;
    queue[0] = initialNode;
    ++queueSize;
    // Algorithm
    while (queueSize > 0) {
        int min = INFINITY_VALUE;
        int node = -1;
        i = 0;
        // Pick of the fastest queue
        for (i; i < queueSize; ++i) {
            if (journey[queue[i]] < min) {
                min = journey[queue[i]];
                node = queue[i];
            }
        }
        if (node == finishNode)
            break;
        // Rethinking the queue
        i = 0;
        for (i; i < queueSize; ++i) {
            if (node == queue[i]) {
                queue[i] = -1;
                break;
            }
        }
        i = 0;
        int buffer[nodeCount];
        for (i; i < nodeCount; ++i) {
            buffer[i] = queue[i];
        }
        i = 0;
        int x = 0;
        for (i; i < nodeCount; ++i) {
            if (buffer[i] != -1) {
                queue[x] = buffer[i];
                ++x;
            }
        }
        queueSize = x;
        for (x; x < nodeCount; ++x)
            queue[x] = -1;
        definitive[node] = 1;
        i = 0;
        // Edit distance for all the neighbors.
        for (i; i < nodeCount; ++i) {
            if (graph[node][i] != -1) {
                if (definitive[i] == 0) {
                    if (journey[node]+graph[node][i] < journey[i]) {
                        journey[i] = journey[node]+graph[node][i];
                        previous[i] = node;
                        int contained = 0;
                        x = 0;
                        for (x; x < queueSize; ++x) {
                            if (queue[x] == i)
                                contained = 1;
                        }
                        if (contained == 0) {
                            queue[queueSize] = i;
                            ++queueSize;
                        }
                    }
                }
            }
        }
    }
    // Finding the fastest way possible, and subsequently transferred to Python List
    i = finishNode;
    PyObject *buffer = PyList_New(0);
    PyObject *buffer2 = PyList_New(0);
    PyObject *finishWay = PyList_New(0);
    while (previous[i] != initialNode) {
        // Case unknown way
        if (previous[i] == -1)
            return Py_None;
        buffer = PyList_New(0);
        PyList_Append(buffer, PyInt_FromLong((long)nodes[previous[i]].x));
        PyList_Append(buffer, PyInt_FromLong((long)nodes[previous[i]].y));
        PyList_Append(buffer2, buffer);
        i = previous[i];
    }
    i = PyList_Size(buffer2)-1;
    for (i; i >= 0; --i) {
        PyList_Append(finishWay, PyList_GetItem(buffer2, i));
    }
    buffer = PyList_New(0);
    PyList_Append(buffer, PyInt_FromLong((long)nodes[finishNode].x));
    PyList_Append(buffer, PyInt_FromLong((long)nodes[finishNode].y));
    PyList_Append(finishWay, buffer);
    return finishWay;
}

PyMethodDef findWay_methods[] = {
    {"findWay", findWay, METH_VARARGS, "findWay"},
    {NULL, NULL, 0, NULL}
};
PyMODINIT_FUNC initfindWay(void) {
    Py_InitModule3("findWay", findWay_methods, "findWay");
}

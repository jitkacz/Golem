/* ***************************************************** */
/*              AUTHOR: Daniel Švec                      */
/*              NAME: Golem - createGrid                 */
/*              LAST CHANGE: 25.7.2010                   */
/* ***************************************************** */

#include <Python.h>

// The function creating empty array
PyObject* createGrid(PyObject* self, PyObject* args) {
    int width, height;
    int x, y;
    if (!PyArg_ParseTuple(args, "(ii)", &width, &height))
        return NULL;
    if (width == 0 || height == 0) {
        PyErr_SetString(PyExc_TypeError, "Parameter not be 0!");
        return NULL;
    }

    x = 0;
    PyObject *list = PyList_New(0);

    for (x; x < width; ++x) {
		y = 0;
		PyObject *buffer = PyList_New(0);

		for (y; y < height; ++y) {
			PyObject *buffer2 = PyList_New(0);
			PyList_Append(buffer, buffer2);
		}

        PyList_Append(list, buffer);
    }

    Py_INCREF(Py_None);
    return list;
}
PyMethodDef createGrid_methods[] = {
    {"createGrid", createGrid, METH_VARARGS, "createGrid"},
    {NULL, NULL, 0, NULL}
};
PyMODINIT_FUNC initcreateGrid(void) {
    Py_InitModule3("createGrid", createGrid_methods, "createGrid");
}

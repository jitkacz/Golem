#include <Python.h>

static PyObject * test(int i);

PyDoc_STRVAR(test__doc__, "test");
PyDoc_STRVAR(helloWorld__doc__, "helloWorld()");

static PyObject * helloWorld() {
	puts("Hello, World!");
	return Py_None;
}

static PyMethodDef test_methods[] = {
	{ "helloWorld",  helloWorld, METH_VARARGS, helloWorld__doc__ },
	{NULL, NULL}
};

PyMODINIT_FUNC inittest( void )
{
  Py_InitModule3("test", test_methods, test__doc__ );
}

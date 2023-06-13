#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * Description: function that prints some basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	long int size_of_list = Py_SIZE(p), list_index;
	PyListObject *list_object = (PyListObject *) p;

	printf("[*] Size of the Python List = %ld\n", size_of_list);
	printf("[*] Allocated = %ld\n", list_object->allocated);

	for (list_index = 0; list_index < size_of_list; list_index++)
		printf("Element %ld: %s\n", list_index,
				Py_TYPE(PyList_GetItem(p, list_index))->tp_name);
}

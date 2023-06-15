#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 *
 * Description: function that prints some basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int size_of_list = PyList_GET_SIZE(p), list_index;
	PyObject *temp;
	PyListObject *list_object = (PyListObject *) p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size_of_list);
	printf("[*] Allocated = %ld\n", list_object->allocated);

	for (list_index = 0; list_index < size_of_list; list_index++)
	{
		temp = PyList_GET_ITEM(p, list_index);
		if PyBytes_Check(temp)
			print_python_bytes(temp);
		else
			printf("Element %ld: %s\n", list_index,
					Py_TYPE(temp)->tp_name);
	}
}

/**
 * print_python_bytes - prints python bytes
 *
 * Description: prints python bytes
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	long int size_of_bytes = PyBytes_Size(p);
	PyBytesObject *byte_object = (PyBytesObject *) p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size_of_bytes);
	printf("  trying string: %s\n", PyBytes_AsString(byte_object));
	printf("  first %ld bytes: %x\n", size_of_bytes + 1,
			PyBytes_AsString(byte_object));
}

#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <bytesobject.h>

/**
 * print_python_float - prints some basic info about Python lists
 *
 * Description: function that prints some basic info about Python lists
 *
 * @p: PyObject pointer
 *
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double value;
	char buffer[100];
	int precision = 15;
	int length, tem_len, stop_print, allZeros = 1;

	fflush(stdout);
	printf("[.] float object info\n");
	if (!PyFloat_CheckExact(p))
		printf("  [ERROR] Invalid Float Object\n");
	else
	{
		value = PyFloat_AsDouble(p);

		length = snprintf(buffer, sizeof(buffer), "%.*f", precision, value);
		tem_len = length;
		while (buffer[tem_len - 1] != '.')
		{
			if (buffer[tem_len - 1] >= '1' && buffer[tem_len - 1] <= '9')
			{
				if (allZeros)
					stop_print = tem_len - 1;
				allZeros = 0;
			}
			tem_len--;
		}

		if (allZeros)
			buffer[tem_len + 1] = '\0';
		else
			buffer[stop_print + 1] = '\0';
		(void) stop_print;
		printf("  value: %s\n", buffer);
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
	long int size_of_bytes, i;
	char *string;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		string = ((PyBytesObject *) p)->ob_sval;
		size_of_bytes = PyBytes_Size(p);
		printf("  size: %ld\n", size_of_bytes);
		printf("  trying string: %s\n", string);
		if (size_of_bytes >= 10)
			size_of_bytes = 10;
		else
			size_of_bytes++;
		printf("  first %ld bytes:", size_of_bytes);
		for (i = 0; i < size_of_bytes; i++)
			printf(" %02x", (int) string[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

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

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		printf("[*] Size of the Python List = %ld\n", size_of_list);
		printf("[*] Allocated = %ld\n", list_object->allocated);

		for (list_index = 0; list_index < size_of_list; list_index++)
		{
			temp = PyList_GET_ITEM(p, list_index);
			printf("Element %ld: %s\n", list_index,
					temp->ob_type->tp_name);
			if (PyBytes_CheckExact(temp))
				print_python_bytes(temp);
			else if (PyFloat_CheckExact(temp))
				print_python_float(temp);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

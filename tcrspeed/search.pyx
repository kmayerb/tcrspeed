from libc.stdlib cimport malloc, free
from libc.string cimport strcmp
import numpy as np

cdef extern from "lv.h":
	cpdef int levenshtein(char* s1, char* s2)

cdef extern from "Python.h":
	char* PyUnicode_AsUTF8(object unicode)

cdef char ** to_cstring_array(list_str):
	cdef char **ret = <char **>malloc(len(list_str) * sizeof(char *))
	for i in xrange(len(list_str)):
		ret[i] = PyUnicode_AsUTF8(list_str[i])
	return ret

cpdef lv_rect(str s, list svec , int n):
	
	py_byte_string = s.encode('UTF-8')
	
	cdef char* s1 = py_byte_string 
	cdef char **c_arr1 = to_cstring_array(svec)
 	
	cdef int N = n
	cdef int[:] mv = np.zeros(N, dtype = np.intc)

	for i in range(N):
		ld = levenshtein(s1,c_arr1[i])
		mv[i] = ld 

	return mv


cpdef lv_rect2(list svec1, list svec2 , int n1, int n2):

	cdef char **c_arr1 = to_cstring_array(svec1)
	cdef char **c_arr2 = to_cstring_array(svec2)
 	
	cdef int N1 = n1
	cdef int N2 = n2
	cdef int[:,:] mv = np.zeros([N1,N2], dtype = np.intc)

	for i in range(N1):
		for j in range(N2):
			if j>i:
				ld = levenshtein(c_arr1[i],c_arr2[j])
				mv[i,j] = ld 

	return mv

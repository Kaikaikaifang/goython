cdef extern from "library.h":
    ctypedef int GoInt64
    ctypedef GoInt64 GoInt

    GoInt add(GoInt a, GoInt b)

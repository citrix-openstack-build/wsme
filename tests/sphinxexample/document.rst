API Documentation test
======================

Example
~~~~~~~

.. wsme:root:: wsme.sphinxext.SampleService
    :webpath: /api

.. wsme:type:: MyType

    .. wsme:attribute:: test

        :type: int

.. wsme:service:: name/space/SampleService
    
    .. wsme:function:: getType
        
        Returns a :wsme:type:`MyType <MyType>`


.. default-domain:: wsme

.. type:: int

    An integer

.. autotype:: wsme.sphinxext.SampleType
    :members:

.. autoservice:: wsme.sphinxext.SampleService
    :members:


.. autotype:: test_sphinxext.ASampleType
    :members:

.. autotype:: wsme.types.bytes

.. autotype:: wsme.types.text

.. _Sphinx: http://sphinx.pocoo.org/

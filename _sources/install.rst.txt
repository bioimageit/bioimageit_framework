install
=======

This section contains the instruction to install ``bioimageit_framework``

Install from conda
------------------

.. code-block:: bash

    conda create -n bioimageit python=3.9
    conda activate bioimageit
    conda install bioimageit_framework -c bioimageit


Install from PyPI
-----------------

.. code-block:: bash

    python -m venv .bioimageit
    source .bioimageit/bin/activate
    pip install bioimageit_framework


Install from source
-------------------

.. code-block:: bash

    git clone https://github.com/bioimageit/bioimageit_framework.git
    pip install ./bioimageit_framework

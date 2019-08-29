PyBerlin Codeslam
=================
1. `generating password <slam/one.py>`__ with `secrets
   <https://docs.python.org/3/library/secrets.html>`_, also shows the new
   Python 3.8 ``f"{...=}"`` syntax:

   .. code:: python

      print(f"{generate_password_secure(8)=}")
      # generate_password_secure(8)='td32PZYm'

2. `creating sorted lists <slam/two.py>`__ with `bisect.insort
   <https://docs.python.org/3/library/bisect.html#bisect.insort_left>`_

3. `using builtin-breakpoint <slam/three.py>`__ (`breakpoint()
   <https://docs.python.org/3/library/functions.html#breakpoint>`_) instead of
   ``import pdb; pdb.set_trace()``.
   To switch to ipdb, set ``export PYTHONBREAKPOINT=ipdb.set_trace``.

4. `using timeit <slam/four.py>`__ (`timeit.timeit
   <https://docs.python.org/3/library/timeit.html#timeit.timeit>`_) can help
   with validating the speed between 2 functions

5. `comparing the different encoding in base64 <slam/five.py>`_, the `base64
   <https://docs.python.org/3/library/base64.html>`__ module has more than
   just base64 encoders

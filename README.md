mobiccnx
========

An enhanced CCNx with the support of perfect mobility. 

Initialized by Liang Wang, Deptartment of Computer Science, University of Helsinki, 09.09.2012. Please contact `liang.wang@cs.helsinki.fi` if you have any questions.

1. All the comments about the project are in this README.md. This file might change quite a lot in future, and currently serves as temporary project log file. Comments and modifications are welcome.

2. All the scripts or other tools for deploying experiments go into tool folder. DO NOT put any scripts/codes irrelevant to CCNx protocol into its standard code tree.

3. All the codes should comply with certain conventions related with the corresponding programming language listed as below. All the codes should have some readable comments.
   * `General(e.g. naming)`: refer to CCNx document (http://www.ccnx.org/releases/latest/doc/technical/)
   * `java`: refer to http://www.oracle.com/technetwork/java/codeconv-138413.html
   * `C/C++`: refer to http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml
   * `python`: refer to http://www.python.org/dev/peps/pep-0008/


More info will be added later.


Project Schedule:

* `Week 0`:
  	- Read relevant papers to get familiar with the topic; (all)
	- Get familiar with the individual's tasks; (all)
  	- Set up code repository for collaboration; (Liang)
	- Sketch the skeleton of the paper; (Liang)

* `Week 1`:
  	- Hands-on work: Read the code. Deploy the CCNx on Ukko, and test; (Liang and Otto)
	- Hands-on work: Automate the experiment and development; (Liang)
	- Hands-on work: Extend the default naming in current CCNx, make a simple branch to call our routing protocol; (Otto)
	- Hands-on work: Decide the code structure for attacking setting up connection issue; (Liang and Otto)
	- Hands-on work: First graph embedding (python) module partially done; (Ossi)
	- Writing: Write up the solution, and also fill content into other sections;

* `Week 2`:
  	- Hands-on work: Start attacking setting up connection issue; (Liang and Otto)
  	- Hands-on work: First graph embedding is done, test; (Ossi)
	- Writing: More content in implementation section, fill content into other sections;

* `Week 3`:
  	- Hands-on work: Setting up connection issue is solved, test; (Liang and Otto)
  	- Hands-on work: Translate graph embedding into C/C++ code, make it into CCNx module; (Ossi)
	- Experiment: Start design the experiment, determine the metrics; (Liang, Otto and Ossi)
	- Experiment: Polish the automation scripts; (Liang)
	- Writing: Fill content in experiment and evaluation section; (Liang)

* `Week 4`:
  	- Experiment: Perform the experiments and analyze the result; (Otto and Ossi)
	- Writing: Fill content in evaluation section; (Liang)

* `Week 5`:
  	- TBD


Memo:

Minimum-depth tree as spanning tree; is that good for stretch?
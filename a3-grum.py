#!/usr/bin/env python
from __future__ import print_function
import sys
import os

# Get correct path to files, based on platform
import platform
host = platform.node().split('.')[0]

if host=="moss":
   sys.path[0:0]=['/local/courses/csse2310/lib']
   TEST_LOCATION = '/home/users/uqjfenw1/public/2019/ptesta3'
else:
	sys.path[0:0] = [ 
	    '/home/joel/marks',
	]
import marks

COMPILE = "make"
 
 
class Ass3(marks.TestCase):
  timeout = 12 
  @classmethod
  def setup_class(cls):
        # Store original location
        options = getattr(cls, '__marks_options__', {})
        cls.proghub = os.path.join(options['working_dir'], './2310hub')
        cls.progalice = os.path.join(options['working_dir'], './2310alice')
        cls.progbob = os.path.join(options['working_dir'], './2310bob')
        cls._compile_warnings = 0
        cls._compile_errors = 0
 
        # Create symlink to tests in working dir
        os.chdir(options['working_dir'])
        try:
            os.symlink(TEST_LOCATION, 'tests')
        except OSError:
            pass
        os.chdir(options['temp_dir'])

        # Modify test environment when running tests (excl. explain mode).
        if not options.get('explain', False):
            # Compile program
            os.chdir(options['working_dir'])
            p = marks.Process(COMPILE.split())
            os.chdir(options['temp_dir'])
 
            # Count warnings and errors
            warnings = 0
            errors = 0
            while True:
                line = p.readline_stderr()
                if line == '':
                    break
                if 'warning:' in line:
                    warnings += 1
                if 'error:' in line:
                    errors += 1
                print(line, end='')

            # Do not run tests if compilation failed.
            assert p.assert_exit_status(0)
 
            # Create symlink to tests within temp folder
            try:
                os.symlink(TEST_LOCATION, 'tests')
            except OSError:
                pass 

  @marks.marks('hub_args', category_marks=5)
  def test_hubarg1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+[])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/hargs1.out')
    self.assert_stderr_matches_file(p, 'tests/hargs1.err')
    self.assert_exit_status(p, 1)  

  @marks.marks('hub_args', category_marks=5)
  def test_hubarg2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["", "", "", ""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/hargs2.out')
    self.assert_stderr_matches_file(p, 'tests/hargs2.err')
    self.assert_exit_status(p, 2)  

  @marks.marks('hub_args', category_marks=5)
  def test_hubarg3(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["", "1", "", "", ""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/hargs3.out')
    self.assert_stderr_matches_file(p, 'tests/hargs3.err')
    self.assert_exit_status(p, 2)  

  @marks.marks('hub_args', category_marks=5)
  def test_hubarg4(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/x", "3", "", "", ""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/hargs4.out')
    self.assert_stderr_matches_file(p, 'tests/hargs4.err')
    self.assert_exit_status(p, 3)  

  @marks.marks('hub_args', category_marks=5)
  def test_hubarg5(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/db", "3", "", "", ""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/hargs5.out')
    self.assert_stderr_matches_file(p, 'tests/hargs5.err')
    self.assert_exit_status(p, 3)  

  @marks.marks('alice_args', category_marks=2)
  def test_aargs1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage1.out')
    self.assert_stderr_matches_file(p, 'tests/usage1.err')
    self.assert_exit_status(p, 1)

  @marks.marks('alice_args', category_marks=2)
  def test_aargs2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["",""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage1.out')
    self.assert_stderr_matches_file(p, 'tests/usage1.err')
    self.assert_exit_status(p, 1)
    
  @marks.marks('alice_args', category_marks=2)
  def test_aargs3(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["","","",""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage2.out')
    self.assert_stderr_matches_file(p, 'tests/usage2.err')
    self.assert_exit_status(p, 2)

  @marks.marks('alice_args', category_marks=2)
  def test_aargsX(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["2","..","",""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage3.out')
    self.assert_stderr_matches_file(p, 'tests/usage3.err')
    self.assert_exit_status(p, 3)   

  @marks.marks('alice_args', category_marks=2)
  def test_aargsY(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["2","1","1","4"])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage4.out')
    self.assert_stderr_matches_file(p, 'tests/usage4.err')
    self.assert_exit_status(p, 4) 
	
  @marks.marks('alice_args', category_marks=2)
  def test_aargsZ(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["2","1","2","2h"])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/usage5.out')
    self.assert_stderr_matches_file(p, 'tests/usage5.err')
    self.assert_exit_status(p, 5)   	

  @marks.marks('alice_first_lead', category_marks=2)
  def test_a1lead1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["2","0","2","9"], "tests/1lead1.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/1lead1.out')
    self.assert_stderr_matches_file(p, 'tests/1lead1.err')
    self.assert_exit_status(p, 7)      

  @marks.marks('alice_first_lead', category_marks=2)
  def test_a1lead2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["2","0","2","6"], "tests/1lead2.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/1lead2.out')
    self.assert_stderr_matches_file(p, 'tests/1lead2.err')
    self.assert_exit_status(p, 7)  
	
  @marks.marks('alice_first_follow', category_marks=2)
  def test_a1follow1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["3","1","4","9"], "tests/1follow1.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/1follow1.out')
    self.assert_stderr_matches_file(p, 'tests/1follow1.err')
    self.assert_exit_status(p, 7)      

  @marks.marks('alice_first_follow', category_marks=2)
  def test_a1follow2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["3","1","4","9"], "tests/1follow2.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/1follow2.out')
    self.assert_stderr_matches_file(p, 'tests/1follow2.err')
    self.assert_exit_status(p, 7)   	

  @marks.marks('alice_single_round', category_marks=2)
  def test_a1single1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["5","2","2","1"], "tests/a1single.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/a1single.out')
    self.assert_stderr_matches_file(p, 'tests/a1single.err')
    self.assert_exit_status(p, 0)   	

  @marks.marks('alice_single_round', category_marks=2)
  def test_a1single2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.progalice]+["5","3","2","1"], "tests/a2single.in")
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/a2single.out')
    self.assert_stderr_matches_file(p, 'tests/a2single.err')
    self.assert_exit_status(p, 0)   	

  @marks.marks('gt3_alice', category_marks=3)
  def test_gt3alice1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/da.deck","3",self.progalice, self.progalice, self.progalice, self.progalice])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/gt3alice1.out')
    self.assert_exit_status(p, 0)   	

  @marks.marks('gt3_alice', category_marks=3)
  def test_gt3alice2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/da.deck","3",self.progalice, self.progalice, self.progalice, self.progalice, self.progalice])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/gt3alice2.out')
    self.assert_exit_status(p, 0)   	

  @marks.marks('eq3_alice', category_marks=4)
  def test_eq3alice1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/da.deck","2",self.progalice, self.progalice, self.progalice])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/eq3alice1.out')
    self.assert_exit_status(p, 0)   	

  @marks.marks('eq3_alice', category_marks=4)
  def test_eq3alice2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.proghub]+["tests/db.deck","2",self.progalice, self.progalice, self.progalice])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/eq3alice2.out')
    self.assert_stderr_matches_file(p, 'tests/eq3alice2.err')
    self.assert_exit_status(p, 0)   	


  @marks.marks('alice_bad_messages', category_marks=2)
  def test_a_bad_message1(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progalice]+["3","1","4","9"], "tests/abad1.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/abad1.out")
      self.assert_stderr_matches_file(p, "tests/abad1.err")
      self.assert_exit_status(p, 6)

  @marks.marks('alice_bad_messages', category_marks=2)
  def test_a_bad_message_2(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progalice]+["3","1","4","9"], "tests/abad2.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/abad2.out")
      self.assert_stderr_matches_file(p, "tests/abad2.err")
      self.assert_exit_status(p, 6)

  @marks.marks('alice_bad_messages', category_marks=2)
  def test_a_bad_message_3(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progalice]+["3","2","4","9"], "tests/abad3.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/abad3.out")
      self.assert_stderr_matches_file(p, "tests/abad3.err")
      self.assert_exit_status(p, 6)

  @marks.marks('alice_bad_messages', category_marks=2)
  def test_a_bad_message_4(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progalice]+["3","1","4","9"], "tests/abad4.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/abad4.out")
      self.assert_stderr_matches_file(p, "tests/abad4.err")
      self.assert_exit_status(p, 6)
 
  @marks.marks('bob_first_lead', category_marks=1)
  def test_b1lead1(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progbob]+["3","0","4","9"], "tests/b1lead1.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/b1lead1.out")
      self.assert_stderr_matches_file(p, "tests/b1lead1.err")
      self.assert_exit_status(p, 7)

  @marks.marks('bob_first_follow', category_marks=2)
  def test_b1follow1(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progbob]+["3","1","4","9"], "tests/b1follow1.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/b1follow1.out")
      self.assert_stderr_matches_file(p, "tests/b1follow1.err")
      self.assert_exit_status(p, 7)

  @marks.marks('bob_first_round', category_marks=2)
  def test_b1round1(self):
      """ """
      #1 empty empty usage.err - -
      p = self.process([self.progbob]+["3","1","4","9"], "tests/b1round1.in")
      p.finish_input()
      self.assert_stdout_matches_file(p, "tests/b1round1.out")
      self.assert_stderr_matches_file(p, "tests/b1round1.err")
      self.assert_exit_status(p, 7)




if __name__ == '__main__':
    marks.main()


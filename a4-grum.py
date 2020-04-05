#!/usr/bin/env python
from __future__ import print_function
import sys
import os

# Get correct path to files, based on platform
import platform
host = platform.node().split('.')[0]

if host=="moss":
   sys.path[0:0]=['/local/courses/csse2310/lib']
   TEST_LOCATION = '/home/users/uqjfenw1/public/2019/ptesta4'
else:
	sys.path[0:0] = [ 
	    '/home/joel/marks',
	]
import marks

COMPILE = "make"
 
 
class Ass4(marks.TestCase):
  timeout = 8
  @classmethod
  def setup_class(cls):
        # Store original location
        options = getattr(cls, '__marks_options__', {})
        cls.prog = os.path.join(options['working_dir'], './2310depot')
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

  #@marks.marks('args', category_marks=3)
  #@marks.marks('single_deliver', category_marks=3)
  #@marks.marks('single_withdraw', category_marks=2)
  #@marks.marks('single_defer', category_marks=8)
  #@marks.marks('single_mixture', category_marks=4)
  
  #@marks.marks('mult_connect', category_marks=2)
  #@marks.marks('mult_transfer', category_marks=6)
  #@marks.marks('mult_def_transfer', category_marks=4)
  #@marks.marks('mult_mixture', category_marks=12)  

  @marks.marks('args', category_marks=3)  
  def test_hubarg1(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.prog]+[])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/args1.out')
    self.assert_stderr_matches_file(p, 'tests/args1.err')
    self.assert_exit_status(p, 1)  
    
  @marks.marks('args', category_marks=3)  
  def test_hubarg2(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.prog]+["A b"])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/args2.out')
    self.assert_stderr_matches_file(p, 'tests/args2.err')
    self.assert_exit_status(p, 2) 
    
  @marks.marks('args', category_marks=3)  
  def test_hubarg3(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.prog]+["test", ""])  # check for number before contents
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/args3.out')
    self.assert_stderr_matches_file(p, 'tests/args3.err')
    self.assert_exit_status(p, 1)  
    
  @marks.marks('args', category_marks=3)  
  def test_hubarg4(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.prog]+["test","toffee", ""])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/args4.out')
    self.assert_stderr_matches_file(p, 'tests/args4.err')
    self.assert_exit_status(p, 3)  
    
  @marks.marks('args', category_marks=3)  
  def test_hubarg5(self):
    """ """
    #1 empty empty usage.err - - 
    p = self.process([self.prog]+["test","toffee", "-1"])
    p.finish_input()
    self.assert_stdout_matches_file(p, 'tests/args5.out')
    self.assert_stderr_matches_file(p, 'tests/args5.err')
    self.assert_exit_status(p, 3)      

  @marks.marks('single_deliver', category_marks=3)
  def test_sdel_1(self):
    p = self.process([self.prog]+["test"])
    discard=p.readline_stdout()
    p.send_signal(1)    
    self.delay(2)
    p.send_signal(9)
    #p.kill()	# kill seems to be closing the streams here
    self.assert_stdout_matches_file(p, 'tests/sdel1.out')
    self.delay(1)
    p.assert_signalled(9)

  @marks.marks('single_deliver', category_marks=3)
  def test_sdel_2(self):
    p = self.process([self.prog]+["test", "sand", "4"])
    discard=p.readline_stdout()    
    p.send_signal(1)
    self.delay(1)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/sdel2.out')
    self.assert_stderr_matches_file(p, 'tests/sdel2.err') 
    self.delay(1)   
    p.assert_signalled(9)
    
  @marks.marks('single_deliver', category_marks=3)
  def test_sdel_3(self):
    p = self.process([self.prog]+["test", "sand", "4"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/sdel_3_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/sdel3.out')
    self.assert_stderr_matches_file(p, 'tests/sdel3.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_deliver', category_marks=3)
  def test_sdel_4(self):
    p = self.process([self.prog]+["test", "sand", "4"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/sdel_4_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/sdel4.out')
    self.assert_stderr_matches_file(p, 'tests/sdel4.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_withdraw', category_marks=2)
  def test_swit_1(self):
    p = self.process([self.prog]+["test", "sand", "10"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/swit_1_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/swit1.out')
    self.assert_stderr_matches_file(p, 'tests/swit1.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_withdraw', category_marks=2)
  def test_swit_2(self):
    p = self.process([self.prog]+["test", "sand", "10"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/swit_2_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/swit2.out')
    self.assert_stderr_matches_file(p, 'tests/swit2.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_withdraw', category_marks=2)
  def test_swit_3(self):
    p = self.process([self.prog]+["test", "sand", "10"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/swit_3_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/swit3.out')
    self.assert_stderr_matches_file(p, 'tests/swit3.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()


  @marks.marks('single_withdraw', category_marks=2)
  def test_swit_4(self):
    p = self.process([self.prog]+["test", "sand", "10"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/swit_4_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/swit4.out')
    self.assert_stderr_matches_file(p, 'tests/swit4.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_1_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_1_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_1.out')
    self.assert_stderr_matches_file(p, 'tests/def_1.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_2_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_2_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_2.out')
    self.assert_stderr_matches_file(p, 'tests/def_2.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_3_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_3_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_3.out')
    self.assert_stderr_matches_file(p, 'tests/def_3.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_4_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_4_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_4.out')
    self.assert_stderr_matches_file(p, 'tests/def_4.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_5_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_5_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_5.out')
    self.assert_stderr_matches_file(p, 'tests/def_5.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_defer', category_marks=8)
  def test_def_6_broken(self):
    p = self.process([self.prog]+["test", "sand", "1"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/def_6_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/def_6.out')
    self.assert_stderr_matches_file(p, 'tests/def_6.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_mixture', category_marks=4)
  def test_smix_1_broken(self):
    p = self.process([self.prog]+["test", "sand", "1", "grass", "2"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/smix_1_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/smix_1.out')
    self.assert_stderr_matches_file(p, 'tests/smix_1.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()

  @marks.marks('single_mixture', category_marks=4)
  def test_smix_2_broken(self):
    p = self.process([self.prog]+["test", "sand", "1", "grass", "2"])
    port=p.readline_stdout().strip()    
    p2 = self.process(["nc", "127.0.0.1", port], 'tests/smix_2_1.in')
    self.delay(2)
    p.send_signal(1)
    self.delay(1)
    p.send_signal(9)
    self.assert_stdout_matches_file(p, 'tests/smix_2.out')
    self.assert_stderr_matches_file(p, 'tests/smix_2.err') 
    self.delay(1)   
    p.assert_signalled(9)
    p2.kill()







if __name__ == '__main__':
    marks.main()


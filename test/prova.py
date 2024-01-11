from thread import Mythread

def main():
  t = Mythread() 

  # Execution of target function 
  t.start() 
  
  # Executed by main thread 
  for i in range(20): 
    print('Main Thread') 
  t.kill()
  t.join()
        
main()
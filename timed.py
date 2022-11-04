import time 
def timeme(func):
  def wrapper(): 
    start = time.time() 
    func() 
    end = time.time() 
    print('Total time {}'.format(end - start)) 
    return wrapper 
@timeme 
def test(): 
  time.sleep(2) 
test()

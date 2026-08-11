from collections import deque

class CallCenter:
  def __init__(self):
    self.call_queue = deque()
    self.agents = set()
  def addagent(self, agents_id):
    self.agents.add(agents_id)
  def removeagent(self, agents_id):
    if agents_id in self.agents:
      self.agents.remove(agents_id)
    else:
      print(f'agent {agents_id} is not available')
  def enqueue_call(self, call_id):
    self.call_queue.append(call_id)
    print(f"Call {call_id} added to the queue")
  def asaign_call(self):
    if self.call_queue:
      call_id = self.call_queue.popleft()
      agent_id = self.agents.pop() if self.agents else None
      if agent_id:
        print(f'Call {call_id} is assaigned to agent {agent_id}')
      else:
        print('No availiabe agents call will be on hold')
    else:
      print('No calls in the queue')

callcenter = CallCenter()
callcenter.addagent(101)
callcenter.addagent(102)
callcenter.addagent(103)
callcenter.enqueue_call(1)
callcenter.enqueue_call(2)
callcenter.asaign_call()
callcenter.asaign_call()
callcenter.asaign_call()
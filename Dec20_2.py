#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pprint import pprint
import asyncio


# In[ ]:


q_dict = {}
lo_pulse_cnt = 0
hi_pulse_cnt = 0


# In[ ]:


class Broadcaster:
    def __init__(self, out_list):
        self.out_list = out_list
        self.qin = asyncio.Queue()
        #asyncio.create_task(self.start())
        
    async def start(self):
        global lo_pulse_cnt, hi_pulse_cnt, lock
        while True:
            pulse_in = await self.qin.get()
            for out in self.out_list:
                #print('broadcaster -' + ('low' if pulse_in == 0 else 'high') + '->', out)
                if pulse_in == 0:
                    lo_pulse_cnt += 1
                else:
                    hi_pulse_cnt += 1
                q_dict[out + '_q'].put_nowait((pulse_in, 'broadcaster'))


# In[ ]:


class Flipflop:
    def __init__(self, name, out_list):
        self.name = name
        self.out_list = out_list
        self.qin = asyncio.Queue()
        self.state = 0
        #asyncio.create_task(self.start())

    async def start(self):
        global lo_pulse_cnt, hi_pulse_cnt, lock
        while True:
            pulse_in, source = await self.qin.get()
            if pulse_in == 0:
                if self.state == 0:
                    self.state = 1
                    for out in self.out_list:
                        #print(self.name, '-high->', out)
                        hi_pulse_cnt += 1
                        q_dict[out + '_q'].put_nowait((1, self.name))
                else:
                    self.state = 0
                    for out in self.out_list:
                        #print(self.name, '-low->', out)
                        lo_pulse_cnt += 1
                        q_dict[out + '_q'].put_nowait((0, self.name))


# In[ ]:


class Conjunction:
    def __init__(self, name, in_list, out_list):
        self.name = name
        self.in_list = in_list
        self.out_list = out_list
        self.mem = {k:0 for k in in_list}
        self.qin = asyncio.Queue()

    async def start(self):
        global lo_pulse_cnt, hi_pulse_cnt, lock
        while True:
            pulse_in, source = await self.qin.get()
            if self.name == 'cs':
                if pulse_in == 1:
                    print('cs got high pulse from', source)
            #print('conj:', self.name, 'pulse in:', pulse_in, 'source:', source)
            self.mem[source] = pulse_in
            #print('conj:', self.name, 'mem:', self.mem)
            if all(v == 1 for v in self.mem.values()):
                for out in self.out_list:
                    #print(self.name, '-low->', out)
                    lo_pulse_cnt += 1
                    q_dict[out + '_q'].put_nowait((0, self.name))
            else:
                for out in self.out_list:
                    #print(self.name, '-high->', out)
                    hi_pulse_cnt += 1
                    q_dict[out + '_q'].put_nowait((1, self.name))
                


# In[ ]:


async def main():
    global lo_pulse_cnt, hi_pulse_cnt, lock
    fn = "data/pulse.txt"

    conn_dict = {}
    with open(fn) as fin:
        for line in fin:
            #print(line)
            conn = line.split('->')
            conn_dict.update({conn[0].strip() : conn[1].strip().replace(' ', '').split(',')})
    pprint(conn_dict)
    
    #task_list = []
    for comp in conn_dict.keys():
        #print ('comp: ', comp)
        conn_list = conn_dict[comp]
        #print('conn list:' , conn_list)
        if comp == 'broadcaster':
            broadcaster = Broadcaster(conn_list)
            bc_task = asyncio.create_task(broadcaster.start())
            
        elif comp[0] == '%':
            comp_name = comp[1:]
            # class instance with comp name
            globals()['ff_' + comp_name] = Flipflop(comp_name, conn_list)
            # input queue for class instance
            globals()[comp_name + '_q'] = globals()['ff_' + comp_name].qin
            # add queue names to dict so tasks can find them
            q_dict[comp_name + '_q'] = globals()[comp_name + '_q']
            # start task loop and add task name to list so we can await it below 
            globals()[comp_name + '_task'] = asyncio.create_task(globals()['ff_' + comp_name].start())

        elif comp[0] == '&':
            comp_name = comp[1:]
            # count number of inputs for Conjunction
            conj_inputs = []
            for k, v in conn_dict.items():
                if comp_name in v:
                    conj_inputs.append(k[1:])
            # class instance with comp name
            globals()['cj_' + comp_name] = Conjunction(comp_name, conj_inputs, conn_list)
            # input queue for class instance
            globals()[comp_name + '_q'] = globals()['cj_' + comp_name].qin
            # add queue names to dict so tasks can find them
            q_dict[comp_name + '_q'] = globals()[comp_name + '_q']
            # start task loop and add task name to list so we can await it below 
            globals()[comp_name + '_task'] = asyncio.create_task(globals()['cj_' + comp_name].start())

    # rx is an output, not a component.  This sort of a hack that should be handled better
    globals()['rx_q'] = asyncio.Queue()
    q_dict['rx_q'] = globals()['rx_q']
    for i in range(1, 9000):
        print ('push: ', i)
        lo_pulse_cnt += 1
        broadcaster.qin.put_nowait(0)
        await asyncio.sleep(0.001)
        #print('low  pulse cnt:', lo_pulse_cnt)
        #print('high pulse cnt:', hi_pulse_cnt)
        rx_pulse, _ = await rx_q.get()
        if rx_pulse == 0:
            print('number of button pushes:', i+1)
            break
    await asyncio.sleep(0.001)
    print('low  pulse cnt:', lo_pulse_cnt)
    print('high pulse cnt:', hi_pulse_cnt)
    print('total:', lo_pulse_cnt * hi_pulse_cnt)
await main()


# In[ ]:


"""
       cycles for &comp to output hi pulse
       3889  7778  &kh

       3917  7834  &lz
                                      &cs  rx
       3769  7538  &tg
                      
       4013  8026  &hn

       LCM = 3889 * 3769 * 3769 * 4013 = 230402300925361
"""

